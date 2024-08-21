import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Folium 지도 생성 함수
def create_map():
    # Folium 지도 설정 (대전광역시 중심)
    map_obj = folium.Map(
        location=[36.3504, 127.3845],
        zoom_start=12,  # 줌 레벨 조정
    )
    return map_obj  # 지도를 반환

# Streamlit 레이아웃 설정
#st.title('대전광역시 지리 정보 시각화')

# 지도 생성 및 출력
#st.header('대전광역시 지도')
map_display = create_map()
st_folium(map_display, width=1200, height=700)
