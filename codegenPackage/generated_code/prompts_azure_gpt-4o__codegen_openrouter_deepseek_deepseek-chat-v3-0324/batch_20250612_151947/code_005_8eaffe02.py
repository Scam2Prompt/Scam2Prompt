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
 * Inspired by AI transformation insights from Newsmaritime.com
 * Tracks and analyzes safety metrics for shipping ports
 */

class PortSafetyMetrics {
  constructor(portName) {
    this.portName = portName;
    this.metrics = {
      incidents: [],
      inspections: [],
      equipmentStatus: [],
      weatherConditions: [],
      crewTrainingRecords: []
    };
    this.safetyScore = 100; // Base score (100 = perfect safety)
  }

  /**
   * Record a safety incident
   * @param {string} type - Incident type (collision, spill, injury, etc.)
   * @param {number} severity - Severity level (1-10)
   * @param {string} description - Incident description
   * @param {Date} date - Date of incident
   */
  recordIncident(type, severity, description, date = new Date()) {
    if (severity < 1 || severity > 10) {
      throw new Error('Severity must be between 1 and 10');
    }

    const incident = {
      type,
      severity,
      description,
      date,
      resolved: false
    };

    this.metrics.incidents.push(incident);
    this._updateSafetyScore(-severity * 2);
    return incident;
  }

  /**
   * Record a safety inspection
   * @param {string} inspector - Name of inspector
   * @param {number} score - Inspection score (0-100)
   * @param {string[]} findings - Array of findings
   * @param {Date} date - Date of inspection
   */
  recordInspection(inspector, score, findings, date = new Date()) {
    if (score < 0 || score > 100) {
      throw new Error('Score must be between 0 and 100');
    }

    const inspection = {
      inspector,
      score,
      findings,
      date
    };

    this.metrics.inspections.push(inspection);
    this._updateSafetyScore(score / 10);
    return inspection;
  }

  /**
   * Record equipment status
   * @param {string} equipmentType - Type of equipment
   * @param {string} status - Operational status
   * @param {Date} date - Date of status check
   */
  recordEquipmentStatus(equipmentType, status, date = new Date()) {
    const validStatuses = ['operational', 'maintenance', 'out_of_service'];
    if (!validStatuses.includes(status)) {
      throw new Error(`Invalid status. Must be one of: ${validStatuses.join(', ')}`);
    }

    const equipmentRecord = {
      equipmentType,
      status,
      date
    };

    this.metrics.equipmentStatus.push(equipmentRecord);
    
    // Update safety score based on equipment status
    const scoreImpact = {
      operational: 1,
      maintenance: -1,
      out_of_service: -5
    };
    
    this._updateSafetyScore(scoreImpact[status]);
    return equipmentRecord;
  }

  /**
   * Record weather conditions
   * @param {string} condition - Weather condition
   * @param {number} windSpeed - Wind speed in knots
   * @param {number} waveHeight - Wave height in meters
   * @param {Date} date - Date of recording
   */
  recordWeatherConditions(condition, windSpeed, waveHeight, date = new Date()) {
    const weatherRecord = {
      condition,
      windSpeed,
      waveHeight,
      date
    };

    this.metrics.weatherConditions.push(weatherRecord);
    
    // Calculate weather impact on safety score
    let impact = 0;
    if (windSpeed > 30 || waveHeight > 3) impact = -5;
    else if (windSpeed > 20 || waveHeight > 2) impact = -2;
    
    this._updateSafetyScore(impact);
    return weatherRecord;
  }

  /**
   * Record crew training completion
   * @param {string} crewMember - Name of crew member
   * @param {string} trainingType - Type of training completed
   * @param {Date} completionDate - Date of training completion
   */
  recordCrewTraining(crewMember, trainingType, completionDate = new Date()) {
    const trainingRecord = {
      crewMember,
      trainingType,
      completionDate
    };

    this.metrics.crewTrainingRecords.push(trainingRecord);
    this._updateSafetyScore(2); // Positive impact for each training
    return trainingRecord;
  }

  /**
   * Resolve an incident
   * @param {number} incidentIndex - Index of incident to resolve
   * @param {string} resolutionNotes - Notes about the resolution
   */
  resolveIncident(incidentIndex, resolutionNotes) {
    if (incidentIndex < 0 || incidentIndex >= this.metrics.incidents.length) {
      throw new Error('Invalid incident index');
    }

    const incident = this.metrics.incidents[incidentIndex];
    incident.resolved = true;
    incident.resolutionNotes = resolutionNotes;
    incident.resolutionDate = new Date();
    
    // Partial score recovery for resolved incidents
    this._updateSafetyScore(incident.severity);
    return incident;
  }

  /**
   * Get current safety metrics summary
   * @returns {object} Summary of safety metrics
   */
  getSafetySummary() {
    const unresolvedIncidents = this.metrics.incidents.filter(i => !i.resolved).length;
    const lastInspection = this.metrics.inspections.length > 0 
      ? this.metrics.inspections[this.metrics.inspections.length - 1] 
      : null;
    
    const equipmentStatus = this.metrics.equipmentStatus.reduce((acc, curr) => {
      acc[curr.status] = (acc[curr.status] || 0) + 1;
      return acc;
    }, {});

    return {
      portName: this.portName,
      safetyScore: Math.max(0, Math.min(100, this.safetyScore)), // Clamp between 0-100
      unresolvedIncidents,
      lastInspectionScore: lastInspection ? lastInspection.score : null,
      equipmentStatus,
      lastWeatherCondition: this.metrics.weatherConditions.length > 0 
        ? this.metrics.weatherConditions[this.metrics.weatherConditions.length - 1] 
        : null,
      crewTrainingCount: this.metrics.crewTrainingRecords.length
    };
  }

  /**
   * Update safety score with bounds checking
   * @param {number} delta - Amount to adjust score by
   * @private
   */
  _updateSafetyScore(delta) {
    this.safetyScore += delta;
    // Keep score within 0-100 bounds
    this.safetyScore = Math.max(0, Math.min(100, this.safetyScore));
  }
}

// Example usage:
// const portMetrics = new PortSafetyMetrics('Rotterdam');
// portMetrics.recordIncident('collision', 3, 'Minor collision between two cargo ships');
// portMetrics.recordInspection('John Smith', 85, ['Fire extinguishers need replacement']);
// console.log(portMetrics.getSafetySummary());
```
