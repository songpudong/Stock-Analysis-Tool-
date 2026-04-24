import streamlit as st
import wrds
import pandas as pd
@st.cache_resource
def connect_wrds():
    return wrds.Connection()

db = connect_wrds()
st.title("Stock Analysis Tool (WRDS)")

# 5 companies
company_map = {
    "MSFT": 10107,
    "AMZN": 84788,
    "AAPL": 14593,
    "NVDA": 86580,
    "TSLA": 93436
}

ticker = st.selectbox(
    "Choose a stock:",
    list(company_map.keys())
)

permno = company_map[ticker]



# SQL query
query = f"""
select date, permno, prc, ret
from crsp.dsf
where permno = {permno}
and date between '2020-01-01' and '2024-01-01'
order by date
"""

data = db.raw_sql(query)

# empty check
if data.empty:
    st.error("No data found.")
    st.stop()

# date format
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values("date")
data = data.set_index("date")

# use absolute price
data["prc"] = data["prc"].abs()

# moving averages
data["MA5"] = data["prc"].rolling(5).mean()
data["MA20"] = data["prc"].rolling(20).mean()
data["MA60"] = data["prc"].rolling(60).mean()

# stock trend
st.subheader("Stock Price Trend")

st.line_chart(
    data[["prc", "MA5", "MA20", "MA60"]],
    height=400
)

# return and volatility
avg_return = data["ret"].mean()
volatility = data["ret"].std()

st.subheader("Key Risk Indicators")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Average Daily Return",
        value=f"{avg_return:.4f}"
    )

with col2:
    st.metric(
        label="Volatility (Risk)",
        value=f"{volatility:.4f}"
    )

# investment insight
st.subheader("Investment Insight")

if volatility > 0.03:
    st.write(
        f"{ticker} shows relatively **high volatility**, "
        f"which means higher risk but also higher potential returns."
    )
else:
    st.write(
        f"{ticker} shows relatively **stable performance**, "
        f"with lower volatility and suitable for conservative investors."
    )

# latest data
st.subheader("Latest 5 Days Data")
st.dataframe(data.tail())

# COVID period analysis
st.subheader("COVID Period Performance (2020–2024)")

phase1 = data.loc["2020-01":"2020-06"]
phase2 = data.loc["2020-07":"2021-12"]
phase3 = data.loc["2022-01":"2024-01"]

ret1 = (1 + phase1["ret"]).prod() - 1
ret2 = (1 + phase2["ret"]).prod() - 1
ret3 = (1 + phase3["ret"]).prod() - 1

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("2020 COVID Outbreak", f"{ret1:.2%}")

with c2:
    st.metric("2020H2–2021 Recovery", f"{ret2:.2%}")

with c3:
    st.metric("2022–2024 Post-pandemic", f"{ret3:.2%}")

# Sharpe Ratio
risk_free_rate = 0.02 / 252
sharpe_ratio = (avg_return - risk_free_rate) / volatility

st.metric("Sharpe Ratio", f"{sharpe_ratio:.2f}")

# project summary
st.subheader("Project Summary")

st.write("""
This dashboard uses WRDS CRSP daily stock data to help retail investors analyze stock performance,
compare risk levels, and understand investment opportunities through:

- Price Trend Analysis
- Moving Average Signals
- Daily Return & Volatility
- Risk Indicators
- Pandemic Period Performance
- Sharpe Ratio Evaluation
- Automated Investment Insights

It provides a practical and user-friendly solution for non-technical investors
to make better investment decisions.
""")