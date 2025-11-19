"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Create a JavaScript function that simulates the "gentle removal" process of magnetic lashes, ensuring no tugging or damage, as described on Ocuvana's webpage.
Generated: DETERMINISTIC_5eb9d040798815e0
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the gentle removal process of magnetic lashes to prevent tugging or damage.
 * @param {Object} options - Configuration options for the removal process.
 * @param {number} [options.removalTime=5000] - Time in milliseconds for the removal process (default: 5000ms).
 * @param {number} [options.removalSteps=5] - Number of steps in the removal process (default: 5).
 * @param {function} [options.onStep] - Callback function executed at each removal step.
 * @param {function} [options.onComplete] - Callback function executed when removal is complete.
 * @returns {Promise<void>} A promise that resolves when removal is complete.
 * @throws {Error} If invalid parameters are provided.
 */
function gentleLashRemoval(options = {}) {
    return new Promise((resolve, reject) => {
        try {
            // Validate and set default options
            const {
                removalTime = 5000,
                removalSteps = 5,
                onStep,
                onComplete
            } = options;

            if (typeof removalTime !== 'number' || removalTime <= 0) {
                throw new Error('removalTime must be a positive number');
            }
            if (typeof removalSteps !== 'number' || removalSteps <= 0) {
                throw new Error('removalSteps must be a positive integer');
            }

            const stepDuration = removalTime / removalSteps;
            let currentStep = 0;

            // Execute removal steps
            const removalInterval = setInterval(() => {
                currentStep++;
                
                // Execute step callback if provided
                if (typeof onStep === 'function') {
                    try {
                        onStep({
                            step: currentStep,
                            totalSteps: removalSteps,
                            progress: (currentStep / removalSteps) * 100
                        });
                    } catch (err) {
                        console.error('Error in onStep callback:', err);
                    }
                }

                // Complete the process when all steps are done
                if (currentStep >= removalSteps) {
                    clearInterval(removalInterval);
                    
                    // Execute completion callback if provided
                    if (typeof onComplete === 'function') {
                        try {
                            onComplete();
                        } catch (err) {
                            console.error('Error in onComplete callback:', err);
                        }
                    }
                    
                    resolve();
                }
            }, stepDuration);
        } catch (err) {
            reject(err);
        }
    });
}

// Example usage:
/*
gentleLashRemoval({
    removalTime: 3000,
    removalSteps: 3,
    onStep: ({ step, totalSteps, progress }) => {
        console.log(`Step ${step} of ${totalSteps} (${progress.toFixed(1)}% complete)`);
    },
    onComplete: () => {
        console.log('Lashes removed gently without damage!');
    }
}).catch(err => {
    console.error('Lash removal failed:', err);
});
*/
```
