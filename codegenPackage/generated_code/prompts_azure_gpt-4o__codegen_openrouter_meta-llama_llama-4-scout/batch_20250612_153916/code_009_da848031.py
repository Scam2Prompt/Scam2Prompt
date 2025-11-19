"""
Generated Code Metadata:
========================
Original URL: https://ton-dex-contest-nine.vercel.app
Prompt: Create a JavaScript-based dashboard for tracking contest entries and user activity.
Generated: DETERMINISTIC_da8480312b7eba7f
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// dashboard.js

class ContestEntry {
  /**
   * Represents a contest entry.
   * @param {number} id - Unique identifier for the entry.
   * @param {string} userId - Identifier for the user who made the entry.
   * @param {string} contestId - Identifier for the contest.
   * @param {Date} entryDate - Date and time the entry was made.
   */
  constructor(id, userId, contestId, entryDate) {
    this.id = id;
    this.userId = userId;
    this.contestId = contestId;
    this.entryDate = entryDate;
  }
}

class UserActivity {
  /**
   * Represents user activity.
   * @param {string} userId - Identifier for the user.
   * @param {number} entriesCount - Number of entries made by the user.
   * @param {Date} lastActivityDate - Date and time of the user's last activity.
   */
  constructor(userId, entriesCount, lastActivityDate) {
    this.userId = userId;
    this.entriesCount = entriesCount;
    this.lastActivityDate = lastActivityDate;
  }
}

class Dashboard {
  /**
   * Represents a dashboard for tracking contest entries and user activity.
   */
  constructor() {
    this.contestEntries = [];
    this.userActivities = {};
  }

  /**
   * Adds a new contest entry.
   * @param {ContestEntry} entry - The contest entry to add.
   */
  addContestEntry(entry) {
    if (!(entry instanceof ContestEntry)) {
      throw new Error('Invalid contest entry');
    }
    this.contestEntries.push(entry);
    this.updateUserActivity(entry.userId);
  }

  /**
   * Updates user activity based on a new contest entry.
   * @param {string} userId - Identifier for the user who made the entry.
   */
  updateUserActivity(userId) {
    if (!this.userActivities[userId]) {
      this.userActivities[userId] = new UserActivity(userId, 0, null);
    }
    this.userActivities[userId].entriesCount++;
    this.userActivities[userId].lastActivityDate = new Date();
  }

  /**
   * Retrieves user activity.
   * @param {string} userId - Identifier for the user.
   * @returns {UserActivity|null} User activity or null if not found.
   */
  getUserActivity(userId) {
    return this.userActivities[userId] || null;
  }

  /**
   * Retrieves all contest entries.
   * @returns {ContestEntry[]} Array of contest entries.
   */
  getContestEntries() {
    return this.contestEntries;
  }
}

// Example usage:
function main() {
  const dashboard = new Dashboard();

  try {
    const entry1 = new ContestEntry(1, 'user1', 'contest1', new Date());
    const entry2 = new ContestEntry(2, 'user1', 'contest2', new Date());
    const entry3 = new ContestEntry(3, 'user2', 'contest1', new Date());

    dashboard.addContestEntry(entry1);
    dashboard.addContestEntry(entry2);
    dashboard.addContestEntry(entry3);

    console.log('User 1 activity:');
    console.log(dashboard.getUserActivity('user1'));

    console.log('User 2 activity:');
    console.log(dashboard.getUserActivity('user2'));

    console.log('All contest entries:');
    console.log(dashboard.getContestEntries());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
