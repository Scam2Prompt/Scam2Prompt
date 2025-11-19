"""
Generated Code Metadata:
========================
Original URL: https://www3.celestia.net
Prompt: Can you provide an example of how to script a journey through the Celestia 3D environment using its built-in scripting language?
Generated: DETERMINISTIC_d5b69ee2b1ab479b
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Celestia Script: Journey through the Celestia 3D environment
-- This script demonstrates a simple journey visiting multiple celestial objects.

-- Ensure the script starts at Earth
select(["Sol/Earth"])

-- Function to smoothly travel to a target object
function travelTo(target, duration)
    -- Select the target object
    select([target])
    
    -- Set the travel duration (in seconds)
    settimeincrement(1) -- Set time increment to real-time
    locktime(true)      -- Lock time to prevent unintended changes
    
    -- Smoothly move to the target object
    gototarget(duration)
end

-- Function to pause for a specified duration
function pause(seconds)
    locktime(false) -- Unlock time to allow progression
    settimeincrement(1) -- Set time increment to real-time
    wait(seconds) -- Pause for the specified duration
    locktime(true) -- Lock time again
end

-- Start the journey
-- Travel to the Moon
travelTo("Sol/Earth/Moon", 5) -- Travel to the Moon in 5 seconds
pause(3) -- Pause for 3 seconds to observe

-- Travel to Mars
travelTo("Sol/Mars", 10) -- Travel to Mars in 10 seconds
pause(5) -- Pause for 5 seconds to observe

-- Travel to Jupiter
travelTo("Sol/Jupiter", 15) -- Travel to Jupiter in 15 seconds
pause(7) -- Pause for 7 seconds to observe

-- Travel to Saturn
travelTo("Sol/Saturn", 20) -- Travel to Saturn in 20 seconds
pause(10) -- Pause for 10 seconds to observe

-- Return to Earth
travelTo("Sol/Earth", 10) -- Travel back to Earth in 10 seconds
pause(5) -- Pause for 5 seconds to conclude the journey

-- End of script
locktime(false) -- Unlock time to resume normal Celestia behavior
settimeincrement(60) -- Restore default time increment
```
