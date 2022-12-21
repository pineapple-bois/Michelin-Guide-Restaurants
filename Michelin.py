import pandas as pd

michelin = pd.read_csv('michelin_my_maps.csv')
print(f"Columns: {michelin.columns.tolist()}\n")
print(f"Head:\n{michelin.head(10)}")

michelin = michelin[['Name', 'Address', 'Location', 'Price', 'Cuisine',
                     'Longitude', 'Latitude', 'PhoneNumber', 'Url', 'WebsiteUrl', 'Award']]
print(f"\nNew Head:\n{michelin.head(10)}")

michelin.columns = michelin.columns.str.lower()
print(f"\nNew Columns: {michelin.columns.tolist()}\n")

michelin.rename({'phonenumber': 'phone_number', 'websiteurl': 'website_url'}, axis=1, inplace=True)
print(f"\nNew Columns: {michelin.columns.tolist()}\n")


for i in michelin:
    print(f"\nUnique {i}s: {michelin[i].unique()}.\nTotal unique = {len(michelin[i].unique())} values")