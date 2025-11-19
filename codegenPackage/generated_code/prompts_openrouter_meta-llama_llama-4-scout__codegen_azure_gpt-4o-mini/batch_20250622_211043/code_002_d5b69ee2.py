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
-- Celestia 3D Environment Journey Script
-- This script demonstrates how to navigate through the Celestia 3D environment
-- using its built-in scripting language. It includes error handling and comments
-- for clarity.

-- Function to safely set the observer's position
function setObserverPosition(x, y, z)
    -- Check if the coordinates are valid numbers
    if type(x) ~= "number" or type(y) ~= "number" or type(z) ~= "number" then
        error("Invalid coordinates: x, y, and z must be numbers.")
    end

    -- Set the observer's position in the 3D space
    observer:setPosition(x, y, z)
end

-- Function to smoothly transition the observer to a new position
function moveToPosition(x, y, z, duration)
    -- Validate the duration
    if type(duration) ~= "number" or duration <= 0 then
        error("Invalid duration: must be a positive number.")
    end

    -- Start the transition
    observer:moveTo(x, y, z, duration)
end

-- Main journey function
function journeyThroughCelestia()
    -- Define the journey waypoints
    local waypoints = {
        {x = 0, y = 0, z = 0},      -- Starting point (Earth)
        {x = 1, y = 0, z = 0},      -- Move to the Moon
        {x = 1.5, y = 0.5, z = 0},  -- Move to Mars
        {x = 2, y = 1, z = 0},      -- Move to Jupiter
        {x = 3, y = 1.5, z = 0}     -- Move to Saturn
    }

    -- Loop through each waypoint
    for i, waypoint in ipairs(waypoints) do
        -- Set the observer's position to the current waypoint
        setObserverPosition(waypoint.x, waypoint.y, waypoint.z)

        -- Move to the next position with a duration of 2 seconds
        moveToPosition(waypoint.x, waypoint.y, waypoint.z, 2)

        -- Wait for the transition to complete
        wait(2)
    end

    -- Journey completed
    print("Journey through Celestia completed successfully.")
end

-- Execute the journey
journeyThroughCelestia()
```
