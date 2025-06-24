import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def download_audio_with_ytdlp(link):
    try:
        command = [
            "yt-dlp",
            "-x",  
            "--audio-format", "mp3",  
            "-o", "%(title)s.%(ext)s", 
            link
        ]
        subprocess.run(command, check=True)
        logging.info("Download concluído com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar yt-dlp: {e}")

link = input("Digite o link em questão: ")
download_audio_with_ytdlp(link)
