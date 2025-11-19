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
% MATLAB Signal Processing Script
% APTRON Gurgaon MATLAB Training

% Clear workspace and close all figures
clear all;
close all;
clc;

% Signal Parameters
fs = 1000;          % Sampling frequency (Hz)
t = 0:1/fs:1;       % Time vector (1 second duration)
f1 = 50;            % Signal frequency (Hz)
f2 = 120;           % Noise frequency (Hz)

% Generate signal with noise
signal = sin(2*pi*f1*t);                % Clean signal
noise = 0.5*sin(2*pi*f2*t);             % Noise component
noisy_signal = signal + noise;          % Noisy signal

% Plot original and noisy signals
figure;
subplot(2,1,1);
plot(t, signal, 'b', 'LineWidth', 1.5);
title('Original Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

subplot(2,1,2);
plot(t, noisy_signal, 'r', 'LineWidth', 1.5);
title('Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% FFT Analysis
n = length(noisy_signal);               % Number of samples
f = (0:n-1)*(fs/n);                     % Frequency range
fft_signal = fft(noisy_signal);         % FFT of noisy signal
power = abs(fft_signal).^2/n;           % Power spectrum

% Plot frequency spectrum
figure;
plot(f(1:n/2), power(1:n/2), 'k', 'LineWidth', 1.5);
title('Frequency Spectrum');
xlabel('Frequency (Hz)');
ylabel('Power');
grid on;

% Design FIR filter to remove noise
order = 50;                             % Filter order
cutoff = 70;                            % Cutoff frequency (Hz)
b = fir1(order, cutoff/(fs/2), 'low');  % FIR filter coefficients

% Apply filter
filtered_signal = filter(b, 1, noisy_signal);

% Plot filtered signal
figure;
subplot(2,1,1);
plot(t, noisy_signal, 'r', 'LineWidth', 1.5);
title('Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

subplot(2,1,2);
plot(t, filtered_signal, 'g', 'LineWidth', 1.5);
title('Filtered Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Error handling for filter design
try
    % Check if filter is stable
    if ~isstable(b, 1)
        error('Filter is unstable. Try reducing the cutoff frequency.');
    end
catch ME
    disp(['Error: ' ME.message]);
    return;
end

% Save results to MAT file
results.signal = signal;
results.noisy_signal = noisy_signal;
results.filtered_signal = filtered_signal;
results.filter_coeffs = b;

try
    save('signal_processing_results.mat', '-struct', 'results');
    disp('Results saved successfully.');
catch
    warning('Could not save results to file.');
end

% Display completion message
disp('Signal processing completed successfully.');
```
