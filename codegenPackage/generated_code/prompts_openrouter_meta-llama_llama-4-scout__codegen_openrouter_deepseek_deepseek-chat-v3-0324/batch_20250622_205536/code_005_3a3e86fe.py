"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write a JavaScript code snippet to create a running plan that includes easy runs, long runs, interval workouts, tempo runs, hill repeats, strides, cross-training, and strength training, and provide tips on maximizing running stamina.
Generated: DETERMINISTIC_3a3e86feddc3efee
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Running Plan Generator
 * Creates a comprehensive running training plan with various workout types
 * and provides tips for maximizing running stamina.
 */

class RunningPlanGenerator {
  constructor() {
    this.workoutTypes = {
      EASY_RUN: 'Easy Run',
      LONG_RUN: 'Long Run',
      INTERVAL: 'Interval Workout',
      TEMPO: 'Tempo Run',
      HILLS: 'Hill Repeats',
      STRIDES: 'Strides',
      CROSS_TRAINING: 'Cross-Training',
      STRENGTH: 'Strength Training'
    };

    this.tipsForStamina = [
      'Gradually increase weekly mileage by no more than 10%',
      'Incorporate one long run per week to build endurance',
      'Include regular interval training to improve VO2 max',
      'Maintain proper hydration and nutrition',
      'Get adequate sleep for recovery',
      'Use tempo runs to improve lactate threshold',
      'Include strength training to prevent injuries',
      'Practice proper running form to increase efficiency',
      'Allow for proper recovery between hard workouts',
      'Consider periodization in your training plan'
    ];
  }

  /**
   * Generates a weekly running plan
   * @param {number} weeks - Number of weeks for the plan
   * @param {string} level - Runner's level (beginner, intermediate, advanced)
   * @returns {Object} Training plan with workouts and tips
   */
  generatePlan(weeks = 8, level = 'intermediate') {
    if (typeof weeks !== 'number' || weeks < 1) {
      throw new Error('Weeks must be a positive number');
    }

    if (!['beginner', 'intermediate', 'advanced'].includes(level)) {
      throw new Error('Level must be beginner, intermediate, or advanced');
    }

    const plan = {
      weeks: weeks,
      level: level,
      schedule: [],
      tips: this._getTipsForLevel(level)
    };

    for (let week = 1; week <= weeks; week++) {
      plan.schedule.push(this._generateWeek(week, level));
    }

    return plan;
  }

  /**
   * Generates a single week of workouts
   * @private
   * @param {number} weekNumber - Current week number
   * @param {string} level - Runner's level
   * @returns {Object} Week schedule
   */
  _generateWeek(weekNumber, level) {
    const week = {
      week: weekNumber,
      workouts: []
    };

    // Base workouts for all levels
    week.workouts.push(this._createWorkout(this.workoutTypes.EASY_RUN, '30-45 min', 'Recovery pace'));
    week.workouts.push(this._createWorkout(this.workoutTypes.LONG_RUN, this._getLongRunDuration(weekNumber, level), 'Conversational pace'));

    // Level-specific workouts
    if (level === 'beginner') {
      week.workouts.push(this._createWorkout(this.workoutTypes.STRIDES, '4-6 x 100m', 'Fast but controlled'));
      week.workouts.push(this._createWorkout(this.workoutTypes.CROSS_TRAINING, '30-45 min', 'Cycling or swimming'));
    } else if (level === 'intermediate') {
      week.workouts.push(this._createWorkout(this.workoutTypes.TEMPO, '20-30 min', 'Comfortably hard pace'));
      week.workouts.push(this._createWorkout(this.workoutTypes.INTERVAL, '6-8 x 400m', '5K race pace with recovery'));
      week.workouts.push(this._createWorkout(this.workoutTypes.STRENGTH, '30 min', 'Core and leg exercises'));
    } else { // advanced
      week.workouts.push(this._createWorkout(this.workoutTypes.TEMPO, '30-40 min', 'Comfortably hard pace'));
      week.workouts.push(this._createWorkout(this.workoutTypes.INTERVAL, '8-10 x 400m', '5K race pace with recovery'));
      week.workouts.push(this._createWorkout(this.workoutTypes.HILLS, '6-8 repeats', 'Steady effort uphill'));
      week.workouts.push(this._createWorkout(this.workoutTypes.STRENGTH, '45 min', 'Full-body strength training'));
    }

    return week;
  }

  /**
   * Creates a workout object
   * @private
   * @param {string} type - Workout type
   * @param {string} duration - Workout duration
   * @param {string} description - Workout description
   * @returns {Object} Workout object
   */
  _createWorkout(type, duration, description) {
    return {
      type: type,
      duration: duration,
      description: description,
      completed: false
    };
  }

  /**
   * Gets appropriate long run duration based on week and level
   * @private
   * @param {number} weekNumber - Current week number
   * @param {string} level - Runner's level
   * @returns {string} Duration string
   */
  _getLongRunDuration(weekNumber, level) {
    const baseTimes = {
      beginner: ['45 min', '50 min', '55 min', '60 min', '65 min', '70 min', '75 min', '80 min'],
      intermediate: ['60 min', '70 min', '80 min', '90 min', '100 min', '110 min', '120 min', '130 min'],
      advanced: ['90 min', '100 min', '110 min', '120 min', '130 min', '140 min', '150 min', '160 min']
    };

    const index = Math.min(weekNumber - 1, baseTimes[level].length - 1);
    return baseTimes[level][index];
  }

  /**
   * Gets tips appropriate for the runner's level
   * @private
   * @param {string} level - Runner's level
   * @returns {string[]} Array of tips
   */
  _getTipsForLevel(level) {
    const levelSpecificTips = {
      beginner: [
        'Start with run/walk intervals if needed',
        'Focus on consistency rather than speed',
        'Allow extra recovery time between workouts'
      ],
      intermediate: [
        'Balance hard and easy days',
        'Work on pacing strategies',
        'Consider adding some race-specific workouts'
      ],
      advanced: [
        'Include periodization in your training',
        'Consider double workout days for peak training',
        'Focus on race-specific preparation'
      ]
    };

    return [...this.tipsForStamina, ...levelSpecificTips[level]];
  }
}

// Example usage:
try {
  const planGenerator = new RunningPlanGenerator();
  const trainingPlan = planGenerator.generatePlan(8, 'intermediate');
  console.log(trainingPlan);
} catch (error) {
  console.error('Error generating training plan:', error.message);
}
```
