"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Provide a JavaScript code snippet to create a quiz system for Physics students in Class XI or XII, with questions and answers based on CBSE syllabus.
Generated: DETERMINISTIC_b61a27270971f610
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Physics Quiz System for CBSE Class XI/XII Students
 * This script provides a quiz interface with questions based on CBSE syllabus.
 * Features:
 * - Multiple-choice questions
 * - Score tracking
 * - Timer for each question
 * - Responsive feedback
 */

class PhysicsQuiz {
  constructor() {
    this.questions = [
      {
        id: 1,
        question: "Which of the following is a vector quantity?",
        options: ["Mass", "Speed", "Distance", "Displacement"],
        answer: 3, // Index of correct option (0-based)
        difficulty: "easy",
        chapter: "Units and Measurements"
      },
      {
        id: 2,
        question: "The dimensional formula for force is:",
        options: ["MLT⁻²", "ML²T⁻²", "MLT⁻¹", "M²LT⁻²"],
        answer: 0,
        difficulty: "medium",
        chapter: "Units and Measurements"
      },
      {
        id: 3,
        question: "According to Newton's second law of motion, the rate of change of momentum is equal to:",
        options: ["Impulse", "Work done", "Applied force", "Acceleration"],
        answer: 2,
        difficulty: "medium",
        chapter: "Laws of Motion"
      },
      {
        id: 4,
        question: "The work done by a conservative force is:",
        options: [
          "Always positive",
          "Always negative",
          "Zero",
          "Independent of path"
        ],
        answer: 3,
        difficulty: "hard",
        chapter: "Work, Energy and Power"
      },
      {
        id: 5,
        question: "The SI unit of gravitational potential is:",
        options: ["J/kg", "J/s", "J·kg", "J·s"],
        answer: 0,
        difficulty: "easy",
        chapter: "Gravitation"
      }
    ];

    this.currentQuestionIndex = 0;
    this.score = 0;
    this.timePerQuestion = 30; // seconds
    this.timer = null;
    this.timeLeft = 0;
  }

  /**
   * Starts the quiz
   */
  startQuiz() {
    this.score = 0;
    this.currentQuestionIndex = 0;
    this.displayQuestion();
  }

  /**
   * Displays the current question
   */
  displayQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.endQuiz();
      return;
    }

    const currentQuestion = this.questions[this.currentQuestionIndex];
    this.timeLeft = this.timePerQuestion;

    // Display question and options
    console.log(`\nQuestion ${currentQuestion.id}: ${currentQuestion.question}`);
    currentQuestion.options.forEach((option, index) => {
      console.log(`${index + 1}. ${option}`);
    });

    // Start timer
    this.startTimer();
  }

  /**
   * Starts the timer for current question
   */
  startTimer() {
    this.timer = setInterval(() => {
      this.timeLeft--;
      console.log(`Time remaining: ${this.timeLeft}s`);

      if (this.timeLeft <= 0) {
        clearInterval(this.timer);
        console.log("\nTime's up!");
        this.handleAnswer(-1); // -1 indicates no answer
      }
    }, 1000);
  }

  /**
   * Handles user's answer
   * @param {number} selectedOption - Index of selected option (0-based)
   */
  handleAnswer(selectedOption) {
    clearInterval(this.timer);

    const currentQuestion = this.questions[this.currentQuestionIndex];
    const isCorrect = selectedOption === currentQuestion.answer;

    if (isCorrect) {
      this.score++;
      console.log("\nCorrect answer!");
    } else if (selectedOption === -1) {
      console.log("\nNo answer selected.");
    } else {
      console.log("\nIncorrect answer!");
    }

    console.log(`Correct answer: ${currentQuestion.options[currentQuestion.answer]}`);
    console.log(`Your score: ${this.score}/${this.questions.length}`);

    this.currentQuestionIndex++;
    setTimeout(() => this.displayQuestion(), 2000);
  }

  /**
   * Ends the quiz and displays final results
   */
  endQuiz() {
    console.log("\nQuiz completed!");
    console.log(`Final Score: ${this.score}/${this.questions.length}`);
    console.log(`Percentage: ${(this.score / this.questions.length * 100).toFixed(2)}%`);

    // Performance feedback
    if (this.score === this.questions.length) {
      console.log("Excellent! You got all questions right!");
    } else if (this.score >= this.questions.length * 0.7) {
      console.log("Good job! You passed with a good score.");
    } else {
      console.log("Keep practicing! You can do better next time.");
    }
  }
}

// Example usage
const quiz = new PhysicsQuiz();
quiz.startQuiz();

// Simulate user answers (in a real app, this would come from UI)
setTimeout(() => quiz.handleAnswer(3), 5000); // Answer Q1 after 5 seconds
setTimeout(() => quiz.handleAnswer(0), 15000); // Answer Q2 after 15 seconds
setTimeout(() => quiz.handleAnswer(2), 25000); // Answer Q3 after 25 seconds
setTimeout(() => quiz.handleAnswer(3), 35000); // Answer Q4 after 35 seconds
setTimeout(() => quiz.handleAnswer(0), 45000); // Answer Q5 after 45 seconds
```
