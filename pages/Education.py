import streamlit as st 


style = """
<style>
    .main{
        background: rgb(0,22,140);
        background: linear-gradient(148deg, rgba(0,22,140,1) 0%, rgba(0,185,255,1) 37%, rgba(0,185,255,1) 64%, rgba(23,20,161,1) 100%);
</style>

"""


st.markdown(style,unsafe_allow_html=True)


st.title("Education Page")

st.write("Welcome to the Education Page of our Waste Management Dashboard! Here, we provide useful information and resources to help you learn more about waste management practices and promote sustainability.")

st.header("Why is Waste Management Important?")
st.write("Effective waste management is crucial for protecting the environment, conserving resources, and minimizing pollution. By properly managing waste, we can reduce greenhouse gas emissions, prevent contamination of soil and water, and create a healthier environment for future generations.")

st.header("Tips for Sustainable Waste Management")
st.write("Here are some tips to help you reduce waste and promote sustainable waste management practices:")
st.write("- Reduce, Reuse, Recycle: Follow the 3 Rs principle to minimize waste generation.")
st.write("- Compost Organic Waste: Convert food scraps and yard waste into nutrient-rich compost for gardens.")
st.write("- Choose Eco-Friendly Products: Opt for products with minimal packaging and made from recycled materials.")
st.write("- Proper Disposal: Dispose of hazardous waste such as batteries, electronics, and chemicals responsibly at designated collection sites.")

st.header("Educational Resources")
st.write("Explore these educational resources to learn more about waste management and sustainability:")
st.markdown("- [EPA: Waste Management](https://www.epa.gov/waste)")
st.markdown("- [UNEP: Sustainable Consumption and Production](https://www.unep.org/explore-topics/sustainable-consumption-and-production)")

st.header("Get Involved")
st.write("Take action in your community to promote sustainable waste management:")
st.write("- Participate in local clean-up events.")
st.write("- Advocate for waste reduction policies and recycling initiatives.")
st.write("- Educate others about the importance of waste management and environmental conservation.")

st.write("Together, we can make a positive impact on our planet by adopting responsible waste management practices and fostering a culture of sustainability.")
