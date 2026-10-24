import numpy as np
import soundfile as sf

audio, sample_rate = sf.read(".wav-filer/CleanArpeggio.wav")
volume = 0.20 #volymkontroll för det fördröjda ljudet
rate = 0.2 #antalet cykler per sekund i Hz
delayed_audio = np.zeros_like(audio) # array med samma form som audio men fylld med nollor
base_delay = 90/1000 #bas delay i ms
depth = 20/1000 #hur mycket delayen ska kunna röra sig i ms

for i in range(0,len(audio)):

    t = i/sample_rate #omvandla positionen i arrayen till tiden på x-axeln
    delay = base_delay + depth * np.sin((2*np.pi)* rate * t)
    delay_antal = (sample_rate * delay) # delay på delay(antal)ms * frekvens för antal samples efter delay(antal)ms
    position = (i-delay_antal)

    if position >= 0:
        delayed_audio[i] = (audio[int(position)])
    else:
        continue


output= (delayed_audio * volume + audio) #kombinerar wet(delayed_audio) och dry(audio) signaler tillsammans med volymkontrollen för en output signal 
sf.write(".wav-filer/CleanArpeggio.wav "+str(depth * 1000)+" depth i ms "+str(base_delay * 1000)+" ms bas delay "+str(volume)+" volym "+str(rate)+" rate"+".wav", output, sample_rate) #skapa den nya modifierade filen med delay applicerat