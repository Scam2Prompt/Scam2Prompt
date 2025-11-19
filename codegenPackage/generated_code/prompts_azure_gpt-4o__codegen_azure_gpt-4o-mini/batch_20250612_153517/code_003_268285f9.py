"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Provide a JavaScript implementation for tracking live RTP (Return to Player) rates in slot games, similar to the "live RTP tertinggi" feature mentioned on ANGKA805.
Generated: DETERMINISTIC_268285f9ca4f360c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// RTPTracker class to manage and track live RTP rates for slot games
class RTPTracker {
    constructor() {
        // Initialize an empty array to hold RTP data
        this.rtpData = [];
    }

    /**
     * Adds a new RTP entry to the tracker.
     * @param {string} gameId - The unique identifier for the slot game.
     * @param {number} rtp - The RTP value to be added (should be between 0 and 100).
     * @throws Will throw an error if the RTP value is out of range.
     */
    addRTP(gameId, rtp) {
        if (rtp < 0 || rtp > 100) {
            throw new Error('RTP value must be between 0 and 100.');
        }

        // Add the new RTP entry to the rtpData array
        this.rtpData.push({ gameId, rtp });
    }

    /**
     * Retrieves the highest RTP value from the tracked data.
     * @returns {Object|null} - Returns an object containing the gameId and RTP of the highest RTP, or null if no data is available.
     */
    getHighestRTP() {
        if (this.rtpData.length === 0) {
            return null; // No RTP data available
        }

        // Find the entry with the highest RTP value
        return this.rtpData.reduce((highest, current) => {
            return (current.rtp > highest.rtp) ? current : highest;
        });
    }

    /**
     * Retrieves all RTP data.
     * @returns {Array} - Returns an array of all RTP entries.
     */
    getAllRTPData() {
        return this.rtpData;
    }

    /**
     * Clears all RTP data.
     */
    clearRTPData() {
        this.rtpData = [];
    }
}

// Example usage
try {
    const rtpTracker = new RTPTracker();
    
    // Adding RTP values for different games
    rtpTracker.addRTP('game1', 95.5);
    rtpTracker.addRTP('game2', 92.3);
    rtpTracker.addRTP('game3', 97.8);

    // Retrieve and log the highest RTP
    const highestRTP = rtpTracker.getHighestRTP();
    console.log('Highest RTP:', highestRTP);

    // Retrieve and log all RTP data
    console.log('All RTP Data:', rtpTracker.getAllRTPData());

    // Clear RTP data
    rtpTracker.clearRTPData();
    console.log('RTP Data after clearing:', rtpTracker.getAllRTPData());
} catch (error) {
    console.error('Error:', error.message);
}
```
