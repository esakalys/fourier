
import numpy as np
import random
    
# Functions to generate random sinusoidal waveforms
def genRandCos(x, aLim, omegaLim):
    
    amplitude = random.randrange(-aLim, aLim)
    omega = random.randrange(omegaLim[0], omegaLim[1])
    return amplitude*np.cos(omega*x), amplitude, omega
    
def genRandSin(x, aLim, omegaLim):
    
    amplitude = random.randrange(-aLim, aLim)
    omega = random.randrange(omegaLim[0], omegaLim[1])
    return amplitude*np.sin(omega*x), amplitude, omega
    
def genRandSinusoid(x, aLim, omegaLim):
    
    amplitude = random.randrange(-aLim, aLim)
    omega = random.randrange(omegaLim[0], omegaLim[1])
    
    sinusoid = random.randint(0, 1)
    
    if sinusoid == 0:
        return amplitude*np.cos(omega*x), amplitude, omega, 'cos'
    else:
        return amplitude*np.sin(omega*x), amplitude, omega, 'sin'
    
# Function to generate signal with a specified number of random sinusoids
def genSignal(x, aLim, omegaLim, compNum):

    signal = 0*x
    
    frequencies = []
    amplitudes = []
    compTypes = []

    for i in range(compNum):
        [sinusoid, amp, freq, tp] = genRandSinusoid(x, aLim, omegaLim)
        
        frequencies.append(freq/(2*np.pi))
        amplitudes.append(amp)
        compTypes.append(tp)
        
        signal = signal + sinusoid

    return signal, frequencies, amplitudes, compTypes
