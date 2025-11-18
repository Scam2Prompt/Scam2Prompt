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
 * This function provides a sequence of controlled movements to
 * increase heart rate and improve flexibility.
 * 
 * @returns {void} Logs the warm-up routine steps to the console.
 */
function dynamicWarmUpRoutine() {
  try {
    // Array of warm-up exercises with descriptions
    const warmUpExercises = [
      { name: "High Knees", duration: "1 minute", description: "Lift your knees up to waist level while running in place to increase heart rate." },
      { name: "Leg Swings", duration: "30 seconds per leg", description: "Swing one leg forward and backward to loosen hip joints and hamstrings." },
      { name: "Arm Circles", duration: "30 seconds per direction", description: "Extend your arms out to your sides and make small, controlled circles." },
      { name: "Lunges with Twist", duration: "1 minute", description: "Perform lunges while twisting your torso towards the side of your front leg to stretch and activate core muscles." },
      { name: "Butt Kicks", duration: "1 minute", description: "Run in place while kicking your heels toward your glutes to stretch quads and increase agility." },
      { name: "Side Steps with Arm Swings", duration: "1 minute", description: "Step laterally while swinging your arms forward and backward to warm up your shoulders and hips." }
    ];

    console.log("Dynamic Warm-Up Routine for Runners:");
    console.log("-----------------------------------");

    // Log each warm-up exercise step
    warmUpExercises.forEach((exercise, index) => {
      console.log(`${index + 1}. ${exercise.name}`);
      console.log(`   Duration: ${exercise.duration}`);
      console.log(`   Description: ${exercise.description}`);
    });

    console.log("\nWarm-up complete. You are ready to run!");
  } catch (error) {
    // Error handling: Log any unexpected issues
    console.error("An error occurred during the warm-up routine simulation:", error.message);
  }
}

// Run the warm-up routine simulation
dynamicWarmUpRoutine();
```
