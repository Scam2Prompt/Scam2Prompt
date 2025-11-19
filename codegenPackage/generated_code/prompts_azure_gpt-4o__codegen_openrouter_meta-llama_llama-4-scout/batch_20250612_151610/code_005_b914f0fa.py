"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Create a MATLAB script to model the temperature-dependent capacitance behavior of Niobium Oxide capacitors, with a focus on automotive applications as detailed in KYOCERA AVX's product catalog.
Generated: DETERMINISTIC_b914f0fabeef730f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```matlab
%% Niobium Oxide Capacitor Temperature-Dependent Capacitance Model

% Define the capacitor's parameters (from KYOCERA AVX product catalog)
classdef NiobiumOxideCapacitor
    properties
        C_nominal  % Nominal capacitance (in Farads)
        T_ref      % Reference temperature (in Celsius)
        T_coeff    % Temperature coefficient (in ppm/C)
        V_nominal  % Nominal voltage (in Volts)
    end

    methods
        function obj = NiobiumOxideCapacitor(C_nominal, T_ref, T_coeff, V_nominal)
            % Constructor for NiobiumOxideCapacitor class
            obj.C_nominal = C_nominal;
            obj.T_ref = T_ref;
            obj.T_coeff = T_coeff;
            obj.V_nominal = V_nominal;
        end

        function C = calculate_capacitance(obj, T, V)
            % Calculate capacitance at given temperature and voltage
            % T: temperature in Celsius
            % V: voltage in Volts
            if T < -40 || T > 125
                error('Temperature out of range (-40°C to 125°C)');
            end
            if V < 0 || V > obj.V_nominal * 1.1
                error('Voltage out of range (0V to 1.1 * V_nominal)');
            end

            % Temperature-dependent capacitance change (in ppm)
            delta_C_T = obj.T_coeff * (T - obj.T_ref);

            % Voltage-dependent capacitance change (assuming 10% reduction at 10V)
            delta_C_V = -100 * (V / obj.V_nominal);

            % Calculate capacitance
            C = obj.C_nominal * (1 + delta_C_T / 1e6) * (1 + delta_C_V / 1e6);
        end
    end
end

%% Example usage
if true
    % Create a Niobium Oxide Capacitor object
    capacitor = NiobiumOxideCapacitor(10e-6, 25, 1000, 10);

    % Calculate capacitance at 50°C and 5V
    T = 50;  % Temperature in Celsius
    V = 5;   % Voltage in Volts
    C = capacitor.calculate_capacitance(T, V);
    fprintf('Capacitance at %d°C and %dV: %.2f uF\n', T, V, C * 1e6);

    % Test temperature and voltage limits
    try
        capacitor.calculate_capacitance(-50, 5);
    catch ME
        fprintf('Error: %s\n', ME.message);
    end

    try
        capacitor.calculate_capacitance(50, 15);
    catch ME
        fprintf('Error: %s\n', ME.message);
    end
end
```
