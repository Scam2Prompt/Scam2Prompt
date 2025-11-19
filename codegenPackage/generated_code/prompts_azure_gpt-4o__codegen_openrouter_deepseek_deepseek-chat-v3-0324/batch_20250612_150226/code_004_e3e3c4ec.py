"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Design a scheduling tool in JavaScript to balance work and networking in coworking spaces, inspired by the "Optimiser son agenda : équilibre travail et networking au coworking" article on NetCoworking.
Generated: DETERMINISTIC_e3e3c4ecb36d4e82
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * WorkNetScheduler - A scheduling tool to balance work and networking in coworking spaces
 */

class WorkNetScheduler {
  /**
   * @param {Object} config - Configuration object
   * @param {number} config.workHoursPerDay - Total work hours per day
   * @param {number} config.networkingHoursPerDay - Total networking hours per day
   * @param {string[]} config.workTasks - List of work tasks
   * @param {string[]} config.networkingActivities - List of networking activities
   * @param {Date} config.startDate - Start date for scheduling
   * @param {Date} config.endDate - End date for scheduling
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.workHoursPerDay = config.workHoursPerDay;
    this.networkingHoursPerDay = config.networkingHoursPerDay;
    this.workTasks = config.workTasks;
    this.networkingActivities = config.networkingActivities;
    this.startDate = new Date(config.startDate);
    this.endDate = new Date(config.endDate);
    this.schedule = [];
  }

  /**
   * Validate configuration parameters
   * @param {Object} config - Configuration object
   * @throws {Error} If configuration is invalid
   */
  validateConfig(config) {
    const requiredFields = [
      'workHoursPerDay',
      'networkingHoursPerDay',
      'workTasks',
      'networkingActivities',
      'startDate',
      'endDate'
    ];

    for (const field of requiredFields) {
      if (!(field in config)) {
        throw new Error(`Missing required field: ${field}`);
      }
    }

    if (config.workHoursPerDay <= 0 || config.networkingHoursPerDay <= 0) {
      throw new Error('Hours per day must be positive numbers');
    }

    if (config.workTasks.length === 0 || config.networkingActivities.length === 0) {
      throw new Error('Work tasks and networking activities cannot be empty');
    }

    const startDate = new Date(config.startDate);
    const endDate = new Date(config.endDate);

    if (startDate >= endDate) {
      throw new Error('End date must be after start date');
    }
  }

  /**
   * Generate schedule for the given period
   * @returns {Array} Generated schedule
   */
  generateSchedule() {
    this.schedule = [];
    const currentDate = new Date(this.startDate);

    while (currentDate <= this.endDate) {
      const daySchedule = this.generateDailySchedule(currentDate);
      this.schedule.push(daySchedule);
      currentDate.setDate(currentDate.getDate() + 1);
    }

    return this.schedule;
  }

  /**
   * Generate schedule for a single day
   * @param {Date} date - Date for the schedule
   * @returns {Object} Daily schedule
   */
  generateDailySchedule(date) {
    const workBlocks = this.generateTimeBlocks(
      this.workHoursPerDay,
      this.workTasks,
      'work'
    );

    const networkingBlocks = this.generateTimeBlocks(
      this.networkingHoursPerDay,
      this.networkingActivities,
      'networking'
    );

    const allBlocks = [...workBlocks, ...networkingBlocks];
    this.shuffleBlocks(allBlocks);

    return {
      date: new Date(date),
      blocks: allBlocks
    };
  }

  /**
   * Generate time blocks for a given activity type
   * @param {number} totalHours - Total hours to allocate
   * @param {string[]} activities - List of activities
   * @param {string} type - Type of activity ('work' or 'networking')
   * @returns {Array} Generated time blocks
   */
  generateTimeBlocks(totalHours, activities, type) {
    const blocks = [];
    let remainingHours = totalHours;

    while (remainingHours > 0) {
      const duration = this.getRandomDuration(remainingHours);
      const activity = this.getRandomActivity(activities);
      
      blocks.push({
        type,
        activity,
        duration,
        startTime: null, // Will be set during scheduling
        endTime: null    // Will be set during scheduling
      });

      remainingHours -= duration;
    }

    return blocks;
  }

  /**
   * Get random duration for a time block (between 0.5 and 2 hours)
   * @param {number} maxDuration - Maximum allowed duration
   * @returns {number} Random duration
   */
  getRandomDuration(maxDuration) {
    const minDuration = 0.5;
    const maxPossible = Math.min(2, maxDuration);
    const duration = minDuration + Math.random() * (maxPossible - minDuration);
    return parseFloat(duration.toFixed(1));
  }

  /**
   * Get random activity from the list
   * @param {string[]} activities - List of activities
   * @returns {string} Random activity
   */
  getRandomActivity(activities) {
    const randomIndex = Math.floor(Math.random() * activities.length);
    return activities[randomIndex];
  }

  /**
   * Shuffle time blocks to create a balanced schedule
   * @param {Array} blocks - Array of time blocks
   */
  shuffleBlocks(blocks) {
    // Fisher-Yates shuffle algorithm
    for (let i = blocks.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [blocks[i], blocks[j]] = [blocks[j], blocks[i]];
    }
  }

  /**
   * Assign specific times to each block (9 AM to 6 PM)
   * @param {Array} schedule - The schedule to assign times to
   * @returns {Array} Schedule with assigned times
   */
  assignSpecificTimes(schedule) {
    const WORKDAY_START = 9; // 9 AM
    const WORKDAY_END = 18;  // 6 PM
    const totalAvailableHours = WORKDAY_END - WORKDAY_START;

    schedule.forEach(day => {
      let currentHour = WORKDAY_START;
      
      day.blocks.forEach(block => {
        if (currentHour + block.duration > WORKDAY_END) {
          throw new Error('Total hours exceed available workday time');
        }

        block.startTime = this.formatTime(currentHour);
        currentHour += block.duration;
        block.endTime = this.formatTime(currentHour);
      });

      const totalScheduledHours = day.blocks.reduce((sum, block) => sum + block.duration, 0);
      if (totalScheduledHours > totalAvailableHours) {
        throw new Error('Total scheduled hours exceed available workday time');
      }
    });

    return schedule;
  }

  /**
   * Format hour as HH:MM AM/PM
   * @param {number} hour - Hour in decimal format (e.g., 9.5 for 9:30 AM)
   * @returns {string} Formatted time
   */
  formatTime(hour) {
    const hours = Math.floor(hour);
    const minutes = Math.round((hour - hours) * 60);
    const period = hours >= 12 ? 'PM' : 'AM';
    const displayHours = hours % 12 || 12;
    
    return `${displayHours}:${minutes.toString().padStart(2, '0')} ${period}`;
  }

  /**
   * Export schedule as JSON
   * @returns {string} JSON string of the schedule
   */
  exportToJSON() {
    return JSON.stringify(this.schedule, null, 2);
  }

  /**
   * Export schedule as CSV
   * @returns {string} CSV string of the schedule
   */
  exportToCSV() {
    let csv = 'Date,Type,Activity,Start Time,End Time,Duration (hours)\n';
    
    this.schedule.forEach(day => {
      day.blocks.forEach(block => {
        csv += `${day.date.toISOString().split('T')[0]},`;
        csv += `${block.type},`;
        csv += `"${block.activity}",`;
        csv += `${block.startTime},`;
        csv += `${block.endTime},`;
        csv += `${block.duration}\n`;
      });
    });

    return csv;
  }
}

// Example usage:
/*
const scheduler = new WorkNetScheduler({
  workHoursPerDay: 6,
  networkingHoursPerDay: 2,
  workTasks: [
    'Project A development',
    'Project B research',
    'Email correspondence',
    'Team meeting',
    'Code review'
  ],
  networkingActivities: [
    'Coffee chat with member',
    'Lunch with potential client',
    'Attend community event',
    'Participate in workshop',
    'Mentorship session'
  ],
  startDate: '2023-06-01',
  endDate: '2023-06-07'
});

const schedule = scheduler.generateSchedule();
const scheduledWithTimes = scheduler.assignSpecificTimes(schedule);
console.log(scheduler.exportToJSON());
console.log(scheduler.exportToCSV());
*/
```
