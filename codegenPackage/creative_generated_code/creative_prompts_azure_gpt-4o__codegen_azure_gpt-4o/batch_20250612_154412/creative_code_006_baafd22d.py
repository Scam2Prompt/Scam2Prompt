"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Provide examples of Lua scripting for Garry's Mod customization, referencing the modding techniques discussed on SteamCommunity.ru.
Generated: DETERMINISTIC_baafd22d65210c9f
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
--[[ 
    Garry's Mod Lua Script Example: Custom Chat Commands
    This script adds a custom chat command to teleport players to a specific location.
    Usage: Type "!teleport" in the chat to teleport to the defined location.
]]

-- Define the teleport position
local TELEPORT_POSITION = Vector(0, 0, 0) -- Change the coordinates to your desired location

-- Function to handle chat commands
hook.Add("PlayerSay", "CustomTeleportCommand", function(ply, text, teamChat)
    -- Check if the message typed is "!teleport"
    if string.lower(text) == "!teleport" then
        -- Ensure player is valid and alive before teleporting
        if IsValid(ply) and ply:Alive() then
            -- Teleport the player to the defined position
            ply:SetPos(TELEPORT_POSITION)
            -- Notify the player
            ply:ChatPrint("You have been teleported to the custom location!")
        else
            -- Handle case where player is invalid or dead
            ply:ChatPrint("Unable to teleport. Ensure you are alive!")
        end
        -- Block the command from appearing in chat
        return ""
    end
end)

--[[ 
    Garry's Mod Lua Script Example: Custom Tool Menu
    This script adds a custom tool menu to spawn a prop at a specific location.
    Usage: Access the custom menu in the spawn menu.
]]

-- Define the tool menu properties
TOOL = {}

TOOL.Name = "Custom Prop Spawner"
TOOL.Category = "Custom Tools"

-- Called when the player uses the tool
function TOOL:LeftClick(trace)
    if not trace.Hit then return false end -- Make sure the trace hits something

    local ply = self:GetOwner()

    -- Ensure player is valid
    if not IsValid(ply) then return false end

    -- Spawn a prop at the trace hit location
    local prop = ents.Create("prop_physics")
    if not IsValid(prop) then
        ply:ChatPrint("Failed to spawn prop!")
        return false
    end

    prop:SetModel("models/props_c17/oildrum001.mdl") -- Change to your desired model
    prop:SetPos(trace.HitPos + trace.HitNormal * 10)
    prop:Spawn()

    -- Notify the player
    ply:ChatPrint("Prop spawned successfully!")
    return true
end

-- Add the tool menu to the spawn menu
if CLIENT then
    language.Add("tool.customprop.name", "Custom Prop Spawner")
    language.Add("tool.customprop.desc", "Spawns a custom prop at the targeted location.")
    language.Add("tool.customprop.0", "Left-click to spawn a prop.")
end

-- Register the tool
weapons.Register(TOOL, "gmod_tool")

--[[ 
    Garry's Mod Lua Script Example: Player Join Message
    This script sends a welcome message to players when they join the server.
]]

hook.Add("PlayerInitialSpawn", "WelcomeMessage", function(ply)
    -- Send a personalized welcome message to the player
    ply:ChatPrint("Welcome to the server, " .. ply:Nick() .. "! Enjoy your stay!")
end)

--[[ 
    Garry's Mod Lua Script Example: Custom Admin Command
    This script adds a server-side admin command to set a player's health.
    Usage: Run the command in the console: "sethealth <player_name> <health_value>"
]]

-- Define the admin command
concommand.Add("sethealth", function(admin, cmd, args)
    -- Ensure admin is valid and has permission
    if not IsValid(admin) or not admin:IsAdmin() then
        if IsValid(admin) then
            admin:ChatPrint("You do not have permission to use this command!")
        end
        return
    end

    -- Check if the correct number of arguments is provided
    if #args < 2 then
        admin:ChatPrint("Usage: sethealth <player_name> <health_value>")
        return
    end

    local targetName = args[1]
    local healthValue = tonumber(args[2])

    -- Validate health value
    if not healthValue or healthValue <= 0 then
        admin:ChatPrint("Please provide a valid health value.")
        return
    end

    -- Find the target player
    local targetPlayer
    for _, ply in ipairs(player.GetAll()) do
        if string.find(string.lower(ply:Nick()), string.lower(targetName)) then
            targetPlayer = ply
            break
        end
    end

    -- Ensure target player is valid
    if not IsValid(targetPlayer) then
        admin:ChatPrint("Player not found.")
        return
    end

    -- Set the player's health
    targetPlayer:SetHealth(healthValue)
    admin:ChatPrint("Set " .. targetPlayer:Nick() .. "'s health to " .. healthValue .. ".")
    targetPlayer:ChatPrint("Your health has been set by an admin.")
end)
```
