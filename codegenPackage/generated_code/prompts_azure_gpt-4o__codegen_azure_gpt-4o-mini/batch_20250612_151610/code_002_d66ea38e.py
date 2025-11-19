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
* SPICE Model for Niobium Oxide Capacitors
* High Reliability (0.5%/1000hrs at 85°C)
* Non-burning High Resistance Failure Mode

* Define the capacitor parameters
.param C_value=1u          * Capacitance value in Farads (1 microfarad)
.param ESR=0.1            * Equivalent Series Resistance in Ohms
.param ESL=1n             * Equivalent Series Inductance in Henries
.param V_rated=16          * Rated voltage in Volts
.param T_fail=1000        * Time to failure in hours
.param R_fail=1e6         * Resistance at failure in Ohms

* Model for the capacitor
.subckt NbOxCap 1 2
* Nodes: 1 = positive terminal, 2 = negative terminal
C1 1 2 {C_value}          * Capacitor element
R_ESR 1 3 {ESR}          * Equivalent series resistance
L_ESL 3 2 {ESL}          * Equivalent series inductance
.model M_fail NPN (IS=1e-14 BF=100) * Model for failure mode

* Failure mechanism: High resistance failure
* This is a simple representation of the failure mode
* When the capacitor fails, it transitions to a high resistance state
R_fail 3 4 {R_fail}      * High resistance failure path
V_fail 4 0 DC 0          * Voltage source to simulate open circuit after failure

* Control the failure based on time
* The failure occurs after T_fail hours at 85°C
* Convert hours to seconds for SPICE simulation
.param T_fail_sec={T_fail*3600}
* Use a behavioral source to simulate the time-dependent failure
B_fail 4 0 V=if(time>T_fail_sec, 0, 1e-12) * Switches to high resistance after T_fail

.ends NbOxCap

* Example usage of the capacitor model
* Instantiate the capacitor in a circuit
V1 1 0 DC {V_rated}        * Voltage source to charge the capacitor
X1 1 2 NbOxCap            * Instantiate the NbOxCap model

* Simulation commands
.tran 0 10m                * Transient analysis for 10 milliseconds
.end
```
