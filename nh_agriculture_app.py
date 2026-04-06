"""
NH Agriculture Data Project
Analyzes agricultural trends in New Hampshire
Data Source: USDA NASS 2025
"""

# NH Agriculture Data Project
# Developer: Kehinde Fabiyi
# COMP 424 - Spring 2026

import pandas as pd
import matplotlib.pyplot as  plt

# Variables 
state = "New Hampshire"
total_farms = 3850
total_acres = 420000
avg_farm_size = 109
maple_syrup = 152000
divider = "============================="


data = pd.read_csv("nh_agriculture_data.csv")

# --- Display settings ---
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

print("Agriculture in", state)
print(divider)
print("Total farms (2025):", total_farms)
print("Total farmland:", total_acres, "acres")
print("Average farm size:", avg_farm_size, "acres")
print("Maple syrup produced:", maple_syrup, "gallons")

# --- Analyze the data ---
print(divider)
print("Maple Syrup Data:")
maple_data = data[data["category"] == "Maple Syrup"]
print(maple_data)

print(divider)
print("Hay:")
hay_data = data[data["category"] == "Hay"]
print(hay_data)

print(divider)
print("Value of production - All Categories:")
all_value = data[data["metric"] == "Value of Production"]
print(all_value)

print(divider)
print("Total Hay Production Value")
total_hay_value = all_value["value"].sum()
print("$", total_hay_value)

plt.figure(figsize=(8, 5))
plt.bar(all_value["category"], all_value["value"], color="green")
plt.title("Hay Value of Production in New Hampshire (2025)")
plt.xlabel("Category")
plt.ylabel("Value in Dollars")
plt.tight_layout()
plt.savefig("hay_chart.png")
print("Chart saved as hay_chart.png!")

farm_data = data[data["category"] == "Farm Operations"]
plt.figure(figsize=(8, 5))
plt.bar(farm_data["metric"], farm_data["value"], color="blue")
plt.title("Farm Operations in New Hampshire (2025)")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("farm_chart.png")
print("Farm chart saved as farm_chart.png!")

plt.figure(figsize=(8, 5))
plt.bar(maple_data["metric"], maple_data["value"], color="orange")
plt.title("Maple Syrup Production in New Hampshire (2025)")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("maple_chart.png")
print("Maple chart saved as maple_chart.png!")
