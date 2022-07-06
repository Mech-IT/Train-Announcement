import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
import speech_recognition
def texttospeech(text,filename):
    myobj = gTTS(text=text, lang="hi", slow=False)
    myobj.save(filename)
def mergeaudios(audios):

    announcement=AudioSegment.empty()
    for audio in audios:
        announcement+= AudioSegment.from_mp3(audio)
    return announcement
def generateannouncement() :
    import pandas as pd
    df = pd.read_csv('Book1.csv')
    for i in range(len(df)):
            texttospeech((str(df.iat[i,0])+"  "+df.iat[i,5]+"  "+df.iat[i,3]),"2_hindi.mp3")
            texttospeech( df.iat[i,1], "4_hindi.mp3")
            texttospeech( df.iat[i,2], "6_hindi.mp3")
            texttospeech( str(df.iat[i,4]), "9_hindi.mp3")
            audios = [f"{i}_hindi.mp3" for i in range(1, 11)]
            announcement=mergeaudios(audios)
            announcement.export(f"announcement_{df.iat[i,0]}.mp3",format="mp3")


def generateskeleton():
    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=0000
    endTime=3000
    extract = song[startTime:endTime]
    extract.export("1_hindi.mp3")

    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=4000
    endTime=5000
    extract = song[startTime:endTime]
    extract.export("3_hindi.mp3")

    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=6300
    endTime=7300
    extract = song[startTime:endTime]
    extract.export("5_hindi.mp3")

    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=8800
    endTime=10000
    extract = song[startTime:endTime]
    extract.export("7_hindi.mp3")

    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=10000
    endTime=11170
    extract = song[startTime:endTime]
    extract.export("8_hindi.mp3")

    song = AudioSegment.from_mp3("Lucknow Train Announcement Hindi.mp3")
    startTime=11400
    endTime=19000
    extract = song[startTime:endTime]
    extract.export("10_hindi.mp3")
if __name__ == '__main__':
    print("Generating Skeleton...")
    generateskeleton()
    print("Now Generating Announcement...")
    generateannouncement()

