import streamlit as it
import time
it.set_page_config(page_title="op",page_icon=None,layout="wide")
col1,col2,col3,col4,col5 = it.columns(5)
it.title = "chương trình đoán tính cách bằng thứ tôi ăn hằng ngày"
asw = "idk"
with col1:
    if it.button("con mèo"):
        asw = "con mèo"
        ghi_chu = "bạn lười"
with col2:
    if it.button("con chó"):
        asw = "con chó"
        ghi_chu = "bạn hay sủa"
with col3:
    if it.button("con sư tử"):
        asw = "con sư tử"
        ghi_chu = "bạn quá dữ"
with col4:
    if it.button("con ngựa"):
        asw = "con ngựa"
        ghi_chu = "bạn hay chạy nợ"
with col5:
    if it.button("con thiên nga"):
        asw = "con thiên nga"
        ghi_chu = "bạn sắp lên thiên đàn r đấy"
with it.sidebar:
    pass
it.expander(asw)