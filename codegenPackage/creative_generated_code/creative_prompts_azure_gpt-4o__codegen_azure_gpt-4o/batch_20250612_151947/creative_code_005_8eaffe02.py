"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.newsmaritime.com
Prompt: Create a JavaScript snippet for tracking shipping port safety metrics, inspired by the AI transformation insights shared on Newsmaritime.com.
Generated: DETERMINISTIC_8eaffe02a9683a45
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shipping Port Safety Metrics Tracker
 * This script tracks and calculates safety metrics for shipping ports, inspired by AI transformation insights.
 * Metrics tracked: incidents, inspections, violations, and safety score
 */

// Class to represent a shipping port
class ShippingPort {
  constructor(name) {
    this.name = name;
    this.incidents = 0;
    this.inspections = 0;
    this.violations = 0;
    this.safetyScore = 100; // Initial safety score (out of 100)
  }

  /**
   * Record an incident at the port.
   */
  recordIncident() {
    this.incidents++;
    this.updateSafetyScore();
  }

  /**
   * Record an inspection at the port.
   * @param {number} violations - Number of violations found during the inspection
   */
  recordInspection(violations) {
    if (typeof violations !== 'number' || violations < 0) {
      console.error("Invalid number of violations. Must be a non-negative number.");
      return;
    }
    this.inspections++;
    this.violations += violations;
    this.updateSafetyScore();
  }

  /**
   * Update the safety score based on incidents, inspections, and violations.
   */
  updateSafetyScore() {
    const incidentPenalty = this.incidents * 2; // Each incident decreases score by 2
    const violationPenalty = this.violations * 1; // Each violation decreases score by 1
    const inspectionBonus = this.inspections * 0.5; // Each inspection increases score by 0.5

    // Safety score formula
    this.safetyScore = Math.max(100 - incidentPenalty - violationPenalty + inspectionBonus, 0);
  }

  /**
   * Get the current metrics of the port.
   * @returns {object} An object containing the port's metrics
   */
  getMetrics() {
    return {
      name: this.name,
      incidents: this.incidents,
      inspections: this.inspections,
      violations: this.violations,
      safetyScore: this.safetyScore.toFixed(2), // Convert to fixed-point notation for readability
    };
  }
}

// Example usage:

// Create a shipping port instance
const port = new ShippingPort("Port of AI Transformation");

// Record incidents and inspections
port.recordIncident();
port.recordInspection(3);
port.recordInspection(2);

// Retrieve and log the metrics
console.log(port.getMetrics());
```
