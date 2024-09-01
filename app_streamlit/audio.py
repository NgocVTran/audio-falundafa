import streamlit as st
from application.const import dct_mapping_name

def app_audio(title):
    # 1. GIANG PHAP
    st.markdown("#### Giảng Pháp")

    # Danh sách các liên kết MP3
    mp3_links_intro = dct_mapping_name[title][0]  # intro
    mp3_links_qna = dct_mapping_name[title][1]  # Q&A
    # Tên của các bài
    mp3_names_intro = [f"Phần {part}" for part in range(1, len(mp3_links_intro) + 1)]
    mp3_names_qna = [f"Câu {part}" for part in range(1, len(mp3_links_qna) + 1)]

    generate_playlist(mp3_links=mp3_links_intro, mp3_names=mp3_names_intro)

    # 2. Cau hoi cua hoc vien
    st.markdown("#### Trả lời câu hỏi của học viên")
    generate_playlist(mp3_links=mp3_links_qna, mp3_names=mp3_names_qna)

def generate_playlist(mp3_links, mp3_names):
    # Tạo danh sách các bài
    playlist_items = "".join(
        [f'<li><a href="{link}">{mp3_names[i]}</a></li>' for i, link in enumerate(mp3_links)])

    # Mã HTML sử dụng Plyr.js cho trình phát nhạc
    html_code = f"""
        <link rel="stylesheet" href="https://cdn.plyr.io/3.7.2/plyr.css" />
        <div id="nowPlaying" style="font-family: Arial; font-weight: bold; margin-bottom: 10px;">Đang phát: {mp3_names[0]}</div>
        <audio id="player" controls">
            <source src="{mp3_links[0]}" type="audio/mp3" />
            Your browser does not support the audio element.
        </audio>

        <ul id="playlist">
            {playlist_items}
            </div>
        </ul>
        <style>
            #playlist a {{
                font-family: Arial;
                font-size: 12.5px;
                text-decoration: none;
                color: black;
            }}
            #playlist a:hover{{
                text-decoration: underline;
            }}
        </style>


        <script src="https://cdn.plyr.io/3.7.2/plyr.polyfilled.js"></script>
        <script>
        document.addEventListener('DOMContentLoaded', function () {{
            const player = new Plyr('#player', {{ controls: ['play', 'progress', 'current-time', 'mute', 'volume'] }});
            const links = document.querySelectorAll('#playlist a');
            let currentTrack = 0;

            function playTrack(index) {{
                document.getElementById('nowPlaying').textContent = 'Đang phát: ' + links[index].textContent; // Cập nhật tên bài hát
                player.source = {{
                    type: 'audio',
                    sources: [{{
                        src: links[index].getAttribute('href'),
                        type: 'audio/mp3'
                    }}]
                }};
                player.play();
            }}

            player.on('ended', function() {{
                currentTrack = (currentTrack + 1) % links.length; // Chuyển sang bài hát tiếp theo
                playTrack(currentTrack);
            }});

            links.forEach((link, index) => {{
                link.addEventListener('click', function(e) {{
                    e.preventDefault();
                    currentTrack = index;
                    playTrack(currentTrack);
                }});
            }});
        }});
        </script>
        """

    # Hiển thị mã HTML và JavaScript trên Streamlit
    st.components.v1.html(html_code, height=200, scrolling=True)




