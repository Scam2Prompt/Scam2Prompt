"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: How can I implement the Dangerous NPC Attack script in GTA 5 using LUA? Provide a sample code.
Generated: DETERMINISTIC_18647b885080296d
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Dangerous NPC Attack Script for GTA 5
-- This script allows NPCs to attack the player when they come within a certain range.

-- Constants
local ATTACK_RANGE = 20.0 -- Distance within which NPCs will attack the player
local ATTACK_COOLDOWN = 5000 -- Cooldown time in milliseconds between attacks

-- Function to check if the player is within attack range
local function isPlayerInRange(npc, player)
    local npcCoords = GetEntityCoords(npc)
    local playerCoords = GetEntityCoords(player)
    local distance = Vdist(npcCoords.x, npcCoords.y, npcCoords.z, playerCoords.x, playerCoords.y, playerCoords.z)
    return distance <= ATTACK_RANGE
end

-- Function to make the NPC attack the player
local function npcAttack(npc, player)
    -- Ensure the NPC is not already attacking
    if not IsEntityPlayingAnim(npc, "combat@attack", "attack", 3) then
        -- Start the attack animation
        TaskPlayAnim(npc, "combat@attack", "attack", 8.0, -8.0, -1, 0, 0, false, false, false)
        -- Apply damage to the player
        ApplyDamageToPed(player, 10, false) -- Damage value can be adjusted
        -- Wait for cooldown before allowing another attack
        Citizen.Wait(ATTACK_COOLDOWN)
    end
end

-- Main loop to monitor NPCs and player
Citizen.CreateThread(function()
    local player = PlayerPedId() -- Get the player's character
    while true do
        Citizen.Wait(1000) -- Check every second
        local npcs = GetNearbyNpcs() -- Function to get nearby NPCs (to be implemented)

        for _, npc in ipairs(npcs) do
            if isPlayerInRange(npc, player) then
                npcAttack(npc, player)
            end
        end
    end
end)

-- Function to get nearby NPCs (placeholder implementation)
function GetNearbyNpcs()
    local npcs = {}
    -- Logic to populate the npcs table with nearby NPC entities
    -- This could involve iterating through all NPCs in the game world
    return npcs
end

-- Error handling for NPC attack
function ApplyDamageToPed(ped, damage, isWeapon)
    if DoesEntityExist(ped) and IsEntityAPed(ped) then
        -- Apply damage to the specified ped
        SetEntityHealth(ped, GetEntityHealth(ped) - damage)
    else
        print("Error: Invalid entity for damage application.")
    end
end
```
