"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Generate SPICE model code for simulating Niobium Oxide capacitors with high reliability (0.5%/1000hrs at 85°C) and non-burning high resistance failure mode, as outlined in KYOCERA AVX's resources.
Generated: DETERMINISTIC_d66ea38ee5284d11
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```spice
* Niobium Oxide Capacitor SPICE Model
* High Reliability (0.5%/1000hrs at 85°C)
* Non-burning high resistance failure mode
* Based on KYOCERA AVX specifications
* Model parameters for simulation

.SUBCKT NIOBIUM_OXIDE_CAP 1 2 PARAMS:
+ C=1u       ; Nominal capacitance (Farads)
+ VMAX=10    ; Maximum voltage rating (Volts)
+ ESR=0.1    ; Equivalent series resistance (Ohms)
+ ESL=1n     ; Equivalent series inductance (Henries)
+ LEAK=1n    ; Leakage current (Amps)
+ TCO=150ppm ; Temperature coefficient (ppm/°C)
+ T_OP=25    ; Operating temperature (°C)

* Main capacitor with voltage and temperature dependence
C1 1 3 {C*(1 + TCO*1e-6*(TEMP-T_OP))} 
R_ESR 3 4 {ESR}
L_ESL 4 2 {ESL}

* Leakage current model
G_LEAK 1 2 VALUE={V(1,2)*LEAK/VMAX}

* Non-burning high resistance failure mode
R_FAIL 1 2 1G TC=0,0

* Voltage derating above rated voltage
.if (V(1,2) > VMAX)
    R_DERATE 1 2 {1MEG*(V(1,2)/VMAX)**10}
.endif

* Temperature derating above 85°C
.if (TEMP > 85)
    R_TEMP_DERATE 1 2 {1MEG*exp((TEMP-85)/10)}
.endif

* Model for reliability degradation over time
* 0.5% degradation per 1000 hours at 85°C
.if (TIME > 0)
    R_AGING 1 2 {1MEG*(1 + 0.005*(TIME/3600)/1000)}
.endif

.ENDS NIOBIUM_OXIDE_CAP

* Example usage:
* X1 VCC GND NIOBIUM_OXIDE_CAP PARAMS: C=10u VMAX=16 ESR=0.05
```
