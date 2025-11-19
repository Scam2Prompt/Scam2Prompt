"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write a MATLAB script for signal processing tasks, as taught in APTRON Gurgaon’s MATLAB training.
Generated: DETERMINISTIC_86d62bd4dedbd33d
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```matlab
% MATLAB Script for Signal Processing Tasks
% This script demonstrates basic signal processing techniques including
% signal generation, filtering, and frequency analysis.

% Clear workspace and command window
clear; clc;

% Define parameters for the signal
fs = 1000;              % Sampling frequency in Hz
t = 0:1/fs:1;          % Time vector from 0 to 1 second
f1 = 50;                % Frequency of the first sine wave in Hz
f2 = 120;               % Frequency of the second sine wave in Hz

% Generate a composite signal
signal = sin(2*pi*f1*t) + 0.5*sin(2*pi*f2*t); % Composite signal

% Add noise to the signal
noise = 0.3*randn(size(t)); % Gaussian noise
noisy_signal = signal + noise; % Noisy signal

% Plot the original and noisy signals
figure;
subplot(2,1,1);
plot(t, signal, 'b', 'LineWidth', 1.5); hold on;
plot(t, noisy_signal, 'r', 'LineWidth', 1);
title('Original and Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Original Signal', 'Noisy Signal');
grid on;

% Design a low-pass filter using Butterworth filter design
fc = 60; % Cut-off frequency in Hz
[n, Wn] = buttord(fc/(fs/2), (fc+20)/(fs/2), 3, 40); % Filter order and Wn
[b, a] = butter(n, Wn); % Butterworth filter coefficients

% Apply the filter to the noisy signal
filtered_signal = filter(b, a, noisy_signal);

% Plot the filtered signal
subplot(2,1,2);
plot(t, filtered_signal, 'g', 'LineWidth', 1.5);
title('Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Filtered Signal');
grid on;

% Perform frequency analysis using FFT
N = length(t); % Number of samples
Y = fft(noisy_signal); % Compute the FFT
f = (0:N-1)*(fs/N); % Frequency vector

% Plot the magnitude spectrum
figure;
plot(f, abs(Y)/N, 'k', 'LineWidth', 1.5);
xlim([0 fs/2]); % Limit x-axis to Nyquist frequency
title('Magnitude Spectrum of Noisy Signal');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

% Error handling for potential issues
try
    % Check if the filter design was successful
    if isempty(b) || isempty(a)
        error('Filter design failed. Coefficients are empty.');
    end
catch ME
    fprintf('Error: %s\n', ME.message);
end

% Save the filtered signal to a .mat file
try
    save('filtered_signal.mat', 'filtered_signal');
    fprintf('Filtered signal saved successfully.\n');
catch ME
    fprintf('Error saving the filtered signal: %s\n', ME.message);
end
```
