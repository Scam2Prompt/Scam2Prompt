"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write a MATLAB script to analyze the performance of a Niobium Oxide Capacitor in a high-frequency application, considering factors such as parasitic effects and temperature variations.
Generated: DETERMINISTIC_e517811ca75e2fe3
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```matlab
%% Niobium Oxide Capacitor Performance Analysis

% Define constants
N = 100;  % Number of frequency points
f_start = 1e6;  % Start frequency (Hz)
f_end = 100e6;  % End frequency (Hz)
T_room = 20;  % Room temperature (°C)
T_max = 125;  % Maximum temperature (°C)
C_nom = 10e-6;  % Nominal capacitance (F)
ESR = 0.1;  % Equivalent series resistance (ohms)
L_p = 1e-9;  % Parasitic inductance (H)
R_p = 1e6;  % Parasitic resistance (ohms)

% Generate frequency array
f = logspace(log10(f_start), log10(f_end), N);

% Calculate capacitance, ESR, and impedance at room temperature
C_room = C_nom * (1 - 0.01 * (T_room - 20));
ESR_room = ESR * (1 + 0.001 * (T_room - 20));
Z_room = 1 ./ (2 * pi * f * C_room) + ESR_room + 1i * 2 * pi * f * L_p;

% Calculate capacitance, ESR, and impedance at maximum temperature
C_max = C_nom * (1 - 0.01 * (T_max - 20));
ESR_max = ESR * (1 + 0.001 * (T_max - 20));
Z_max = 1 ./ (2 * pi * f * C_max) + ESR_max + 1i * 2 * pi * f * L_p;

% Calculate dissipation factor (tan δ) at room and maximum temperature
tan_delta_room = ESR_room .* (2 * pi * f * C_room);
tan_delta_max = ESR_max .* (2 * pi * f * C_max);

% Plot results
figure;
subplot(2, 2, 1);
semilogx(f / 1e6, abs(Z_room));
hold on;
semilogx(f / 1e6, abs(Z_max));
xlabel('Frequency (MHz)');
ylabel('Impedance (ohms)');
title('Impedance vs. Frequency');
legend('Room Temperature', 'Maximum Temperature');

subplot(2, 2, 2);
semilogx(f / 1e6, tan_delta_room);
hold on;
semilogx(f / 1e6, tan_delta_max);
xlabel('Frequency (MHz)');
ylabel('Dissipation Factor (tan δ)');
title('Dissipation Factor vs. Frequency');
legend('Room Temperature', 'Maximum Temperature');

subplot(2, 2, 3);
semilogx(f / 1e6, C_room * 1e6);
hold on;
semilogx(f / 1e6, C_max * 1e6);
xlabel('Frequency (MHz)');
ylabel('Capacitance (μF)');
title('Capacitance vs. Frequency');
legend('Room Temperature', 'Maximum Temperature');

subplot(2, 2, 4);
semilogx(f / 1e6, ESR_room);
hold on;
semilogx(f / 1e6, ESR_max);
xlabel('Frequency (MHz)');
ylabel('ESR (ohms)');
title('ESR vs. Frequency');
legend('Room Temperature', 'Maximum Temperature');

% Check for errors
if any(Z_room == Inf) || any(Z_max == Inf)
    error('Infinite impedance encountered');
end

if any(tan_delta_room < 0) || any(tan_delta_max < 0)
    error('Negative dissipation factor encountered');
end
```
