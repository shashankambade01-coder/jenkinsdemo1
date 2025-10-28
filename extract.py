import pandas as pd

print("Extract Data")

data = {
     'Id': [101,102,103]
    ,'Name': ['John', 'Jane', 'Doe']
    ,'Age': [28, 34, 29]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)