import sinusoidGen as sg
import numpy as np
import matplotlib.pyplot as plt
import time

# Function that carries out a fourier transform on a given time domain function for a given frequency range
def fourierTransform(f, t, omega):

    fourierReal = []
    fourierImag = []
    fourierAbs = []
    fourier = []
    
    index = 1
    
    estTimeH = 0
    estTimeM = 0
    estTimeS = 0
    
    tBegin = time.time()
    
    for i in omega:
        
        #Time Measurements
        
        tStart = time.time()
        elapsedTime = round(time.time() - tBegin, 2)
        
        percLeft = round(100*(i/max(omega)), 2)
        
        if index % 100 == 0:
        
            print(str(percLeft) + '% Done')
            print('Estimated time Remaining: ' + 
                  str(estTimeH) + ':' + str(estTimeM) + ':' + str(estTimeS))
            print('Elapsed time: ' + str(elapsedTime)+'s')
            
        #Fourier Transform
        
        value = 0.0 + 0.0j
        
        for k in range(len(t)):
            expMul = np.exp(-i*t[k]*1j)
            value = value + f[k] * expMul
        
        fourierReal.append(abs(value.real))
        fourierImag.append(abs(value.imag))
        fourierAbs.append(abs(value))
        fourier.append(value)
        
        #Time Measurements
        
        tDelta = time.time() - tStart
        iterationsLeft = len(omega) - index
        estTime = iterationsLeft * tDelta
        
        
        estTimeH = int(estTime // 3600)
        estTimeM = int((estTime % 3600) // 60)
        estTimeS = int(estTime % 60)
        
        index = index + 1
        
    return fourierReal, fourierImag, fourierAbs, fourier
