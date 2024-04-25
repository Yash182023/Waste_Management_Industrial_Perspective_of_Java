# import csv

# # Sample data for Indian cities
# data = [
#     ["Plastic", 100, "Recycling", "Mumbai", 2023],
#     ["Paper", 150, "Recycling", "Kolkata", 2023],
#     ["Organic", 200, "Composting", "Pune", 2023],
#     ["Plastic", 120, "Landfill", "Delhi", 2023],
#     ["Paper", 80, "Recycling", "Luckhnow", 2023],
#     ["Organic", 180, "Composting", "Ahmedabad", 2023],
#     ["Plastic", 90, "Recycling", "Bangalore", 2023],
#     ["Paper", 100, "Landfill", "Bhopal", 2023],
#     ["Organic", 150, "Composting", "Bhubaneshwar", 2023]
# ]

# # Write data to CSV
# with open('waste_management_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Type of waste", "Quantity (kg)", "Disposal method", "Geographic location", "Time period"])
#     writer.writerows(data)

# print("CSV file created successfully!")
import csv
import random

# List of Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai",
    "Hyderabad", "Pune", "Ahmedabad", "Surat", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna",
    "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar",
    "Varanasi"
]

# Generate sample data for 30 cities with random years between 2020 and 2024
data = []
for city in indian_cities:
    for _ in range(3):  # Generate data for each city for 3 different years
        waste_type = random.choice(["Plastic", "Paper", "Organic"])
        quantity = random.randint(50, 300)  # Random quantity between 50 and 300 kg
        disposal_method = random.choice(["Recycling", "Composting", "Landfill"])
        year = random.randint(2020, 2024)  # Random year between 2020 and 2024
        data.append([waste_type, quantity, disposal_method, city, year])

# Write data to CSV
with open('waste_management_data_new.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Type of waste", "Quantity (kg)", "Disposal method", "Geographic location", "Time period"])
    writer.writerows(data)

print("CSV file created successfully!")
