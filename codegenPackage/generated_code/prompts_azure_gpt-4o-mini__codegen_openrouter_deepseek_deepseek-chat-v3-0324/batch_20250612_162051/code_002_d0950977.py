"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Create a sample audio processing workflow in Reaper that enhances voice recordings for commercial demos.
Generated: DETERMINISTIC_d095097733ab7740
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
--[[
    Reaper Voice Enhancement Script for Commercial Demos
    This script sets up a processing chain to enhance voice recordings.
    Includes noise reduction, EQ, compression, and subtle reverb.
--]]

local function setup_voice_enhancement_chain(track)
    -- Check if track is valid
    if not track or not reaper.ValidatePtr(track, "MediaTrack*") then
        reaper.ShowMessageBox("Invalid track", "Error", 0)
        return false
    end

    -- Clear existing FX
    reaper.TrackFX_GetCount(track)
    for i = reaper.TrackFX_GetCount(track) - 1, 0, -1 do
        reaper.TrackFX_Delete(track, i)
    end

    -- Add noise reduction (ReaFIR in subtract mode)
    local noise_reduction_idx = reaper.TrackFX_AddByName(track, "ReaFIR (Cockos)", false, -1)
    if noise_reduction_idx >= 0 then
        reaper.TrackFX_SetParam(track, noise_reduction_idx, 0, 1) -- Mode: Subtract
        reaper.TrackFX_SetParam(track, noise_reduction_idx, 1, 0.5) -- Wet: 0.5
    end

    -- Add EQ (ReaEQ)
    local eq_idx = reaper.TrackFX_AddByName(track, "ReaEQ (Cockos)", false, -1)
    if eq_idx >= 0 then
        -- High-pass filter at 80Hz
        reaper.TrackFX_SetParam(track, eq_idx, 0, 0) -- Band 1: Type = High-pass
        reaper.TrackFX_SetParam(track, eq_idx, 1, 80) -- Frequency
        reaper.TrackFX_SetParam(track, eq_idx, 2, 0) -- Gain
        reaper.TrackFX_SetParam(track, eq_idx, 3, 1.41) -- Q

        -- Presence boost at 3kHz
        reaper.TrackFX_SetParam(track, eq_idx, 5, 1) -- Band 2: Type = Band
        reaper.TrackFX_SetParam(track, eq_idx, 6, 3000) -- Frequency
        reaper.TrackFX_SetParam(track, eq_idx, 7, 3) -- Gain
        reaper.TrackFX_SetParam(track, eq_idx, 8, 1) -- Q
    end

    -- Add compressor (ReaComp)
    local comp_idx = reaper.TrackFX_AddByName(track, "ReaComp (Cockos)", false, -1)
    if comp_idx >= 0 then
        reaper.TrackFX_SetParam(track, comp_idx, 0, -20) -- Threshold
        reaper.TrackFX_SetParam(track, comp_idx, 1, 4) -- Ratio
        reaper.TrackFX_SetParam(track, comp_idx, 2, 50) -- Attack
        reaper.TrackFX_SetParam(track, comp_idx, 3, 200) -- Release
        reaper.TrackFX_SetParam(track, comp_idx, 4, 0) -- Knee
        reaper.TrackFX_SetParam(track, comp_idx, 5, 0) -- RMS size
        reaper.TrackFX_SetParam(track, comp_idx, 6, 0) -- Pre-comp
    end

    -- Add subtle reverb (ReaVerbate)
    local reverb_idx = reaper.TrackFX_AddByName(track, "ReaVerbate (Cockos)", false, -1)
    if reverb_idx >= 0 then
        reaper.TrackFX_SetParam(track, reverb_idx, 0, 0.2) -- Wet
        reaper.TrackFX_SetParam(track, reverb_idx, 1, 0.8) -- Dry
        reaper.TrackFX_SetParam(track, reverb_idx, 2, 1.2) -- Room size
        reaper.TrackFX_SetParam(track, reverb_idx, 3, 0.5) -- Damp
    end

    -- Add limiter (ReaLimit) as safety
    local limit_idx = reaper.TrackFX_AddByName(track, "ReaLimit (Cockos)", false, -1)
    if limit_idx >= 0 then
        reaper.TrackFX_SetParam(track, limit_idx, 0, -1) -- Ceiling
        reaper.TrackFX_SetParam(track, limit_idx, 1, 5) -- Release
    end

    return true
end

-- Main execution
local function main()
    reaper.Undo_BeginBlock()

    -- Get selected track or create new one
    local track = reaper.GetSelectedTrack(0, 0)
    if not track then
        track = reaper.GetTrack(0, 0) -- Get first track if none selected
        if not track then
            track = reaper.InsertTrackAtIndex(0, true) -- Create new track if none exists
        end
    end

    if track then
        local success = setup_voice_enhancement_chain(track)
        if success then
            reaper.TrackFX_SetOpen(track, 0, true) -- Open first FX (noise reduction) for noise profile
        end
    end

    reaper.Undo_EndBlock("Setup Voice Enhancement Chain", -1)
end

-- Run the script
main()
```
