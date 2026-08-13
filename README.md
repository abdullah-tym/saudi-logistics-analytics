# 🇸🇦 Saudi Arabia Regional Logistics & Supply Chain Optimization

## Executive Summary
This analytics project evaluates supply chain performance and delivery bottlenecks across key Saudi logistics hubs (Jeddah, Riyadh, Dammam, NEOM). Using Python, SQL, and Power BI, the project identifies root causes for delivery delays and provides actionable recommendations to improve On-Time In-Full (OTIF) rates.

![Dashboard Preview](dashboard_preview.png)

## Business Impact & Key Insights
* **Primary Bottleneck Hub:** *Dammam Gateway* exhibited the lowest OTIF rate (61%), driven largely by customs clearance delays.
* **Carrier Efficiency:** *SAL Express* achieved the highest speed rank with an average delivery window of 1.8 days across major metropolitan routes.
* **Cost Savings Potential:** Addressing warehouse processing delays in Riyadh could prevent an estimated 120,000 SAR in monthly SLA penalty fees.

## Tech Stack
* **Python (Pandas, NumPy):** Synthetic logistics data engineering and SLA violation tagging.
* **SQL (PostgreSQL / BigQuery):** Window functions (`DENSE_RANK`), conditional aggregation (`CASE WHEN`), CTEs for route ranking.
* **Power BI:** Interactive performance dashboard with key supply chain KPIs.

## Repository Structure
```text
├── generate_data.py          # Python data generation & processing
├── warehouse_analysis.sql    # Analytical SQL queries (OTIF, Cost, Ranking)
├── saudi_logistics_data.csv  # Cleaned dataset (1,000 shipments)
├── dashboard_preview.png     # Power BI / Excel dashboard screenshot
└── README.md                 # Executive summary & findings
