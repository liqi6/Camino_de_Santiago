import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True, center = [42.5, -4.0], zoom = 8 
    )
    m.add_basemap(basemap)

    geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
    # Define a style function to set line color to navy
    style = {"color": "navy", "weight": 3, "opacity": 0.8}
    m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)
    
    m.to_streamlit(height=700)


    st.header("intro")
    
    markdown = """
    
    | **路線名稱**      | **起點**                  | **終點**                        | **距離**       | **特色**                        |
    |------------------|-------------------------|--------------------------------|---------------|--------------------------------|
    | **法國之路**      | 聖讓-皮耶-德波爾特 🇫🇷    | 聖地亞哥-德孔波斯特拉 (西班牙)       | 約 780 公里    | 最受歡迎，設施完善，風景多樣。           |
    | **北方之路**      | 依倫 (西班牙)             | 聖地亞哥-德孔波斯特拉            | 約 825 公里    | 沿北部海岸線，風景優美但地形較艱難。         |
    | **葡萄牙之路**    | 里斯本/波爾圖 (葡萄牙)     | 聖地亞哥-德孔波斯特拉            | 約 620 公里    | 穿越葡萄牙北部，歷史與美食並存。          |
    | **銀之路**        | 塞維亞 (西班牙)           | 聖地亞哥-德孔波斯特拉            | 約 1000 公里   | 途經西班牙內陸，古羅馬遺跡豐富。          |
    | **原始之路**      | 奧維耶多 (西班牙)         | 聖地亞哥-德孔波斯特拉            | 約 321 公里    | 最古老的路線，山地挑戰性高，風景壯麗。      |
    | **英格蘭之路**    | 拉科魯尼亞/費羅爾 (西班牙)  | 聖地亞哥-德孔波斯特拉            | 約 120 公里    | 適合短期徒步，當年英格蘭人登岸之路。         |
    | **聖雅各海岸之路**| 聖塞瓦斯提安 (西班牙)      | 聖地亞哥-德孔波斯特拉            | 約 825 公里    | 與北方之路重疊，沿途海岸風光引人入勝。        |
    
    """
    
    st.markdown(markdown)

# Data for the routes
routes = ["法國之路", "北方之路", "葡萄牙之路", "銀之路", "原始之路", "英格蘭之路", "聖雅各海岸之路"]
distances_km = [780, 825, 620, 1000, 321, 120, 825]

# Create a histogram
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(routes, distances_km, color='skyblue')
ax.set_xlabel('距離 (公里)')
ax.set_title('朝聖者之路 路線長度分布')

# Display the plot in Streamlit
st.pyplot(fig)


