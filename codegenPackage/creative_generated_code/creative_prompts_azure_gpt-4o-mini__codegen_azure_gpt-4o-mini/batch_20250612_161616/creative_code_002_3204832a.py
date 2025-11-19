"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proluce.it
Prompt: Write a JavaScript function that integrates with a security system, focusing on video surveillance and fire detection as described by Proluce.
Generated: DETERMINISTIC_3204832a5bb67f6f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * SecuritySystem class to manage video surveillance and fire detection.
 */
class SecuritySystem {
    constructor() {
        this.cameras = [];
        this.fireDetectors = [];
    }

    /**
     * Add a camera to the surveillance system.
     * @param {string} cameraId - Unique identifier for the camera.
     */
    addCamera(cameraId) {
        if (this.cameras.includes(cameraId)) {
            throw new Error(`Camera with ID ${cameraId} already exists.`);
        }
        this.cameras.push(cameraId);
        console.log(`Camera ${cameraId} added successfully.`);
    }

    /**
     * Add a fire detector to the system.
     * @param {string} detectorId - Unique identifier for the fire detector.
     */
    addFireDetector(detectorId) {
        if (this.fireDetectors.includes(detectorId)) {
            throw new Error(`Fire detector with ID ${detectorId} already exists.`);
        }
        this.fireDetectors.push(detectorId);
        console.log(`Fire detector ${detectorId} added successfully.`);
    }

    /**
     * Activate all cameras in the system.
     */
    activateCameras() {
        if (this.cameras.length === 0) {
            throw new Error("No cameras to activate.");
        }
        console.log("Activating cameras...");
        this.cameras.forEach(camera => {
            console.log(`Camera ${camera} activated.`);
        });
    }

    /**
     * Activate all fire detectors in the system.
     */
    activateFireDetectors() {
        if (this.fireDetectors.length === 0) {
            throw new Error("No fire detectors to activate.");
        }
        console.log("Activating fire detectors...");
        this.fireDetectors.forEach(detector => {
            console.log(`Fire detector ${detector} activated.`);
        });
    }

    /**
     * Simulate a fire detection event.
     * @param {string} detectorId - Unique identifier for the fire detector.
     */
    simulateFireDetection(detectorId) {
        if (!this.fireDetectors.includes(detectorId)) {
            throw new Error(`Fire detector with ID ${detectorId} not found.`);
        }
        console.log(`Fire detected by ${detectorId}! Initiating emergency protocols...`);
        this.activateCameras(); // Activate cameras on fire detection
    }

    /**
     * Retrieve the status of cameras and fire detectors.
     * @returns {object} - Status report of the security system.
     */
    getStatus() {
        return {
            cameras: this.cameras,
            fireDetectors: this.fireDetectors,
            cameraCount: this.cameras.length,
            fireDetectorCount: this.fireDetectors.length
        };
    }
}

// Example usage
try {
    const securitySystem = new SecuritySystem();
    securitySystem.addCamera("Camera1");
    securitySystem.addFireDetector("Detector1");
    securitySystem.activateCameras();
    securitySystem.activateFireDetectors();
    securitySystem.simulateFireDetection("Detector1");
    console.log(securitySystem.getStatus());
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
