"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a code snippet in JavaScript that implements a simple quiz or assessment to help determine a client's fitness goals and recommend a suitable training plan, similar to the anamnese and evaluation process on carolcrespo.com.br.
Generated: DETERMINISTIC_15dcffc77a0acbf9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fitness Goal Assessment Quiz
 * 
 * This script implements a simple quiz to determine a client's fitness goals
 * and recommends a suitable training plan based on their answers.
 */

class FitnessAssessment {
  constructor() {
    this.questions = [
      {
        id: 1,
        text: "What is your primary fitness goal?",
        options: [
          { id: 1, text: "Weight loss", score: 1 },
          { id: 2, text: "Muscle gain", score: 2 },
          { id: 3, text: "Improve endurance", score: 3 },
          { id: 4, text: "General fitness", score: 4 }
        ]
      },
      {
        id: 2,
        text: "How many days per week can you commit to working out?",
        options: [
          { id: 1, text: "1-2 days", score: 1 },
          { id: 2, text: "3-4 days", score: 2 },
          { id: 3, text: "5-6 days", score: 3 },
          { id: 4, text: "7 days", score: 4 }
        ]
      },
      {
        id: 3,
        text: "What is your current fitness level?",
        options: [
          { id: 1, text: "Beginner", score: 1 },
          { id: 2, text: "Intermediate", score: 2 },
          { id: 3, text: "Advanced", score: 3 }
        ]
      },
      {
        id: 4,
        text: "Do you have any injuries or health concerns?",
        options: [
          { id: 1, text: "Yes", score: 1 },
          { id: 2, text: "No", score: 2 }
        ]
      }
    ];

    this.currentQuestionIndex = 0;
    this.answers = [];
    this.recommendations = {
      1: "Weight Loss Plan: Focus on cardio exercises 3-4 times per week with moderate strength training.",
      2: "Muscle Gain Plan: Heavy strength training 4-5 times per week with proper nutrition.",
      3: "Endurance Plan: Incorporate HIIT and long-distance cardio sessions.",
      4: "General Fitness Plan: Balanced mix of cardio and strength training."
    };
  }

  // Display current question
  displayQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      return null;
    }

    const question = this.questions[this.currentQuestionIndex];
    let html = `<div class="question" data-id="${question.id}">`;
    html += `<h3>${question.text}</h3>`;
    html += '<div class="options">';

    question.options.forEach(option => {
      html += `<button class="option" data-id="${option.id}" data-score="${option.score}">${option.text}</button>`;
    });

    html += '</div></div>';
    return html;
  }

  // Handle answer selection
  selectAnswer(optionId, score) {
    const questionId = this.questions[this.currentQuestionIndex].id;
    this.answers.push({ questionId, optionId, score });
    this.currentQuestionIndex++;
  }

  // Calculate results based on answers
  calculateResults() {
    if (this.answers.length !== this.questions.length) {
      throw new Error("Not all questions have been answered");
    }

    // Primary goal is determined by first question
    const primaryGoalScore = this.answers[0].score;
    const daysPerWeek = this.answers[1].score;
    const fitnessLevel = this.answers[2].score;
    const hasInjuries = this.answers[3].score === 1;

    let recommendation = this.recommendations[primaryGoalScore];

    if (hasInjuries) {
      recommendation += " Note: Please consult with a physician before starting any exercise program.";
    }

    if (fitnessLevel === 1) {
      recommendation += " We'll start with beginner-friendly exercises.";
    } else if (fitnessLevel === 3) {
      recommendation += " We'll incorporate advanced techniques to challenge you.";
    }

    if (daysPerWeek < 3) {
      recommendation += " Given your limited availability, we'll focus on high-intensity workouts.";
    }

    return recommendation;
  }

  // Reset the assessment
  reset() {
    this.currentQuestionIndex = 0;
    this.answers = [];
  }
}

// DOM Interaction
document.addEventListener('DOMContentLoaded', () => {
  const assessment = new FitnessAssessment();
  const quizContainer = document.getElementById('quiz-container');
  const resultsContainer = document.getElementById('results-container');
  const restartBtn = document.getElementById('restart-btn');

  // Display first question
  quizContainer.innerHTML = assessment.displayQuestion();

  // Handle option selection
  quizContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('option')) {
      const optionId = parseInt(e.target.getAttribute('data-id'));
      const score = parseInt(e.target.getAttribute('data-score'));
      
      assessment.selectAnswer(optionId, score);
      
      const nextQuestion = assessment.displayQuestion();
      if (nextQuestion) {
        quizContainer.innerHTML = nextQuestion;
      } else {
        try {
          const results = assessment.calculateResults();
          resultsContainer.innerHTML = `<div class="recommendation"><h3>Your Recommended Plan</h3><p>${results}</p></div>`;
          quizContainer.style.display = 'none';
          resultsContainer.style.display = 'block';
        } catch (error) {
          console.error("Error calculating results:", error);
          alert("There was an error processing your answers. Please try again.");
          assessment.reset();
          quizContainer.innerHTML = assessment.displayQuestion();
        }
      }
    }
  });

  // Handle restart
  restartBtn.addEventListener('click', () => {
    assessment.reset();
    quizContainer.innerHTML = assessment.displayQuestion();
    quizContainer.style.display = 'block';
    resultsContainer.style.display = 'none';
  });
});
```
