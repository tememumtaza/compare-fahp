import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page title
st.set_page_config(page_title="FAHP vs Konvesional Ranking Points", page_icon=":bar_chart:")

# Create a function to calculate the ranking difference and output the modified DataFrame
def calculate_ranking_difference(df):
    # Get the first and second columns as data_a and data_b
    data_a = df.iloc[:, 0].tolist()
    data_b = df.iloc[:, 1].tolist()

    # create the DataFrame
    df_out = pd.DataFrame(columns=['Alternatif', 'Rank Konvesnional', 'Rank Fuzzy AHP', 'Keterangan', 'Selisih Index'])
    for i, a_value in enumerate(data_a):
        b_value = data_b[i]
        # find the index of the values in data_b
        a_index = data_b.index(a_value)
        b_index = data_b.index(b_value)

        # compare the indexes to determine if A is higher, equal, or lower
        if a_index < b_index:
            output = 'Lebih Tinggi'
        elif a_index > b_index:
            output = 'Lebih Rendah'
        else:
            output = 'Sama'

        # calculate the difference in index for this row
        selisih_index = abs(a_index - b_index)

        # add a new row to the DataFrame
        df_out.loc[i] = [a_value, a_index+1, b_index+1, output, selisih_index]

    # output the modified DataFrame to the user
    st.write(df_out.set_index('Alternatif'))

    # output the DataFrame to a CSV file
    df_out.to_csv('output.csv', index=False)

# Set the title and description of the app
st.title("FAHP vs Konvesional Ranking Points")
st.write("This app compares the ranking points of two methods, FAHP and Konvesional.")

# Add a file uploader to load the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    calculate_ranking_difference(df)

    # Create a scatter plot of the ranking points
    fig, ax = plt.subplots()
    ax.scatter(df['FAHP'], range(1, len(df)+1), label='FAHP')
    ax.scatter(df['Konvesional'], range(1, len(df)+1), label='Konvesional')

    # Set the y-axis label and title
    ax.set_ylabel('Alternatif')
    ax.set_title('FAHP vs Konvesional Ranking Points')

    # Display the legend and show the plot
    ax.legend()
    st.pyplot(fig)