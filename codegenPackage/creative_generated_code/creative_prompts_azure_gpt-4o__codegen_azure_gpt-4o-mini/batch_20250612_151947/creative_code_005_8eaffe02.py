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
 * ShippingPortSafetyMetricsTracker
 * A class to track safety metrics for shipping ports.
 * 
 * This class provides methods to log incidents, retrieve metrics, 
 * and calculate safety ratings based on the logged data.
 */
class ShippingPortSafetyMetricsTracker {
    constructor() {
        // Initialize an empty array for storing incident records
        this.incidents = [];
    }

    /**
     * Logs a new incident.
     * @param {string} description - Description of the incident.
     * @param {Date} date - Date of the incident.
     * @param {number} severity - Severity level of the incident (1-5).
     * @throws Will throw an error if severity is out of bounds (1-5).
     */
    logIncident(description, date, severity) {
        if (severity < 1 || severity > 5) {
            throw new Error('Severity must be between 1 and 5');
        }

        // Create an incident object
        const incident = {
            description,
            date: date instanceof Date ? date : new Date(date),
            severity
        };

        // Push the incident to the incidents array
        this.incidents.push(incident);
        console.log('Incident logged:', incident);
    }

    /**
     * Retrieves all logged incidents.
     * @returns {Array} - Array of incident objects.
     */
    getIncidents() {
        return this.incidents;
    }

    /**
     * Calculates the average severity of incidents.
     * @returns {number} - Average severity (0 if no incidents logged).
     */
    calculateAverageSeverity() {
        if (this.incidents.length === 0) {
            return 0;
        }

        const totalSeverity = this.incidents.reduce((sum, incident) => sum + incident.severity, 0);
        return totalSeverity / this.incidents.length;
    }

    /**
     * Clears all logged incidents.
     */
    clearIncidents() {
        this.incidents = [];
        console.log('All incidents cleared');
    }
}

// Example usage
try {
    const tracker = new ShippingPortSafetyMetricsTracker();
    tracker.logIncident('Cargo spill incident', '2023-10-01', 4);
    tracker.logIncident('Slip and fall accident', '2023-10-02', 2);
    console.log('Incidents:', tracker.getIncidents());
    console.log('Average Severity:', tracker.calculateAverageSeverity());
    
    tracker.clearIncidents();
    console.log('Incidents after clearing:', tracker.getIncidents());
} catch (error) {
    console.error('Error:', error.message);
}
```
