"""
Generated Code Metadata:
========================
Original URL: https://www.newsmaritime.com
Prompt: Create a JavaScript snippet for tracking shipping port safety metrics, inspired by the AI transformation insights shared on Newsmaritime.com.
Generated: DETERMINISTIC_8eaffe02a9683a45
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shipping Port Safety Metrics Tracker
 * 
 * This module tracks and provides insights into shipping port safety metrics.
 * 
 * @module PortSafetyMetrics
 */

// Define a class to encapsulate port safety metrics
class PortSafetyMetrics {
  /**
   * Constructor to initialize port safety metrics
   * 
   * @param {string} portName - Name of the port
   */
  constructor(portName) {
    this.portName = portName;
    this.metrics = {
      incidents: 0,
      injuries: 0,
      fatalities: 0,
      cargoDamage: 0,
    };
  }

  /**
   * Log an incident
   * 
   * @param {string} incidentType - Type of incident (injury, fatality, cargo damage)
   * @param {number} [severity=1] - Severity of the incident
   */
  logIncident(incidentType, severity = 1) {
    try {
      switch (incidentType) {
        case 'injury':
          this.metrics.injuries += severity;
          break;
        case 'fatality':
          this.metrics.fatalities += severity;
          break;
        case 'cargo damage':
          this.metrics.cargoDamage += severity;
          break;
        default:
          throw new Error(`Invalid incident type: ${incidentType}`);
      }
      this.metrics.incidents++;
    } catch (error) {
      console.error(`Error logging incident: ${error.message}`);
    }
  }

  /**
   * Get the current safety metrics
   * 
   * @returns {object} Safety metrics
   */
  getSafetyMetrics() {
    return { ...this.metrics };
  }

  /**
   * Calculate the incident rate
   * 
   * @param {number} totalShipments - Total number of shipments
   * @returns {number} Incident rate
   */
  calculateIncidentRate(totalShipments) {
    if (totalShipments <= 0) {
      throw new Error('Total shipments must be greater than zero');
    }
    return (this.metrics.incidents / totalShipments) * 100;
  }
}

// Example usage
function main() {
  const port = new PortSafetyMetrics('Port of Example');

  // Log some incidents
  port.logIncident('injury', 2);
  port.logIncident('fatality');
  port.logIncident('cargo damage', 3);

  // Get the current safety metrics
  const metrics = port.getSafetyMetrics();
  console.log(`Safety Metrics for ${port.portName}:`, metrics);

  // Calculate the incident rate
  const totalShipments = 1000;
  const incidentRate = port.calculateIncidentRate(totalShipments);
  console.log(`Incident Rate for ${port.portName}: ${incidentRate}%`);
}

main();
```
