# Stock Analysis Tool (WRDS)

## 1. Project Overview

This project analyzes the stock performance of five major technology companies using WRDS CRSP daily stock data from 2020 to 2024.

The selected companies are:

* Microsoft (MSFT)
* Apple (AAPL)
* Amazon (AMZN)
* Nvidia (NVDA)
* Tesla (TSLA)

The project combines financial analysis and interactive visualization to help investors better understand stock return, volatility, investment risk, and long-term opportunities.

In addition to Jupyter Notebook analysis, an interactive Streamlit dashboard is developed for practical investment decision support.

---

## 2. Data Source

This project uses:

### WRDS (Wharton Research Data Services)

Database:

### CRSP Daily Stock File (crsp.dsf)

Time Period:

### 2020-01-01 to 2024-01-01

Why WRDS:

* Official academic financial database
* Higher reliability than Yahoo Finance
* Commonly used in university finance research
* Supports professional financial analysis and regression modeling

---

## 3. Methods

This project applies both financial analysis and interactive dashboard development.

Main methods include:

* Data extraction from WRDS using SQL queries
* Data cleaning using Pandas
* Daily return analysis
* Volatility analysis using standard deviation
* Moving Average analysis (MA5, MA20, MA60)
* COVID period performance comparison
* Benchmark comparison across five companies
* Sharpe Ratio evaluation
* OLS Regression analysis
* Streamlit dashboard development for visualization

The Streamlit application provides dynamic stock selection, automatic risk analysis, and practical investment insights for users.

---

## 4. Key Findings

The analysis shows that:

* Tesla and Nvidia have higher return potential but also significantly higher volatility and investment risk
* Microsoft and Apple demonstrate stronger stability and better long-term investment value
* Amazon shows relatively balanced performance during post-pandemic recovery
* Regression results confirm a positive relationship between volatility and return
* COVID-19 significantly affected stock performance across different periods

These findings support the classical financial theory that higher expected return is usually associated with higher investment risk.

---

## 5. How to Run

### Step 1

Open Anaconda Prompt or Command Prompt

### Step 2

Navigate to the project folder

```bash
cd your_project_folder
```
### Step 3

Run the Streamlit application

```bash
streamlit run stock_app.py.py
```

### Step 4

Open the browser and use the interactive dashboard

Default local URL:

http://localhost:8501

### WRDS Requirements

A valid WRDS account with CRSP access is required.

University VPN may be needed for off-campus access.

---

## 6. Files Included

### ACC102_final.ipynb

Main notebook containing:

* Data extraction
* Financial analysis
* Regression model
* Benchmark comparison
* Final conclusion

### stock_app.py

Interactive Streamlit dashboard

### README.md

Project documentation

---

## 7. Product Link / Demo
GitHub Repository:

(https://github.com/songpudong/Stock-Analysis-Tool)

Demo Video:

[Your Demo Video Link Here]

---

## 8. Limitations & Next Steps

### Limitations

* Analysis is limited to five selected technology companies
* Only CRSP daily stock data is used
* No real-time market data integration
* Industry coverage is relatively narrow

### Next Steps

* Add more industries and company comparisons
* Integrate ESG and sustainability indicators
* Add predictive modeling and forecasting functions
* Improve dashboard interactivity and advanced visualization features

---

## 9. Conclusion

This project provides a practical and data-driven framework for evaluating stock investment opportunities using academic financial databases and interactive dashboard tools.

It helps investors make better decisions based on:

* Return expectations
* Risk tolerance
* Market conditions
* Investment objectives

The combination of WRDS, regression analysis, and Streamlit dashboard makes this project both academically rigorous and practically useful.

This project demonstrates how financial data analysis can be transformed into a practical decision-support tool for real-world investment analysis.

