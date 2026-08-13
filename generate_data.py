import pandas as pd
import numpy as np

# Set seed for reproducible random data
np.random.seed(42)
NUM_RECORDS = 1000

# Define Saudi logistics categorical entities
hubs = [
    'Jeddah Port Hub', 
    'Riyadh Central Hub', 
    'Dammam Logistics Gateway', 
    'NEOM Supply Hub', 
    'Madinah Distribution Center'
]
cities = ['Riyadh', 'Jeddah', 'Dammam', 'NEOM', 'Madinah', 'Tabuk', 'Khobar']
couriers = ['SAL Express', 'SMSA Express', 'Aramex KSA', 'SPL (Saudi Post)']
statuses = [
    'On-Time', 
    'Delayed - Customs', 
    'Delayed - Weather', 
    'Delayed - Traffic/Route', 
    'Delayed - Warehouse'
]

# Generate synthetic features
shipment_ids = [f'KSA-LOG-{1000 + i}' for i in range(NUM_RECORDS)]
origin_hubs = np.random.choice(hubs, size=NUM_RECORDS, p=[0.30, 0.25, 0.20, 0.15, 0.10])
destination_cities = np.random.choice(cities, size=NUM_RECORDS)
courier_partners = np.random.choice(couriers, size=NUM_RECORDS, p=[0.35, 0.25, 0.25, 0.15])

# Continuous numeric variables
distances_km = np.random.randint(150, 1400, size=NUM_RECORDS)
weights_kg = np.round(np.random.uniform(0.5, 50.0, size=NUM_RECORDS), 2)

# Calculate SLA logic (Expected vs. Actual Days)
# Base SLA is 1 day per 400 KM (minimum 1 day)
expected_days = np.clip(np.ceil(distances_km / 400), 1, 5).astype(int)

# Simulate realistic delay distributions based on origin hub
delay_probabilities = []
for hub in origin_hubs:
    if hub == 'Dammam Logistics Gateway':
        delay_probabilities.append(0.38)  # Higher delay rate due to customs bottleneck
    elif hub == 'Jeddah Port Hub':
        delay_probabilities.append(0.25)
    else:
        delay_probabilities.append(0.18)

# Determine delay status and actual days taken
is_delayed = np.array([np.random.rand() < p for p in delay_probabilities])
actual_days = expected_days.copy()

# Add delay penalty days to delayed packages
actual_days[is_delayed] += np.random.randint(1, 4, size=np.sum(is_delayed))

# Assign appropriate status categories based on delay boolean
delivery_statuses = []
for delayed in is_delayed:
    if not delayed:
        delivery_statuses.append('On-Time')
    else:
        delivery_statuses.append(
            np.random.choice(
                ['Delayed - Customs', 'Delayed - Weather', 'Delayed - Traffic/Route', 'Delayed - Warehouse'],
                p=[0.40, 0.15, 0.25, 0.20]
            )
        )

# Cost logic (Base rate + Distance fee + Weight multiplier)
base_cost = 25.0
shipping_costs_sar = np.round(
    base_cost + (distances_km * 0.08) + (weights_kg * 2.5), 2
)

# Assemble DataFrame
df = pd.DataFrame({
    'Shipment_ID': shipment_ids,
    'Origin_Hub': origin_hubs,
    'Destination_City': destination_cities,
    'Courier_Partner': courier_partners,
    'Distance_KM': distances_km,
    'Expected_Days': expected_days,
    'Actual_Days': actual_days,
    'Shipping_Cost_SAR': shipping_costs_sar,
    'Weight_KG': weights_kg,
    'Delivery_Status': delivery_statuses,
    'Is_Delayed': is_delayed.astype(int)
})

# Save to CSV
df.to_csv('saudi_logistics_data.csv', index=False)
print(f"Successfully generated {NUM_RECORDS} records -> saudi_logistics_data.csv")