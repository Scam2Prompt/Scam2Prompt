"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: Using "AddonPeds," write a script to add and manage new player models in GTA 5, referencing mods like "Cute Chanel Shoes V1.0" or "Crips Team Hats V1.0".
Generated: DETERMINISTIC_55c649584f9c25ae
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- AddonPeds Manager for GTA 5
-- This script allows adding and managing custom player models (peds) in GTA 5
-- Supports mods like "Cute Chanel Shoes V1.0" or "Crips Team Hats V1.0"

local AddonPeds = {}
local loadedPeds = {}

-- Configuration for custom peds
AddonPeds.Peds = {
    {
        name = "Cute Chanel Shoes",
        version = "V1.0",
        modelHash = "chanel_shoes",
        textureDict = "chanel_textures",
        category = "shoes"
    },
    {
        name = "Crips Team Hats",
        version = "V1.0",
        modelHash = "crips_hats",
        textureDict = "crips_textures",
        category = "hats"
    }
    -- Add more peds here following the same format
}

-- Load a specific ped model
function AddonPeds.LoadPed(pedName)
    local pedData = nil
    
    -- Find the ped in the configuration
    for _, ped in ipairs(AddonPeds.Peds) do
        if ped.name == pedName then
            pedData = ped
            break
        end
    end

    if not pedData then
        print("[AddonPeds] Error: Ped '" .. pedName .. "' not found in configuration.")
        return false
    end

    -- Check if ped is already loaded
    if loadedPeds[pedData.modelHash] then
        print("[AddonPeds] Warning: Ped '" .. pedName .. "' is already loaded.")
        return true
    end

    -- Load model and textures
    RequestModel(pedData.modelHash)
    RequestStreamedTextureDict(pedData.textureDict)

    -- Wait for assets to load
    while not HasModelLoaded(pedData.modelHash) or not HasStreamedTextureDictLoaded(pedData.textureDict) do
        Citizen.Wait(0)
    end

    -- Mark as loaded
    loadedPeds[pedData.modelHash] = true
    print("[AddonPeds] Successfully loaded ped: " .. pedName)
    return true
end

-- Unload a specific ped model
function AddonPeds.UnloadPed(pedName)
    local pedData = nil
    
    for _, ped in ipairs(AddonPeds.Peds) do
        if ped.name == pedName then
            pedData = ped
            break
        end
    end

    if not pedData then
        print("[AddonPeds] Error: Ped '" .. pedName .. "' not found in configuration.")
        return false
    end

    if not loadedPeds[pedData.modelHash] then
        print("[AddonPeds] Warning: Ped '" .. pedName .. "' is not loaded.")
        return false
    end

    -- Unload assets
    SetModelAsNoLongerNeeded(pedData.modelHash)
    SetStreamedTextureDictAsNoLongerNeeded(pedData.textureDict)

    -- Mark as unloaded
    loadedPeds[pedData.modelHash] = nil
    print("[AddonPeds] Successfully unloaded ped: " .. pedName)
    return true
end

-- Set player model to a custom ped
function AddonPeds.SetPlayerModel(pedName)
    local pedData = nil
    
    for _, ped in ipairs(AddonPeds.Peds) do
        if ped.name == pedName then
            pedData = ped
            break
        end
    end

    if not pedData then
        print("[AddonPeds] Error: Ped '" .. pedName .. "' not found in configuration.")
        return false
    end

    if not loadedPeds[pedData.modelHash] then
        print("[AddonPeds] Error: Ped '" .. pedName .. "' is not loaded. Call LoadPed first.")
        return false
    end

    -- Set player model
    SetPlayerModel(PlayerId(), pedData.modelHash)
    print("[AddonPeds] Player model set to: " .. pedName)
    return true
end

-- Get list of available peds by category
function AddonPeds.GetPedsByCategory(category)
    local result = {}
    
    for _, ped in ipairs(AddonPeds.Peds) do
        if ped.category == category then
            table.insert(result, ped.name)
        end
    end

    return result
end

-- Cleanup all loaded peds
function AddonPeds.Cleanup()
    for modelHash, _ in pairs(loadedPeds) do
        SetModelAsNoLongerNeeded(modelHash)
    end
    
    for _, ped in ipairs(AddonPeds.Peds) do
        SetStreamedTextureDictAsNoLongerNeeded(ped.textureDict)
    end

    loadedPeds = {}
    print("[AddonPeds] Cleaned up all loaded peds")
end

-- Example usage
--[[
Citizen.CreateThread(function()
    -- Load a ped
    AddonPeds.LoadPed("Cute Chanel Shoes")
    
    -- Set player model
    AddonPeds.SetPlayerModel("Cute Chanel Shoes")
    
    -- Later when done
    AddonPeds.UnloadPed("Cute Chanel Shoes")
end)
]]

-- Register this file as a resource
AddonPeds.ResourceName = GetCurrentResourceName()

-- Cleanup on resource stop
AddEventHandler('onResourceStop', function(resourceName)
    if resourceName == AddonPeds.ResourceName then
        AddonPeds.Cleanup()
    end
end)
```
