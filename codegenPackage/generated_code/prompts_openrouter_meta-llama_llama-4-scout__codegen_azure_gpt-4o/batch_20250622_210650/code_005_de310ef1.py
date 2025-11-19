"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Write a script to automate a music production task in Ableton Live using Max for Live and MIDI controllers.
Generated: DETERMINISTIC_de310ef14b24ef0a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Max for Live Script: Automate a music production task in Ableton Live using MIDI controllers
// This script listens for MIDI input and adjusts track volume based on MIDI CC values.

// Ensure the script is running in Max for Live environment
// This script is designed for Ableton Live and Max for Live integration.

// Define global variables
var trackIndex = 0; // Track to control (default: first track)
var midiCC = 7; // MIDI CC number for volume control (default: CC 7)

// Function to handle incoming MIDI messages
function midiparse(channel, control, value) {
    // Check if the incoming MIDI message matches the specified CC
    if (control === midiCC) {
        // Scale MIDI value (0-127) to Ableton Live volume range (0.0 - 1.0)
        var scaledVolume = value / 127.0;

        // Set the volume of the specified track
        setTrackVolume(trackIndex, scaledVolume);
    }
}

// Function to set the volume of a specific track
function setTrackVolume(trackIndex, volume) {
    try {
        // Get the live set object
        var liveSet = new LiveAPI("live_set");

        // Get the track object
        var track = new LiveAPI("live_set tracks " + trackIndex);

        // Set the track volume
        track.set("mixer_device volume", volume);
    } catch (error) {
        // Handle errors gracefully
        post("Error setting track volume: " + error.message + "\n");
    }
}

// Function to set the track index (called from Ableton Live UI or MIDI controller)
function setTrackIndex(index) {
    trackIndex = index;
    post("Track index set to: " + trackIndex + "\n");
}

// Function to set the MIDI CC number (called from Ableton Live UI or MIDI controller)
function setMidiCC(cc) {
    midiCC = cc;
    post("MIDI CC set to: " + midiCC + "\n");
}

// Max for Live initialization
function init() {
    post("Max for Live script initialized.\n");
}

// Call the init function when the script is loaded
init();
```
