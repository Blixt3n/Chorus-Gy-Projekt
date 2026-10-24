import soundfile as sf
import numpy as np

audio, sample_rate = sf.read(".wav-filer/elgitarrG-sträng.wav")
volume = 0.10 #volymkontroll för det fördröjda ljudet
delay = 500/1000 #delaykontroll i ms för fördröjningen av dry

print("Samplingsfrekvens:", sample_rate)
print("Antal samples:", len(audio))
print("De första 10 samples:", audio[:10])

delay_amount = (sample_rate * delay) # delay på delay(antal)ms * frekvens för antal samples efter delay(antal)ms
delayed_audio = np.zeros_like(audio) # array med samma form som audio men fylld med nollor
delayed_audio[int(delay_amount):] = audio[:-int(delay_amount)] #skapar en delay på 10ms där ljudet skjuts fram med 441 samples

output= (delayed_audio * volume + audio) #kombinerar wet(delayed_audio) och dry(audio) signaler tillsammans med volymkontrollen för en output signal 

print("De första position 441 till 451 samples av output:", output[441:451]) 
print("De första position 441 till 451 samples av delayed_audio:", delayed_audio[441:451])


sf.write(".wav-filer/elgitarrG-sträng_delayed" +str(delay * 1000)+"ms" + str(volume)+"volym"+".wav", output, sample_rate) #skapa den nya modifierade filen med delay applicerat