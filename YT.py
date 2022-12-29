# import api pytube
from pytube import YouTube, Playlist

# YT link to download
video = YouTube('INGRESE SU URL PARA DESCARGA')

# Parámetros para la descarga
video.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download()


# For Download Playlist
"""
playlist = Playlist(
 'https://www.youtube.com/watch?v=ygBAqpSQRLU&list=PLRb5wMnj65To_GS_ZIpSmjA3Sov-8h-ii')

for video in playlist.videos:
    print('Descargando {}'.format(video.title))
    video.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download()
    print('-----------------------------------------------')
"""
