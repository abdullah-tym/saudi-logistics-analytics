-- 1. Regional On-Time In-Full (OTIF) Performance by Hub
SELECT 
    Origin_Hub,
    COUNT(Shipment_ID) AS Total_Shipments,
    SUM(CASE WHEN Is_Delayed = 0 THEN 1 ELSE 0 END) AS On_Time_Shipments,
    ROUND((SUM(CASE WHEN Is_Delayed = 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(Shipment_ID)), 2) AS OTIF_Percentage,
    ROUND(AVG(Actual_Days - Expected_Days), 2) AS Avg_Delay_Days
FROM saudi_logistics_data
GROUP BY Origin_Hub
ORDER BY OTIF_Percentage ASC;


-- 2. Courier Speed & Cost Efficiency Ranking
WITH CourierStats AS (
    SELECT 
        Courier_Partner,
        COUNT(Shipment_ID) AS Total_Deliveries,
        ROUND(AVG(Actual_Days), 2) AS Avg_Delivery_Time,
        ROUND(SUM(Shipping_Cost_SAR), 2) AS Total_Cost_SAR,
        ROUND(AVG(Shipping_Cost_SAR / Weight_KG), 2) AS Cost_Per_KG
    FROM saudi_logistics_data
    GROUP BY Courier_Partner
)
SELECT 
    Courier_Partner,
    Total_Deliveries,
    Avg_Delivery_Time,
    Cost_Per_KG,
    DENSE_RANK() OVER (ORDER BY Avg_Delivery_Time ASC) AS Speed_Rank,
    DENSE_RANK() OVER (ORDER BY Cost_Per_KG ASC) AS Cost_Efficiency_Rank
FROM CourierStats;


-- 3. Top Bottleneck Routes & Delay Reasons
SELECT 
    Origin_Hub,
    Destination_City,
    Delivery_Status,
    COUNT(Shipment_ID) AS Incident_Count,
    ROUND(SUM(Shipping_Cost_SAR), 2) AS Total_Impacted_Value_SAR
FROM saudi_logistics_data
WHERE Delivery_Status LIKE 'Delayed%'
GROUP BY Origin_Hub, Destination_City, Delivery_Status
HAVING COUNT(Shipment_ID) > 3
ORDER BY Total_Impacted_Value_SAR DESC;