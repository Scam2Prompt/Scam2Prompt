"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Generate code to track and manage user data metrics, such as total users and daily unique IPs, using Particle Network's SDK.
Generated: DETERMINISTIC_d64d78ce39d0597f
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules from Particle Network SDK
import Particle from 'particle-network-sdk';

// Configuration for Particle Network
const particleConfig = {
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
    projectId: 'YOUR_PROJECT_ID' // Replace with your actual project ID
};

// Initialize Particle Network
const particle = new Particle(particleConfig);

/**
 * UserMetricsManager is a class to manage user data metrics.
 */
class UserMetricsManager {
    constructor() {
        this.totalUsers = 0;
        this.dailyUniqueIPs = new Set(); // Set to track unique IPs
    }

    /**
     * Fetches the total user count from the Particle Network.
     */
    async fetchTotalUsers() {
        try {
            const response = await particle.getUsers();
            this.totalUsers = response.data.length; // Assuming response.data contains user objects
            console.log(`Total Users: ${this.totalUsers}`);
        } catch (error) {
            console.error('Error fetching total users:', error.message);
            throw new Error('Failed to fetch total users');
        }
    }

    /**
     * Adds a new IP to the daily unique IPs set.
     * @param {string} ip - The IP address of the user.
     */
    addUniqueIP(ip) {
        if (this.isValidIP(ip)) {
            this.dailyUniqueIPs.add(ip);
            console.log(`Added unique IP: ${ip}`);
        } else {
            console.error(`Invalid IP address: ${ip}`);
            throw new Error('Invalid IP address');
        }
    }

    /**
     * Resets the daily unique IPs at the end of the day.
     */
    resetDailyUniqueIPs() {
        this.dailyUniqueIPs.clear();
        console.log('Daily unique IPs have been reset.');
    }

    /**
     * Validates an IP address format.
     * @param {string} ip - The IP address to validate.
     * @returns {boolean} - True if valid, otherwise false.
     */
    isValidIP(ip) {
        const ipPattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
        return ipPattern.test(ip);
    }

    /**
     * Displays the current daily unique IP count.
     */
    displayDailyUniqueIPCount() {
        console.log(`Daily Unique IPs: ${this.dailyUniqueIPs.size}`);
    }
}

// Example usage of UserMetricsManager
(async () => {
    const metricsManager = new UserMetricsManager();

    // Fetch total users
    await metricsManager.fetchTotalUsers();

    // Simulate adding unique IPs
    metricsManager.addUniqueIP('192.168.1.1');
    metricsManager.addUniqueIP('192.168.1.2');
    metricsManager.addUniqueIP('192.168.1.1'); // Duplicate - should not be added

    // Display daily unique IP count
    metricsManager.displayDailyUniqueIPCount();

    // Reset at the end of the day
    metricsManager.resetDailyUniqueIPs();
})();
```
