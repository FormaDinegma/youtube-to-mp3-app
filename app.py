import os
import streamlit as st
import yt_dlp
from pydub import AudioSegment

st.title("🎧 YouTube to MP3 Downloader")
st.caption("Uso personal – Descarga canciones en MP3 desde YouTube buscando por nombre o artista.")

query = st.text_input("🔍 Escribe el nombre de la canción y/o artista")

if st.button("Buscar y Descargar"):
    if not query:
        st.warning("⚠️ Por favor escribe algo para buscar.")
    else:
        with st.spinner("Buscando y descargando..."):

            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'outtmpl': 'temp.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([f"ytsearch1:{query}"])

                sound = AudioSegment.from_mp3("temp.mp3")
                output_path = "cancion_360.mp3"
                sound.export(output_path, format="mp3", bitrate="360k")
                os.remove("temp.mp3")

                with open(output_path, "rb") as file:
                    st.success("✅ ¡Descarga completa!")
                    st.download_button("📥 Descargar MP3", file, file_name="cancion.mp3")

                os.remove(output_path)

            except Exception as e:
                st.error(f"❌ Error durante la descarga: {e}")
