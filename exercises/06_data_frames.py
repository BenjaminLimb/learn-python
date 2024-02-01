import pandas as pd

# Table Name: food
# Columns: "fdc_id","data_type","description","food_category_id","publication_date"
# Example Row: "319874","sample_food","HUMMUS, SABRA CLASSIC","16","2019-04-01"
root_dir = '/Users/benjaminlimb/git/learn-python/food/FoodData_Central_foundation_food_csv_2023-10-26/'
food = pd.read_csv(root_dir + "food.csv")
food = food.query('description == "Hummus"')
print(food)

# Table Name: nutrient
# Columns: "id","name","unit_name","nutrient_nbr","rank"
# Example Row: "2047","Energy (Atwater General Factors)","KCAL","957","280.0"
nutrient = pd.read_csv(root_dir + "nutrient.csv")
print(nutrient)

# Table Name: food_nutrient
# Columns: "id","fdc_id","nutrient_id","amount","data_points","derivation_id","min","max","median","footnote","min_year_acquired"
# Example Row: "2201847","319877","1051","56.3","1","1","","","","",""
food_nutrient = pd.read_csv(root_dir + "food_nutrient.csv", dtype={})
print(food_nutrient)

# Join the food table with the nutrient table using the food_nutrient table as a bridge. Relationships are as follows:
# Join food and food_nutrient on fdc_id, join food_nutrient and nutrient on nutrient_id
# Create a dataframe with this joined data

# https://chat.openai.com/c/81a0b0c1-add2-4452-a074-a2e28df76036

# Join food and food_nutrient on fdc_id
merged_data = pd.merge(food, food_nutrient, left_on="fdc_id", right_on="fdc_id", how="inner")

# Join the resulting dataframe with nutrient on nutrient_id
merged_data = pd.merge(merged_data, nutrient, left_on="nutrient_id", right_on="id", how="inner")

print(merged_data)


exit()
