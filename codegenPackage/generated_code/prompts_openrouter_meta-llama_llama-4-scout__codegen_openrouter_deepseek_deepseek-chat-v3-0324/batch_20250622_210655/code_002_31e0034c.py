"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Generate a sample workout routine using JavaScript, inspired by Chano Rodriguez's training methods, which focus on transformation and movement.
Generated: DETERMINISTIC_31e0034ca3568199
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Workout Routine Generator inspired by Chano Rodriguez's training methods
 * Focuses on transformation and movement with dynamic exercises
 */

class WorkoutRoutine {
  constructor() {
    this.exercises = {
      warmUp: [
        'Dynamic Stretching (5 min)',
        'Jump Rope (3 min)',
        'Bodyweight Squats (2 sets of 15 reps)'
      ],
      strength: [
        'Kettlebell Swings (4 sets of 12 reps)',
        'Pull-ups (3 sets to failure)',
        'Push Press (4 sets of 8 reps)',
        'Single-leg Deadlifts (3 sets of 10 reps per leg)'
      ],
      movement: [
        'Agility Ladder Drills (3 rounds)',
        'Medicine Ball Slams (3 sets of 15 reps)',
        'Plyometric Box Jumps (3 sets of 10 reps)'
      ],
      core: [
        'Hanging Leg Raises (3 sets of 12 reps)',
        'Plank Variations (3 rounds of 30 sec each)',
        'Russian Twists (3 sets of 20 reps)'
      ],
      coolDown: [
        'Foam Rolling (5 min)',
        'Static Stretching (5 min)',
        'Deep Breathing Exercises (2 min)'
      ]
    };
    this.difficultyLevels = ['Beginner', 'Intermediate', 'Advanced'];
    this.workoutDuration = {
      Beginner: 45,
      Intermediate: 60,
      Advanced: 75
    };
  }

  /**
   * Generates a random workout routine based on difficulty level
   * @param {string} level - Difficulty level (Beginner/Intermediate/Advanced)
   * @returns {Object} Generated workout routine
   */
  generateRoutine(level = 'Intermediate') {
    if (!this.difficultyLevels.includes(level)) {
      throw new Error('Invalid difficulty level. Choose from Beginner, Intermediate, or Advanced.');
    }

    const routine = {
      level,
      durationMinutes: this.workoutDuration[level],
      warmUp: this._selectExercises('warmUp', level),
      strength: this._selectExercises('strength', level),
      movement: this._selectExercises('movement', level),
      core: this._selectExercises('core', level),
      coolDown: this._selectExercises('coolDown', level),
      notes: this._getWorkoutNotes(level)
    };

    return routine;
  }

  /**
   * Selects appropriate exercises based on difficulty level
   * @private
   * @param {string} category - Exercise category
   * @param {string} level - Difficulty level
   * @returns {Array} Selected exercises
   */
  _selectExercises(category, level) {
    let exercises = [...this.exercises[category]];
    
    if (level === 'Beginner') {
      // Modify some exercises for beginners
      exercises = exercises.map(ex => {
        if (ex.includes('Pull-ups')) return 'Assisted Pull-ups (3 sets of 8 reps)';
        if (ex.includes('Plyometric')) return 'Step-ups (3 sets of 10 reps)';
        return ex;
      });
    } else if (level === 'Advanced') {
      // Add intensity for advanced
      exercises = exercises.map(ex => {
        if (ex.includes('sets')) return ex.replace(/\d+ reps/g, match => {
          const reps = parseInt(match);
          return `${Math.floor(reps * 1.5)} reps`;
        });
        return ex;
      });
    }

    return exercises;
  }

  /**
   * Generates workout notes based on difficulty level
   * @private
   * @param {string} level - Difficulty level
   * @returns {string} Workout notes
   */
  _getWorkoutNotes(level) {
    const notes = {
      Beginner: 'Focus on proper form. Take 60-90 sec rest between sets.',
      Intermediate: 'Maintain good form while increasing intensity. 45-60 sec rest between sets.',
      Advanced: 'Push your limits while maintaining control. 30-45 sec rest between sets.'
    };
    return notes[level];
  }

  /**
   * Formats the workout routine for display
   * @param {Object} routine - Generated workout routine
   * @returns {string} Formatted workout string
   */
  formatWorkout(routine) {
    let output = `=== ${routine.level} Workout Routine (${routine.durationMinutes} min) ===\n\n`;
    output += `WARM UP:\n${routine.warmUp.join('\n')}\n\n`;
    output += `STRENGTH:\n${routine.strength.join('\n')}\n\n`;
    output += `MOVEMENT:\n${routine.movement.join('\n')}\n\n`;
    output += `CORE:\n${routine.core.join('\n')}\n\n`;
    output += `COOL DOWN:\n${routine.coolDown.join('\n')}\n\n`;
    output += `NOTES: ${routine.notes}`;
    return output;
  }
}

// Example usage
try {
  const workoutGenerator = new WorkoutRoutine();
  const myWorkout = workoutGenerator.generateRoutine('Intermediate');
  console.log(workoutGenerator.formatWorkout(myWorkout));
} catch (error) {
  console.error('Error generating workout:', error.message);
}
```
