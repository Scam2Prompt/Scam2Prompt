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
-- Optimize Audio Processing for Voice Acting in Reaper
-- Tailored to Eric Navarro's microphone (Cad E100s) and audio interface (SSL 2)

-- Script settings
local SCRIPT_NAME = "Optimize Audio Processing for Voice Acting"

-- Reaper API functions
local reaper = reaper

-- Audio settings
local SAMPLE_RATE = 48 -- kHz
local BIT_DEPTH = 24 -- bits

-- EQ settings
local EQ_FREQ_1 = 100 -- Hz
local EQ_GAIN_1 = 3 -- dB
local EQ_FREQ_2 = 200 -- Hz
local EQ_GAIN_2 = 2 -- dB
local EQ_FREQ_3 = 8000 -- Hz
local EQ_GAIN_3 = -3 -- dB

-- Compression settings
local COMP_THRESHOLD = -20 -- dB
local COMP_RATIO = 4
local COMP_ATTACK = 10 -- ms
local COMP_RELEASE = 100 -- ms

-- Noise reduction settings
local NR_THRESHOLD = -30 -- dB
local NR_ATTACK = 10 -- ms
local NR_RELEASE = 100 -- ms

-- Function to optimize audio processing
local function optimize_audio_processing(track)
    -- Set track sample rate and bit depth
    reaper.SetTrackSampleRate(track, SAMPLE_RATE)
    reaper.SetTrackBitDepth(track, BIT_DEPTH)

    -- Add EQ
    local eq_guid = reaper.TrackFX_AddByName(track, "Reaper EQ")
    reaper.TrackFX_SetParam(track, eq_guid, 0, EQ_FREQ_1, true) -- Frequency 1
    reaper.TrackFX_SetParam(track, eq_guid, 1, EQ_GAIN_1, true) -- Gain 1
    reaper.TrackFX_SetParam(track, eq_guid, 2, EQ_FREQ_2, true) -- Frequency 2
    reaper.TrackFX_SetParam(track, eq_guid, 3, EQ_GAIN_2, true) -- Gain 2
    reaper.TrackFX_SetParam(track, eq_guid, 4, EQ_FREQ_3, true) -- Frequency 3
    reaper.TrackFX_SetParam(track, eq_guid, 5, EQ_GAIN_3, true) -- Gain 3

    -- Add compressor
    local comp_guid = reaper.TrackFX_AddByName(track, "Reaper Compressor")
    reaper.TrackFX_SetParam(track, comp_guid, 0, COMP_THRESHOLD, true) -- Threshold
    reaper.TrackFX_SetParam(track, comp_guid, 1, COMP_RATIO, true) -- Ratio
    reaper.TrackFX_SetParam(track, comp_guid, 2, COMP_ATTACK / 1000, true) -- Attack
    reaper.TrackFX_SetParam(track, comp_guid, 3, COMP_RELEASE / 1000, true) -- Release

    -- Add noise reduction
    local nr_guid = reaper.TrackFX_AddByName(track, "Reaper Noise Reduction")
    reaper.TrackFX_SetParam(track, nr_guid, 0, NR_THRESHOLD, true) -- Threshold
    reaper.TrackFX_SetParam(track, nr_guid, 1, NR_ATTACK / 1000, true) -- Attack
    reaper.TrackFX_SetParam(track, nr_guid, 2, NR_RELEASE / 1000, true) -- Release
end

-- Main function
local function main()
    -- Get selected tracks
    local num_tracks = reaper.GetNumTracks()
    for i = 0, num_tracks - 1 do
        local track = reaper.GetTrack(0, i)
        if reaper.IsTrackSelected(track) then
            optimize_audio_processing(track)
        end
    end

    -- Show message box
    reaper.MessageBox("Audio processing optimized for voice acting.", SCRIPT_NAME, 0)
end

-- Run main function
main()
```
