"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Create a JavaScript function to model Agile workflows for a team, incorporating mentorship principles highlighted by CrestAgile.
Generated: DETERMINISTIC_74c2dfef59ca5a1c
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
 * AgileWorkflowManager - Models Agile workflows with mentorship principles.
 * @class
 */
class AgileWorkflowManager {
  /**
   * @constructor
   * @param {Object} config - Configuration object
   * @param {string} config.teamName - Name of the team
   * @param {Array} config.members - Array of team members
   * @param {Object} config.mentors - Key-value pairs of mentors and mentees
   * @param {number} config.sprintDuration - Duration of sprints in days
   */
  constructor(config) {
    if (!config || !config.teamName || !config.members) {
      throw new Error('Invalid configuration: teamName and members are required');
    }

    this.teamName = config.teamName;
    this.members = config.members;
    this.mentors = config.mentors || {};
    this.sprintDuration = config.sprintDuration || 14;
    this.currentSprint = 1;
    this.backlog = [];
    this.inProgress = [];
    this.completed = [];
    this.blockers = [];
    this.mentorshipSessions = [];
  }

  /**
   * Add a task to the backlog
   * @param {Object} task - Task object
   * @param {string} task.id - Unique task ID
   * @param {string} task.title - Task title
   * @param {string} task.description - Task description
   * @param {string} task.assignedTo - Team member assigned to task
   * @param {number} task.estimate - Estimated story points
   */
  addToBacklog(task) {
    if (!task || !task.id || !task.title) {
      throw new Error('Task must have at least id and title');
    }

    if (task.assignedTo && !this.members.includes(task.assignedTo)) {
      throw new Error(`Assigned member ${task.assignedTo} is not part of the team`);
    }

    this.backlog.push(task);
  }

  /**
   * Move task from backlog to in-progress
   * @param {string} taskId - ID of task to start
   */
  startTask(taskId) {
    const taskIndex = this.backlog.findIndex(task => task.id === taskId);
    if (taskIndex === -1) {
      throw new Error(`Task with ID ${taskId} not found in backlog`);
    }

    const task = this.backlog[taskIndex];
    this.backlog.splice(taskIndex, 1);
    this.inProgress.push(task);
  }

  /**
   * Complete a task and move it to completed
   * @param {string} taskId - ID of task to complete
   */
  completeTask(taskId) {
    const taskIndex = this.inProgress.findIndex(task => task.id === taskId);
    if (taskIndex === -1) {
      throw new Error(`Task with ID ${taskId} not found in progress`);
    }

    const task = this.inProgress[taskIndex];
    this.inProgress.splice(taskIndex, 1);
    this.completed.push(task);
  }

  /**
   * Add a blocker to a task
   * @param {string} taskId - ID of blocked task
   * @param {string} reason - Reason for blocker
   */
  addBlocker(taskId, reason) {
    const task = this.inProgress.find(t => t.id === taskId);
    if (!task) {
      throw new Error(`Task with ID ${taskId} not found in progress`);
    }

    this.blockers.push({
      taskId,
      reason,
      date: new Date()
    });
  }

  /**
   * Resolve a blocker
   * @param {string} taskId - ID of task with resolved blocker
   */
  resolveBlocker(taskId) {
    const blockerIndex = this.blockers.findIndex(b => b.taskId === taskId);
    if (blockerIndex === -1) {
      throw new Error(`No blocker found for task ${taskId}`);
    }

    this.blockers.splice(blockerIndex, 1);
  }

  /**
   * Schedule a mentorship session
   * @param {string} mentor - Mentor name
   * @param {string} mentee - Mentee name
   * @param {Date} date - Session date
   * @param {string} topic - Session topic
   */
  scheduleMentorshipSession(mentor, mentee, date, topic) {
    if (!this.mentors[mentor] || !this.mentors[mentor].includes(mentee)) {
      throw new Error(`${mentor} is not assigned as mentor for ${mentee}`);
    }

    this.mentorshipSessions.push({
      mentor,
      mentee,
      date,
      topic,
      completed: false
    });
  }

  /**
   * Complete a mentorship session
   * @param {string} mentor - Mentor name
   * @param {string} mentee - Mentee name
   * @param {Date} date - Session date
   */
  completeMentorshipSession(mentor, mentee, date) {
    const session = this.mentorshipSessions.find(s => 
      s.mentor === mentor && 
      s.mentee === mentee && 
      s.date.getTime() === date.getTime()
    );

    if (!session) {
      throw new Error('Mentorship session not found');
    }

    session.completed = true;
  }

  /**
   * Advance to the next sprint
   */
  nextSprint() {
    // Carry over incomplete tasks to next sprint
    this.backlog = [...this.backlog, ...this.inProgress];
    this.inProgress = [];
    this.blockers = [];
    this.currentSprint++;
  }

  /**
   * Get sprint metrics
   * @returns {Object} Sprint metrics
   */
  getSprintMetrics() {
    return {
      sprint: this.currentSprint,
      backlogCount: this.backlog.length,
      inProgressCount: this.inProgress.length,
      completedCount: this.completed.length,
      blockersCount: this.blockers.length,
      mentorshipSessions: this.mentorshipSessions.filter(s => s.completed).length
    };
  }

  /**
   * Get mentorship pairs
   * @returns {Array} Array of mentorship pairs
   */
  getMentorshipPairs() {
    return Object.entries(this.mentors).flatMap(([mentor, mentees]) => 
      mentees.map(mentee => ({ mentor, mentee }))
    );
  }
}

// Example usage:
/*
const config = {
  teamName: 'Alpha Team',
  members: ['Alice', 'Bob', 'Charlie', 'Dana'],
  mentors: {
    'Alice': ['Bob', 'Charlie'],
    'Dana': ['Charlie']
  },
  sprintDuration: 14
};

const workflow = new AgileWorkflowManager(config);
*/
```
