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

# adding x-axis units
x_units_question = st.checkbox("Do you require adding units for the x-axis")
if x_units_question:
    x_axis_unit_entry = st.text_input("Enter the x-axis units")
    st.write(f"x-axis units will be: {x_axis_unit_entry}")
else:
    x_axis_unit_entry = None
st.divider()

# processing the data for the plotting math
x_axis = df_1[x_axis_selection]
st.write("This is the x-axis data", x_axis) # later remove the wording
st.divider()

# streamlit picking # of plots (lines) for the graph
num_plots = int(st.number_input("Enter the number of plots (lines) you want on the graph", min_value=1, max_value=10, placeholder="Enter number here", step=1))
st.write(num_plots)
st.divider() 

# Enter the units for the y-axis
y_units_question = st.checkbox("Do you require adding units for the y-axis")
if y_units_question:
    y_axis_unit_entry = st.text_input("Enter the y-axis units")
    st.write(f"y-axis units will be: {y_axis_unit_entry}")
else: 
    y_axis_unit_entry = None
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

st.divider()
# Customize plot
ax.set_xlabel(f"{x_axis_selection} ({x_axis_unit_entry})")
y_axis_label_option = st.checkbox("Add a Custom Y-axis Label")  # adding an option for y-axis label
if y_axis_label_option:
    y_axis_label = st.text_input("Enter y-axis label here")
else: 
    y_axis_label = "Y-axis values"
ax.set_ylabel(f"{y_axis_label} ({y_axis_unit_entry})")
graph_title = st.checkbox("Add a Custom Graph Title")  # adding an option for a title
if graph_title:
    title_entry = st.text_input("Enter Title Here")
else: 
    title_entry = "Linear Regression Plot"
ax.set_title(title_entry)
ax.legend()
ax.grid(True)

# Show plot in Streamlit
st.pyplot(fig)
