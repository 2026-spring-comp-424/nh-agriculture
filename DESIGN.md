## Design nh_agriculture_data.csv
## Developer: Kehinde Fabiyi

### Design for main program(nh_agriculture_app.py)
- Imports `pandas as pd` for reading and analyzing CSV data
- Imports `matplotlib.pyplot as plt` for creating charts 
- Defines variables for key statistics:
  - `state` = "New Hampshire"
  - `total_farms` = 3850
  - `total_acres` = 420000
  - `avg_farm_size` = 109
  - `maple_syrup` = 152000
  - `divider` = "==========================="
- Reads `nh_agriculture_data.csv` using `pd.read_csv()` and assigns to `data`
- Sets display options to show all columns using `pd.set_option()`

### Design for Summary Output
- Prints title using `state` variable 
- Prints `divider` to separate sections 
- Prints `total_farms`, `total_acres`, `avg_farm_size`, `maple_syrup` with labels
- Displays a summary of key NH agriculture statistics for 2025 

### Design for Maple Syrup Analysis
- Filters `data` where `category` equals `Maple Syrup`
- Assigns filtered result to `maple_data`
- Calls `print()` to show `maple_data`
- Shows the maple syrup data including yield per tap and total production

### Design for Hay Analysis 
- Filters `data` where `category` equals `Hay`
- Assigns filtered result to `hay_data`
- Calls `print()` to show `hay_data`
- Shows all four hay measurements including acres, production, price and value

### Design for Value of Production Analysis
- Filters `data` where `metric` equals `Value of Production`
- Assigns filtered result to `all_value`
- Calls `print()` to show `all_value`
- Shows the dollar value for all three hay categories

### Design for Total Hay Value Calculation
- Takes `all_value["value"]` column 
- Calls `.sum()` to add all values together 
- Assigns result to `total_hay_value`
- Calls `print()` to display result 
- Adds up all hay production values to get the total in dollars

### Design for Hay Value Bar Chart
- Creates figure with  `figsize=(8, 5)`
- Calls `plt.bar()` with:
  - x = `all_value["category"]` (category names)
  - y = `all_value["value"]` (dollar values)
  - color = `green`
- Adds title: `Hay Value of Production in New Hampshire (2025)`
- Adds x label: `Category`
- Adds y label: `Value in Dollars`
- Saves chart as `hay_chart.png` using `plt.savefig()`
- Prints confirmation message: `Chart saved as hay_chart.png!`

### Design for Farm Operations Bar Chart
- Filters data where category equals `Farm Operations`
- Assigns filtered result to `farm_data`
- Creates figure with `figsize=(8, 5)`
- Calls `plt.bar()` with:
   - x = farm_data["metric"] (metric names)
   - y = farm_data["value"] (values)
   - color = `blue`
- Adds title: `Farm Operations in New Hampshire (2025)`
- Adds x label: `Metric`
- Adds y label: `Value`
- Saves chart as `farm_chart.png` using `plt.savefig()`
- Prints confirmation message: `Farm chart saved as farm_chart.png!`

### Design for Maple Syrup Bar Chart
- Uses `maple_data` already filtered earlier in the program
- Creates figure with `figsize=(8, 5)`
- Calls `plt.bar()` with:
  - x = maple_data["metric"] (metric names)
  - y = maple_data["value"] (values)
  - color = `orange`
- Adds title: `Maple Syrup Production in New Hampshire (2025)`
- Adds x label: `Metric`
- Adds y label: `Value`
- Saves chart as `maple_chart.png` using `plt.savefig()`
- Prints confirmation message: `Maple chart saved as maple_chart.png!`