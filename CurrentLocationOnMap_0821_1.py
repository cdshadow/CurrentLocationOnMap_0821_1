import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static

# 타이틀 설정
st.title("현위치 지도 표시")

# Geopy 초기화
geolocator = Nominatim(user_agent="geoapiExercises")

# 위치 입력 필드
user_input = st.text_input("위치 입력", "대전")  # 기본 입력 값을 대전으로 설정


# Folium 지도 생성 함수
def create_map():
    # Folium 지도 설정 (대전광역시 중심)
    map_obj = folium.Map(
        location=[36.3504, 127.3845],
        zoom_start=12,  # 줌 레벨 조정
    )

# Streamlit 레이아웃 설정
#st.title('대전광역시 지리 정보 시각화')

# 지도 생성 및 출력
#st.header('대전광역시 지도')
map_display = create_map()
st_folium(map_display, width=1200, height=700)
