"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Write a Node.js script to simulate the impact of different internet speeds (e.g., 333 MEGA, 555 MEGA, 888 MEGA) on video call quality, considering factors such as resolution, frame rate, and latency.
Generated: DETERMINISTIC_61b80953212777bf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const readline = require('readline');

// Define constants for video call quality parameters
const RESOLUTIONS = {
  LOW: '480p',
  MEDIUM: '720p',
  HIGH: '1080p',
};
const FRAME_RATES = {
  LOW: 15,
  MEDIUM: 30,
  HIGH: 60,
};
const LATENCY_THRESHOLDS = {
  LOW: 50, // in ms
  MEDIUM: 100, // in ms
  HIGH: 200, // in ms
};

// Define internet speed tiers (in Mbps)
const INTERNET_SPEEDS = {
  '333 MEGA': 333,
  '555 MEGA': 555,
  '888 MEGA': 888,
};

// Function to simulate video call quality based on internet speed
function simulateVideoCallQuality(speed) {
  let resolution, frameRate, latency;

  // Determine video call quality parameters based on speed
  if (speed >= 888) {
    resolution = RESOLUTIONS.HIGH;
    frameRate = FRAME_RATES.HIGH;
    latency = LATENCY_THRESHOLDS.LOW;
  } else if (speed >= 555) {
    resolution = RESOLUTIONS.MEDIUM;
    frameRate = FRAME_RATES.MEDIUM;
    latency = LATENCY_THRESHOLDS.MEDIUM;
  } else if (speed >= 333) {
    resolution = RESOLUTIONS.LOW;
    frameRate = FRAME_RATES.LOW;
    latency = LATENCY_THRESHOLDS.HIGH;
  } else {
    throw new Error('Internet speed is too low for a stable video call.');
  }

  // Return the simulated video call quality
  return {
    resolution,
    frameRate,
    latency,
  };
}

// Function to display simulation results
function displayResults(speedLabel, quality) {
  console.log(`Internet Speed: ${speedLabel}`);
  console.log(`Video Call Quality:`);
  console.log(`  Resolution: ${quality.resolution}`);
  console.log(`  Frame Rate: ${quality.frameRate} fps`);
  console.log(`  Latency: ${quality.latency} ms`);
  console.log('-----------------------------------');
}

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Prompt the user to select an internet speed tier
rl.question(
  `Select an internet speed tier (${Object.keys(INTERNET_SPEEDS).join(', ')}): `,
  (speedLabel) => {
    try {
      // Validate user input and simulate video call quality
      const speed = INTERNET_SPEEDS[speedLabel];
      if (!speed) {
        throw new Error('Invalid internet speed tier selected.');
      }

      const quality = simulateVideoCallQuality(speed);
      displayResults(speedLabel, quality);
    } catch (error) {
      // Handle errors gracefully
      console.error(`Error: ${error.message}`);
    } finally {
      // Close the readline interface
      rl.close();
    }
  }
);
```
