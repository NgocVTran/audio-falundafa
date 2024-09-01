import streamlit as st
from application.const import lst_pages, falun_icon, lst_title
from app_streamlit import audio, home, guide

# Cấu hình trang
st.set_page_config(
    page_title="Audio Support - Falun Dafa",  # Đổi tiêu đề trang
    page_icon=falun_icon  # Đổi biểu tượng trang, có thể dùng emoji hoặc đường dẫn đến file hình ảnh
)

# Thêm ảnh biểu tượng phía trên chữ "Menu"
st.sidebar.image(falun_icon, width=150)
st.sidebar.title("Audio Hỗ Trợ Tu Luyện")

# Tạo sidebar với radio để chọn trang
page = st.sidebar.radio("", lst_pages)

# Hàm hiển thị nội dung các trang

def home_page():
    st.title("Falun Dafa")
    home.content()

def guide_page():
    st.title("Hướng dẫn sử dụng")
    guide.content()

def list_page():
    # st.title("Danh sách các năm")
    # Hiển thị danh sách các năm trong sidebar
    title = st.sidebar.radio("Chọn audio:", lst_title)
    display_works_by_year(title)

def display_works_by_year(title):
    st.subheader(f"{title}")
    # Thêm logic để hiển thị các tác phẩm của năm đã chọn
    st.write(f"Audio của năm {title}.")
    audio.app_audio(title)


# Điều hướng giữa các trang dựa vào lựa chọn từ radio
if page == lst_pages[0]:
    home_page()
elif page == lst_pages[1]:
    guide_page()
elif page == lst_pages[2]:
    list_page()


