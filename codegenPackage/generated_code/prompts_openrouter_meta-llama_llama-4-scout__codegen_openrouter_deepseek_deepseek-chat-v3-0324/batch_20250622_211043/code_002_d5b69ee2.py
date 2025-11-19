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
--[[
Celestia 3D Environment Journey Script
This script demonstrates a basic journey through the Celestia 3D environment
using its built-in Lua scripting language.
--]]

-- Wait for Celestia to fully initialize
wait(1.0)

-- Set initial observer parameters
obs = celestia:getobserver()
obs:setposition(1e9, 0, 0)  -- Start 1 billion km from origin
obs:setorientation(0, 0, 1, 0)  -- Facing positive Z axis

-- Select Earth as the reference object
earth = celestia:find("Sol/Earth")
celestia:select(earth)

-- Set field of view
celestia:setfov(45)

-- Function to smoothly move the observer
function move_to(position, duration, fov)
    celestia:goto(position, duration)
    if fov then
        celestia:setfov(fov, duration)
    end
    wait(duration + 0.5)  -- Add small buffer
end

-- Main journey sequence
try
    -- Approach Earth
    move_to(earth:getposition(), 10.0, 30.0)
    
    -- Orbit around Earth
    for i = 1, 4 do
        angle = math.rad(i * 90)
        x = math.cos(angle) * 2e5
        z = math.sin(angle) * 2e5
        move_to(earth:getposition() + celestia:newvector(x, 0, z), 5.0)
    end
    
    -- Fly to Moon
    moon = celestia:find("Sol/Earth/Moon")
    move_to(moon:getposition(), 8.0, 20.0)
    
    -- View Earth from Moon's surface
    obs:setframe("eclipticj2000", moon)
    obs:setposition(0, 0, 0)
    obs:lookat(earth:getposition())
    celestia:setfov(5.0, 3.0)
    wait(5.0)
    
    -- Travel to Saturn
    saturn = celestia:find("Sol/Saturn")
    move_to(saturn:getposition() + celestia:newvector(0, 0, 5e5), 15.0, 45.0)
    
    -- View Saturn's rings
    obs:lookat(saturn:getposition())
    celestia:setfov(30.0, 5.0)
    wait(10.0)
    
    print("Journey complete!")
catch
    print("Error during journey: " .. tostring(_ERROR))
end
```
