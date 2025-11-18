"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://z-innovations.de
Prompt: Provide an example of a CNC programming script that could be used in a consulting project to optimize production workflows, as described by z-innovations.
Generated: DETERMINISTIC_e5162412cbd233b6
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```gcode
(Consulting Project CNC Program for Optimized Workflow by Z-Innovations)
(Program Number: O0001)
(Description: Optimized milling workflow for a rectangular pocket)
(Revision: 1.0)
(Date: YYYY-MM-DD)
(Operator: John Doe)

O0001
(PROGRAM START)

(--- Tool Setup ---)
(T1: 10mm Flat End Mill)
G20                (Set units to inches)
G17                (Select XY Plane)
G90                (Set absolute positioning)

(--- Safety and Initialization ---)
G21                (Set units to millimeters)
G94                (Set feed rate mode to mm/min)
G40                (Cancel cutter radius compensation)
G49                (Cancel tool length offset)
G80                (Cancel canned cycle)
G28 G91 Z0         (Return Z-axis to machine home)
G28 G91 Y0         (Return Y-axis to machine home)
G28 G91 X0         (Return X-axis to machine home)
G90                (Return to absolute position mode)

(--- Tool Change ---)
T1 M06             (Select Tool 1: 10mm Flat End Mill)
S1500 M03          (Set spindle speed to 1500 RPM and turn spindle clockwise)
G54                (Select work offset #1)

(--- Coolant Setup ---)
M08                (Turn coolant ON)

(--- Pocket Milling ---)
G0 X0 Y0 Z5        (Rapid positioning to safe height above starting point)
G0 X10 Y10         (Rapid move to pocket start location)
G1 Z-5 F100        (Linear feed move to cut depth at 100 mm/min feed rate)
(Perform pocket clearing using zigzag toolpath)
G91                (Switch to incremental positioning mode)
G1 X20 F300        (Move tool 20mm in X direction at 300 mm/min)
G1 Y20 F300        (Move tool 20mm in Y direction at 300 mm/min)
G1 X-20 F300       (Move tool -20mm in X direction at 300 mm/min)
G1 Y-20 F300       (Move tool -20mm in Y direction at 300 mm/min)
G90                (Back to absolute positioning mode)

(--- Return to Safe Position ---)
G0 Z10             (Lift tool to safe height)
G0 X0 Y0           (Return tool to origin)

(--- Coolant Shutdown ---)
M09                (Turn coolant OFF)

(--- End Program ---)
M30                (End program and reset)

(PROGRAM END)
```
