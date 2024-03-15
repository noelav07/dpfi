import streamlit as st
import pandas as pd

input_csv_path = "/home/noel/Development/dpfi/dataset/review.csv"
output_csv_path = "/home/noel/Development/dpfi/real_reviews.csv"

# Load input and output CSVs
input_data = pd.read_csv(input_csv_path, sep='\t')
output_data = pd.read_csv(output_csv_path, sep='\t')

# Ensure both DataFrames have the same columns
common_columns = input_data.columns.intersection(output_data.columns)
input_data = input_data[common_columns]
output_data = output_data[common_columns]

# Display input CSV
st.subheader("Input Dataset")
st.write(input_data)

# Display number of rows and columns in input CSV
num_rows_input, num_cols_input = input_data.shape
st.write(f"Number of rows in input CSV: {num_rows_input}")
st.write(f"Number of columns in input CSV: {num_cols_input}")

# Display output CSV
st.subheader("Output Data")
st.write(output_data)

# Display number of rows and columns in output CSV
num_rows_output, num_cols_output = output_data.shape
st.write(f"Number of rows in output CSV: {num_rows_output}")
st.write(f"Number of columns in output CSV: {num_cols_output}")

# Find differences between input and output CSV
if input_data.shape == output_data.shape:
    differences = (input_data != output_data).any(axis=None)
    if differences:
        st.write("Differences found between input and output CSV.")
    else:
        st.write("No differences found between input and output CSV.")
# else:
#     st.write("Input and output CSVs have different shapes and cannot be compared directly.")

# else:
#     st.markdown("Differences found between input and output CSV.")


input_not_in_output = input_data[~input_data.isin(output_data)].dropna()
if not input_not_in_output.empty:
    st.subheader("Deceptive Review")
    st.write(input_not_in_output)
else:
    st.write("All rows from input CSV are present in output CSV.")
