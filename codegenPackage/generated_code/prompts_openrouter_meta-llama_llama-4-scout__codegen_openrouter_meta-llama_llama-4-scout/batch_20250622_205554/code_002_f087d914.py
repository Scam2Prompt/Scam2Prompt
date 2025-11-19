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
 * Simple Rewards System for Students
 * =====================================
 */

// Define a Student class
class Student {
  /**
   * Constructor for Student
   * @param {string} name - Student's name
   * @param {number} grade - Student's current grade
   */
  constructor(name, grade) {
    this.name = name;
    this.grade = grade;
    this.rewards = [];
  }

  /**
   * Add a reward to the student's account
   * @param {string} reward - Reward description
   */
  addReward(reward) {
    this.rewards.push(reward);
  }

  /**
   * Display student's information and rewards
   */
  displayInfo() {
    console.log(`Name: ${this.name}`);
    console.log(`Grade: ${this.grade}`);
    console.log(`Rewards: ${this.rewards.join(', ')}`);
  }
}

// Define a RewardsSystem class
class RewardsSystem {
  /**
   * Constructor for RewardsSystem
   */
  constructor() {
    this.students = {};
    this.rewardsCriteria = [
      { grade: 90, reward: 'Certificate of Excellence' },
      { grade: 85, reward: 'Special Privileges' },
      { grade: 80, reward: 'Merit-based Scholarship' },
    ];
  }

  /**
   * Add a student to the system
   * @param {string} name - Student's name
   * @param {number} grade - Student's current grade
   */
  addStudent(name, grade) {
    if (this.students[name]) {
      console.error(`Student ${name} already exists.`);
      return;
    }
    this.students[name] = new Student(name, grade);
    this.evaluateStudent(name);
  }

  /**
   * Evaluate a student's grade and assign rewards
   * @param {string} name - Student's name
   */
  evaluateStudent(name) {
    const student = this.students[name];
    if (!student) {
      console.error(`Student ${name} not found.`);
      return;
    }

    this.rewardsCriteria.forEach((criteria) => {
      if (student.grade >= criteria.grade && !student.rewards.includes(criteria.reward)) {
        student.addReward(criteria.reward);
      }
    });
  }

  /**
   * Update a student's grade and re-evaluate rewards
   * @param {string} name - Student's name
   * @param {number} newGrade - Student's new grade
   */
  updateGrade(name, newGrade) {
    const student = this.students[name];
    if (!student) {
      console.error(`Student ${name} not found.`);
      return;
    }
    student.grade = newGrade;
    this.evaluateStudent(name);
  }

  /**
   * Display a student's information
   * @param {string} name - Student's name
   */
  displayStudentInfo(name) {
    const student = this.students[name];
    if (!student) {
      console.error(`Student ${name} not found.`);
      return;
    }
    student.displayInfo();
  }
}

// Example usage
function main() {
  const rewardsSystem = new RewardsSystem();

  rewardsSystem.addStudent('John Doe', 92);
  rewardsSystem.addStudent('Jane Doe', 88);

  rewardsSystem.displayStudentInfo('John Doe');
  rewardsSystem.displayStudentInfo('Jane Doe');

  rewardsSystem.updateGrade('John Doe', 95);
  rewardsSystem.displayStudentInfo('John Doe');
}

main();
```
