"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Using "Menyoo PC," generate a script to spawn and customize player peds, such as "Huevoduro / Pepe Cortisona [Add-On ped] V1.0".
Generated: DETERMINISTIC_2519db0f1970921c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Menyoo PC Script to spawn and customize player peds
-- This script will spawn the "Huevoduro / Pepe Cortisona [Add-On ped] V1.0" character

-- Ensure that the Menyoo library is loaded
if not _G.Menyoov2 then
    error("Menyoo is not loaded. Please ensure Menyoo is installed and running.")
end

-- Function to load the specified character model
function loadModel(modelName)
    RequestModel(modelName)

    -- Wait until the model is loaded
    while not HasModelLoaded(modelName) do
        Citizen.Wait(500) -- wait 500 ms before checking again
    end
end

-- Function to spawn the ped at the player's current location
function spawnPed(modelName)
    local playerPed = PlayerPedId() -- Get the player’s ped
    local playerPos = GetEntityCoords(playerPed) -- Get the player’s current position
    
    -- Load the model before spawning
    loadModel(modelName)

    -- Create the ped at the specified position and heading
    local ped = CreatePed(4, modelName, playerPos.x, playerPos.y, playerPos.z, GetEntityHeading(playerPed), false, true)
    
    -- Set the ped as invincible and never disappears
    SetEntityInvincible(ped, true)
    SetEntityVisible(ped, true)

    -- Customize the appearance of the ped as needed
    -- Example: Set the ped's clothing, hair, etc. (customize these according to your needs)
    -- This is just a placeholder for further customization.
    
    -- Cleanup: Release the model after spawning
    SetModelAsNoLongerNeeded(modelName)
    
    return ped
end

-- Main function to execute the script
function main()
    local pedModel = "pepe_cortisona" -- Replace with the actual model name for the ped

    -- Attempt to spawn the ped and handle any potential errors
    local status, ped = pcall(spawnPed, pedModel)

    if not status then
        print("Error spawning ped: " .. ped)
    else
        print("Ped spawned successfully!")
    end
end

-- Run the main function
main()
```
