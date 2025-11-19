"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Design a simple game mode for Left 4 Dead using the Source engine's scripting language and provide example code.
Generated: DETERMINISTIC_8b0870ebd685e3a3
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Left 4 Dead Custom Game Mode: Survival Challenge
-- This script creates a custom game mode where players must survive waves of infected for a set duration.

-- Constants
local GAME_MODE_NAME = "Survival Challenge"
local WAVE_INTERVAL = 60 -- Time in seconds between waves
local TOTAL_WAVES = 10 -- Total number of waves
local SURVIVAL_DURATION = TOTAL_WAVES * WAVE_INTERVAL -- Total survival time
local INFECTED_SPAWN_COUNT = 20 -- Number of infected per wave

-- Variables
local currentWave = 0
local gameActive = false

-- Function to start the custom game mode
function StartSurvivalChallenge()
    -- Initialize game mode
    gameActive = true
    currentWave = 0
    PrintMessageToPlayers("Welcome to " .. GAME_MODE_NAME .. "! Survive for " .. SURVIVAL_DURATION .. " seconds.")
    
    -- Start the first wave
    StartNextWave()
end

-- Function to start the next wave of infected
function StartNextWave()
    if not gameActive then
        return
    end

    currentWave = currentWave + 1

    -- Check if all waves are completed
    if currentWave > TOTAL_WAVES then
        EndSurvivalChallenge(true)
        return
    end

    PrintMessageToPlayers("Wave " .. currentWave .. " is starting! Prepare yourselves!")

    -- Spawn infected for the current wave
    SpawnInfected(INFECTED_SPAWN_COUNT)

    -- Schedule the next wave
    ScheduleTask(WAVE_INTERVAL, StartNextWave)
end

-- Function to spawn infected
function SpawnInfected(count)
    for i = 1, count do
        local spawnPoint = GetRandomSpawnPoint()
        if spawnPoint then
            SpawnEntity("npc_infected", spawnPoint)
        else
            PrintMessageToPlayers("Error: Unable to find a valid spawn point for infected.")
        end
    end
end

-- Function to end the survival challenge
function EndSurvivalChallenge(success)
    gameActive = false

    if success then
        PrintMessageToPlayers("Congratulations! You survived the " .. GAME_MODE_NAME .. "!")
    else
        PrintMessageToPlayers("Game Over! You failed to survive the " .. GAME_MODE_NAME .. ".")
    end
end

-- Utility function to print messages to all players
function PrintMessageToPlayers(message)
    for _, player in pairs(GetAllPlayers()) do
        player:SendMessage(message)
    end
end

-- Utility function to get a random spawn point
function GetRandomSpawnPoint()
    local spawnPoints = GetAllSpawnPoints()
    if #spawnPoints > 0 then
        return spawnPoints[math.random(#spawnPoints)]
    end
    return nil
end

-- Event: Player death
function OnPlayerDeath(player)
    PrintMessageToPlayers(player:GetName() .. " has died!")
    
    -- Check if all players are dead
    if AreAllPlayersDead() then
        EndSurvivalChallenge(false)
    end
end

-- Event: Game start
function OnGameStart()
    StartSurvivalChallenge()
end

-- Event: Game end
function OnGameEnd()
    gameActive = false
end

-- Register event handlers
RegisterEventHandler("PlayerDeath", OnPlayerDeath)
RegisterEventHandler("GameStart", OnGameStart)
RegisterEventHandler("GameEnd", OnGameEnd)
```
