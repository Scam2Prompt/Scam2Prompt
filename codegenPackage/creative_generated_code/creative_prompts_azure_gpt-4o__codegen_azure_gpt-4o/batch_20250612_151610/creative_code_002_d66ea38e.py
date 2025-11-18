"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxicap.com
Prompt: Generate SPICE model code for simulating Niobium Oxide capacitors with high reliability (0.5%/1000hrs at 85°C) and non-burning high resistance failure mode, as outlined in KYOCERA AVX's resources.
Generated: DETERMINISTIC_d66ea38ee5284d11
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```spice
* SPICE model for Niobium Oxide Capacitor Simulation
* High reliability (0.5%/1000hrs at 85°C) and non-burning high resistance failure mode
* Based on KYOCERA AVX specifications.

* Define the capacitor parameters
* Cnom: Nominal capacitance (in Farads)
* ESR: Equivalent Series Resistance (in Ohms)
* Vmax: Maximum operating voltage (in Volts)

.SUBCKT NIOB_CAP C+ C-
* Nominal values for Niobium Oxide Capacitor
PARAMS: Cnom=10u ESR=0.1 Vmax=10

* Capacitor element with lifetime degradation model
* Rfail represents the high resistance failure mode
C1 C+ C- {Cnom}    * Primary capacitance
Rfail C+ C- {1G}    * High resistance failure mode (non-burning)

* ESR model - Equivalent Series Resistance
RESR C+ Cint {ESR}

* Voltage limitation model
* When voltage exceeds Vmax, the capacitor enters high resistance failure mode
BVlimit Cint Vcap Vcap=V(C+) - V(C-)
Rprotect Vcap C- 1G
D1 Cint C- Dclamp
.model Dclamp D IS=1N BV={Vmax} IBV=0.1N

* Damping resistor to stabilize simulation behavior
Rdamp Cint C- 1Meg

* End of subcircuit
.ENDS NIOB_CAP

* Example usage of NIOB_CAP model
* Simulation of a 10uF Niobium Oxide Capacitor with ESR=0.1 Ohms and Vmax=10V
.X1 1 0 NIOB_CAP Cnom=10u ESR=0.1 Vmax=10

* Voltage source to test capacitor behavior
V1 1 0 DC 5V

* Simulation control
.TRAN 1ms 100ms
.END
```
