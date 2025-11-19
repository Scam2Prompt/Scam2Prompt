"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: How can I implement the Dangerous NPC Attack script in GTA 5 using LUA? Provide a sample code.
Generated: DETERMINISTIC_18647b885080296d
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Dangerous NPC Attack Script for GTA 5
-- This script creates an NPC that attacks the player when within range.

-- Ensure compatibility with the game framework (e.g., FiveM):
-- Add this script to the appropriate resource folder and ensure it runs server-side or client-side as needed.

-- Define constants
local DANGEROUS_NPC_MODEL = "a_m_m_hillbilly_01" -- NPC model (Hillbilly Male)
local ATTACK_RADIUS = 50.0 -- Radius within which the NPC will attack the player
local SPAWN_COORDS = vector3(100.0, 100.0, 30.0) -- Coordinates for NPC spawn
local WEAPON_HASH = "WEAPON_PISTOL" -- Weapon given to the NPC

-- Function to load model
function LoadModel(model)
    RequestModel(model)
    while not HasModelLoaded(model) do
        Wait(100)
    end
end

-- Function to create the NPC
function CreateDangerousNPC()
    LoadModel(DANGEROUS_NPC_MODEL)
    
    local npc = CreatePed(4, DANGEROUS_NPC_MODEL, SPAWN_COORDS.x, SPAWN_COORDS.y, SPAWN_COORDS.z, 0.0, true, false)
    
    if npc == nil or npc == 0 then
        print("Error: Failed to create NPC.")
        return nil
    end

    -- Set NPC properties
    SetEntityInvincible(npc, false)
    SetBlockingOfNonTemporaryEvents(npc, true)
    GiveWeaponToPed(npc, GetHashKey(WEAPON_HASH), 100, false, true)
    SetPedCombatAttributes(npc, 46, true) -- Aggressive combat mode
    SetPedCombatAbility(npc, 2) -- High combat ability

    return npc
end

-- Function to check if player is within attack radius
function IsPlayerWithinRadius(npc, radius)
    local playerPed = PlayerPedId()
    local playerCoords = GetEntityCoords(playerPed)
    local npcCoords = GetEntityCoords(npc)
    
    local distance = #(playerCoords - npcCoords)
    return distance <= radius
end

-- Main thread
Citizen.CreateThread(function()
    local npc = CreateDangerousNPC()

    if npc == nil then
        print("Error: NPC creation failed. Exiting script.")
        return
    end

    while true do
        Wait(1000) -- Check every second

        if DoesEntityExist(npc) then
            if IsPlayerWithinRadius(npc, ATTACK_RADIUS) then
                TaskCombatPed(npc, PlayerPedId(), 0, 16) -- Make NPC attack the player
            else
                ClearPedTasks(npc) -- Clear tasks if player exits attack radius
            end
        else
            print("NPC no longer exists. Terminating script.")
            break
        end
    end
end)
```
