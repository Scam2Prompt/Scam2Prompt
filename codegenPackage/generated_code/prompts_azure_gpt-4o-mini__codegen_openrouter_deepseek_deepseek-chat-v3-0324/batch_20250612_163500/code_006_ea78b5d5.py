"""
Generated Code Metadata:
========================
Original URL: https://yyy-60q.pages.dev
Prompt: Describe how to set up a recurring quest on Layer3 that rewards users with XP and achievements.
Generated: DETERMINISTIC_ea78b5d555916856
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready JavaScript (Node.js) implementation for setting up a recurring quest on Layer3 with XP and achievement rewards:

```javascript
const { Layer3Client } = require('@layer3/sdk');
const { CronJob } = require('cron');

/**
 * Layer3 Quest Manager
 * Handles recurring quests with XP and achievement rewards
 */
class QuestManager {
  /**
   * @param {Object} config - Configuration object
   * @param {string} config.apiKey - Layer3 API key
   * @param {string} config.questId - Base quest ID
   * @param {number} config.xpReward - XP reward amount
   * @param {string} config.achievementId - Achievement ID to award
   * @param {string} config.cronSchedule - Cron schedule for recurrence
   */
  constructor(config) {
    this.client = new Layer3Client(config.apiKey);
    this.config = config;
    this.cronJob = null;
  }

  /**
   * Initialize and start the recurring quest
   */
  async start() {
    try {
      // Verify quest exists
      await this.client.getQuest(this.config.questId);
      
      // Set up recurring job
      this.cronJob = new CronJob(
        this.config.cronSchedule,
        this.executeQuest.bind(this),
        null,
        true,
        'UTC'
      );
      
      console.log(`Recurring quest started with schedule: ${this.config.cronSchedule}`);
    } catch (error) {
      console.error('Failed to start quest:', error);
      throw new Error('Quest initialization failed');
    }
  }

  /**
   * Stop the recurring quest
   */
  stop() {
    if (this.cronJob) {
      this.cronJob.stop();
      console.log('Recurring quest stopped');
    }
  }

  /**
   * Execute the quest and reward participants
   */
  async executeQuest() {
    try {
      const timestamp = new Date().toISOString();
      const recurringQuestId = `${this.config.questId}-${timestamp}`;
      
      // Create recurring quest instance
      await this.client.createQuestInstance({
        id: recurringQuestId,
        parentId: this.config.questId,
        isRecurring: true
      });
      
      // Get participants (implementation depends on your requirements)
      const participants = await this.getParticipants();
      
      // Reward each participant
      for (const userId of participants) {
        try {
          await this.client.awardXP(userId, this.config.xpReward, recurringQuestId);
          await this.client.grantAchievement(userId, this.config.achievementId);
          console.log(`Rewarded user ${userId}`);
        } catch (userError) {
          console.error(`Failed to reward user ${userId}:`, userError);
          // Continue with next user even if one fails
        }
      }
      
      console.log(`Quest ${recurringQuestId} completed successfully`);
    } catch (error) {
      console.error('Quest execution failed:', error);
      // Implement your retry or alert logic here
    }
  }

  /**
   * Get participants for the current quest cycle
   * @returns {Promise<string[]>} Array of user IDs
   */
  async getParticipants() {
    // Implement your participant logic here
    // This could query your database, API, or on-chain data
    return []; // Return array of user IDs
  }
}

// Example usage
const questManager = new QuestManager({
  apiKey: 'your_layer3_api_key',
  questId: 'daily-challenge',
  xpReward: 100,
  achievementId: 'daily-participant',
  cronSchedule: '0 0 * * *' // Daily at midnight UTC
});

// Start the quest
questManager.start()
  .catch(err => console.error('Startup error:', err));

// Handle graceful shutdown
process.on('SIGTERM', () => {
  questManager.stop();
  process.exit(0);
});

process.on('SIGINT', () => {
  questManager.stop();
  process.exit(0);
});
```
