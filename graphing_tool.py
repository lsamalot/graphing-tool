import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import streamlit

excel_file = r"C:\Users\lsama\coding_c_drive\Graphing_Tool\bio107_lab_student_data.xlsx"
df_1= pd.read_excel(excel_file)

# get the column names of the df
column_names = df_1.columns.to_list() # make list out of column names
df_2 = pd.DataFrame({"index": range(len(column_names)), #create a range for the index column of the DataFrame_2
                  "columns": column_names})
print(f"DataFrame 2\n", df_2) # display the dataframe so that the user can pick the x and y column of data
# Pick your index from the df_2 for your x-axis
x = int(input("which column will be the x-axis data, according to the df_2 index?")) #integer for picking x-axix df_1 column
y_column_num = int(input("How many y-axis columns are you plotting with the same x-axis?"))
r = list(range(1, y_column_num +1)) # make a list from which to iterate from

for i in r:
    y_var = f"y_{i}" # create a new key for y-data(column)
    y_column_selection = int(input(f"From df_2, which column will be the y-{i} axis data")) # integer for picking y-axix df_1 column
    slope, intersect, r_value, p_value, std_err = linregress(df_1.iloc[:, x], df_1.iloc[:, y_column_selection]) 
    y_pred = df_1.iloc[:, x] * slope + intersect

    # graphing section
    plt.figure(i)
    plt.scatter(df_1.iloc[:, x], df_1.iloc[:, y_column_selection])
    plt.plot(df_1.iloc[:, x], y_pred)
    plt.title(f"{df_1.columns[x]} vs {df_1.columns[y_column_selection]}")
    plt.xlabel(f"{df_1.columns[x]} (cm)")
    plt.ylabel(f"{df_1.columns[y_column_selection]} (cm)")