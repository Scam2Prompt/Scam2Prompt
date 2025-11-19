"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Write a code snippet in JavaScript to create a simple quiz that assesses a user's eligibility to donate plasma based on the requirements listed on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_a8d1c929e6f494e9
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple quiz to assess user's eligibility to donate plasma based on Orlando Plasma Centers website requirements.
 */

// Eligibility requirements
const eligibilityRequirements = {
  age: { min: 18, max: 70 },
  weight: { min: 110 }, // in pounds
  health: ["good", "excellent"],
  ironLevel: { min: 12 }, // in mg/dL
  hemoglobinLevel: { min: 12 }, // in g/dL
  bloodPressure: { systolic: { min: 90, max: 160 }, diastolic: { min: 50, max: 100 } },
  pulse: { min: 50, max: 100 }, // in beats per minute
  lastDonation: { days: 28 }, // in days
};

/**
 * Quiz class to assess user's eligibility to donate plasma.
 */
class PlasmaDonationQuiz {
  constructor() {
    this.userData = {};
  }

  /**
   * Ask user for their age and validate it.
   * @returns {boolean} True if age is valid, false otherwise.
   */
  askAge() {
    let age = parseInt(prompt("How old are you?"));
    if (isNaN(age) || age < eligibilityRequirements.age.min || age > eligibilityRequirements.age.max) {
      alert(`You must be between ${eligibilityRequirements.age.min} and ${eligibilityRequirements.age.max} years old.`);
      return this.askAge();
    }
    this.userData.age = age;
    return true;
  }

  /**
   * Ask user for their weight and validate it.
   * @returns {boolean} True if weight is valid, false otherwise.
   */
  askWeight() {
    let weight = parseFloat(prompt("How much do you weigh (in pounds)?"));
    if (isNaN(weight) || weight < eligibilityRequirements.weight.min) {
      alert(`You must weigh at least ${eligibilityRequirements.weight.min} pounds.`);
      return this.askWeight();
    }
    this.userData.weight = weight;
    return true;
  }

  /**
   * Ask user about their health and validate it.
   * @returns {boolean} True if health is valid, false otherwise.
   */
  askHealth() {
    let health = prompt("How would you describe your health? (good/excellent)");
    health = health.toLowerCase();
    if (!eligibilityRequirements.health.includes(health)) {
      alert(`You must have ${eligibilityRequirements.health.join(" or ")} health.`);
      return this.askHealth();
    }
    this.userData.health = health;
    return true;
  }

  /**
   * Ask user for their iron level and validate it.
   * @returns {boolean} True if iron level is valid, false otherwise.
   */
  askIronLevel() {
    let ironLevel = parseFloat(prompt("What is your iron level (in mg/dL)?"));
    if (isNaN(ironLevel) || ironLevel < eligibilityRequirements.ironLevel.min) {
      alert(`Your iron level must be at least ${eligibilityRequirements.ironLevel.min} mg/dL.`);
      return this.askIronLevel();
    }
    this.userData.ironLevel = ironLevel;
    return true;
  }

  /**
   * Ask user for their hemoglobin level and validate it.
   * @returns {boolean} True if hemoglobin level is valid, false otherwise.
   */
  askHemoglobinLevel() {
    let hemoglobinLevel = parseFloat(prompt("What is your hemoglobin level (in g/dL)?"));
    if (isNaN(hemoglobinLevel) || hemoglobinLevel < eligibilityRequirements.hemoglobinLevel.min) {
      alert(`Your hemoglobin level must be at least ${eligibilityRequirements.hemoglobinLevel.min} g/dL.`);
      return this.askHemoglobinLevel();
    }
    this.userData.hemoglobinLevel = hemoglobinLevel;
    return true;
  }

  /**
   * Ask user for their blood pressure and validate it.
   * @returns {boolean} True if blood pressure is valid, false otherwise.
   */
  askBloodPressure() {
    let systolic = parseInt(prompt("What is your systolic blood pressure?"));
    let diastolic = parseInt(prompt("What is your diastolic blood pressure?"));
    if (
      isNaN(systolic) ||
      isNaN(diastolic) ||
      systolic < eligibilityRequirements.bloodPressure.systolic.min ||
      systolic > eligibilityRequirements.bloodPressure.systolic.max ||
      diastolic < eligibilityRequirements.bloodPressure.diastolic.min ||
      diastolic > eligibilityRequirements.bloodPressure.diastolic.max
    ) {
      alert(
        `Your blood pressure must be between ${eligibilityRequirements.bloodPressure.systolic.min}/${eligibilityRequirements.bloodPressure.diastolic.min} and ${eligibilityRequirements.bloodPressure.systolic.max}/${eligibilityRequirements.bloodPressure.diastolic.max}.`
      );
      return this.askBloodPressure();
    }
    this.userData.bloodPressure = { systolic, diastolic };
    return true;
  }

  /**
   * Ask user for their pulse and validate it.
   * @returns {boolean} True if pulse is valid, false otherwise.
   */
  askPulse() {
    let pulse = parseInt(prompt("What is your pulse (in beats per minute)?"));
    if (isNaN(pulse) || pulse < eligibilityRequirements.pulse.min || pulse > eligibilityRequirements.pulse.max) {
      alert(`Your pulse must be between ${eligibilityRequirements.pulse.min} and ${eligibilityRequirements.pulse.max} beats per minute.`);
      return this.askPulse();
    }
    this.userData.pulse = pulse;
    return true;
  }

  /**
   * Ask user for the number of days since their last donation and validate it.
   * @returns {boolean} True if days since last donation is valid, false otherwise.
   */
  askLastDonation() {
    let days = parseInt(prompt("How many days have passed since your last plasma donation?"));
    if (isNaN(days) || days < eligibilityRequirements.lastDonation.days) {
      alert(`You must have not donated plasma in the last ${eligibilityRequirements.lastDonation.days} days.`);
      return this.askLastDonation();
    }
    this.userData.lastDonation = days;
    return true;
  }

  /**
   * Run the quiz and determine user's eligibility to donate plasma.
   * @returns {boolean} True if user is eligible, false otherwise.
   */
  runQuiz() {
    if (
      this.askAge() &&
      this.askWeight() &&
      this.askHealth() &&
      this.askIronLevel() &&
      this.askHemoglobinLevel() &&
      this.askBloodPressure() &&
      this.askPulse() &&
      this.askLastDonation()
    ) {
      return true;
    }
    return false;
  }

  /**
   * Display user's eligibility result.
   * @param {boolean} eligible True if user is eligible, false otherwise.
   */
  displayResult(eligible) {
    if (eligible) {
      alert("You are eligible to donate plasma.");
    } else {
      alert("You are not eligible to donate plasma.");
    }
  }
}

// Run the quiz
let quiz = new PlasmaDonationQuiz();
let eligible = quiz.runQuiz();
quiz.displayResult(eligible);
```
