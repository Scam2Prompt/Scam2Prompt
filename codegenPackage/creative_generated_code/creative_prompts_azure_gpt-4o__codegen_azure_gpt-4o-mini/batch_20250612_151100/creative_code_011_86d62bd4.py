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
% MATLAB Script for Basic Signal Processing Tasks
% This script demonstrates fundamental signal processing techniques
% such as signal generation, filtering, and spectrum analysis.

% Clear workspace, close figures, and clear command window
clear; clc; close all;

% Define parameters for the signal
Fs = 1000;                   % Sampling frequency (Hz)
t = 0:1/Fs:1;               % Time vector (1 second duration)
f1 = 50;                    % Frequency of the first signal (Hz)
f2 = 120;                   % Frequency of the second signal (Hz)

% Generate a composite signal
signal1 = sin(2*pi*f1*t);   % Sine wave at f1
signal2 = 0.5*sin(2*pi*f2*t); % Sine wave at f2 with half amplitude
composite_signal = signal1 + signal2; % Composite signal

% Visualize the composite signal
figure;
subplot(2,1,1);
plot(t, composite_signal);
title('Composite Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Design a low-pass filter using Butterworth filter
fp = 70;                     % Passband frequency (Hz)
fs = 150;                    % Stopband frequency (Hz)
order = 4;                   % Filter order
[n, Wn] = buttord(fp/(Fs/2), fs/(Fs/2), 3, 40); % Determine the order and cutoff
[b, a] = butter(n, Wn);     % Design the filter

% Apply the filter to the composite signal
filtered_signal = filter(b, a, composite_signal); 

% Visualize the filtered signal
subplot(2,1,2);
plot(t, filtered_signal);
title('Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Perform spectrum analysis using FFT
L = length(composite_signal); % Length of the signal
Y = fft(composite_signal);     % Compute the FFT
P2 = abs(Y/L);                 % Two-sided spectrum
P1 = P2(1:L/2+1);              % Single-sided spectrum
P1(2:end-1) = 2*P1(2:end-1);  % Adjust amplitudes

f = Fs*(0:(L/2))/L;           % Frequency axis

% Visualize the spectrum
figure;
plot(f, P1);
title('Single-Sided Amplitude Spectrum of Composite Signal');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

% Error Handling
try
    % Code that might throw an error
    assert(length(signal1) == length(signal2), 'Signal lengths must match!');
catch ME
    fprintf('Error occurred: %s\n', ME.message); % Display the error message
end

% End of MATLAB Script
```
