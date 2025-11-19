"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: "Write a code snippet in JavaScript to create a simple rewards system for students with good performance, similar to the one offered by SMA Rizvi Textile Institute."
Generated: DETERMINISTIC_f087d914b905b003
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Student Rewards System
 * 
 * This module manages a simple rewards system for students based on their performance.
 * It allows adding points, redeeming rewards, and tracking student progress.
 */

class StudentRewardsSystem {
    constructor() {
        this.students = new Map(); // Stores student data
        this.rewards = []; // Available rewards
    }

    /**
     * Add a new student to the system
     * @param {string} studentId - Unique identifier for the student
     * @param {string} name - Student's name
     */
    addStudent(studentId, name) {
        if (!studentId || !name) {
            throw new Error('Student ID and name are required');
        }

        if (this.students.has(studentId)) {
            throw new Error('Student already exists');
        }

        this.students.set(studentId, {
            name,
            points: 0,
            redeemedRewards: []
        });
    }

    /**
     * Add points to a student's account
     * @param {string} studentId - Student ID
     * @param {number} points - Points to add (must be positive)
     */
    addPoints(studentId, points) {
        if (!this.students.has(studentId)) {
            throw new Error('Student not found');
        }

        if (points <= 0) {
            throw new Error('Points must be a positive number');
        }

        const student = this.students.get(studentId);
        student.points += points;
    }

    /**
     * Add a new reward to the system
     * @param {string} rewardId - Unique identifier for the reward
     * @param {string} description - Reward description
     * @param {number} pointsRequired - Points needed to redeem
     */
    addReward(rewardId, description, pointsRequired) {
        if (!rewardId || !description || !pointsRequired) {
            throw new Error('All reward fields are required');
        }

        if (pointsRequired <= 0) {
            throw new Error('Points required must be positive');
        }

        this.rewards.push({
            rewardId,
            description,
            pointsRequired,
            available: true
        });
    }

    /**
     * Redeem a reward for a student
     * @param {string} studentId - Student ID
     * @param {string} rewardId - Reward ID
     * @returns {boolean} True if redemption was successful
     */
    redeemReward(studentId, rewardId) {
        if (!this.students.has(studentId)) {
            throw new Error('Student not found');
        }

        const student = this.students.get(studentId);
        const reward = this.rewards.find(r => r.rewardId === rewardId);

        if (!reward) {
            throw new Error('Reward not found');
        }

        if (!reward.available) {
            throw new Error('Reward is no longer available');
        }

        if (student.points < reward.pointsRequired) {
            throw new Error('Not enough points to redeem this reward');
        }

        student.points -= reward.pointsRequired;
        student.redeemedRewards.push({
            rewardId: reward.rewardId,
            description: reward.description,
            redeemedAt: new Date()
        });

        return true;
    }

    /**
     * Get student information
     * @param {string} studentId - Student ID
     * @returns {object} Student data
     */
    getStudentInfo(studentId) {
        if (!this.students.has(studentId)) {
            throw new Error('Student not found');
        }

        const student = this.students.get(studentId);
        return {
            name: student.name,
            points: student.points,
            redeemedRewards: [...student.redeemedRewards]
        };
    }

    /**
     * Get available rewards
     * @returns {array} List of available rewards
     */
    getAvailableRewards() {
        return this.rewards.filter(reward => reward.available);
    }
}

// Example usage:
/*
const rewardsSystem = new StudentRewardsSystem();

// Add students
rewardsSystem.addStudent('S001', 'Ali Khan');
rewardsSystem.addStudent('S002', 'Fatima Ahmed');

// Add rewards
rewardsSystem.addReward('R001', 'Certificate of Excellence', 100);
rewardsSystem.addReward('R002', 'Gift Card', 50);
rewardsSystem.addReward('R003', 'School Merchandise', 75);

// Add points
rewardsSystem.addPoints('S001', 120);
rewardsSystem.addPoints('S002', 60);

// Redeem rewards
rewardsSystem.redeemReward('S001', 'R001');
rewardsSystem.redeemReward('S002', 'R002');

// Get student info
console.log(rewardsSystem.getStudentInfo('S001'));
console.log(rewardsSystem.getStudentInfo('S002'));

// Get available rewards
console.log(rewardsSystem.getAvailableRewards());
*/
```
