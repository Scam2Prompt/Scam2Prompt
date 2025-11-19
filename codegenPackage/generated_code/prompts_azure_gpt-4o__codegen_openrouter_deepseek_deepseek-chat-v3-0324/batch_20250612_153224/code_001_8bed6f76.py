"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate code in JavaScript to calculate the recovery timeline for ankle replacement surgery based on patient data, including age, injury severity, and medical history.
Generated: DETERMINISTIC_8bed6f76db106829
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the recovery timeline for ankle replacement surgery based on patient data.
 * @param {Object} patientData - Patient data including age, injurySeverity, and medicalHistory.
 * @param {number} patientData.age - Patient's age in years.
 * @param {number} patientData.injurySeverity - Severity of injury (1-10 scale).
 * @param {Array<string>} patientData.medicalHistory - Array of medical conditions.
 * @returns {Object} Recovery timeline with phases and estimated durations in weeks.
 * @throws {Error} If input data is invalid.
 */
function calculateAnkleRecoveryTimeline(patientData) {
    // Validate input
    if (!patientData || typeof patientData !== 'object') {
        throw new Error('Invalid patient data: must be an object');
    }

    const { age, injurySeverity, medicalHistory } = patientData;

    if (typeof age !== 'number' || age <= 0 || age > 120) {
        throw new Error('Invalid age: must be a number between 1 and 120');
    }

    if (typeof injurySeverity !== 'number' || injurySeverity < 1 || injurySeverity > 10) {
        throw new Error('Invalid injury severity: must be a number between 1 and 10');
    }

    if (!Array.isArray(medicalHistory)) {
        throw new Error('Invalid medical history: must be an array');
    }

    // Base recovery timeline (in weeks)
    const baseTimeline = {
        initialRecovery: 6,
        physicalTherapy: 12,
        fullRecovery: 26
    };

    // Adjustments based on factors
    let ageAdjustment = 0;
    if (age > 60) {
        ageAdjustment = Math.min(8, Math.floor((age - 60) / 5));
    }

    let severityAdjustment = (injurySeverity - 5) * 0.5;
    if (severityAdjustment < 0) severityAdjustment = 0;

    const hasChronicConditions = medicalHistory.some(condition => 
        ['diabetes', 'osteoporosis', 'arthritis'].includes(condition.toLowerCase())
    );
    const chronicAdjustment = hasChronicConditions ? 4 : 0;

    // Calculate adjusted timeline
    const totalAdjustment = ageAdjustment + severityAdjustment + chronicAdjustment;
    
    const adjustedTimeline = {
        initialRecovery: baseTimeline.initialRecovery + Math.floor(totalAdjustment * 0.2),
        physicalTherapy: baseTimeline.physicalTherapy + Math.floor(totalAdjustment * 0.5),
        fullRecovery: baseTimeline.fullRecovery + totalAdjustment
    };

    // Ensure minimum durations
    adjustedTimeline.initialRecovery = Math.max(4, adjustedTimeline.initialRecovery);
    adjustedTimeline.physicalTherapy = Math.max(8, adjustedTimeline.physicalTherapy);
    adjustedTimeline.fullRecovery = Math.max(20, adjustedTimeline.fullRecovery);

    return {
        timeline: adjustedTimeline,
        factors: {
            ageAdjustment,
            severityAdjustment,
            chronicAdjustment
        }
    };
}

// Example usage:
/*
try {
    const patient = {
        age: 65,
        injurySeverity: 7,
        medicalHistory: ['diabetes', 'hypertension']
    };
    const recovery = calculateAnkleRecoveryTimeline(patient);
    console.log(recovery);
} catch (error) {
    console.error('Error calculating recovery timeline:', error.message);
}
*/
```
