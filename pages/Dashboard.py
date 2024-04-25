import streamlit as st
import pandas as pd
import plotly.express as px


style = """
<style>
    .main{
        background: rgb(0,22,140);
        background: linear-gradient(148deg, rgba(0,22,140,1) 0%, rgba(109,66,241,1) 50%, rgba(23,20,161,1) 100%);
    }
</style>

"""


st.markdown(style,unsafe_allow_html=True)

# Load the data
df = pd.read_csv('C:/Users/sharm/OneDrive/Desktop/Waste_Management/waste_management_data_new_extended.csv')

# Sidebar
st.sidebar.title('Filter Data')
selected_city = st.sidebar.selectbox('Select City', sorted(df['Geographic location'].unique()))
selected_year = st.sidebar.selectbox('Select Year', sorted(df['Time period'].unique()))

# Filter the data
filtered_df = df[(df['Geographic location'] == selected_city) & (df['Time period'] == selected_year)]

# Main content
st.title('Waste Management Dashboard')

# Display filtered data
st.write(f"Showing data for {selected_city} in {selected_year}:")
st.write(filtered_df)

# Plot waste quantity by disposal method
fig = px.bar(filtered_df, x='Disposal method', y='Quantity (kg)', color='Type of waste', barmode='group', title='Waste Quantity by Disposal Method')
st.plotly_chart(fig)

# Calculate total waste quantity by city
city_waste = df.groupby('Geographic location')['Quantity (kg)'].sum().reset_index()

# Plot total waste quantity by city
fig_city = px.bar(city_waste, x='Geographic location', y='Quantity (kg)', title='Total Waste Quantity by City')
fig_city.update_layout(xaxis_title='City', yaxis_title='Total Quantity (kg)')
st.plotly_chart(fig_city)
