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

```python
# This script is designed for REAPER's ReaScript API (Python).
# It automates an audio processing workflow to enhance voice recordings for commercial demos.
# Ensure REAPER is installed and Python scripting is enabled.

import reaper_python as RPR

# Function to display a message in REAPER's console
def log(message):
    RPR.ShowConsoleMsg(f"{message}\n")

# Step 1: Normalize the selected track(s) to -3 dB
def normalize_tracks():
    track_count = RPR.CountSelectedTracks(0)
    if track_count == 0:
        log("No tracks selected. Please select a track to normalize.")
        return

    for i in range(track_count):
        track = RPR.GetSelectedTrack(0, i)
        RPR.Main_OnCommand(40108, 0)  # Normalize items in track to -3 dB
        log(f"Track {i + 1} normalized to -3 dB.")

# Step 2: Apply EQ to enhance voice clarity
def apply_eq():
    track_count = RPR.CountSelectedTracks(0)
    if track_count == 0:
        log("No tracks selected. Please select a track to apply EQ.")
        return

    for i in range(track_count):
        track = RPR.GetSelectedTrack(0, i)
        fx_index = RPR.TrackFX_AddByName(track, "ReaEQ (Cockos)", False, 1)
        if fx_index == -1:
            log(f"Failed to add ReaEQ to Track {i + 1}.")
            continue

        # Configure EQ bands for voice enhancement
        # Band 1: High-pass filter at 80 Hz
        RPR.TrackFX_SetEQParam(track, fx_index, 0, 0, 1)  # Enable Band 1
        RPR.TrackFX_SetEQParam(track, fx_index, 0, 1, 80)  # Frequency
        RPR.TrackFX_SetEQParam(track, fx_index, 0, 2, 0.7)  # Bandwidth
        RPR.TrackFX_SetEQParam(track, fx_index, 0, 3, 0)  # Gain

        # Band 2: Boost at 3 kHz for clarity
        RPR.TrackFX_SetEQParam(track, fx_index, 1, 0, 1)  # Enable Band 2
        RPR.TrackFX_SetEQParam(track, fx_index, 1, 1, 3000)  # Frequency
        RPR.TrackFX_SetEQParam(track, fx_index, 1, 2, 1)  # Bandwidth
        RPR.TrackFX_SetEQParam(track, fx_index, 1, 3, 3)  # Gain

        # Band 3: High-shelf boost at 10 kHz
        RPR.TrackFX_SetEQParam(track, fx_index, 2, 0, 1)  # Enable Band 3
        RPR.TrackFX_SetEQParam(track, fx_index, 2, 1, 10000)  # Frequency
        RPR.TrackFX_SetEQParam(track, fx_index, 2, 2, 0.7)  # Bandwidth
        RPR.TrackFX_SetEQParam(track, fx_index, 2, 3, 2)  # Gain

        log(f"EQ applied to Track {i + 1}.")

# Step 3: Apply compression to even out dynamics
def apply_compression():
    track_count = RPR.CountSelectedTracks(0)
    if track_count == 0:
        log("No tracks selected. Please select a track to apply compression.")
        return

    for i in range(track_count):
        track = RPR.GetSelectedTrack(0, i)
        fx_index = RPR.TrackFX_AddByName(track, "ReaComp (Cockos)", False, 1)
        if fx_index == -1:
            log(f"Failed to add ReaComp to Track {i + 1}.")
            continue

        # Configure compressor settings
        RPR.TrackFX_SetParam(track, fx_index, 0, 0.2)  # Threshold: -12 dB
        RPR.TrackFX_SetParam(track, fx_index, 1, 3)  # Ratio: 3:1
        RPR.TrackFX_SetParam(track, fx_index, 2, 0.1)  # Attack: 10 ms
        RPR.TrackFX_SetParam(track, fx_index, 3, 0.2)  # Release: 200 ms
        RPR.TrackFX_SetParam(track, fx_index, 4, 1)  # Auto makeup gain: On

        log(f"Compression applied to Track {i + 1}.")

# Step 4: Render the processed track(s) to a new file
def render_tracks():
    RPR.Main_OnCommand(41824, 0)  # Render selected tracks to stem tracks (and mute originals)
    log("Tracks rendered to new stem tracks.")

# Main function to execute the workflow
def main():
    log("Starting audio processing workflow...")
    normalize_tracks()
    apply_eq()
    apply_compression()
    render_tracks()
    log("Audio processing workflow completed.")

# Run the script
main()
```
