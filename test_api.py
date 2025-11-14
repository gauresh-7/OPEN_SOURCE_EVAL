import requests  # This tool lets us make "phone calls" to the internet
import pandas as pd # This is the "Excel for Python" tool

# 1. Setup the "Phone Number" (The API URL)
# "IN" is the code for India. "NY.GDP.MKTP.CD" is the code for GDP.
url = "http://api.worldbank.org/v2/country/IN/indicator/NY.GDP.MKTP.CD?format=json&per_page=50"

print("--- 1. Calling the World Bank... ---")
# 2. Make the call
response = requests.get(url)

# 3. Get the raw data (JSON)
# This data usually comes in a messy list format.
data = response.json()

# The World Bank sends a list with two things:
# data[0] is just info about pages (we don't need this now)
# data[1] is the actual list of GDP numbers (we need this!)
raw_data = data[1]

print("--- 2. Organizing data with Pandas... ---")

# 4. The Magic Step: Create a DataFrame
# A "DataFrame" is just a fancy name for a Table.
df = pd.DataFrame(raw_data)

# 5. Clean the Table
# We only care about the 'date' (Year) and 'value' (GDP Amount)
# Let's pick those two columns and ignore the rest.
simple_table = df[['date', 'value']]

# Let's rename the columns to make them look nice
simple_table.columns = ['Year', 'GDP (USD)']

# 6. Show the result!
print("\nHere is the data for India:")
print(simple_table.head(10)) # .head(10) means "Show me the top 10 rows"