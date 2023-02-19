from pytube import YouTube

url = input("Informe URL: ")
yt = YouTube(url)
print("loading.. .", yt.title)
yt = yt.streams.get_highest_resolution()
yt.download()

print("Video baixa com sucesso!!")	