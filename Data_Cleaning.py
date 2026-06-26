import pandas as pd

# Load file (use your file name)
df = pd.read_excel("train.xlsx")

# Preview
df.head()

# Check null values
print(df.isnull().sum())

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check data types
print(df.info())

# Extract Year & Month
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%B')


print("Total Sales:", df['Sales'].sum())


print(df.groupby('Category')['Sales'].sum())


print(df.groupby('Region')['Sales'].sum())


print(df.groupby('Month Name')['Sales'].sum().sort_values())


print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))


df.to_csv("cleaned_data.csv", index=False)