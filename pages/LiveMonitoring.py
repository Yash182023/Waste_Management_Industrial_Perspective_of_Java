import pandas as pd
import plotly.express as px
import streamlit as st 

st.title("Liveonitoring of Cities")

style = """
<style>
    .main{
        background: rgb(2,189,233);
        background: linear-gradient(148deg, rgba(2,189,233,1) 0%, rgba(0,254,255,1) 37%, rgba(149,246,255,1) 64%, rgba(2,189,233,1) 100%);

    h1{
        color:#000000;
    }
    p{
        color:#000000;
    }
</style>

"""


st.markdown(style,unsafe_allow_html=True)

# Data for Indian cities with latitude, longitude, and severity level
data = {
    'Location': ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai",
                 "Hyderabad", "Pune", "Ahmedabad", "Surat", "Jaipur",
                 "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
                 "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna",
                 "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik",
                 "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar",
                 "Varanasi"],
    'Latitude': [19.0760, 28.7041, 12.9716, 22.5726, 13.0827,
                 17.3850, 18.5204, 23.0225, 21.1702, 26.9124,
                 26.8467, 26.4499, 21.1458, 22.7196, 19.2183,
                 23.2599, 17.6868, 18.5204, 25.5941, 22.3072,
                 28.6139, 30.9000, 27.1767, 27.1767, 19.9975,
                 28.4089, 22.3039, 19.0760, 19.2170, 19.4359],
    'Longitude': [72.8777, 77.1025, 77.5946, 88.3639, 80.2707,
                  78.4867, 73.8567, 72.5714, 72.8311, 75.7873,
                  80.9462, 80.3319, 79.0882, 75.8577, 72.9781,
                  77.4126, 83.2185, 73.8567, 85.1376, 83.0150,
                  77.2090, 29.4000, 78.0071, 78.0071, 73.0169,
                  77.3090, 70.8022, 72.8777, 73.0575, 72.8616],
    'Severity': ['High', 'Medium', 'Low', 'Medium', 'High',
                 'Low', 'High', 'Medium', 'Low', 'High',
                 'Medium', 'High', 'Low', 'High', 'Medium',
                 'Low', 'Medium', 'Low', 'High', 'Medium',
                 'High', 'Low', 'Medium', 'Medium', 'High',
                 'Low', 'Medium', 'High', 'Medium', 'Low']
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot the data on a map
fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name='Location',
                        color='Severity', zoom=4, mapbox_style='carto-positron',
                        color_discrete_map={'High': 'red', 'Medium': 'yellow', 'Low': 'green'})
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)

st.write(df)