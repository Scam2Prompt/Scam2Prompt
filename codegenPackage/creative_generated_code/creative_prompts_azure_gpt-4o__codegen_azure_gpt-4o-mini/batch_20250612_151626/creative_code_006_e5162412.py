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
%
O1000 ( Main Program for Optimizing CNC Production Workflow )
G21 ( Set units to millimeters )
G17 ( Select XY plane )
G90 ( Absolute positioning mode )

( Define tool parameters )
T1 M06 ( Select Tool 1 and change tool )
G0 Z50 ( Move tool to safe height )

( Start spindle )
S1200 M03 ( Start spindle at 1200 RPM in clockwise direction )

( Move to start position )
G0 X0 Y0 ( Rapid move to start position )
G0 Z5 ( Move down to cutting height )

( Begin cutting operation )
G1 Z-10 F100 ( Linear move down to Z=-10 at feed rate of 100 mm/min )
G1 X100 F200 ( Move in X direction to X=100 at feed rate of 200 mm/min )
G1 Y100 ( Move in Y direction to Y=100 )
G1 X0 ( Move back to X=0 )
G1 Y0 ( Move back to Y=0 )
G0 Z50 ( Retract to safe height )

( Tool change example for second operation )
T2 M06 ( Change to Tool 2 )
S1500 M03 ( Start spindle at 1500 RPM for Tool 2 )
G0 X50 Y50 ( Rapid move to new start position for Tool 2 )
G0 Z5 ( Move down to cutting height )
G1 Z-15 F100 ( Linear move down to Z=-15 )
G1 X150 F200 ( Move in X direction to X=150 )
G1 Y150 ( Move in Y direction to Y=150 )
G1 X50 ( Move back to X=50 )
G1 Y50 ( Move back to Y=50 )
G0 Z50 ( Retract to safe height )

( End of program )
M05 ( Stop spindle )
G0 X0 Y0 ( Return to home position )
M30 ( End of program and reset )
%
```
