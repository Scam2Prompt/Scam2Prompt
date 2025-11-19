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

Certainly! Below is a Lua script designed for REAPER (a popular DAW that supports scripting). The code automates an audio processing workflow to enhance voice recordings. This script utilizes REAPER's API to apply various effects and process the audio.

```lua
--[[
Audio Processing Workflow for Enhancing Voice Recordings
Author: [Your Name]
Date: [Insert Date]
Version: 1.0

Description:
This script automates a basic audio processing workflow in REAPER
to enhance voice recordings for commercial demos. It applies noise 
reduction, EQ, compression, and normalization.

Requirements:
- REAPER with SWS Extensions installed
- Voice recording already loaded into REAPER as a media item

Usage:
1. Load the voice recording into a track in REAPER.
2. Run this script via the Actions list.

Note:
Make sure to adjust parameters of plugins as needed for your specific audio content.
--]]

-- Ensure REAPER's API is available
if not reaper then
  error("This script must be run inside REAPER.")
end

--[[ Helper Functions ]]--

-- Apply a specific FX by its name to the active track
function applyFXByName(track, fxName)
  local fxIndex = reaper.TrackFX_AddByName(track, fxName, false, -1)
  if fxIndex == -1 then
    reaper.ShowMessageBox("FX not found: " .. fxName, "Error", 0)
    return false
  end
  return true
end

-- Normalize the selected media item
function normalizeMediaItem(media_item)
  if not media_item then
    reaper.ShowMessageBox("No media item selected for normalization.", "Error", 0)
    return false
  end
  reaper.Main_OnCommand(40362, 0) -- Normalize selected item
  return true
end

--[[ Main Workflow ]]--

-- Get the first selected track and media item
local track = reaper.GetSelectedTrack(0, 0)
local media_item = reaper.GetSelectedMediaItem(0, 0)

if not track then
  reaper.ShowMessageBox("No track selected. Please select a track containing the voice recording.", "Error", 0)
  return
end

if not media_item then
  reaper.ShowMessageBox("No media item selected. Please select the voice recording item in the track.", "Error", 0)
  return
end

-- Step 1: Apply Noise Reduction (ReaFIR)
if not applyFXByName(track, "ReaFIR (Cockos) - Reduce Noise") then
  return
end

-- Step 2: Apply Equalization (ReaEQ)
if not applyFXByName(track, "ReaEQ (Cockos)") then
  return
end

-- Step 3: Apply Compression (ReaComp)
if not applyFXByName(track, "ReaComp (Cockos)") then
  return
end

-- Step 4: Normalize the Voice Recording
if not normalizeMediaItem(media_item) then
  return
end

-- Step 5: Render the processed audio to a new file
local renderCommandID = reaper.NamedCommandLookup("_SWS_RENNDER")
if renderCommandID == 0 then
  reaper.ShowMessageBox("SWS Render command not found. Please ensure SWS Extensions are installed.", "Error", 0)
  return
end

reaper.Main_OnCommand(renderCommandID, 0) -- Render with SWS Extensions

-- Script completion message
reaper.ShowMessageBox("Voice recording enhancement complete. Processed audio has been rendered.", "Success", 0)
```

This script assumes you have the necessary audio plugins installed and configured appropriately. Adjust plugin parameters in REAPER for specific use cases.
