import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        # m = leafmap.Map(center=[40, -100], zoom=4)
        # cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        # regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"

        # m.add_geojson(regions, layer_name="US Regions")
        # m.add_points_from_xy(
        #     cities,
        #     x="longitude",
        #     y="latitude",
        #     color_column="region",
        #     icon_names=["gear", "map", "leaf", "globe"],
        #     spin=True,
        #     add_legend=True,
        # )
        cities = "https://chinchillaz.github.io/streamlit-hw/country_interest.geojson"
        m.add_geojson(cities, layer_name="Intersect towns")
        
        m = leafmap.Map(minimap_control=True)
        m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)
        geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
        
        # Define a style function to set line color to navy
        style = {"color": "navy", "weight": 3, "opacity": 0.8}
        m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)

m.to_streamlit(height=700)
