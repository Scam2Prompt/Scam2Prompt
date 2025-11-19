"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a JavaScript function that simulates a DBT skills training session, allowing users to practice mindfulness and distress tolerance techniques.
Generated: DETERMINISTIC_c1d384944818f581
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * DBT Skills Training Simulator
 * This module provides a simulation for practicing DBT (Dialectical Behavior Therapy) skills,
 * including mindfulness and distress tolerance techniques.
 */

class DBTSkillsSimulator {
  constructor() {
    this.skills = {
      mindfulness: [
        "Observe: Notice your surroundings without judgment.",
        "Describe: Put words to your experience.",
        "Participate: Fully engage in the present moment."
      ],
      distressTolerance: [
        "STOP: Stop, Take a step back, Observe, Proceed mindfully.",
        "TIP: Temperature, Intense exercise, Paced breathing.",
        "Distract: Use ACCEPTS (Activities, Contributing, Comparisons, Emotions, Pushing away, Thoughts, Sensations)."
      ]
    };
    this.currentSession = null;
  }

  /**
   * Starts a new DBT skills training session.
   * @param {string} skillType - Type of skill to practice ('mindfulness' or 'distressTolerance')
   * @returns {Object} Session object with skill type and start time
   * @throws {Error} If invalid skill type is provided
   */
  startSession(skillType) {
    if (!this.skills[skillType]) {
      throw new Error("Invalid skill type. Choose 'mindfulness' or 'distressTolerance'.");
    }

    this.currentSession = {
      skillType,
      startTime: new Date(),
      currentSkillIndex: 0,
      completedSkills: []
    };

    return {
      message: `Session started for ${skillType} skills.`,
      session: this.currentSession
    };
  }

  /**
   * Gets the current skill to practice.
   * @returns {Object} Current skill information
   * @throws {Error} If no session is active
   */
  getCurrentSkill() {
    if (!this.currentSession) {
      throw new Error("No active session. Start a session first.");
    }

    const { skillType, currentSkillIndex } = this.currentSession;
    const skill = this.skills[skillType][currentSkillIndex];

    return {
      skill,
      progress: `${currentSkillIndex + 1}/${this.skills[skillType].length}`,
      session: this.currentSession
    };
  }

  /**
   * Completes the current skill and moves to the next one.
   * @returns {Object} Next skill information or session completion message
   * @throws {Error} If no session is active
   */
  completeCurrentSkill() {
    if (!this.currentSession) {
      throw new Error("No active session. Start a session first.");
    }

    const { skillType, currentSkillIndex } = this.currentSession;
    const completedSkill = this.skills[skillType][currentSkillIndex];
    
    this.currentSession.completedSkills.push(completedSkill);
    
    if (currentSkillIndex < this.skills[skillType].length - 1) {
      this.currentSession.currentSkillIndex++;
      return this.getCurrentSkill();
    } else {
      const endTime = new Date();
      const duration = (endTime - this.currentSession.startTime) / 1000;
      const completedSession = { ...this.currentSession, endTime, duration };
      this.currentSession = null;
      
      return {
        message: "Session completed! Great job practicing your DBT skills.",
        session: completedSession
      };
    }
  }

  /**
   * Ends the current session prematurely.
   * @returns {Object} Session summary
   * @throws {Error} If no session is active
   */
  endSession() {
    if (!this.currentSession) {
      throw new Error("No active session to end.");
    }

    const endTime = new Date();
    const duration = (endTime - this.currentSession.startTime) / 1000;
    const completedSession = { ...this.currentSession, endTime, duration };
    this.currentSession = null;

    return {
      message: "Session ended. Remember, any practice is better than none.",
      session: completedSession
    };
  }

  /**
   * Provides a guided breathing exercise.
   * @param {number} duration - Duration in seconds (default: 60)
   * @returns {Object} Breathing exercise instructions
   */
  guidedBreathing(duration = 60) {
    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error("Duration must be a positive number.");
    }

    const cycles = Math.floor(duration / 10) || 1;
    
    return {
      instructions: "Follow this breathing pattern:",
      steps: [
        "1. Inhale deeply for 4 seconds",
        "2. Hold your breath for 2 seconds",
        "3. Exhale slowly for 4 seconds",
        `4. Repeat for ${cycles} ${cycles === 1 ? 'cycle' : 'cycles'} (about ${duration} seconds)`
      ],
      duration
    };
  }

  /**
   * Provides a body scan meditation exercise.
   * @param {number} duration - Duration in minutes (default: 5)
   * @returns {Object} Body scan instructions
   */
  bodyScanMeditation(duration = 5) {
    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error("Duration must be a positive number.");
    }

    return {
      instructions: "Perform a body scan meditation:",
      steps: [
        "1. Find a comfortable position",
        "2. Bring attention to your toes and feet",
        "3. Gradually move attention up through your body",
        "4. Notice sensations without judgment",
        "5. When your mind wanders, gently return focus",
        `6. Continue for ${duration} ${duration === 1 ? 'minute' : 'minutes'}`
      ],
      duration: duration * 60
    };
  }
}

// Example usage:
// const simulator = new DBTSkillsSimulator();
// console.log(simulator.startSession('mindfulness'));
// console.log(simulator.getCurrentSkill());
// console.log(simulator.completeCurrentSkill());
// console.log(simulator.guidedBreathing(30));
// console.log(simulator.bodyScanMeditation(3));
```
