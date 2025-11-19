"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Write a JavaScript function that calculates the estimated time for repairing a diesel turbo based on predefined repair steps and customer-specific issues.
Generated: DETERMINISTIC_60776323a59bff0d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated repair time for a diesel turbo based on predefined steps and customer issues.
 * @param {Object} repairSteps - An object containing predefined repair steps and their time estimates.
 * @param {Array} customerIssues - An array of strings representing the customer's specific issues.
 * @returns {Object} An object containing the total time estimate and breakdown of steps.
 * @throws {Error} If invalid input is provided.
 */
function calculateTurboRepairTime(repairSteps, customerIssues) {
    // Validate input
    if (!repairSteps || typeof repairSteps !== 'object' || Object.keys(repairSteps).length === 0) {
        throw new Error('Invalid repair steps provided');
    }
    
    if (!Array.isArray(customerIssues)) {
        throw new Error('Customer issues must be an array');
    }

    // Initialize result object
    const result = {
        totalTime: 0,
        steps: []
    };

    try {
        // Calculate time for each matching issue
        customerIssues.forEach(issue => {
            if (typeof issue !== 'string') {
                console.warn(`Skipping invalid issue: ${issue}`);
                return;
            }

            const normalizedIssue = issue.trim().toLowerCase();
            let found = false;

            // Check for matching repair step
            for (const [step, time] of Object.entries(repairSteps)) {
                const normalizedStep = step.trim().toLowerCase();
                if (normalizedStep.includes(normalizedIssue) || normalizedIssue.includes(normalizedStep)) {
                    result.totalTime += time;
                    result.steps.push({
                        step: step,
                        time: time,
                        matchedIssue: issue
                    });
                    found = true;
                    break;
                }
            }

            if (!found) {
                console.warn(`No matching repair step found for issue: ${issue}`);
            }
        });

        // Add base inspection time if no issues matched
        if (result.steps.length === 0 && repairSteps.baseInspection) {
            result.totalTime = repairSteps.baseInspection;
            result.steps.push({
                step: 'Base Inspection',
                time: repairSteps.baseInspection,
                matchedIssue: 'General inspection'
            });
        }

        return result;
    } catch (error) {
        console.error('Error calculating repair time:', error);
        throw new Error('Failed to calculate repair time');
    }
}

// Example usage:
/*
const repairSteps = {
    'Base Inspection': 0.5,
    'Turbocharger Removal': 1.5,
    'Turbocharger Disassembly': 1,
    'Bearing Replacement': 2,
    'Seal Replacement': 1.5,
    'Turbine Cleaning': 1,
    'Turbocharger Reassembly': 1.5,
    'Turbocharger Installation': 1.5,
    'System Testing': 0.5
};

const customerIssues = ['bearing noise', 'oil leaks'];
const estimate = calculateTurboRepairTime(repairSteps, customerIssues);
console.log(estimate);
*/
```
