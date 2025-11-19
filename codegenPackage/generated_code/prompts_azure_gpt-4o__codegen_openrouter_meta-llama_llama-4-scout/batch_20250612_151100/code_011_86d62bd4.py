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
%% Signal Processing Script
% This script demonstrates basic signal processing tasks in MATLAB.

%% Clear Workspace and Command Window
clear all;
close all;
clc;

%% Generate a Sample Signal
% Generate a sample signal with a mix of frequencies
fs = 1000;  % Sampling frequency (Hz)
t = 0:1/fs:1;  % Time vector (s)
f1 = 10;  % Frequency 1 (Hz)
f2 = 20;  % Frequency 2 (Hz)
signal = sin(2*pi*f1*t) + 0.5*sin(2*pi*f2*t);

%% Add Noise to the Signal
% Add Gaussian white noise to the signal
noise = randn(size(t));
noisy_signal = signal + noise;

%% Plot Original and Noisy Signals
% Plot the original and noisy signals
figure;
subplot(2,1,1);
plot(t, signal);
xlabel('Time (s)');
ylabel('Amplitude');
title('Original Signal');

subplot(2,1,2);
plot(t, noisy_signal);
xlabel('Time (s)');
ylabel('Amplitude');
title('Noisy Signal');

%% Filter the Noisy Signal
% Design a simple low-pass filter to remove high-frequency noise
order = 4;  % Filter order
cutoff_frequency = 30;  % Cutoff frequency (Hz)
[b, a] = butter(order, cutoff_frequency/(fs/2), 'low');
filtered_signal = filter(b, a, noisy_signal);

%% Plot Filtered Signal
% Plot the filtered signal
figure;
plot(t, filtered_signal);
xlabel('Time (s)');
ylabel('Amplitude');
title('Filtered Signal');

%% Calculate Signal-to-Noise Ratio (SNR)
% Calculate the SNR of the original and noisy signals
signal_power = mean(signal.^2);
noise_power = mean((noisy_signal - signal).^2);
snr = 10*log10(signal_power/noise_power);
fprintf('SNR: %.2f dB\n', snr);

%% Calculate Mean Squared Error (MSE)
% Calculate the MSE between the original and filtered signals
mse = mean((signal - filtered_signal).^2);
fprintf('MSE: %.2f\n', mse);
```
