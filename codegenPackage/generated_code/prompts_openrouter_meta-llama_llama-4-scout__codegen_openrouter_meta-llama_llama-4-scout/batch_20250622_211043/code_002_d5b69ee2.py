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
-- Celestia 3D Script: Journey Through the Solar System

-- Define the journey parameters
local journeyWaypoints = {
    -- Earth
    { longitude = 0, latitude = 0, distance = 1.5, duration = 5 },
    -- Mars
    { longitude = 0, latitude = 0, distance = 2.5, duration = 10 },
    -- Jupiter
    { longitude = 0, latitude = 0, distance = 5.2, duration = 15 },
}

-- Function to move to a waypoint
local function moveToWaypoint(waypoint)
    -- Set the destination
    celestia:gotoLocation(waypoint.longitude, waypoint.latitude, waypoint.distance)
    
    -- Wait for the specified duration
    sys:sleep(waypoint.duration)
end

-- Main journey function
local function journeyThroughSolarSystem()
    -- Check if Celestia is running
    if not celestia then
        error("Celestia is not running")
    end

    -- Begin the journey
    for i, waypoint in ipairs(journeyWaypoints) do
        print("Moving to waypoint " .. i .. "...")
        moveToWaypoint(waypoint)
    end
end

-- Error handling and script execution
local function main()
    -- Try to execute the journey
    local status, err = pcall(journeyThroughSolarSystem)
    
    -- Handle any errors
    if not status then
        print("Error: " .. tostring(err))
    end
end

-- Run the main function
main()
```
