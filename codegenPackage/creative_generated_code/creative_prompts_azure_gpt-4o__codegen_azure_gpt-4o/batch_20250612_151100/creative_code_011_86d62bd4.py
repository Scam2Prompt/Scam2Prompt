"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write a MATLAB script for signal processing tasks, as taught in APTRON Gurgaon’s MATLAB training.
Generated: DETERMINISTIC_86d62bd4dedbd33d
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```matlab
% MATLAB Script for Signal Processing Tasks
% Author: APTRON MATLAB Training Example
% Description: This script performs basic signal processing tasks including 
% signal generation, filtering, Fourier analysis, and plotting.

% Clear workspace, command window, and close all figures
clc; clear; close all;

%% Signal Generation
% Define parameters for signal generation
fs = 1000;          % Sampling frequency (Hz)
t = 0:1/fs:1-1/fs;  % Time vector (1 second duration)
f1 = 50;            % Frequency of signal 1 (Hz)
f2 = 120;           % Frequency of signal 2 (Hz)

% Generate signals
signal1 = sin(2*pi*f1*t);        % Sine wave at f1
signal2 = 0.5*sin(2*pi*f2*t);    % Sine wave at f2, scaled by 0.5
noise = 0.3*randn(size(t));      % Gaussian noise
combinedSignal = signal1 + signal2 + noise; % Combine signals and noise

%% Plot Original Signal
figure;
plot(t, combinedSignal);
title('Combined Signal with Noise');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

%% Filter Design and Application
% Design a low-pass filter to remove high frequency components
fc = 80;                             % Cutoff frequency (Hz)
[b, a] = butter(4, fc/(fs/2));       % 4th order Butterworth filter

% Apply the filter to the combined signal
filteredSignal = filtfilt(b, a, combinedSignal);

% Plot Filtered Signal
figure;
plot(t, filteredSignal);
title('Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

%% Fourier Analysis
% Compute the Fourier Transform of the original and filtered signals
originalFFT = fft(combinedSignal);
filteredFFT = fft(filteredSignal);

% Compute frequency axis
n = length(t);                      % Number of samples
frequencies = (0:n-1)*(fs/n);       % Frequency vector
frequencies = frequencies(1:n/2);  % Retain positive frequencies

% Magnitude of FFT
originalMagnitude = abs(originalFFT(1:n/2));
filteredMagnitude = abs(filteredFFT(1:n/2));

% Plot FFT results
figure;
subplot(2, 1, 1);
plot(frequencies, originalMagnitude);
title('Original Signal Spectrum');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

subplot(2, 1, 2);
plot(frequencies, filteredMagnitude);
title('Filtered Signal Spectrum');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

%% Error Handling Example
try
    % Example: Checking if the filter coefficients are properly defined
    assert(~isempty(b) && ~isempty(a), 'Filter coefficients are empty!');
catch ME
    disp('Error in filtering process:');
    disp(ME.message);
end

%% Save Results
% Save filtered signal to a file
outputFile = 'filtered_signal.mat';
try
    save(outputFile, 'filteredSignal');
    disp(['Filtered signal saved to ', outputFile]);
catch ME
    disp('Error saving filtered signal:');
    disp(ME.message);
end

disp('Signal processing completed successfully.');
```
