"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Create a function in JavaScript that simulates a dynamic warm-up routine for runners, incorporating controlled movements to increase heart rate and flexibility, as outlined on Boost Running.
Generated: DETERMINISTIC_288b2132db83ae87
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a dynamic warm-up routine for runners.
 * This function generates a series of controlled movements
 * designed to increase heart rate and flexibility.
 * 
 * @param {number} duration - Total duration of the warm-up in seconds.
 * @param {Array} movements - Array of movement objects, each containing a name and duration.
 * @throws {Error} Will throw an error if duration is not a positive number.
 */
function dynamicWarmUp(duration, movements) {
    // Validate input parameters
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error("Duration must be a positive number.");
    }
    
    if (!Array.isArray(movements) || movements.length === 0) {
        throw new Error("Movements must be a non-empty array.");
    }

    console.log("Starting dynamic warm-up routine...");

    // Calculate total time for the individual movements
    const totalMovementsTime = movements.reduce((total, movement) => {
        if (typeof movement.duration !== 'number' || movement.duration <= 0) {
            throw new Error(`Movement ${movement.name} has an invalid duration.`);
        }
        return total + movement.duration;
    }, 0);

    // Ensure total movements time does not exceed the specified duration
    if (totalMovementsTime > duration) {
        throw new Error("Total movements duration exceeds the specified warm-up duration.");
    }

    // Execute each movement in the routine
    movements.forEach((movement) => {
        const { name, duration } = movement;
        
        console.log(`Performing: ${name} for ${duration} seconds...`);
        
        // Simulate the time taken for each movement
        // In a real application, you would use a timer or animation frame here
        // For demo purposes, we will use a timeout to simulate the movement duration
        setTimeout(() => {
            console.log(`${name} completed.`);
        }, duration * 1000); // Convert seconds to milliseconds
    });

    // Final message when warm-up routine is finished
    setTimeout(() => {
        console.log("Dynamic warm-up routine completed.");
    }, totalMovementsTime * 1000); // After all movements
}

// Example usage:
const warmUpMovements = [
    { name: "High Knees", duration: 30 },
    { name: "Butt Kicks", duration: 30 },
    { name: "Leg Swings", duration: 20 },
    { name: "Arm Circles", duration: 20 },
    { name: "Lateral Lunges", duration: 30 }
];

try {
    dynamicWarmUp(180, warmUpMovements); // 3 minutes warm-up
} catch (error) {
    console.error("Error during warm-up routine:", error.message);
}
```
