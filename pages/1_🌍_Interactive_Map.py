import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    # m = leafmap.Map(
    #     locate_control=True, latlon_control=True, draw_export=True, minimap_control=True, center = [42.5, -4.0], zoom = 7 , minimap_control=True
    # )
    # #m.add_basemap(basemap)
    # m = leafmap.Map(minimap_control=True)
    # #m.add_basemap("OpenTopoMap")
    # m.to_streamlit(height=700)
    # Create the map
    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True,
        center=[42.5, -4.0], zoom=7
    )

    # Clear previous layers if any
    m.clear_layers()

    # Add GeoJSON line to the map
    geojson_url = "https    ://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"

    # Define a style function to set line color to navy
    style = {"color": "navy", "weight": 3, "opacity": 0.8}

    # Add the GeoJSON to the map with the defined style
    m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)

    # Display the map in streamlit
    m.to_streamlit(height=700)
