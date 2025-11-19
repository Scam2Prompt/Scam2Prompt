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
// scheduling-tool.js

/**
 * Scheduling tool to balance work and networking in coworking spaces.
 */

class Schedule {
  /**
   * Initialize a new schedule with a list of time slots.
   * @param {Array} timeSlots - List of time slots in minutes.
   */
  constructor(timeSlots) {
    this.timeSlots = timeSlots;
    this.schedule = [];
  }

  /**
   * Add a work session to the schedule.
   * @param {number} duration - Duration of the work session in minutes.
   * @param {string} description - Description of the work session.
   */
  addWorkSession(duration, description) {
    if (duration > this.timeSlots[0]) {
      throw new Error("Work session duration exceeds available time slot.");
    }
    this.schedule.push({ type: "work", duration, description });
    this.timeSlots.shift();
  }

  /**
   * Add a networking session to the schedule.
   * @param {number} duration - Duration of the networking session in minutes.
   * @param {string} description - Description of the networking session.
   */
  addNetworkingSession(duration, description) {
    if (duration > this.timeSlots[0]) {
      throw new Error("Networking session duration exceeds available time slot.");
    }
    this.schedule.push({ type: "networking", duration, description });
    this.timeSlots.shift();
  }

  /**
   * Print the schedule.
   */
  printSchedule() {
    console.log("Schedule:");
    this.schedule.forEach((session, index) => {
      console.log(`${index + 1}. ${session.type}: ${session.duration} minutes - ${session.description}`);
    });
  }
}

class CoworkingSpace {
  /**
   * Initialize a new coworking space with a name and available time slots.
   * @param {string} name - Name of the coworking space.
   * @param {Array} timeSlots - List of available time slots in minutes.
   */
  constructor(name, timeSlots) {
    this.name = name;
    this.timeSlots = timeSlots;
    this.members = [];
  }

  /**
   * Add a member to the coworking space.
   * @param {string} name - Name of the member.
   */
  addMember(name) {
    this.members.push(name);
  }

  /**
   * Create a schedule for a member.
   * @param {string} memberName - Name of the member.
   * @returns {Schedule} Schedule for the member.
   */
  createSchedule(memberName) {
    if (!this.members.includes(memberName)) {
      throw new Error("Member not found in coworking space.");
    }
    return new Schedule([...this.timeSlots]);
  }
}

// Example usage:
const coworkingSpace = new CoworkingSpace("NetCoworking", [60, 30, 90, 60]);
coworkingSpace.addMember("John Doe");

const schedule = coworkingSpace.createSchedule("John Doe");
schedule.addWorkSession(60, "Focus on project X");
schedule.addNetworkingSession(30, "Meet with fellow members");
schedule.addWorkSession(90, "Work on project Y");

schedule.printSchedule();
```
