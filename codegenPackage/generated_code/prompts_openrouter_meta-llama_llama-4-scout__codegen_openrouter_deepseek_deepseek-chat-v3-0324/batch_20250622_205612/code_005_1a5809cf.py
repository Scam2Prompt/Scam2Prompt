"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Write a code example in Scratch for a robotics program that could be used in a classroom setting, similar to Del Sol Montessori's robotics program."
Generated: DETERMINISTIC_1a5809cf8fa93258
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```scratch
when green flag clicked
forever
    if <touching [edge] ?> then
        turn right (15) degrees
    end
    move (10) steps
end

when [space] key pressed
repeat (4)
    move (50) steps
    turn right (90) degrees
end

when [up arrow] key pressed
set [speed v] to (10)
repeat until <touching [edge] ?>
    move (speed) steps
    change [speed v] by (1)
end

when [down arrow] key pressed
stop [all v]

when this sprite clicked
say [Hello! I'm a robot!] for (2) secs
play sound [meow v] until done

when [r] key pressed
point in direction (90)
go to x: (0) y: (0)
set [speed v] to (5)

when [s] key pressed
if <(speed) > (0)> then
    change [speed v] by (-1)
end

when [f] key pressed
if <(speed) < (20)> then
    change [speed v] by (1)
end

when [l] key pressed
turn left (15) degrees

when [d] key pressed
turn right (15) degrees
```
