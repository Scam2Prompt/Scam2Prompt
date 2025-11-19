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
 */

class Patient {
  /**
   * Creates a new Patient instance.
   * @param {number} age - The patient's age.
   * @param {string} injurySeverity - The severity of the injury (mild, moderate, severe).
   * @param {string[]} medicalHistory - The patient's medical history.
   */
  constructor(age, injurySeverity, medicalHistory) {
    this.age = age;
    this.injurySeverity = injurySeverity;
    this.medicalHistory = medicalHistory;
  }
}

class RecoveryTimelineCalculator {
  /**
   * Calculates the recovery timeline in weeks.
   * @param {Patient} patient - The patient data.
   * @returns {object} The recovery timeline.
   */
  calculateRecoveryTimeline(patient) {
    if (!(patient instanceof Patient)) {
      throw new Error('Invalid patient data');
    }

    const baseRecoveryTime = this.getBaseRecoveryTime(patient.injurySeverity);
    const ageAdjustment = this.getAgeAdjustment(patient.age);
    const medicalHistoryAdjustment = this.getMedicalHistoryAdjustment(patient.medicalHistory);

    const totalRecoveryTime = baseRecoveryTime + ageAdjustment + medicalHistoryAdjustment;

    return {
      weeks: totalRecoveryTime,
      milestones: this.getRecoveryMilestones(totalRecoveryTime),
    };
  }

  /**
   * Gets the base recovery time in weeks based on injury severity.
   * @param {string} injurySeverity - The severity of the injury.
   * @returns {number} The base recovery time in weeks.
   */
  getBaseRecoveryTime(injurySeverity) {
    switch (injurySeverity) {
      case 'mild':
        return 6;
      case 'moderate':
        return 12;
      case 'severe':
        return 18;
      default:
        throw new Error(`Invalid injury severity: ${injurySeverity}`);
    }
  }

  /**
   * Gets the age adjustment in weeks.
   * @param {number} age - The patient's age.
   * @returns {number} The age adjustment in weeks.
   */
  getAgeAdjustment(age) {
    if (age < 18) {
      return 2;
    } else if (age < 65) {
      return 0;
    } else {
      return 4;
    }
  }

  /**
   * Gets the medical history adjustment in weeks.
   * @param {string[]} medicalHistory - The patient's medical history.
   * @returns {number} The medical history adjustment in weeks.
   */
  getMedicalHistoryAdjustment(medicalHistory) {
    const adjustments = {
      diabetes: 2,
      smoking: 4,
      previousSurgery: 3,
    };

    let adjustment = 0;
    medicalHistory.forEach((condition) => {
      if (adjustments[condition.toLowerCase()]) {
        adjustment += adjustments[condition.toLowerCase()];
      }
    });

    return adjustment;
  }

  /**
   * Gets the recovery milestones.
   * @param {number} totalRecoveryTime - The total recovery time in weeks.
   * @returns {object[]} The recovery milestones.
   */
  getRecoveryMilestones(totalRecoveryTime) {
    const milestones = [
      { week: 2, description: 'Pain management' },
      { week: 6, description: 'Range of motion exercises' },
      { week: 12, description: 'Strengthening exercises' },
    ];

    return milestones.filter((milestone) => milestone.week <= totalRecoveryTime);
  }
}

// Example usage:
function main() {
  try {
    const patient = new Patient(45, 'moderate', ['diabetes']);
    const calculator = new RecoveryTimelineCalculator();
    const recoveryTimeline = calculator.calculateRecoveryTimeline(patient);

    console.log(`Recovery time: ${recoveryTimeline.weeks} weeks`);
    console.log('Recovery milestones:');
    recoveryTimeline.milestones.forEach((milestone) => {
      console.log(`Week ${milestone.week}: ${milestone.description}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
