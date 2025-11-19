"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Create a sample audio processing workflow in Reaper that enhances voice recordings for commercial demos.
Generated: DETERMINISTIC_d095097733ab7740
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Reaper Audio Processing Workflow Script
-- This script enhances voice recordings for commercial demos
-- by applying various audio effects and processing steps.

-- Function to apply audio effects to selected tracks
function process_voice_recordings()
    -- Check if any track is selected
    local selectedTrackCount = reaper.CountSelectedTracks(0)
    if selectedTrackCount == 0 then
        reaper.ShowMessageBox("Please select at least one track.", "Error", 0)
        return
    end

    -- Loop through selected tracks
    for i = 0, selectedTrackCount - 1 do
        local track = reaper.GetSelectedTrack(0, i)

        -- Set a default volume level for voice tracks
        reaper.SetMediaTrackInfo_Value(track, "D_VOL", 0.75)

        -- Apply compression
        local compressorFXIndex = reaper.TrackFX_AddByName(track, "ReaComp", false, -1)
        if compressorFXIndex == -1 then
            reaper.ShowMessageBox("Failed to add ReaComp to track.", "Error", 0)
            return
        end
        -- Set compressor parameters
        reaper.TrackFX_SetParam(track, compressorFXIndex, 0, 4.0) -- Ratio
        reaper.TrackFX_SetParam(track, compressorFXIndex, 1, -30) -- Threshold
        reaper.TrackFX_SetParam(track, compressorFXIndex, 2, 0.1) -- Attack
        reaper.TrackFX_SetParam(track, compressorFXIndex, 3, 0.5) -- Release

        -- Apply EQ
        local eqFXIndex = reaper.TrackFX_AddByName(track, "ReaEQ", false, -1)
        if eqFXIndex == -1 then
            reaper.ShowMessageBox("Failed to add ReaEQ to track.", "Error", 0)
            return
        end
        -- Boost frequencies for voice presence
        reaper.TrackFX_SetParam(track, eqFXIndex, 0, 0.5) -- Gain for first band
        reaper.TrackFX_SetParam(track, eqFXIndex, 0, 2000) -- Frequency for first band

        -- Apply reverb
        local reverbFXIndex = reaper.TrackFX_AddByName(track, "ReaVerb", false, -1)
        if reverbFXIndex == -1 then
            reaper.ShowMessageBox("Failed to add ReaVerb to track.", "Error", 0)
            return
        end
        -- Set reverb parameters
        reaper.TrackFX_SetParam(track, reverbFXIndex, 0, 0.3) -- Wet level
        reaper.TrackFX_SetParam(track, reverbFXIndex, 1, 0.5) -- Room size

        -- Optional: Normalize audio level
        reaper.Main_OnCommand(40414, 0) -- Normalize selected items
    end

    reaper.ShowMessageBox("Audio processing completed successfully!", "Success", 0)
end

-- Run the audio processing workflow
process_voice_recordings()
```
