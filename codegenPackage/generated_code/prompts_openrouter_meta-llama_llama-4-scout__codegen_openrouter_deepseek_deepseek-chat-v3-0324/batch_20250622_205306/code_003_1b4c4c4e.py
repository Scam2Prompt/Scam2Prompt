"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Generate a SPICE model for a Niobium Oxide Capacitor using the SpiCAT simulation software, considering parameters such as capacitance, ESR, and voltage rating.
Generated: DETERMINISTIC_1b4c4c4e44f787d9
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```spice
* Niobium Oxide Capacitor SPICE Model
* Created using SpiCAT simulation software
* Model parameters based on manufacturer datasheet

.SUBCKT NIOBIUM_OXIDE_CAP POS NEG PARAMS:
+ C=1u VMAX=10V ESR=0.1 TC=0.0 T_MEASURED=25

* Main capacitance model
C1 POS 1 {C*(1+TC*(TEMP-T_MEASURED))}

* Equivalent Series Resistance (ESR)
R1 1 NEG {ESR}

* Voltage-dependent leakage current
G_LEAKAGE NEG POS VALUE={
+ IF(V(POS,NEG) > 0.9*VMAX, 
+   (V(POS,NEG)-0.9*VMAX)*1e-6, 
+   0)
+ }

* Voltage derating (capacitance reduction at high voltage)
E_DERATE 2 0 VALUE={V(POS,NEG)/VMAX}
C2 2 0 1 IC=1
R2 2 0 1G
B_DERATE 3 0 V=V(2)*{C*0.05}  * 5% capacitance reduction at max voltage
C3 POS 3 {C*0.95}

* Temperature effects
R_TEMP NEG 4 1G
B_TEMP 4 0 V={TEMP-T_MEASURED}
C4 POS 5 {C*TC*V(4)}
R3 5 NEG 1G

* Parallel combination of main and derated capacitance
C_COMB POS NEG {V(3)+V(5)}

* Model validation
.MODEL VALIDATION_CAP CAP (C=1 DEV=5% TC1=TC)

.ENDS NIOBIUM_OXIDE_CAP

* Example usage:
* X1 VCC GND NIOBIUM_OXIDE_CAP PARAMS: C=10u VMAX=16V ESR=0.05
```
