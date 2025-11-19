"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Develop a Max for Live patch to create a custom instrument or effect, using the principles of music production and sound design.
Generated: DETERMINISTIC_a5e5fff4143517b3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Max for Live Custom Instrument - Simple Synth
// This patch creates a basic subtractive synthesizer with ADSR envelope control

inlets = 1;
outlets = 2;

// Global variables for synth parameters
var osc1Type = "saw";
var osc2Type = "sine";
var osc1Level = 0.7;
var osc2Level = 0.3;
var filterCutoff = 1000;
var filterResonance = 0.2;
var filterType = "lowpass";
var attack = 50;
var decay = 200;
var sustain = 0.7;
var release = 300;
var masterVolume = 0.8;

// Initialize audio objects
var osc1 = new LiveAPI("live.object", "~osc1");
var osc2 = new LiveAPI("live.object", "~osc2");
var filter = new LiveAPI("live.object", "~filter");
var env = new LiveAPI("live.object", "~env");
var gain = new LiveAPI("live.object", "~gain");

// Setup audio routing
function setup() {
    // Configure oscillators
    osc1.call("set", "type", osc1Type);
    osc1.call("set", "gain", osc1Level);
    
    osc2.call("set", "type", osc2Type);
    osc2.call("set", "gain", osc2Level);
    
    // Configure filter
    filter.call("set", "type", filterType);
    filter.call("set", "frequency", filterCutoff);
    filter.call("set", "resonance", filterResonance);
    
    // Configure envelope
    env.call("set", "attack", attack);
    env.call("set", "decay", decay);
    env.call("set", "sustain", sustain);
    env.call("set", "release", release);
    
    // Configure master gain
    gain.call("set", "gain", masterVolume);
    
    // Connect audio objects
    osc1.call("connect", filter.id);
    osc2.call("connect", filter.id);
    filter.call("connect", env.id);
    env.call("connect", gain.id);
    gain.call("connect", "live_set tracks 0");
}

// Handle note messages
function msg_int(v) {
    if (v > 0) {
        // Note on
        osc1.call("start");
        osc2.call("start");
        env.call("trigger", 1);
    } else {
        // Note off
        env.call("trigger", 0);
    }
}

// Handle parameter changes
function list() {
    var args = arrayfromargs(arguments);
    var param = args[0];
    var value = args[1];
    
    try {
        switch(param) {
            case "osc1Type":
                osc1Type = value;
                osc1.call("set", "type", value);
                break;
            case "osc2Type":
                osc2Type = value;
                osc2.call("set", "type", value);
                break;
            case "osc1Level":
                osc1Level = value;
                osc1.call("set", "gain", value);
                break;
            case "osc2Level":
                osc2Level = value;
                osc2.call("set", "gain", value);
                break;
            case "filterCutoff":
                filterCutoff = value;
                filter.call("set", "frequency", value);
                break;
            case "filterResonance":
                filterResonance = value;
                filter.call("set", "resonance", value);
                break;
            case "filterType":
                filterType = value;
                filter.call("set", "type", value);
                break;
            case "attack":
                attack = value;
                env.call("set", "attack", value);
                break;
            case "decay":
                decay = value;
                env.call("set", "decay", value);
                break;
            case "sustain":
                sustain = value;
                env.call("set", "sustain", value);
                break;
            case "release":
                release = value;
                env.call("set", "release", value);
                break;
            case "masterVolume":
                masterVolume = value;
                gain.call("set", "gain", value);
                break;
            default:
                post("Unknown parameter: " + param + "\n");
        }
    } catch(e) {
        post("Error updating parameter: " + e + "\n");
    }
}

// Initialize on load
setup();
```
