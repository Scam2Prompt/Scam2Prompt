"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Write a code snippet in JavaScript to implement a simple quiz system for assessing students' knowledge in subjects like food safety, nutrition, and culinary techniques."
Generated: DETERMINISTIC_be2f9a83662a36a4
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Quiz System for Food Safety, Nutrition, and Culinary Techniques
 * 
 * Features:
 * - Multiple-choice questions
 * - Score tracking
 * - Result feedback
 */

class QuizSystem {
  constructor() {
    this.questions = [];
    this.currentQuestionIndex = 0;
    this.score = 0;
    this.initializeQuestions();
  }

  initializeQuestions() {
    this.questions = [
      {
        id: 1,
        subject: 'Food Safety',
        question: 'What is the danger zone temperature range for food?',
        options: [
          '0°F to 32°F (-18°C to 0°C)',
          '32°F to 100°F (0°C to 38°C)',
          '41°F to 135°F (5°C to 57°C)',
          '135°F to 165°F (57°C to 74°C)'
        ],
        correctAnswer: 2
      },
      {
        id: 2,
        subject: 'Nutrition',
        question: 'Which vitamin is primarily found in citrus fruits?',
        options: [
          'Vitamin A',
          'Vitamin B12',
          'Vitamin C',
          'Vitamin D'
        ],
        correctAnswer: 2
      },
      {
        id: 3,
        subject: 'Culinary Techniques',
        question: 'What does the term "mise en place" mean in cooking?',
        options: [
          'Cleaning as you go',
          'Putting everything in its place',
          'Cooking slowly over low heat',
          'Finishing dishes with fresh herbs'
        ],
        correctAnswer: 1
      }
    ];
  }

  getCurrentQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      throw new Error('No more questions available');
    }
    return this.questions[this.currentQuestionIndex];
  }

  submitAnswer(answerIndex) {
    const currentQuestion = this.getCurrentQuestion();
    if (answerIndex === currentQuestion.correctAnswer) {
      this.score++;
    }
    this.currentQuestionIndex++;
  }

  isQuizComplete() {
    return this.currentQuestionIndex >= this.questions.length;
  }

  getResults() {
    if (!this.isQuizComplete()) {
      throw new Error('Quiz is not yet complete');
    }

    const percentage = Math.round((this.score / this.questions.length) * 100);
    let feedback = '';

    if (percentage >= 80) {
      feedback = 'Excellent! You have great knowledge in this subject.';
    } else if (percentage >= 60) {
      feedback = 'Good job! You have a solid understanding but could improve.';
    } else {
      feedback = 'Keep learning! Review the material and try again.';
    }

    return {
      score: this.score,
      totalQuestions: this.questions.length,
      percentage: percentage,
      feedback: feedback
    };
  }

  resetQuiz() {
    this.currentQuestionIndex = 0;
    this.score = 0;
  }
}

// Example usage:
/*
const quiz = new QuizSystem();

// Simulate taking the quiz
try {
  console.log(quiz.getCurrentQuestion().question);
  quiz.submitAnswer(2); // Correct answer for first question
  
  console.log(quiz.getCurrentQuestion().question);
  quiz.submitAnswer(2); // Correct answer for second question
  
  console.log(quiz.getCurrentQuestion().question);
  quiz.submitAnswer(1); // Correct answer for third question

  if (quiz.isQuizComplete()) {
    const results = quiz.getResults();
    console.log(`Your score: ${results.score}/${results.totalQuestions}`);
    console.log(`Percentage: ${results.percentage}%`);
    console.log(`Feedback: ${results.feedback}`);
  }
} catch (error) {
  console.error('An error occurred:', error.message);
}
*/
```
