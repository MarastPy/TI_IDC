from openpyxl.workbook import Workbook

import pandas as pd
import numpy as np

### Documentation ###
file_name = 'Task_1.xlsx'

# This excercise contains multiple lists lets put them together.
# Columns represent years
column_header = ['2019','2020',	'2021',	'2022',	'2023',	'2024',	'2025']

# Rows represent Spending Technology Categories
row_header = ['Business Services', 'Hardware', 'IT Services', 'Software', 'Telecom Services']

# Each row in the matrix below represent one Technology and each column one Year of data
test_data = [
    [477.471,	 484.593,	 518.988,	 572.115,	 640.693,	 720.916,	 814.72],
    [2597.189,	2701.082,	3149.978,	3320.256,	3392.421,	3438.651,	3467.47],
    [2600.082,	2628.529,	2896.001,	3286.340,	    None,	4215.841,	4787.348],
    [1556.779,	1654.627,	1831.514,	2025.143,	2237.725,	2481.181,	2762.201],
    [3188.570,	3201.79,	3242.249,	    None,   3355.419,	3402.868,	3444.409]
]

df_row_headers = pd.DataFrame(row_header, columns=['Row Header'])
#print(df_row_headers)
df = pd.DataFrame(test_data, index=row_header, columns=column_header)
#print(df)


# Documentation for interpolate function: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
#
def dfInterpolate(df):
    df_interpolated = df.interpolate(method='linear', axis=0)
    return df_interpolated

print(dfInterpolate(df))


df_fin = pd.concat([df_row_headers, dfInterpolate(df)], axis=0)

# Save df to excel
with pd.ExcelWriter(f'{file_name}') as writer:
    df_fin.to_excel(writer, sheet_name='Approx', index=False)




# Propose a solution how to aproximate the missing points
print(test_data)


