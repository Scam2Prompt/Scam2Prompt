"""
Generated Code Metadata:
========================
Original URL: https://www.cosmicrewards.com
Prompt: Generate a JavaScript code example to track user engagement and rewards on the Cosmic Rewards platform, using metrics such as time played, levels completed, and rewards earned.
Generated: DETERMINISTIC_c43cf1a95cba0917
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cosmic Rewards Engagement Tracker
// This module tracks user engagement metrics such as time played, levels completed, and rewards earned.

class EngagementTracker {
    constructor(userId) {
        if (!userId) {
            throw new Error("User ID is required to initialize the Engagement Tracker.");
        }
        this.userId = userId;
        this.startTime = null;
        this.totalTimePlayed = 0; // in seconds
        this.levelsCompleted = 0;
        this.rewardsEarned = 0;
    }

    // Start tracking time played
    startTracking() {
        if (this.startTime) {
            console.warn("Tracking is already in progress.");
            return;
        }
        this.startTime = Date.now();
        console.log("Started tracking engagement for user:", this.userId);
    }

    // Stop tracking time played and update total time
    stopTracking() {
        if (!this.startTime) {
            console.warn("Tracking has not been started.");
            return;
        }
        const endTime = Date.now();
        this.totalTimePlayed += Math.floor((endTime - this.startTime) / 1000); // convert ms to seconds
        this.startTime = null;
        console.log(`Stopped tracking. Total time played: ${this.totalTimePlayed} seconds.`);
    }

    // Record a level completion
    completeLevel() {
        this.levelsCompleted += 1;
        console.log(`Level completed. Total levels completed: ${this.levelsCompleted}`);
    }

    // Record a reward earned
    earnReward(points) {
        if (points <= 0) {
            throw new Error("Reward points must be greater than zero.");
        }
        this.rewardsEarned += points;
        console.log(`Reward earned: ${points} points. Total rewards earned: ${this.rewardsEarned}`);
    }

    // Get the current engagement metrics
    getMetrics() {
        return {
            userId: this.userId,
            totalTimePlayed: this.totalTimePlayed,
            levelsCompleted: this.levelsCompleted,
            rewardsEarned: this.rewardsEarned,
        };
    }

    // Reset engagement metrics (if needed)
    resetMetrics() {
        this.totalTimePlayed = 0;
        this.levelsCompleted = 0;
        this.rewardsEarned = 0;
        console.log("Engagement metrics have been reset.");
    }
}

// Example usage
try {
    const tracker = new EngagementTracker("user123");
    tracker.startTracking();
    // Simulate gameplay
    setTimeout(() => {
        tracker.completeLevel();
        tracker.earnReward(50);
        tracker.stopTracking();
        console.log(tracker.getMetrics());
    }, 5000); // Simulate 5 seconds of gameplay
} catch (error) {
    console.error("Error:", error.message);
}
```
