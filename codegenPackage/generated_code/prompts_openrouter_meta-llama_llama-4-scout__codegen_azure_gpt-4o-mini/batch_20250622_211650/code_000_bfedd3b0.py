"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a code snippet in Source engine's Hammer editor script to create a custom game mode for Half-Life 2.
Generated: DETERMINISTIC_bfedd3b06aad172f
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Custom Game Mode Script for Half-Life 2 in Hammer Editor

-- Define the custom game mode
function CustomGameMode:Init()
    -- Initialize the game mode
    print("Initializing Custom Game Mode...")
    
    -- Set up game rules
    self:SetGameRules()
    
    -- Register player spawn points
    self:SetupPlayerSpawns()
    
    -- Set up objectives
    self:SetupObjectives()
end

-- Function to set game rules
function CustomGameMode:SetGameRules()
    -- Example: Set the time limit for the game
    self.timeLimit = 300 -- 5 minutes
    print("Game rules set: Time limit is " .. self.timeLimit .. " seconds.")
end

-- Function to set up player spawn points
function CustomGameMode:SetupPlayerSpawns()
    -- Define spawn points
    local spawnPoints = {
        Vector(0, 0, 0), -- Spawn point 1
        Vector(100, 0, 0), -- Spawn point 2
        Vector(0, 100, 0) -- Spawn point 3
    }
    
    -- Loop through spawn points and create them
    for _, spawn in ipairs(spawnPoints) do
        local spawnEntity = ents.Create("info_player_start")
        if spawnEntity then
            spawnEntity:SetPos(spawn)
            spawnEntity:Spawn()
            print("Spawn point created at: " .. tostring(spawn))
        else
            print("Error: Failed to create spawn entity.")
        end
    end
end

-- Function to set up objectives
function CustomGameMode:SetupObjectives()
    -- Example: Create a capture point
    local capturePoint = ents.Create("capture_point")
    if capturePoint then
        capturePoint:SetPos(Vector(50, 50, 0))
        capturePoint:Spawn()
        print("Capture point created at: (50, 50, 0)")
    else
        print("Error: Failed to create capture point.")
    end
end

-- Function to start the game
function CustomGameMode:StartGame()
    print("Starting Custom Game Mode...")
    -- Logic to start the game
end

-- Function to end the game
function CustomGameMode:EndGame()
    print("Ending Custom Game Mode...")
    -- Logic to end the game
end

-- Initialize the custom game mode
CustomGameMode:Init()
```
