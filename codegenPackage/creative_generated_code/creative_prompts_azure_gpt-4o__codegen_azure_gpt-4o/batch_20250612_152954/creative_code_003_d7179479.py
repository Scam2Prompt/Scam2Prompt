"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-explorer.skavel.cz
Prompt: Write code to troubleshoot JavaScript compatibility issues when using Sonic Explorer for audio exploration.
Generated: DETERMINISTIC_d717947936c819f7
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file sonic-explorer-compat-check.js
 * @description This script checks JavaScript compatibility issues when using Sonic Explorer for audio exploration.
 * It detects browser capabilities for essential web audio APIs and suggests fixes for common issues.
 * Ensure this is loaded in the browser environment.
 */

// Check for Web Audio API support
function checkWebAudioAPISupport() {
  try {
    // Validate the presence of AudioContext (or webkitAudioContext for older browsers)
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) {
      throw new Error('Web Audio API is not supported on this browser.');
    }

    console.log('Web Audio API is supported.');
    return true;
  } catch (error) {
    console.error(
      `Web Audio API compatibility issue: ${error.message}. Consider updating your browser or switching to a modern browser like Chrome or Firefox.`
    );
    return false;
  }
}

// Check for MediaDevices support (needed for microphone input)
function checkMediaDevicesSupport() {
  try {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      throw new Error('MediaDevices API is not supported on this browser.');
    }

    console.log('MediaDevices API is supported.');
    return true;
  } catch (error) {
    console.error(
      `MediaDevices API compatibility issue: ${error.message}. Ensure your browser supports getUserMedia for microphone access.`
    );
    return false;
  }
}

// Check for WebAssembly support (used for advanced audio processing)
function checkWebAssemblySupport() {
  try {
    if (typeof WebAssembly !== 'object') {
      throw new Error('WebAssembly is not supported on this browser.');
    }

    console.log('WebAssembly is supported.');
    return true;
  } catch (error) {
    console.error(
      `WebAssembly compatibility issue: ${error.message}. Update your browser to enable advanced audio processing.`
    );
    return false;
  }
}

// Run all compatibility checks
function runCompatibilityChecks() {
  console.log('Running Sonic Explorer compatibility checks...');

  const webAudioAPI = checkWebAudioAPISupport();
  const mediaDevicesAPI = checkMediaDevicesSupport();
  const webAssembly = checkWebAssemblySupport();

  if (webAudioAPI && mediaDevicesAPI && webAssembly) {
    console.log(
      'All compatibility checks passed. This browser is suitable for Sonic Explorer.'
    );
  } else {
    console.log(
      'Some compatibility checks failed. Sonic Explorer may not function properly on this browser.'
    );
  }
}

// Execute the checks when the script is loaded
runCompatibilityChecks();
```
