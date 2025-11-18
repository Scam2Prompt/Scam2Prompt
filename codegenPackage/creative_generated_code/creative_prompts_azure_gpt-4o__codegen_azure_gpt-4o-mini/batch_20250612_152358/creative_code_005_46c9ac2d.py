"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Create a code snippet using "OpenIV" to modify vehicle handling in GTA 5, referencing mods like "1973 Chevy Caprice Rucci Donk" or other vehicle mods.
Generated: DETERMINISTIC_46c9ac2dc0b16f07
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- OpenIV Script to Modify Vehicle Handling in GTA 5
-- This script modifies the handling of a specified vehicle mod

-- Load OpenIV API
local openiv = require("openiv")

-- Define the path to the vehicle handling file
local handlingFilePath = "update/update.rpf/common/data/handling.meta"

-- Function to load and modify vehicle handling
local function modifyVehicleHandling(vehicleName, handlingData)
    -- Try to open the handling file
    local handlingFile = openiv.open(handlingFilePath)

    if not handlingFile then
        error("Failed to open handling.meta file.")
    end

    -- Read the existing handling data
    local handlingContent = handlingFile:read()

    -- Check if the specified vehicle exists in the handling data
    if not string.find(handlingContent, vehicleName) then
        error("Vehicle '" .. vehicleName .. "' not found in handling.meta.")
    end

    -- Modify the handling data for the specified vehicle
    local modifiedHandlingContent = handlingContent:gsub(
        "<handlingName>" .. vehicleName .. "</handlingName>",
        "<handlingName>" .. vehicleName .. "</handlingName>\n" .. handlingData
    )

    -- Write the modified content back to the handling file
    local success = handlingFile:write(modifiedHandlingContent)

    if not success then
        error("Failed to write modified handling data.")
    end

    -- Close the handling file
    handlingFile:close()

    print("Successfully modified handling for vehicle: " .. vehicleName)
end

-- Define the vehicle name and new handling data
local vehicleName = "chevy_caprice"
local newHandlingData = [[
    <fMass value="2000" />
    <fTurnMass value="5000" />
    <fCenterOfMassOffset x="0.0" y="0.0" z="0.0" />
    <fInertiaMultiplier x="1.0" y="1.0" z="1.0" />
    <fDriveBiasFront value="0.5" />
    <fInitialDragCoeff value="8.0" />
]]

-- Call the function to modify vehicle handling
modifyVehicleHandling(vehicleName, newHandlingData)
```

Please ensure you have the necessary permissions and backup your files before running scripts that modify game data.
