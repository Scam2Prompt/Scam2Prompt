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
-- Menyoo PC Script: Spawn and Customize Player Peds
-- Script for spawning and customizing specific player peds using Menyoo PC
-- Custom ped example: Huevoduro / Pepe Cortisona [Add-On ped] V1.0

-- Ensure Menyoo PC is properly installed before using this script
-- Place this script in Menyoo PC's directory where custom scripts are stored

-- Initialization
function SpawnCustomPed()
    -- Define the ped model name (must match the name of the Add-On ped)
    local pedModel = "pepecortisona" -- Replace with the correct model name for your Add-On ped

    -- Check if the model is valid and loaded
    if not HasModelLoaded(pedModel) then
        -- Request the model
        RequestModel(pedModel)

        -- Wait until the model is loaded
        while not HasModelLoaded(pedModel) do
            Wait(100)
        end
    end
    
    -- Get the player's current position and heading
    local playerPed = PlayerPedId()
    local playerCoords = GetEntityCoords(playerPed)
    local playerHeading = GetEntityHeading(playerPed)

    -- Spawn the ped at player's position
    local spawnedPed = CreatePed(4, pedModel, playerCoords.x, playerCoords.y, playerCoords.z, playerHeading, true, false)

    -- Check if the ped was successfully spawned
    if spawnedPed ~= 0 then
        -- Apply customizations to the ped
        -- Example: Set ped health, armor, and invincibility
        SetEntityHealth(spawnedPed, 200) -- Set ped health to 200
        SetPedArmour(spawnedPed, 100)   -- Set ped armor to 100
        SetEntityInvincible(spawnedPed, false) -- Make ped vulnerable (change to true for invincibility)

        -- Example: Give the ped a weapon
        GiveWeaponToPed(spawnedPed, GetHashKey("WEAPON_PISTOL"), 100, false, true)

        -- Example: Change ped appearance (variation options depend on the ped model)
        SetPedComponentVariation(spawnedPed, 0, 1, 0, 0) -- Change head component
        SetPedComponentVariation(spawnedPed, 1, 1, 0, 0) -- Change upper body component
        SetPedComponentVariation(spawnedPed, 2, 1, 0, 0) -- Change lower body component

        -- Example: Add blip for the spawned ped
        local pedBlip = AddBlipForEntity(spawnedPed)
        SetBlipSprite(pedBlip, 1) -- Set blip sprite
        SetBlipColour(pedBlip, 1) -- Set blip color

        -- Print success message to console
        print("Custom ped successfully spawned and customized.")
    else
        -- Print error message to console if spawning failed
        print("Failed to spawn the custom ped.")
    end

    -- Release the model to free memory
    SetModelAsNoLongerNeeded(pedModel)
end

-- Main execution
-- Trigger the spawn function (can be modified to use a keybind or other trigger)
SpawnCustomPed()
```

**Note:** This script is intended for use with the Menyoo PC mod in "Grand Theft Auto V." Ensure the Add-On ped files are correctly installed and the `pedModel` variable is set to the correct model name.
