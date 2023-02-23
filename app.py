import numpy as np
import sinusoidGen as sg
import matplotlib.pyplot as plt
from fourier import fourierTransform as ft

def main():
    # Defining Constants

    # Frequency range to analyze
    f = np.linspace(0, 101, 10000)
    omega = f * 2*np.pi

    # Sampling frequency
    fSampling = max(f) * 2.1
    stepSize = 1/fSampling

    # Time limit
    tLim = 0.6
    t = np.arange(-tLim, tLim, stepSize)

    # Sinusoid amplitude and frequency limits
    aLim = 5
    fLimUpper = 100
    fLimLower = 10
    omegaLim = [int(fLimLower * 2*np.pi), int(fLimUpper * 2*np.pi)]

    # Defining Constants Done

    # Generating signal
    signal, frequencies, amplitudes, compTypes = sg.genSignal(t, aLim, omegaLim, 10)

    # Fourier transform
    fourierReal, fourierImag, fourierAbs, fourier = ft(signal, t, omega)

    plt.figure(figsize=(8, 6), dpi=400)
    plt.title('Frequency Spectrum Real')
    index = 0
    for fr in frequencies: 
        if compTypes[index] == 'cos':
            plt.plot([fr, fr], [-abs(amplitudes[index])*max(fourierReal)/aLim, max(fourierReal)*1.1], color='r', linestyle='--')
        index = index + 1
    plt.plot(f, fourierReal, linewidth=1)
    plt.grid(linewidth=0.2)
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency, Hz')
    plt.savefig('plots/real.jpg', dpi=400)

    plt.figure(figsize=(8, 6), dpi=400)
    plt.title('Frequency Spectrum Imaginary')
    index = 0
    for fr in frequencies: 
        if compTypes[index] == 'sin':
            plt.plot([fr, fr], [-abs(amplitudes[index])*max(fourierImag)/aLim, max(fourierImag)*1.1], color='r', linestyle='--')
        index = index + 1
    plt.plot(f, fourierImag, linewidth=1)
    plt.grid(linewidth=0.2)
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency, Hz')
    plt.savefig('plots/imag.jpg', dpi=400)

    plt.figure(figsize=(8, 6), dpi=400)
    plt.title('Frequency Spectrum Amplitude')
    index = 0
    for fr in frequencies: 
        plt.plot([fr, fr], [-abs(amplitudes[index])*max(fourierAbs)/aLim, max(fourierAbs)*1.1], color='r', linestyle='--')
        index = index + 1
    plt.plot(f, fourierAbs, linewidth=1)
    plt.grid(linewidth=0.2)
    plt.xlabel('Amplitude')
    plt.ylabel('Frequency, Hz')
    plt.savefig('plots/abs.jpg', dpi=400)

    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(t, signal, linewidth=1)
    plt.title('Signal')
    plt.grid(linewidth=0.2)
    plt.xlabel('Amplitude')
    plt.ylabel('Time, s')
    plt.savefig('plots/signal.jpg', dpi=400)

if __name__ == '__main__':
    main()