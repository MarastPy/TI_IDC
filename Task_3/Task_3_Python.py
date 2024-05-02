# This sript is used for matching for values in one table compared to other i set it up on matching of 60 percent bcs there were big differences
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

file_name = 'Task_3.xlsx'

excel_name = 'Website Statistics Data.csv'

column_header = ['User Name',	'Start Date',	'Subscription Revenue in Past 3 Months']

data_crm = [
['O. Sosa',	'1998-03-01',	'$1.500'],
['Mrs. Francesca Dotson',	'2005-04-01',	'$200'],
['Abel Valdez, Phd.',	'2000-12-01',	'$350'],
['Yasin Rowland, MBA',	'2010-01-01',	'$100']
]

# Read Website Statistics sample to dataframe
df_wsd = pd.read_csv(excel_name)
print(df_wsd)

# Check the column real names: there was an issue with ' name'
print(df_wsd.columns)

# Read Crm sample to dataframe
df_crm = pd.DataFrame(data_crm,  columns=column_header)
print(df_crm)

# Function for getting percentage of matching values in both tables
def fuzzy_match(first_column, second_column):
    matches = []

    for user_name in second_column:
        ratio = fuzz.token_sort_ratio(first_column, user_name)
        if ratio >= 60:  # percentage of success on name matching
            matches.append(user_name)

    return matches

# Iterate over rows in df_crm
for index, row in df_crm.iterrows():
    name = row["User Name"]
    matches = fuzzy_match(name, df_wsd[" name"])

    if matches:
        best_match = max(matches, key=lambda x: fuzz.token_sort_ratio(name, x))
        print(f"For '{name}', the best match is: {best_match} with {matches}")
        df_wsd.loc[df_wsd[" name"].isin(matches), "CRMName"] = name  # Set corrected name only where matches occurred
        print(df_wsd[" name"])
    else:
        print(f"No match found for '{name}'")
        df_wsd.loc[df_wsd["CRMName"].isnull(), "CRMName"] = df_wsd[" name"]

# Import missing values with original values
df_wsd["CRMName"] = df_wsd["CRMName"].fillna(df_wsd[" name"])
# Renaming the dataframe column
df_wsd.drop(columns=[" name"], inplace=True)
print(df_wsd)


with pd.ExcelWriter(f'{file_name}') as writer:
    df_wsd.to_excel(writer, sheet_name='Approx', index=False)