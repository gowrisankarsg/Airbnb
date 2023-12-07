import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px


airbnb_df = pd.read_csv("airbnb.csv")
    

def home():
    overview = """
        <style>
        p{
            font-size:22px;
            font-family:arial;
        }
        
        
        </style>
        <p>
        <span><b>OVERVIEW :</b></span>&nbsp;The project aims to leverage MongoDB Atlas for analyzing Airbnb data, employing data cleaning, and visualization techniques to gain insights into pricing variations, availability patterns, and location-based trends. The primary goals include establishing a MongoDB connection, developing interactive geospatial visualizations, and creating dynamic plots to provide users with a comprehensive understanding of the Airbnb dataset.
        </p>
    """
    technology = """
        <style>
        #tech{
            font-weight:bold;
        }
        #list{
            margin-left:100px;
            font-size:20px;
        }
        li{
            
            font-family:arial;
        }
        </style>
        <p id='tech'>TECHNOLOGIES :</p>
        <ul id='list'>
            <li>PYTHON</li>
            <li>STREAMLIT</li>
            <li>PLOTLY</li>            
            <li>PANDAS</li>
        </ul>
    """
    st.markdown(overview,unsafe_allow_html=True)
    st.markdown(technology,unsafe_allow_html=True)


def analysis():
    st.header("Price wise analysis")
    hotel_count = airbnb_df.groupby(['Country'])['Name'].count().reset_index().rename(columns={"Name":"Hotel_Count"})
    fig = px.bar(hotel_count,x="Country",y="Hotel_Count",color="Country",title="Country wise hotel count")
    st.plotly_chart(fig)
    hotel_max =  airbnb_df.iloc[airbnb_df.groupby("Country")['Price'].idxmax()]
    fig1 = px.bar(hotel_max,x="Name",y="Price",color="Country",title="Maximum price of hotel")
    st.plotly_chart(fig1)
    hotel_min =  airbnb_df.iloc[airbnb_df.groupby("Country")['Price'].idxmin()]
    fig2 = px.bar(hotel_min,x="Name",y="Price",color="Country",title="Minimum price of hotel")
    st.plotly_chart(fig2)
    st.header("Availability wise analysis")
    availability = st.selectbox("Select any one",["Availability_30","Availability_60","Availability_90","Availability_365"],index=None,placeholder="Select the availability")
    if availability == "Availability_30":
        country = st.selectbox("Select tke country",airbnb_df['Country'].unique(),index=None,placeholder="Select he country name")
        avail_30_range = st.slider("Select the availability days between 0 and 30",0,30,(10,15))
        
        avail_30 = airbnb_df[(airbnb_df["Country"] == country)&(airbnb_df['Availability_30']>avail_30_range[0])&(airbnb_df['Availability_30']< avail_30_range[1])]
        fig3 = px.pie(avail_30.head(10),values="Availability_30",names="Name",hole=.3)
        st.plotly_chart(fig3)
        
    
    if availability == "Availability_60":
        country = st.selectbox("Select tke country",airbnb_df['Country'].unique(),index=None,placeholder="Select he country name")
        avail_60_range = st.slider("Select the availability days between 0 and 60",0,60,(10,15))
        
        avail_60 = airbnb_df[(airbnb_df["Country"] == country)&(airbnb_df['Availability_60']>avail_60_range[0])&(airbnb_df['Availability_60']< avail_60_range[1])]
        fig4 = px.pie(avail_60.head(10),values="Availability_60",names="Name",hole=.3)
        st.plotly_chart(fig4)

    if availability == "Availability_90":
        country = st.selectbox("Select tke country",airbnb_df['Country'].unique(),index=None,placeholder="Select he country name")
        avail_90_range = st.slider("Select the availability days between 0 and 90",0,90,(10,15))
        
        avail_90 = airbnb_df[(airbnb_df["Country"] == country)&(airbnb_df['Availability_90']>avail_90_range[0])&(airbnb_df['Availability_90']< avail_90_range[1])]
        fig5 = px.pie(avail_90.head(10),values="Availability_90",names="Name",hole=.3)
        st.plotly_chart(fig5)

    if availability == "Availability_365":
        country = st.selectbox("Select tke country",airbnb_df['Country'].unique(),index=None,placeholder="Select he country name")
        avail_365_range = st.slider("Select the availability days range 0 to 365",0,365,(10,15))
        
        avail_365 = airbnb_df[(airbnb_df["Country"] == country)&(airbnb_df['Availability_365']>avail_365_range[0])&(airbnb_df['Availability_365']< avail_365_range[1])]
        fig6 = px.pie(avail_365.head(10),values="Availability_365",names="Name",hole=.3)
        st.plotly_chart(fig6)

    st.header("Aminities wise analysis")
    amenities = airbnb_df.iloc[airbnb_df.groupby("Country")['Amenities'].idxmax()]
    fig7 = px.sunburst(amenities,path=["Country","Name"],values="Amenities",title="Maximum amenities of hotel")
    st.plotly_chart(fig7)
    fig8 = px.sunburst(airbnb_df.iloc[airbnb_df.groupby("Country")['Amenities'].idxmin()],path=["Country","Name"],values="Amenities",title="Minimum amenities of hotel")
    st.plotly_chart(fig8)


def location():
    st.map(airbnb_df)




st.title(" :hotel: Airbnb Analysis")
option = option_menu(
    menu_title=None,
    options=["Home","Analysis","Location"],
    icons=["house","bar-chart-fill","geo-alt-fill"],
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#525ceb",
                },
                "nav-link-selected": {"background-color": "green"},
            },
)

if option == "Home":
    home()


if option == "Analysis":
    analysis()
    

if option == "Location":
    location()