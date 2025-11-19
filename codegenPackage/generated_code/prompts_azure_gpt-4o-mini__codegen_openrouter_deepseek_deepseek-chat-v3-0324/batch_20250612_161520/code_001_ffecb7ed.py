"""
Generated Code Metadata:
========================
Original URL: https://fatihinspira.com
Prompt: Generate a JavaScript function that helps users build confidence in the workplace, inspired by the tips provided on Fatih Inspira.
Generated: DETERMINISTIC_ffecb7edc4ed6ea5
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Workplace Confidence Builder
 * A utility to help users build confidence in the workplace with actionable tips.
 * Inspired by Fatih Inspira's confidence-building techniques.
 */

class WorkplaceConfidenceBuilder {
  /**
   * Initialize the confidence builder with default tips and exercises
   */
  constructor() {
    this.tips = [
      "Practice positive self-talk daily",
      "Set small, achievable goals to build momentum",
      "Dress professionally to boost self-image",
      "Prepare thoroughly for meetings and presentations",
      "Maintain good posture - it affects how others perceive you",
      "Celebrate your wins, no matter how small",
      "Step outside your comfort zone regularly",
      "Ask questions when you're unsure",
      "Focus on solutions rather than problems",
      "Build a support network of colleagues"
    ];

    this.exercises = [
      "Power pose for 2 minutes before important events",
      "List 3 work accomplishments daily",
      "Practice speaking clearly in front of a mirror",
      "Record and review your presentations",
      "Initiate one difficult conversation per week"
    ];
  }

  /**
   * Get a random confidence-building tip
   * @returns {string} A random tip
   */
  getRandomTip() {
    if (!this.tips.length) {
      throw new Error("No tips available");
    }
    const randomIndex = Math.floor(Math.random() * this.tips.length);
    return this.tips[randomIndex];
  }

  /**
   * Get a random confidence-building exercise
   * @returns {string} A random exercise
   */
  getRandomExercise() {
    if (!this.exercises.length) {
      throw new Error("No exercises available");
    }
    const randomIndex = Math.floor(Math.random() * this.exercises.length);
    return this.exercises[randomIndex];
  }

  /**
   * Get a personalized confidence-building plan
   * @param {number} duration - Duration of the plan in days
   * @returns {Array} Array of daily confidence-building activities
   */
  getPersonalizedPlan(duration) {
    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error("Duration must be a positive number");
    }

    const plan = [];
    for (let i = 0; i < duration; i++) {
      const day = {
        day: i + 1,
        tip: this.getRandomTip(),
        exercise: this.getRandomExercise(),
        reflectionQuestion: this._getReflectionQuestion()
      };
      plan.push(day);
    }
    return plan;
  }

  /**
   * Add a custom tip to the collection
   * @param {string} tip - The confidence-building tip to add
   */
  addCustomTip(tip) {
    if (typeof tip !== 'string' || !tip.trim()) {
      throw new Error("Tip must be a non-empty string");
    }
    this.tips.push(tip);
  }

  /**
   * Add a custom exercise to the collection
   * @param {string} exercise - The confidence-building exercise to add
   */
  addCustomExercise(exercise) {
    if (typeof exercise !== 'string' || !exercise.trim()) {
      throw new Error("Exercise must be a non-empty string");
    }
    this.exercises.push(exercise);
  }

  /**
   * Get a reflection question (private method)
   * @returns {string} A reflection question
   */
  _getReflectionQuestion() {
    const questions = [
      "What did I do well today?",
      "What challenge did I overcome?",
      "How did I add value to my team today?",
      "What skill did I improve today?",
      "Who did I help today?"
    ];
    const randomIndex = Math.floor(Math.random() * questions.length);
    return questions[randomIndex];
  }
}

// Example usage:
// const confidenceBuilder = new WorkplaceConfidenceBuilder();
// console.log(confidenceBuilder.getRandomTip());
// console.log(confidenceBuilder.getRandomExercise());
// console.log(confidenceBuilder.getPersonalizedPlan(7));

module.exports = WorkplaceConfidenceBuilder;
```
