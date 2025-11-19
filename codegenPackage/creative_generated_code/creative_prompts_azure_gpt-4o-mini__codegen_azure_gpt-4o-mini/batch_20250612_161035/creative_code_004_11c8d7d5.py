"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Provide an example of how to use the NativeUI library to create a custom menu for selecting player skins in GTA 5.
Generated: DETERMINISTIC_11c8d7d5ae6c6f99
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- This script demonstrates how to use the NativeUI library to create a custom menu for selecting player skins in GTA 5.

-- Ensure you have the NativeUI library included in your project.
local NativeUI = require('NativeUI')

-- Create a main menu object
local menu = NativeUI.CreateMenu("Player Skins", "Select a skin for your character")

-- Define a list of skins (this is a simplified example, replace with actual skin hashes)
local skins = {
    {name = "Default", hash = 0x9C9E5E8},
    {name = "Cop", hash = 0xC6B8F5B},
    {name = "Gangster", hash = 0xF7B6A9D},
}

-- Function to apply the selected skin
local function applySkin(skinHash)
    local playerPed = PlayerPedId() -- Get the current player's ped
    if DoesEntityExist(playerPed) then
        -- Change the model to the selected skin
        RequestModel(skinHash)
        while not HasModelLoaded(skinHash) do
            Wait(500) -- Wait for the model to load
        end
        SetPlayerModel(PlayerId(), skinHash) -- Set the player model
        SetModelAsNoLongerNeeded(skinHash) -- Release the model
    else
        print("Error: Player ped does not exist.")
    end
end

-- Add skins to the menu
for _, skin in ipairs(skins) do
    local item = NativeUI.CreateItem(skin.name, "Select this skin.")
    item.Activated = function(sender, index)
        applySkin(skin.hash) -- Apply the selected skin when item is activated
    end
    menu:AddItem(item)
end

-- Function to toggle the menu visibility
local function toggleMenu()
    if menu:Visible() then
        menu:Visible(false) -- Hide the menu
    else
        menu:Visible(true) -- Show the menu
    end
end

-- Key binding to toggle the menu (e.g., press F10)
Citizen.CreateThread(function()
    while true do
        Citizen.Wait(0) -- Prevent freezing
        if IsControlJustPressed(1, 121) then -- F10 key
            toggleMenu() -- Toggle the menu on key press
        end
        menu:ProcessMenus() -- Process menu input
    end
end)

-- Display the menu when it's initialized
menu:Visible(false) -- Start with the menu hidden
```
