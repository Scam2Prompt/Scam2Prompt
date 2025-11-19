"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: "Generate JavaScript code to implement a simple time-tracking system for lawyers, inspired by the features of BillYourTime."
Generated: DETERMINISTIC_acb3bbb7d75ac214
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// time-tracker.js

/**
 * Time Tracker class for lawyers to track their work hours.
 */
class TimeTracker {
  /**
   * Initialize the TimeTracker with an empty list of sessions.
   */
  constructor() {
    this.sessions = [];
  }

  /**
   * Start a new time-tracking session.
   * @param {string} clientName - Name of the client.
   * @param {string} taskDescription - Description of the task.
   */
  startSession(clientName, taskDescription) {
    if (!clientName || !taskDescription) {
      throw new Error('Client name and task description are required.');
    }

    const session = {
      clientName,
      taskDescription,
      startTime: new Date(),
      endTime: null,
      duration: null,
    };

    this.sessions.push(session);
    return session;
  }

  /**
   * End a time-tracking session.
   * @param {number} sessionIndex - Index of the session to end.
   */
  endSession(sessionIndex) {
    if (sessionIndex < 0 || sessionIndex >= this.sessions.length) {
      throw new Error('Invalid session index.');
    }

    const session = this.sessions[sessionIndex];
    if (session.endTime) {
      throw new Error('Session has already been ended.');
    }

    session.endTime = new Date();
    session.duration = (session.endTime - session.startTime) / 60000; // minutes

    return session;
  }

  /**
   * Get all time-tracking sessions.
   * @returns {Array} List of sessions.
   */
  getSessions() {
    return this.sessions;
  }

  /**
   * Calculate total hours tracked for a client.
   * @param {string} clientName - Name of the client.
   * @returns {number} Total hours tracked.
   */
  getTotalHoursForClient(clientName) {
    return this.sessions
      .filter((session) => session.clientName === clientName)
      .reduce((total, session) => total + (session.duration || 0), 0);
  }
}

// Example usage:
function main() {
  const tracker = new TimeTracker();

  try {
    const session1 = tracker.startSession('John Doe', 'Meeting');
    console.log(`Started session for ${session1.clientName}: ${session1.taskDescription}`);

    // Simulate work...
    setTimeout(() => {
      const endedSession = tracker.endSession(0);
      console.log(`Ended session for ${endedSession.clientName}: ${endedSession.taskDescription}`);
      console.log(`Duration: ${endedSession.duration} minutes`);

      const totalHours = tracker.getTotalHoursForClient('John Doe');
      console.log(`Total hours for John Doe: ${totalHours / 60} hours`);

      console.log('All sessions:');
      console.log(tracker.getSessions());
    }, 2000);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
