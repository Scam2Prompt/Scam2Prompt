"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: Create a code snippet using "OpenIV" to modify vehicle handling in GTA 5, referencing mods like "1973 Chevy Caprice Rucci Donk" or other vehicle mods.
Generated: DETERMINISTIC_46c9ac2dc0b16f07
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- OpenIV Lua script to modify vehicle handling for GTA 5
-- Example for "1973 Chevy Caprice Rucci Donk" or similar mods

-- Define the handling data for the vehicle
local handlingData = {
    -- Basic handling
    fMass = 2000.0,                -- Vehicle mass (kg)
    fInitialDragCoeff = 10.0,      -- Drag coefficient
    fDownforceModifier = 0.5,      -- Downforce modifier
    fPercentSubmerged = 85.0,      -- Percentage submerged
    vecCentreOfMassOffset = {x = 0.0, y = 0.0, z = -0.5}, -- Center of mass offset
    
    -- Transmission
    nInitialDriveGears = 4,        -- Number of gears
    fInitialDriveForce = 0.35,     -- Drive force
    fDriveInertia = 1.0,           -- Drive inertia
    fClutchChangeRateScaleUpShift = 2.0, -- Clutch change rate (upshift)
    fClutchChangeRateScaleDownShift = 2.0, -- Clutch change rate (downshift)
    
    -- Engine
    fInitialDriveMaxFlatVel = 160.0, -- Max flat velocity (mph)
    fBrakeForce = 0.8,             -- Brake force
    fBrakeBiasFront = 0.6,         -- Front brake bias
    
    -- Suspension
    fSuspensionForce = 2.0,        -- Suspension force
    fSuspensionCompDamp = 1.4,     -- Suspension compression damping
    fSuspensionReboundDamp = 2.3,  -- Suspension rebound damping
    fSuspensionUpperLimit = 0.1,   -- Suspension upper limit
    fSuspensionLowerLimit = -0.15, -- Suspension lower limit
    fSuspensionRaise = 0.0,        -- Suspension raise
    fSuspensionBiasFront = 0.5,    -- Front suspension bias
    
    -- Traction
    fTractionBiasFront = 0.5,      -- Front traction bias
    fTractionLossMult = 1.0,       -- Traction loss multiplier
    fTractionCurveMax = 2.5,       -- Traction curve max
    fTractionCurveMin = 2.0,       -- Traction curve min
    fTractionCurveLateral = 2.5,   -- Lateral traction curve
    fTractionSpringDeltaMax = 0.1, -- Traction spring delta max
    
    -- Steering
    fSteeringLock = 35.0,          -- Steering lock (degrees)
    fTractionBiasFront = 0.5,      -- Front traction bias
    fTractionBiasRear = 0.5,       -- Rear traction bias
}

-- Function to apply handling data to a vehicle
function ApplyHandlingData(vehicleName, data)
    -- Check if vehicle exists
    if not IsModelInCdimage(vehicleName) then
        print("Error: Vehicle model not found - " .. vehicleName)
        return false
    end
    
    -- Request the model
    RequestModel(vehicleName)
    while not HasModelLoaded(vehicleName) do
        Citizen.Wait(0)
    end
    
    -- Get the vehicle handling
    local handling = GetVehicleHandling(vehicleName)
    if not handling then
        print("Error: Could not get handling for vehicle - " .. vehicleName)
        return false
    end
    
    -- Apply the handling data
    for key, value in pairs(data) do
        if handling[key] ~= nil then
            handling[key] = value
        else
            print("Warning: Invalid handling key - " .. key)
        end
    end
    
    -- Set the modified handling
    SetVehicleHandling(vehicleName, handling)
    
    -- Release the model
    SetModelAsNoLongerNeeded(vehicleName)
    
    print("Successfully applied handling data to " .. vehicleName)
    return true
end

-- Example usage for "1973 Chevy Caprice Rucci Donk"
-- Replace "rucci" with the actual spawn name of the mod
ApplyHandlingData("rucci", handlingData)
```
