"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Provide examples of Lua scripting for Garry's Mod customization, referencing the modding techniques discussed on SteamCommunity.ru.
Generated: DETERMINISTIC_baafd22d65210c9f
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Example 1: Simple Console Command
-- Create a new console command that prints a message to the console
concommand.Add("mycommand", function()
    print("Hello, World!")
end)

-- Example 2: Player Spawn Event
-- Hook into the PlayerSpawn function to print a message when a player spawns
hook.Add("PlayerSpawn", "MySpawnHook", function(ply)
    if ply and ply:IsPlayer() then
        print(ply:Nick() .. " has spawned.")
    end
end)

-- Example 3: Custom Player Model
-- Set a custom player model for all players
function SetCustomModel(ply)
    ply:SetModel("models/player/kli_kt.mdl")
end

hook.Add("PlayerSpawn", "MyModelHook", function(ply)
    if ply and ply:IsPlayer() then
        SetCustomModel(ply)
    end
end)

-- Example 4: Entity Creation
-- Create a new entity when a player uses a specific tool
function CreateEntity(ply, trace)
    if ply:GetActiveWeapon():GetClass() == "weapon_physgun" then
        local ent = ents.Create("prop_physics")
        ent:SetModel("models/props_c17/concrete_barrier001a.mdl")
        ent:SetPos(trace.HitPos)
        ent:Spawn()
    end
end

hook.Add("PhysgunPickup", "MyEntityHook", CreateEntity)

-- Example 5: Error Handling
-- Handle errors when a player tries to use an invalid command
local function MyCommandHandler(ply, cmd, args)
    if not ply or not ply:IsPlayer() then return end

    if cmd == "mycommand" then
        if #args < 1 then
            ply:ChatPrint("Invalid arguments. Usage: mycommand <arg1>")
            return
        end

        -- Handle command logic here
    end
end

concommand.Add("mycommand", function(ply, cmd, args)
    pcall(MyCommandHandler, ply, cmd, args)
end)

-- Example 6: Weapon Modification
-- Modify the default pistol to have increased damage
weapons.Get("weapon_pistol").Primary.Damage = 20

-- Example 7: Client-Side Prediction
-- Send a message to the client when a player fires their pistol
local function OnPlayerFire(ply, wep)
    if wep:GetClass() == "weapon_pistol" then
        net.Start("OnPlayerFire")
        net.WriteEntity(ply)
        net.Broadcast()
    end
end

hook.Add("PrimaryAttack", "MyFireHook", OnPlayerFire)

-- Client-side code
if CLIENT then
    net.Receive("OnPlayerFire", function()
        local ply = net.ReadEntity()
        print(ply:Nick() .. " fired their pistol.")
    end)
end
```
