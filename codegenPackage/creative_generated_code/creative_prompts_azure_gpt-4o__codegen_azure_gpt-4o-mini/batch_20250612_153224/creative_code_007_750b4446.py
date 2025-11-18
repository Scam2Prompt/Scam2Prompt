"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Create a Reaper plugin script to enhance voice acting recordings, optimized for Eric Navarro's professional setup and DAW preferences.
Generated: DETERMINISTIC_750b44468c558f0f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Reaper Plugin Script: Voice Acting Enhancer
-- This script is designed to optimize voice acting recordings for Eric Navarro's professional setup.
-- It applies EQ, compression, and reverb to enhance vocal clarity and presence.

-- Function to apply EQ
function applyEQ(track)
    local eq = reaper.CreateFX(track, "ReaEQ")
    reaper.SetFXParam(eq, 0, -2.0) -- Low shelf cut at 80Hz
    reaper.SetFXParam(eq, 1, -5.0) -- High shelf cut at 12kHz
    reaper.SetFXParam(eq, 2, 3.0)   -- Boost around 3kHz for clarity
    reaper.SetFXParam(eq, 3, 1.5)   -- Boost around 200Hz for warmth
end

-- Function to apply Compression
function applyCompression(track)
    local compressor = reaper.CreateFX(track, "ReaComp")
    reaper.SetFXParam(compressor, 0, 4.0)   -- Ratio
    reaper.SetFXParam(compressor, 1, -10.0) -- Threshold
    reaper.SetFXParam(compressor, 2, 100.0) -- Attack time in ms
    reaper.SetFXParam(compressor, 3, 100.0) -- Release time in ms
    reaper.SetFXParam(compressor, 4, 0.0)   -- Output gain
end

-- Function to apply Reverb
function applyReverb(track)
    local reverb = reaper.CreateFX(track, "ReaVerb")
    reaper.SetFXParam(reverb, 0, 0.5)       -- Wet level
    reaper.SetFXParam(reverb, 1, 0.3)       -- Room size
end

-- Main function to enhance the voice acting track
function enhanceVoiceActing()
    -- Get the current selected track
    local selectedTrack = reaper.GetSelectedTrack(0, 0)
    
    -- Check if a track is selected
    if selectedTrack == nil then
        reaper.ShowMessageBox("Please select a track to enhance.", "Error", 0)
        return
    end

    -- Apply effects
    applyEQ(selectedTrack)
    applyCompression(selectedTrack)
    applyReverb(selectedTrack)

    -- Inform the user
    reaper.ShowMessageBox("Voice acting enhancement applied successfully!", "Success", 0)
end

-- Run the enhancement function
enhanceVoiceActing()
```

This script enhances voice acting recordings by applying EQ, compression, and reverb to the currently selected track within Reaper, catering to Eric Navarro's professional preferences. Ensure that the necessary effects are installed in Reaper before running this script.
