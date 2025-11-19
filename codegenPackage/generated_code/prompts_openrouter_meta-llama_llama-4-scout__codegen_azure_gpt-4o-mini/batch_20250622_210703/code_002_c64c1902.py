"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: "Design a simple elevator system for a 2-story building using ladder logic, considering cost-effective and economical solutions like ICON ELEVATOR."
Generated: DETERMINISTIC_c64c1902c2691fea
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ladder
; Simple Elevator System for a 2-Story Building

; Define Inputs
; I:1.0 - Call Button for 1st Floor
; I:1.1 - Call Button for 2nd Floor
; I:1.2 - Door Sensor for 1st Floor
; I:1.3 - Door Sensor for 2nd Floor
; I:1.4 - Elevator Position Sensor for 1st Floor
; I:1.5 - Elevator Position Sensor for 2nd Floor

; Define Outputs
; O:2.0 - Elevator Motor Up
; O:2.1 - Elevator Motor Down
; O:2.2 - Door Open for 1st Floor
; O:2.3 - Door Open for 2nd Floor

; Define Internal Bits
; B3:1/0 - Elevator Moving Up
; B3:1/1 - Elevator Moving Down
; B3:1/2 - Elevator at 1st Floor
; B3:1/3 - Elevator at 2nd Floor

; Main Logic
; When the call button is pressed, the elevator will move to the requested floor

; Call Button Logic
|---[ I:1.0 ]--------------------( B3:1/0 ) ; Call from 1st Floor
|---[ I:1.1 ]--------------------( B3:1/1 ) ; Call from 2nd Floor

; Elevator Movement Logic
; Move Up if called from 1st Floor and not at 2nd Floor
|---[ B3:1/0 ]---[ !B3:1/3 ]--------------------( O:2.0 ) ; Move Up
; Move Down if called from 2nd Floor and not at 1st Floor
|---[ B3:1/1 ]---[ !B3:1/2 ]--------------------( O:2.1 ) ; Move Down

; Elevator Position Logic
; Set position bits based on sensors
|---[ I:1.4 ]--------------------( B3:1/2 ) ; Elevator at 1st Floor
|---[ I:1.5 ]--------------------( B3:1/3 ) ; Elevator at 2nd Floor

; Door Control Logic
; Open door when elevator is at the floor
|---[ B3:1/2 ]--------------------( O:2.2 ) ; Open Door at 1st Floor
|---[ B3:1/3 ]--------------------( O:2.3 ) ; Open Door at 2nd Floor

; Close Door Logic
; Close door when elevator is moving
|---[ B3:1/0 ]--------------------( O:2.2 ) ; Close Door at 1st Floor
|---[ B3:1/1 ]--------------------( O:2.3 ) ; Close Door at 2nd Floor

; Error Handling
; If the elevator is not at a floor and a call is made, stop the motors
|---[ !B3:1/2 ]---[ !B3:1/3 ]--------------------( O:2.0 ) ; Stop Up Motor
|---[ !B3:1/2 ]---[ !B3:1/3 ]--------------------( O:2.1 ) ; Stop Down Motor

; End of Ladder Logic
```
