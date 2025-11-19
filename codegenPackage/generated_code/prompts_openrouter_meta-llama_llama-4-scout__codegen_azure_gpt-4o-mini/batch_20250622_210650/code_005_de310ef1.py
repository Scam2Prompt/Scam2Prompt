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
// Max for Live script to automate a music production task in Ableton Live
// This script will map MIDI controller input to control a specific parameter in Ableton Live

// Define the MIDI controller and the parameter to control
var midiController = new LiveAPI("live_set");
var parameterPath = "live_set tracks 0 devices 0 parameters 0"; // Adjust the path as needed

// Function to initialize the MIDI controller
function init() {
    // Set up the MIDI input
    var midiInput = new LiveAPI("live_set midi_input");
    midiInput.set("enabled", 1); // Enable MIDI input

    // Set up a listener for MIDI messages
    midiInput.add_listener("midi_note", onMidiNote);
}

// Callback function to handle MIDI note messages
function onMidiNote(value) {
    // Extract MIDI note and velocity from the value
    var note = value[0];
    var velocity = value[1];

    // Check if the note is within a valid range
    if (note >= 0 && note <= 127) {
        // Map the MIDI note to the parameter value (0-1)
        var mappedValue = note / 127;

        // Set the parameter value in Ableton Live
        setParameterValue(mappedValue);
    } else {
        // Log an error if the note is out of range
        post("Error: MIDI note out of range: " + note + "\n");
    }
}

// Function to set the parameter value in Ableton Live
function setParameterValue(value) {
    try {
        var parameter = new LiveAPI(parameterPath);
        parameter.set("value", value); // Set the parameter value
    } catch (error) {
        // Log any errors that occur while setting the parameter
        post("Error setting parameter value: " + error + "\n");
    }
}

// Initialize the script
init();
```
