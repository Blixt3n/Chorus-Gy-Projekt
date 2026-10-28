import numpy as np
import soundfile as sf
from loop_function import loop_function

audio, sample_rate = sf.read(".wav-filer/CleanArpeggio.wav") #läser den aktuella ljud-filen och hämtar varabeln audio (array av samples) och sample_rate (hur fort ljudet spelas upp)
volume = 0.3 #volymkontroll för det fördröjda ljudet
rate = 0.8 #antalet cykler per sekund i Hz
delayed_audio = np.zeros_like(audio) # array med samma form som audio men fylld med nollor
base_delay = 25/1000 #bas delay i ms
depth = 5/1000 #hur mycket delayen ska kunna röra sig i ms

delayed_audio = loop_function(rate, delayed_audio, base_delay, depth, audio, sample_rate) #funktionen som skapar delay-arrayen med fördröjt ljud

output= (delayed_audio * volume + audio) #kombinerar wet(delayed_audio) och dry(audio) signaler tillsammans med volymkontrollen för en output signal 
sf.write(".wav-filer/CleanArpeggio "+str(depth * 1000)+" depth i ms "+str(base_delay * 1000)+" ms bas delay "+str(volume)+" volym "+str(rate)+" rate"+" delayljud.wav", delayed_audio, sample_rate) # skapar en fil med enbart delayljudet
sf.write(".wav-filer/CleanArpeggio "+str(depth * 1000)+" depth i ms "+str(base_delay * 1000)+" ms bas delay "+str(volume)+" volym "+str(rate)+" rate"+".wav", output, sample_rate) #skapa den nya modifierade filen med delay applicerat