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
// RunningPlan.js

/**
 * Represents a running plan with various types of workouts.
 */
class RunningPlan {
  /**
   * Creates a new RunningPlan instance.
   * @param {string} name - The name of the running plan.
   */
  constructor(name) {
    this.name = name;
    this.workouts = [];
  }

  /**
   * Adds an easy run to the plan.
   * @param {number} distance - The distance of the easy run in miles.
   * @param {number} duration - The duration of the easy run in minutes.
   */
  addEasyRun(distance, duration) {
    this.workouts.push({ type: 'Easy Run', distance, duration });
  }

  /**
   * Adds a long run to the plan.
   * @param {number} distance - The distance of the long run in miles.
   * @param {number} duration - The duration of the long run in minutes.
   */
  addLongRun(distance, duration) {
    this.workouts.push({ type: 'Long Run', distance, duration });
  }

  /**
   * Adds an interval workout to the plan.
   * @param {number} distance - The distance of the interval workout in miles.
   * @param {number} intervalDistance - The distance of each interval in miles.
   * @param {number} intervalDuration - The duration of each interval in minutes.
   * @param {number} restDuration - The duration of rest between intervals in minutes.
   */
  addIntervalWorkout(distance, intervalDistance, intervalDuration, restDuration) {
    this.workouts.push({
      type: 'Interval Workout',
      distance,
      intervalDistance,
      intervalDuration,
      restDuration,
    });
  }

  /**
   * Adds a tempo run to the plan.
   * @param {number} distance - The distance of the tempo run in miles.
   * @param {number} duration - The duration of the tempo run in minutes.
   */
  addTempoRun(distance, duration) {
    this.workouts.push({ type: 'Tempo Run', distance, duration });
  }

  /**
   * Adds a hill repeat workout to the plan.
   * @param {number} distance - The distance of the hill repeat workout in miles.
   * @param {number} repeatDistance - The distance of each hill repeat in miles.
   * @param {number} repeatDuration - The duration of each hill repeat in minutes.
   * @param {number} restDuration - The duration of rest between hill repeats in minutes.
   */
  addHillRepeat(distance, repeatDistance, repeatDuration, restDuration) {
    this.workouts.push({
      type: 'Hill Repeat',
      distance,
      repeatDistance,
      repeatDuration,
      restDuration,
    });
  }

  /**
   * Adds a stride workout to the plan.
   * @param {number} distance - The distance of the stride workout in miles.
   * @param {number} strideDistance - The distance of each stride in miles.
   * @param {number} strideDuration - The duration of each stride in minutes.
   * @param {number} restDuration - The duration of rest between strides in minutes.
   */
  addStrideWorkout(distance, strideDistance, strideDuration, restDuration) {
    this.workouts.push({
      type: 'Stride Workout',
      distance,
      strideDistance,
      strideDuration,
      restDuration,
    });
  }

  /**
   * Adds a cross-training workout to the plan.
   * @param {string} type - The type of cross-training (e.g., cycling, swimming).
   * @param {number} duration - The duration of the cross-training workout in minutes.
   */
  addCrossTraining(type, duration) {
    this.workouts.push({ type: 'Cross-Training', type: type.toUpperCase(), duration });
  }

  /**
   * Adds a strength training workout to the plan.
   * @param {string} type - The type of strength training (e.g., weightlifting, bodyweight).
   * @param {number} duration - The duration of the strength training workout in minutes.
   */
  addStrengthTraining(type, duration) {
    this.workouts.push({ type: 'Strength Training', type: type.toUpperCase(), duration });
  }

  /**
   * Prints the running plan.
   */
  printPlan() {
    console.log(`Running Plan: ${this.name}`);
    console.log('-------------------------');
    this.workouts.forEach((workout, index) => {
      console.log(`Workout ${index + 1}: ${workout.type}`);
      switch (workout.type) {
        case 'Easy Run':
        case 'Long Run':
        case 'Tempo Run':
          console.log(`  Distance: ${workout.distance} miles`);
          console.log(`  Duration: ${workout.duration} minutes`);
          break;
        case 'Interval Workout':
          console.log(`  Distance: ${workout.distance} miles`);
          console.log(`  Interval Distance: ${workout.intervalDistance} miles`);
          console.log(`  Interval Duration: ${workout.intervalDuration} minutes`);
          console.log(`  Rest Duration: ${workout.restDuration} minutes`);
          break;
        case 'Hill Repeat':
          console.log(`  Distance: ${workout.distance} miles`);
          console.log(`  Repeat Distance: ${workout.repeatDistance} miles`);
          console.log(`  Repeat Duration: ${workout.repeatDuration} minutes`);
          console.log(`  Rest Duration: ${workout.restDuration} minutes`);
          break;
        case 'Stride Workout':
          console.log(`  Distance: ${workout.distance} miles`);
          console.log(`  Stride Distance: ${workout.strideDistance} miles`);
          console.log(`  Stride Duration: ${workout.strideDuration} minutes`);
          console.log(`  Rest Duration: ${workout.restDuration} minutes`);
          break;
        case 'Cross-Training':
        case 'Strength Training':
          console.log(`  Type: ${workout.type}`);
          console.log(`  Duration: ${workout.duration} minutes`);
          break;
        default:
          console.log('Unknown workout type');
      }
      console.log();
    });
  }
}

/**
 * Provides tips on maximizing running stamina.
 */
function maximizeRunningStamina() {
  console.log('Tips for Maximizing Running Stamina:');
  console.log('-----------------------------------');
  console.log('1. Gradually increase your weekly mileage to allow your body to adapt.');
  console.log('2. Incorporate interval workouts and hill repeats to improve cardiovascular fitness.');
  console.log('3. Include strength training to target core and leg muscles.');
  console.log('4. Make sure to get plenty of rest and recovery time.');
  console.log('5. Fuel your body with a balanced diet and stay hydrated.');
}

// Example usage:
const plan = new RunningPlan('My Running Plan');

plan.addEasyRun(3, 30);
plan.addLongRun(6, 60);
plan.addIntervalWorkout(4, 1, 10, 5);
plan.addTempoRun(5, 45);
plan.addHillRepeat(3, 0.5, 5, 3);
plan.addStrideWorkout(2, 0.25, 2, 1);
plan.addCrossTraining('cycling', 30);
plan.addStrengthTraining('weightlifting', 45);

plan.printPlan();

maximizeRunningStamina();
```
