
falun_icon = "https://dafastorage.blob.core.windows.net/media/Falun.png"

lst_pages = [
    "Home",
    "Hướng dẫn",
    "Bài đọc qua từng năm"
]

lst_title = [
    "1996 - Giảng Pháp tại Pháp hội Sydney",
    # "1997",
    # "1998"
]



#=================================== mapping name ==========================
original_1996_sydney = "https://vi.falundafa.org/lectures/19960000_sydney/19960000_sydney_vn_2017.html"
#--------------
# Khởi tạo danh sách chứa các URL
mp3_1996_sydney_intro = [
    f"https://dafastorage.blob.core.windows.net/1996-sydney-intro/part{part}.mp3"
    for part in range(2, 12)
]
mp3_1996_sydney_qna = [
    f"https://dafastorage.blob.core.windows.net/1996-sydney-qna/part{part}.mp3"
    for part in range(0, 33)
]

#---------------
dct_mapping_name = {
    "1996 - Giảng Pháp tại Pháp hội Sydney": [mp3_1996_sydney_intro, mp3_1996_sydney_qna],
}



