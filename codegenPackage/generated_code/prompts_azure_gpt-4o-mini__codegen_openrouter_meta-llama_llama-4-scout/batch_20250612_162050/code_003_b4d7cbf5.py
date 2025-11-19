"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Create a JavaScript function that tracks user engagement in emotional intelligence courses, akin to the offerings on Agne Doveikaite's website.
Generated: DETERMINISTIC_b4d7cbf57e83191e
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
 * User Engagement Tracker for Emotional Intelligence Courses
 */

// Define a class to track user engagement
class UserEngagementTracker {
  /**
   * Initialize the tracker with an empty object to store user engagement data
   */
  constructor() {
    this.engagementData = {};
  }

  /**
   * Add a new user to the tracker
   * @param {string} userId - Unique identifier for the user
   * @param {string} courseId - Unique identifier for the course
   */
  addUser(userId, courseId) {
    if (!this.engagementData[userId]) {
      this.engagementData[userId] = {};
    }
    if (!this.engagementData[userId][courseId]) {
      this.engagementData[userId][courseId] = {
        lessonsCompleted: 0,
        totalLessons: 0,
        lastActive: null,
      };
    }
  }

  /**
   * Log a user's progress in a course
   * @param {string} userId - Unique identifier for the user
   * @param {string} courseId - Unique identifier for the course
   * @param {number} lessonId - Unique identifier for the lesson
   * @param {boolean} completed - Whether the lesson was completed
   */
  logProgress(userId, courseId, lessonId, completed, totalLessons) {
    try {
      if (!this.engagementData[userId] || !this.engagementData[userId][courseId]) {
        throw new Error("User or course not found");
      }
      if (completed) {
        this.engagementData[userId][courseId].lessonsCompleted++;
      }
      this.engagementData[userId][courseId].totalLessons = totalLessons;
      this.engagementData[userId][courseId].lastActive = new Date();
    } catch (error) {
      console.error(`Error logging progress: ${error.message}`);
    }
  }

  /**
   * Get a user's engagement data for a course
   * @param {string} userId - Unique identifier for the user
   * @param {string} courseId - Unique identifier for the course
   * @returns {object} User engagement data for the course
   */
  getEngagementData(userId, courseId) {
    try {
      if (!this.engagementData[userId] || !this.engagementData[userId][courseId]) {
        throw new Error("User or course not found");
      }
      return this.engagementData[userId][courseId];
    } catch (error) {
      console.error(`Error getting engagement data: ${error.message}`);
      return null;
    }
  }

  /**
   * Get a summary of all user engagement data
   * @returns {object} Summary of user engagement data
   */
  getSummary() {
    const summary = {};
    for (const userId in this.engagementData) {
      summary[userId] = {};
      for (const courseId in this.engagementData[userId]) {
        const engagementData = this.engagementData[userId][courseId];
        summary[userId][courseId] = {
          lessonsCompleted: engagementData.lessonsCompleted,
          totalLessons: engagementData.totalLessons,
          completionRate: engagementData.lessonsCompleted / engagementData.totalLessons,
        };
      }
    }
    return summary;
  }
}

// Example usage:
const tracker = new UserEngagementTracker();

// Add users and courses
tracker.addUser("user1", "course1");
tracker.addUser("user2", "course1");
tracker.addUser("user1", "course2");

// Log progress
tracker.logProgress("user1", "course1", 1, true, 10);
tracker.logProgress("user1", "course1", 2, false, 10);
tracker.logProgress("user2", "course1", 1, true, 10);
tracker.logProgress("user1", "course2", 1, true, 5);

// Get engagement data
console.log(tracker.getEngagementData("user1", "course1"));
console.log(tracker.getEngagementData("user2", "course1"));

// Get summary
console.log(tracker.getSummary());
```
