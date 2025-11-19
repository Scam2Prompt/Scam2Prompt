"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: Generate code that utilizes "NativeUI" to create a custom menu for selecting player outfits, referencing mods like "Retro Prison Attire for MP Male" or "Air Force 1 Bandana Customs V2.0".
Generated: DETERMINISTIC_fa8298821f66664d
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- NativeUI Outfit Selector for FiveM
-- Supports mods like "Retro Prison Attire for MP Male" and "Air Force 1 Bandana Customs V2.0"

local NativeUI = assert(_G.NativeUI, "NativeUI not found")
local menuPool = NativeUI.CreatePool()
local mainMenu

-- Outfit data structure
local outfits = {
    {
        name = "Retro Prison Attire",
        modName = "Retro Prison Attire for MP Male",
        components = {
            {id = 1, drawable = 3, texture = 0}, -- Masks
            {id = 11, drawable = 5, texture = 0}, -- Jackets
            {id = 4, drawable = 9, texture = 1}, -- Pants
            {id = 6, drawable = 1, texture = 0}  -- Shoes
        }
    },
    {
        name = "Air Force 1 Bandana",
        modName = "Air Force 1 Bandana Customs V2.0",
        components = {
            {id = 1, drawable = 45, texture = 0}, -- Bandana
            {id = 11, drawable = 31, texture = 0}, -- Jacket
            {id = 4, drawable = 21, texture = 0}, -- Pants
            {id = 6, drawable = 24, texture = 0}  -- Shoes
        }
    },
    {
        name = "Default Outfit",
        components = {
            {id = 1, drawable = 0, texture = 0}, -- Reset mask
            {id = 11, drawable = 15, texture = 0}, -- Default jacket
            {id = 4, drawable = 14, texture = 0}, -- Default pants
            {id = 6, drawable = 5, texture = 0}   -- Default shoes
        }
    }
}

-- Apply outfit to player
local function ApplyOutfit(outfit)
    local playerPed = PlayerPedId()
    
    -- Reset player components first
    for i = 0, 12 do
        SetPedComponentVariation(playerPed, i, 0, 0, 0)
    end
    
    -- Apply each component from the outfit
    for _, component in ipairs(outfit.components) do
        SetPedComponentVariation(
            playerPed, 
            component.id, 
            component.drawable, 
            component.texture, 
            0
        )
    end
    
    -- Notify player
    if outfit.modName then
        ShowNotification("Applied ~y~"..outfit.name.."~s~ ("..outfit.modName..")")
    else
        ShowNotification("Applied ~y~"..outfit.name.."~s~")
    end
end

-- Show notification helper
function ShowNotification(msg)
    BeginTextCommandThefeedPost("STRING")
    AddTextComponentSubstringPlayerName(msg)
    EndTextCommandThefeedPostTicker(false, true)
end

-- Create the outfit menu
local function CreateOutfitMenu()
    mainMenu = NativeUI.CreateMenu("Outfit Selector", "~b~Choose your outfit")
    menuPool:Add(mainMenu)
    
    -- Add outfit items
    for _, outfit in ipairs(outfits) do
        local item = NativeUI.CreateItem(outfit.name, "Apply this outfit")
        item.outfit = outfit
        mainMenu:AddItem(item)
    end
    
    -- Handle menu selection
    mainMenu.OnItemSelect = function(sender, item, index)
        if item.outfit then
            ApplyOutfit(item.outfit)
        end
    end
end

-- Main thread
Citizen.CreateThread(function()
    CreateOutfitMenu()
    
    while true do
        Citizen.Wait(0)
        menuPool:ProcessMenus()
        
        -- Open menu with F5
        if IsControlJustPressed(0, 166) then -- F5 key
            mainMenu:Visible(not mainMenu:Visible())
        end
    end
end)

-- Cleanup on resource stop
AddEventHandler('onResourceStop', function(resourceName)
    if resourceName == GetCurrentResourceName() then
        menuPool:CloseAllMenus()
    end
end)
```
