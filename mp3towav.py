#import librosa
#data, rate = librosa.load('mix.mp3')

#print(len(data))
from os import path
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from tempfile import mktemp

mp3_audio = AudioSegment.from_file('Tragic_Story.mp3', format="mp3")  # read mp3
wname = mktemp('Tragic_Story.wav')  # use temporary file
mp3_audio.export(wname, format="wav")  # convert to wav
FS, data = wavfile.read(wname)  # read wav file
data=np.mean(data, axis=1) # convert to mono
#plt.specgram(data, Fs=FS, NFFT=128, noverlap=0)  # plot
plt.plot(data)
plt.show()