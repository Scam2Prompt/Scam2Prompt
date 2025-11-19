"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write a JavaScript function that creates a customizable action tracker, inspired by the Action Accelerator Framework, to help users monitor their daily tasks and achievements.
Generated: DETERMINISTIC_943eaddb3a029258
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Action Tracker - A customizable tracker for monitoring daily tasks and achievements.
 * Inspired by the Action Accelerator Framework.
 */
class ActionTracker {
  /**
   * Initializes the ActionTracker with default settings.
   * @param {Object} options - Configuration options for the tracker
   * @param {string} options.name - Name of the tracker
   * @param {Array} options.categories - List of categories for actions
   * @param {Object} options.goals - Daily/weekly goals configuration
   */
  constructor(options = {}) {
    this.name = options.name || 'My Action Tracker';
    this.categories = options.categories || ['Work', 'Personal', 'Health'];
    this.goals = {
      daily: options.goals?.daily || 5,
      weekly: options.goals?.weekly || 25
    };
    this.actions = [];
    this.currentStreak = 0;
    this.longestStreak = 0;
    this.lastActionDate = null;
  }

  /**
   * Adds a new action to the tracker.
   * @param {string} description - Description of the action
   * @param {string} category - Category of the action
   * @param {number} points - Points associated with the action
   * @returns {Object} The added action
   * @throws {Error} If category is invalid or points are negative
   */
  addAction(description, category, points = 1) {
    if (!this.categories.includes(category)) {
      throw new Error(`Invalid category. Available categories: ${this.categories.join(', ')}`);
    }

    if (points < 0) {
      throw new Error('Points must be a positive number');
    }

    const action = {
      id: Date.now(),
      date: new Date(),
      description,
      category,
      points,
      completed: false
    };

    this.actions.push(action);
    this._updateStreak();
    return action;
  }

  /**
   * Marks an action as completed.
   * @param {number} actionId - ID of the action to complete
   * @returns {Object} The completed action
   * @throws {Error} If action is not found
   */
  completeAction(actionId) {
    const action = this.actions.find(a => a.id === actionId);
    if (!action) {
      throw new Error('Action not found');
    }

    action.completed = true;
    return action;
  }

  /**
   * Gets all actions for a specific date.
   * @param {Date} date - Date to filter actions
   * @returns {Array} Filtered actions
   */
  getActionsByDate(date) {
    return this.actions.filter(action => 
      action.date.toDateString() === date.toDateString()
    );
  }

  /**
   * Gets summary statistics for the tracker.
   * @returns {Object} Summary statistics
   */
  getSummary() {
    const completedActions = this.actions.filter(a => a.completed);
    const totalPoints = completedActions.reduce((sum, action) => sum + action.points, 0);
    const dailyAverage = this.actions.length > 0 
      ? (completedActions.length / this.actions.length) * 100 
      : 0;

    return {
      totalActions: this.actions.length,
      completedActions: completedActions.length,
      completionRate: dailyAverage.toFixed(2),
      totalPoints,
      currentStreak: this.currentStreak,
      longestStreak: this.longestStreak,
      dailyGoal: this.goals.daily,
      weeklyGoal: this.goals.weekly
    };
  }

  /**
   * Gets actions grouped by category.
   * @returns {Object} Actions grouped by category
   */
  getActionsByCategory() {
    return this.categories.reduce((acc, category) => {
      acc[category] = this.actions.filter(a => a.category === category);
      return acc;
    }, {});
  }

  /**
   * Updates the streak counter based on consecutive days with actions.
   * @private
   */
  _updateStreak() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    if (!this.lastActionDate) {
      this.currentStreak = 1;
    } else {
      const lastDate = new Date(this.lastActionDate);
      lastDate.setHours(0, 0, 0, 0);

      const diffTime = today - lastDate;
      const diffDays = diffTime / (1000 * 60 * 60 * 24);

      if (diffDays === 1) {
        this.currentStreak++;
      } else if (diffDays > 1) {
        this.currentStreak = 1;
      }
    }

    if (this.currentStreak > this.longestStreak) {
      this.longestStreak = this.currentStreak;
    }

    this.lastActionDate = today;
  }

  /**
   * Resets the tracker to its initial state.
   */
  reset() {
    this.actions = [];
    this.currentStreak = 0;
    this.longestStreak = 0;
    this.lastActionDate = null;
  }
}

// Example usage:
/*
const tracker = new ActionTracker({
  name: 'Productivity Tracker',
  categories: ['Coding', 'Exercise', 'Reading'],
  goals: {
    daily: 3,
    weekly: 15
  }
});

tracker.addAction('Complete project module', 'Coding', 2);
tracker.addAction('30-minute workout', 'Exercise');
tracker.completeAction(tracker.actions[0].id);

console.log(tracker.getSummary());
console.log(tracker.getActionsByCategory());
*/
```
