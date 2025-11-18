"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Write a Lua plugin to integrate custom map features like "Gostown Paradise V beta V3.0" into GTA 5's story mode.
Generated: DETERMINISTIC_0f8256ce124ede53
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- GTA 5 Lua Plugin to Integrate Custom Map Features
-- This script integrates custom map features like "Gostown Paradise V beta V3.0"
-- into GTA 5's story mode. Ensure you have ScriptHookV and the LuaPlugin installed.

-- Configuration table for the custom map
local CustomMapConfig = {
    mapName = "Gostown Paradise V beta V3.0", -- Name of the custom map
    mapFilePath = "./scripts/maps/gostown_paradise_v3.xml", -- Path to the map file
    loadOnStartup = true, -- Automatically load the map when the game starts
}

-- Utility function to log messages
local function log(message)
    print("[CustomMapIntegration]: " .. message)
end

-- Function to load the custom map
local function loadCustomMap()
    -- Check if the map file exists
    local file = io.open(CustomMapConfig.mapFilePath, "r")
    if not file then
        log("Error: Custom map file not found at " .. CustomMapConfig.mapFilePath)
        return false
    end
    io.close(file)

    -- Load the map using the ScriptHookV native function or equivalent
    local success = LoadMapFile(CustomMapConfig.mapFilePath)
    if not success then
        log("Error: Failed to load the custom map.")
        return false
    end

    log("Custom map '" .. CustomMapConfig.mapName .. "' loaded successfully.")
    return true
end

-- Event handler for game startup, triggered when the game begins
local function onGameStart()
    log("Game started.")

    -- Automatically load the custom map if configured
    if CustomMapConfig.loadOnStartup then
        log("Attempting to load custom map...")
        local success = loadCustomMap()
        if not success then
            log("Custom map could not be loaded.")
        end
    end
end

-- Register the game start event
AddEventHandler("onGameStart", onGameStart)

-- Command to manually load the custom map
AddCommandHandler("loadMap", function(args)
    log("Manual map load requested.")
    local success = loadCustomMap()
    if not success then
        log("Custom map could not be loaded.")
    end
end)

-- Command to reload the custom map
AddCommandHandler("reloadMap", function(args)
    log("Reloading the custom map...")
    local success = loadCustomMap()
    if not success then
        log("Failed to reload the custom map.")
    end
end)

-- Error handling: Catch any unexpected errors
local function handleError(err)
    log("Unexpected error occurred: " .. tostring(err))
end

-- Wrap the main logic in error handling
local success, err = pcall(function()
    log("Initializing Custom Map Integration Plugin...")
    if CustomMapConfig.loadOnStartup then
        log("Loading custom map on startup...")
        loadCustomMap()
    end
end)

if not success then
    handleError(err)
end

-- Ensure clean plugin initialization
log("Custom Map Integration Plugin initialized successfully.")
```
