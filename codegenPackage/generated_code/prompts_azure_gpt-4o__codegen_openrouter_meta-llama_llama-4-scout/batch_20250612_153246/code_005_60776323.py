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
 * Calculates the estimated time for repairing a diesel turbo based on predefined repair steps and customer-specific issues.
 */

/**
 * RepairStep class representing a single repair step.
 */
class RepairStep {
  /**
   * @param {string} name - Name of the repair step.
   * @param {number} timeRequired - Time required for the repair step in minutes.
   */
  constructor(name, timeRequired) {
    this.name = name;
    this.timeRequired = timeRequired;
  }
}

/**
 * DieselTurboRepairEstimator class for estimating repair time.
 */
class DieselTurboRepairEstimator {
  /**
   * Predefined repair steps.
   * @type {RepairStep[]}
   */
  static PREDEFINED_REPAIR_STEPS = [
    new RepairStep('Inspection', 30),
    new RepairStep('Cleaning', 60),
    new RepairStep('Part Replacement', 120),
    new RepairStep('Testing', 90),
  ];

  /**
   * Calculates the estimated time for repairing a diesel turbo.
   * @param {string[]} customerIssues - Customer-specific issues.
   * @param {boolean} isTurbochargerReplaced - Whether the turbocharger is replaced.
   * @returns {number} Estimated time in minutes.
   */
  static calculateEstimatedTime(customerIssues, isTurbochargerReplaced) {
    let estimatedTime = 0;

    // Add time for predefined repair steps
    DieselTurboRepairEstimator.PREDEFINED_REPAIR_STEPS.forEach((step) => {
      estimatedTime += step.timeRequired;
    });

    // Add time for customer-specific issues
    customerIssues.forEach((issue) => {
      switch (issue) {
        case 'clogged-air-filter':
          estimatedTime += 30;
          break;
        case 'faulty-sensor':
          estimatedTime += 60;
          break;
        case 'damaged-turbine':
          estimatedTime += 120;
          break;
        default:
          throw new Error(`Unknown customer issue: ${issue}`);
      }
    });

    // Add extra time if turbocharger is replaced
    if (isTurbochargerReplaced) {
      estimatedTime += 180;
    }

    return estimatedTime;
  }
}

// Example usage:
try {
  const customerIssues = ['clogged-air-filter', 'faulty-sensor'];
  const isTurbochargerReplaced = true;
  const estimatedTime = DieselTurboRepairEstimator.calculateEstimatedTime(customerIssues, isTurbochargerReplaced);
  console.log(`Estimated time: ${estimatedTime} minutes`);
} catch (error) {
  console.error(error.message);
}
```
