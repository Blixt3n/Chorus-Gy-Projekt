import numpy as np

def loop_function(rate, delayed_audio, base_delay, depth, audio, sample_rate):
    for i in range(0,len(audio)):

        t = i/sample_rate #omvandla positionen i arrayen till tiden på x-axeln
        delay = base_delay + depth * np.sin((2*np.pi)* rate * t) #2pi radianer * antalet cykler per sekund * tiden som gått (omvandlat genom i/sample_rate)
        delay_amount = (sample_rate * delay) # delay på delay(antal)ms * frekvens för antal samples efter delay(antal)ms
        position = (i-delay_amount) #beskriver positionen i index på det sample som jag ska hämta från käll-arrayen

        #loop för att placera in rätt sample i målet (delayed_audio) från källan (audio) baserat på position variabeln och i
        if position >= 0:
            delayed_audio[i] = (audio[int(position)])
        else:
            continue
    return(delayed_audio)

