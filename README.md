# CHANNEL-PROFITABILITY-ANALYSIS
# Hybrid Channel Profitability & FX Risk Analysis

## 🎯 Project Overview
This project is a comprehensive strategic business intelligence study designed to identify the true drivers of profitability across **B2B (Wholesale)** and **D2C (Direct-to-Consumer)** sales channels.

While many companies focus on top-line revenue growth, this analysis deep-dives into the **Contribution Margin** by accounting for hidden costs such as:
- Returns
- Marketing ROI
- Financing costs (DSO – Days Sales Outstanding)
- Currency (FX) volatility

---

## 🛠️ Tech Stack & Methodology
- **Database:** PostgreSQL (Data modeling & complex financial views)  
- **Analysis:** Python (Pandas, NumPy for financial calculations)  
- **Visualization:** Matplotlib, Seaborn, Plotly (Strategic dashboards & waterfall charts)  
- **Framework:** 8-Phase Consulting Methodology (From Business Understanding to Final Action Plan)

---

## 🏗️ Project Framework

### 1. Business Understanding & Data Modeling
The analysis categorizes products into **Premium, Mid, and Entry** segments across two primary channels.  

A custom SQL view (`v_master_financial_report`) was developed to unify:
- Production Costs (USD/TL)  
- Platform Commissions  
- Logistics & Return Costs  
- Marketing Spend per Segment  

### 2. Financial Metrics Calculated
The core of the analysis is based on the **Contribution Margin formula**:

```text
Contribution Margin =
Net Revenue - (COGS + Commissions + Marketing + Logistics + Returns + Financing Costs)
```
### 3. Key Analytical Phases

**Waterfall Analysis:** Identifying where profit "leaks" in each channel

**FX Stress Test:** Simulating a +20% USD shock to measure margin resilience

**DSO Optimization:** Measuring the impact of payment terms (90 vs 60 days) on B2B profitability

**Marketing ROI Simulation:** Proposing optimal resource allocation based on marginal profit growth

## 📈 Key Strategic Insights
## 🚀 B2B: The Profit Engine

**Massive Efficiency:** B2B marketing ROI is ~22x more productive than D2C

**Financial Lever:** Reducing DSO from 90 to 60 days unlocks ~82M TL in hidden profit by reducing financing costs

## ⚠️ D2C: The Operational Challenge

**Profit Erosion:** The Entry segment is highly sensitive to return costs and marketing spend, often operating at low single-digit margins

**FX Vulnerability:** A currency shock hits D2C Entry products hardest, making operational efficiency (reducing returns) a necessity for survival

## 📋 Executive Action Plan (The Result)

**Scale B2B Volume:** Redirect growth capital to B2B segments where every 1 TL spent yields the highest incremental profit

**Optimize D2C Entry:** Implement a "Fix or Exit" strategy; reduce return rates by 50% before further scaling

**Implement Early Settlement:** Incentivize B2B clients to shorten the cash cycle, effectively turning "time" into net profit

**Premium Pivot:** Shift D2C marketing focus toward Premium/Mid segments to build a more FX-resilient portfolio

## 👤 Author

**Melek İkiz**
Data Analyst / Business Intelligence Specialist
