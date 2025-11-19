"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Generate a code example for adding custom player models using the AddonPeds feature in GTA 5.
Generated: DETERMINISTIC_42e3154a0fcf8d4d
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- GTA 5 AddonPeds example
-- This script demonstrates how to add custom player models using the AddonPeds feature

-- Define the addon ped model name and its corresponding Peds data
local pedModelName = "my_custom_ped" -- Change to your custom model name

-- Check if the model is valid and load it
function loadModel(model)
    RequestModel(model) -- Request the model
    while not HasModelLoaded(model) do -- Wait until the model is loaded
        Citizen.Wait(500) -- Wait to prevent freezing
    end
end

-- Function to add and spawn the custom ped
function spawnCustomPed(plantLocation)
    -- Load the model
    loadModel(pedModelName)

    -- Create the ped at the specified coordinates (example coordinates used)
    local x, y, z = table.unpack(plantLocation)
    local ped = CreatePed(0, pedModelName, x, y, z, 0.0, true, false)

    if ped then
        -- Set the ped properties as needed
        SetEntityInvincible(ped, true) -- Make the ped invincible
        SetBlockingOfNonTemporaryEvents(ped, true) -- Prevent the ped from being interrupted by events
        TaskSetBlockingOfNonTemporaryEvents(ped, true) -- Further block events
        return ped
    else
        print("Error: Could not spawn the ped.")
    end
end

-- Example usage
Citizen.CreateThread(function()
    -- Coordinates for where to spawn the custom ped (modify these coordinates)
    local spawnLocation = { 123.45, -123.45, 30.00 } 

    -- Attempt to spawn the custom ped
    local resultPed = spawnCustomPed(spawnLocation)

    if resultPed then
        print("Custom ped spawned successfully.")
    else
        print("Failed to spawn custom ped.")
    end
end)

-- Clean up function to delete the ped if needed
function deletePed(ped)
    if DoesEntityExist(ped) then
        DeleteEntity(ped) -- Delete the ped entity
    end
end

-- Call deletePed when necessary (you should call it when the ped is no longer needed)
-- deletePed(resultPed) -- Uncomment and use this as needed
```
