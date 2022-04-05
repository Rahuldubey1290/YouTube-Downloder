from pytube import YouTube

a= int(input("Enter 1 for video and any other number for music \n"))
link= input("Enter the link\n")
yt = YouTube(link)

if a==1:
    print('Video Title:',yt.title,'\t''Video Views:',yt.views,'\t')
    videos=yt.streams.filter(only_video=True)
    videos1=list(enumerate(videos))
    for i in videos1:
        print(i)
    inp = int(input('Enter The index No.(0,1,2...):\n'))
    videos[inp].download()

else:

    print('Music Title',yt.title)
    music=yt.streams.filter(only_audio=True)
    music1=list(enumerate(music))
    for j in music1:
        print(j)
    inp1 = int(input('Enter The Index No.(0,1,2...):\n'))
    music[inp1].download()

print("Successfully")