import streamlit as st
import folium
from streamlit_folium import st_folium

# Folium 지도 생성 (대전광역시 중심)
map_obj = folium.Map(
    location=[36.3504, 127.3845],  # 대전광역시 중심 좌표
    zoom_start=12  # 줌 레벨 설정
)

# Streamlit 앱에 지도 표시
st_folium(map_obj, width=800, height=600)
