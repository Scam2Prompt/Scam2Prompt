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
* SPICE Model for Niobium Oxide Capacitor
* This model includes capacitance, ESR, and voltage rating parameters.

* Parameters
.param C = 100u          ; Capacitance in Farads (e.g., 100 µF)
.param ESR = 0.1         ; Equivalent Series Resistance in Ohms (e.g., 0.1 Ω)
.param Vmax = 16         ; Maximum Voltage Rating in Volts (e.g., 16 V)

* Voltage Source for Testing
V1 1 0 DC 12             ; DC voltage source (e.g., 12 V for testing)

* Niobium Oxide Capacitor Model
* Capacitor with ESR
C1 1 2 {C}               ; Capacitor with specified capacitance
R1 2 0 {ESR}             ; ESR in series with the capacitor

* Voltage Rating Protection
D1 1 0 Dclamp            ; Diode to clamp voltage exceeding Vmax
.model Dclamp D(IS=1e-15 BV={Vmax}) ; Diode model with breakdown voltage set to Vmax

* Simulation Control
.tran 0 10ms             ; Transient analysis for 10 ms
.end
```
