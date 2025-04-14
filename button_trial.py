import pandas as pd
from scipy.stats import linregress
import streamlit as st


excel_file = r"C:\Users\lsama\coding_c_drive\Graphing_Tool\bio107_lab_student_data.xlsx"
df_1= pd.read_excel(excel_file)

# get the column names of the df
column_names = df_1.columns.to_list() # make list out of column names
df_2 = pd.DataFrame({"index": range(len(column_names)), #create a range for the index column of the DataFrame_2
                  "columns": column_names})
# streamlit picking the x-axis
x = st.radio("Pick you X-axis for the graph", options=df_2["columns"], index=0)
st.write(x) # erase after
st.divider()

# streamlit picking # of y-axis columns to graph
y_column_num = st.number_input("Enter the number of y-axis columns to graph", min_value=1, max_value=10, placeholder="Place number here", step=1)
st.write(y_column_num)
st.divider()


r = list(range(1, y_column_num + 1)) #make a list (processes from y_column_num) from which to iterate from
for i in r:
    y_var = f"y_{i}" # Create a new key for y-data(column) 
    # streamlit version of 'y_column_selection'
    y_column_selection = st.radio(f"Pick which column will be the y-{i} axis data", options=df_2["columns"], index=0)
    st.write(y_column_selection) #just to see what the selection would be - erase afterwards

    # #processing the data for the graphing and r_values for each iteration
    # slope, intersect, r_value, p_value, std_err = linregress(df_1.iloc[:, x], df_1.iloc[:, y_column_selection])
    # y_pred = df_1.iloc[:, x] * slope + intersect

    # # graphing section for each iteration
    # plt.figure(i)
    # plt.scatter(df_1.iloc[:, x], df_1.iloc[:, y_column_selection])
    # plt.plot(df_1.iloc[:, x], y_pred)
    # plt.title(f"{df_1.columns[x]} vs {df_1.columns[y_column_selection]}")
    # plt.xlabel(f"{df_1.columns[x]} (cm)")
    # plt.ylabel(f"{df_1.columns[y_column_selection]} (cm)")