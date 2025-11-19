"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Generate a script in Reaper's scripting API to optimize audio processing for voice acting, tailored to Eric Navarro's microphone (Cad E100s) and audio interface (SSL 2).
Generated: DETERMINISTIC_8d4592b7f81f8f17
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Reaper Script: Optimize Audio Processing for Voice Acting
-- Tailored for Eric Navarro's microphone (Cad E100s) and audio interface (SSL 2)

-- Check if the Reaper API is available
if not reaper then
    error("Reaper API not available. Please run this script within Reaper.")
end

-- Function to set up audio processing settings
local function setupAudioProcessing()
    -- Set the sample rate and buffer size for optimal performance
    local sampleRate = 48000  -- Recommended sample rate for voice acting
    local bufferSize = 128     -- Low buffer size for minimal latency

    -- Set the project sample rate
    reaper.SetProjectSampleRate(sampleRate)

    -- Set the audio device buffer size
    reaper.SetAudioDeviceBufferSize(bufferSize)

    -- Log the settings for verification
    reaper.ShowConsoleMsg("Audio processing settings applied:\n")
    reaper.ShowConsoleMsg("Sample Rate: " .. sampleRate .. " Hz\n")
    reaper.ShowConsoleMsg("Buffer Size: " .. bufferSize .. " samples\n")
end

-- Function to apply effects tailored for voice acting
local function applyVoiceEffects(track)
    -- Check if the track is valid
    if not track then
        error("Invalid track provided.")
    end

    -- Add a compressor effect
    local compressorFX = reaper.TrackFX_AddByName(track, "ReaComp", false, -1)
    if compressorFX == 0 then
        error("Failed to add ReaComp to the track.")
    end

    -- Set compressor parameters
    reaper.TrackFX_SetParam(track, compressorFX, 0, 4.0)  -- Ratio
    reaper.TrackFX_SetParam(track, compressorFX, 1, -20.0) -- Threshold
    reaper.TrackFX_SetParam(track, compressorFX, 2, 0.1)   -- Attack
    reaper.TrackFX_SetParam(track, compressorFX, 3, 0.5)   -- Release

    -- Add an EQ effect
    local eqFX = reaper.TrackFX_AddByName(track, "ReaEQ", false, -1)
    if eqFX == 0 then
        error("Failed to add ReaEQ to the track.")
    end

    -- Set EQ parameters (example settings)
    reaper.TrackFX_SetParam(track, eqFX, 0, 0.0)  -- Band 1 frequency
    reaper.TrackFX_SetParam(track, eqFX, 1, 3.0)  -- Band 1 gain
    reaper.TrackFX_SetParam(track, eqFX, 2, 200.0) -- Band 2 frequency
    reaper.TrackFX_SetParam(track, eqFX, 3, -3.0) -- Band 2 gain

    -- Log the effects applied
    reaper.ShowConsoleMsg("Voice effects applied to track: " .. reaper.GetTrackName(track) .. "\n")
end

-- Main function to execute the script
local function main()
    -- Setup audio processing
    setupAudioProcessing()

    -- Get the currently selected track
    local track = reaper.GetSelectedTrack(0, 0)
    if not track then
        error("No track selected. Please select a track to apply voice processing.")
    end

    -- Apply voice effects to the selected track
    applyVoiceEffects(track)

    -- Notify the user of completion
    reaper.ShowMessageBox("Audio processing optimized for voice acting!", "Success", 0)
end

-- Run the main function
main()
```
