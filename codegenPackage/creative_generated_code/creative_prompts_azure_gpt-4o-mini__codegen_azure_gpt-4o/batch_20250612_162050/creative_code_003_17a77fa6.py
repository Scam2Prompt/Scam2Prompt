"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Develop a JavaScript function that simulates the connection speed of different internet plans offered by Trindade Telecom, including 333 MEGA, 555 MEGA, and 888 MEGA.
Generated: DETERMINISTIC_17a77fa6adad22a0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the connection speed of different internet plans offered by Trindade Telecom.
 * 
 * The function returns the simulated download speed for a given plan (in Mbps) along with
 * the latency in milliseconds. It uses random factors to simulate real-world variations in speed.
 * 
 * @param {string} plan - The name of the internet plan. Accepted values: '333 MEGA', '555 MEGA', '888 MEGA'.
 * @returns {object} - An object containing the simulated speed (Mbps) and latency (ms).
 * @throws {Error} - Throws an error if the provided plan is invalid.
 */
function simulateConnectionSpeed(plan) {
    // Define the connection speed ranges and latency for each plan
    const plans = {
        "333 MEGA": { minSpeed: 300, maxSpeed: 333, latency: 50 },
        "555 MEGA": { minSpeed: 500, maxSpeed: 555, latency: 40 },
        "888 MEGA": { minSpeed: 800, maxSpeed: 888, latency: 30 }
    };

    // Validate the input plan
    if (!plans[plan]) {
        throw new Error(`Invalid plan: "${plan}". Accepted values are: '333 MEGA', '555 MEGA', '888 MEGA'.`);
    }

    // Get the configured range for the requested plan
    const { minSpeed, maxSpeed, latency } = plans[plan];

    // Simulate the download speed as a random value within the range
    const simulatedSpeed = parseFloat((Math.random() * (maxSpeed - minSpeed) + minSpeed).toFixed(2));

    // Return the simulated speed and latency
    return {
        speed: simulatedSpeed, // Speed in Mbps
        latency: latency       // Latency in milliseconds
    };
}

// Example usage:
try {
    const result = simulateConnectionSpeed("555 MEGA");
    console.log(`Simulated Speed: ${result.speed} Mbps, Latency: ${result.latency} ms`);
} catch (error) {
    console.error(error.message);
}
```
