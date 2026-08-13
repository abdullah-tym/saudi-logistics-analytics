# 🇸🇦 Saudi Arabia Regional Logistics & Supply Chain Analytics

## Executive Summary
This end-to-end data analytics project evaluates supply chain performance, carrier reliability, and delivery bottlenecks across key commercial and industrial hubs in Saudi Arabia (Jeddah, Riyadh, Dammam, NEOM, and Madinah). 

Using **Python**, **SQL**, and **Power BI**, the project processes 1,000 regional shipment records to identify root causes for delivery delays, evaluate courier performance against Service Level Agreements (SLAs), and provide actionable recommendations to improve **On-Time In-Full (OTIF)** delivery rates in line with Vision 2030 logistics initiatives.

---

## Key Business Insights & Strategic Recommendations

* **Primary Bottleneck Hub:** **Dammam Gateway** exhibited the lowest OTIF rate (**61.2%**), driven primarily by customs clearance documentation delays on cross-border and regional freight.
* **Carrier Efficiency Leader:** **SAL Express** achieved the highest speed rank across major metropolitan routes with an average delivery window of **1.8 days** and an overall OTIF rate of **82.4%**.
* **Financial Risk Mitigation:** Addressing warehouse processing bottlenecks at the *Riyadh Central Logistics* hub could prevent an estimated **120,000 SAR** in monthly SLA penalty fees and holding costs.
* **Payment & Fulfillment Trend:** Over **68%** of delayed shipments were associated with heavy freight (>30 KG), highlighting a capacity mismatch in last-mile delivery fleets.

---

## Tech Stack & Data Architecture

| Technology | Role in Project | Key Functions / Libraries |
| :--- | :--- | :--- |
| **Python** | Data Engineering & Validation | `Pandas`, `NumPy` (Data generation, missing value handling, SLA logic) |
| **SQL** | Analytical Processing & CTEs | `DuckDB` / `PostgreSQL` (Conditional aggregation, Window Functions, Ranking) |
| **Power BI** | Executive Reporting | Data Modeling (Star Schema), DAX Measures, Regional Performance Maps |
| **Git / GitHub** | Version Control & Documentation | Repository management, Markdown documentation |

---

## Data Schema (`saudi_logistics_data.csv`)

| Column Name | Data Type | Description | Sample Value |
| :--- | :--- | :--- | :--- |
| `Shipment_ID` | String (VARCHAR) | Unique identifier for each shipment | `KSA-LOG-1042` |
| `Origin_Hub` | String (VARCHAR) | Dispatching logistics facility | `Jeddah Port Hub` |
| `Destination_City` | String (VARCHAR) | Recipient Saudi city | `Riyadh` |
| `Courier_Partner` | String (VARCHAR) | Assigned logistics provider | `SAL Express` |
| `Distance_KM` | Integer (INT) | Route distance in kilometers | `950` |
| `Expected_Days` | Integer (INT) | Target SLA delivery window | `2` |
| `Actual_Days` | Integer (INT) | Actual transit duration | `4` |
| `Shipping_Cost_SAR`| Float (DECIMAL) | Total shipping cost in Saudi Riyals | `185.50` |
| `Weight_KG` | Float (DECIMAL) | Package weight in kilograms | `12.5` |
| `Delivery_Status` | String (VARCHAR) | Status outcome or delay reason | `Delayed - Customs` |
| `Is_Delayed` | Integer (BOOLEAN) | Binary flag (`1` = Delayed, `0` = On-Time) | `1` |

---

## SQL Deep Dive & Analytical Logic

### 1. Regional On-Time In-Full (OTIF) Performance
Calculates total volume, on-time shipments, OTIF percentage, and average delay duration grouped by regional logistics hub.

```sql
SELECT 
    Origin_Hub,
    COUNT(Shipment_ID) AS Total_Shipments,
    SUM(CASE WHEN Is_Delayed = 0 THEN 1 ELSE 0 END) AS On_Time_Shipments,
    ROUND((SUM(CASE WHEN Is_Delayed = 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(Shipment_ID)), 2) AS OTIF_Percentage,
    ROUND(AVG(Actual_Days - Expected_Days), 2) AS Avg_Delay_Days
FROM saudi_logistics_data
GROUP BY Origin_Hub
ORDER BY OTIF_Percentage ASC;