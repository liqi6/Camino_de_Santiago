import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/Camino_logo.pngg"
st.sidebar.image(logo)

# Customize page title
st.title("Camino de Santiago")

st.markdown(
    """
    朝聖者之路（Camino de Santiago）是歐洲著名的朝聖路線，終點位於西班牙北部加利西亞的聖地亞哥-德孔波斯特拉大教堂（Santiago de Compostela），據說是聖雅各的長眠之地。這條路線自中世紀起便吸引無數朝聖者徒步前往，途中穿越山脈、河谷與村莊，既是一場身心挑戰，也是文化與自然的體驗。今天，無論是出於宗教、文化探索或運動目的，每年都有數十萬人踏上這段富有意義的旅程，感受道路上的和平與反思。
    """
)

st.header("intro")

markdown = """
### 主要朝聖者之路表格

| **路線名稱**      | **起點**                  | **終點**                        | **距離**       | **特色**                        |
|------------------|-------------------------|--------------------------------|---------------|--------------------------------|
| **法國之路**      | 聖讓-皮耶-德波爾特 (法國)   | 聖地亞哥-德孔波斯特拉 (西班牙)       | 約 780 公里    | 最受歡迎，設施完善，風景多樣。           |
| **北方之路**      | 依倫 (西班牙)             | 聖地亞哥-德孔波斯特拉            | 約 825 公里    | 沿北部海岸線，風景優美但地形較艱難。         |
| **葡萄牙之路**    | 里斯本/波爾圖 (葡萄牙)     | 聖地亞哥-德孔波斯特拉            | 約 620 公里    | 穿越葡萄牙北部，歷史與美食並存。          |
| **銀之路**        | 塞維亞 (西班牙)           | 聖地亞哥-德孔波斯特拉            | 約 1000 公里   | 途經西班牙內陸，古羅馬遺跡豐富。          |
| **原始之路**      | 奧維耶多 (西班牙)         | 聖地亞哥-德孔波斯特拉            | 約 321 公里    | 最古老的路線，山地挑戰性高，風景壯麗。      |
| **英格蘭之路**    | 拉科魯尼亞/費羅爾 (西班牙)  | 聖地亞哥-德孔波斯特拉            | 約 120 公里    | 適合短期徒步，當年英格蘭人登岸之路。         |
| **聖雅各海岸之路**| 聖塞瓦斯提安 (西班牙)      | 聖地亞哥-德孔波斯特拉            | 約 825 公里    | 與北方之路重疊，沿途海岸風光引人入勝。        |

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
#m.add_basemap("OpenTopoMap")
m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)
# Add GeoJSON line to the map
geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
m.add_geojson(geojson_url, layer_name="Camino de Santiago Route")

m.to_streamlit(height=500)
