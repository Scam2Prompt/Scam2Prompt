"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: Design a circuit for a 9V battery-powered device that produces a 30KHz frequency output, similar to the Hulda Clark Zapper.
Generated: DETERMINISTIC_b0bd8b7de49e1868
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Circuit design for a 9V battery-powered 30KHz frequency generator (Zapper-like device)
This is a SPICE netlist that can be simulated in tools like LTSpice or ngspice
"""

# 30KHz Zapper Circuit Netlist
* 9V Battery-Powered 30KHz Frequency Generator
* Based on similar principles to Hulda Clark Zapper design

V1 1 0 DC 9V      ; 9V power supply
R1 1 2 10k        ; Current limiting resistor
C1 2 0 10nF       ; Timing capacitor
R2 2 3 100k       ; Feedback resistor
R3 3 0 100k       ; Feedback resistor
X1 2 3 0 0 1 LM555 ; 555 timer IC configured as astable oscillator

* Output stage
R4 3 4 1k         ; Output resistor
Q1 4 5 0 2N3904   ; NPN transistor for output buffering
R5 5 0 1k         ; Output load resistor
D1 0 5 LED        ; Optional output indicator LED

* Frequency calculation components (for ~30KHz)
* f = 1.44 / ((R1 + 2*R2) * C1)
* With R1=10k, R2=100k, C1=10nF:
* f = 1.44 / ((10k + 2*100k) * 10nF) = ~30.7KHz

.model 2N3904 NPN(Is=1.4e-14 Bf=300 Vaf=15 Ikf=0.06 Ise=3e-13 Ne=1.6)

.control
tran 0.1ms 1ms    ; Transient analysis for 1ms with 0.1ms steps
plot v(5)         ; Plot output voltage
.endc

.end
```
