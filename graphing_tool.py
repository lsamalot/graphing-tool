import pandas as pd
from scipy.stats import linregress
import streamlit as st
import matplotlib.pyplot as plt


excel_file = r"C:\Users\lsama\coding_c_drive\Graphing_Tool\bio107_lab_student_data.xlsx"
df_1= pd.read_excel(excel_file)

# get the column names of the df
column_names = df_1.columns.to_list() # make list out of column names


# streamlit picking the x-axis
x_axis_selection = st.radio("Select the X-axis for the graph",
            column_names)
st.write(x_axis_selection) 
st.divider()

# processing the data for the plotting math
x_axis = df_1[x_axis_selection]
st.write("This is the x-axis data", x_axis) # later remove the wording
st.divider()

# streamlit picking # of plots (lines) for the graph
num_plots = int(st.number_input("Enter the number of plots (lines) you want on the graph", min_value=1, max_value=10, placeholder="Enter number here", step=1))
st.write(num_plots)
st.divider() 

# set up the plotting canvas
fig, ax = plt.subplots()

st.divider()

# iterate as many times as the number of plots, to select all y-axis data
for i in range(1, num_plots+1):
    # streamlit version of 'y_column_selection'
    y_column_selection = st.radio(f"Pick which column will be the y-{i} axis data", options=column_names, index=0)
    y_data = df_1[y_column_selection]
    st.write(y_data) #just to see what the selection would be - erase afterwards

    # Here we will take y_data and run linregress
    slope, intercept, r_value, p_value, std_err = linregress(x_axis, y_data)

    # Compute regression line
    y_fit = slope * x_axis + intercept

    # plot original data
    ax.scatter(x_axis, y_data, label=f"{y_column_selection} (R²={r_value**2:.2f})")
    ax.plot(x_axis, y_fit, '--', label=f"{y_column_selection} fit")

# Customize plot
ax.set_xlabel(x_axis_selection)
ax.set_ylabel("Y-axis values")
ax.set_title("Linear Regression Plot")
ax.legend()
ax.grid(True)

# Show plot in Streamlit
st.pyplot(fig) 
