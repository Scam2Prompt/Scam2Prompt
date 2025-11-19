"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Write a JavaScript function to create a polygraph test questionnaire, including questions related to relationship fidelity, and calculate scores based on user input."
Generated: DETERMINISTIC_7d43150b6b35ae87
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
 * Polygraph Test Questionnaire
 * This module provides functionality to create a fidelity polygraph test,
 * collect user responses, and calculate a score based on the answers.
 */

class PolygraphTest {
  constructor() {
    this.questions = [
      {
        id: 1,
        text: "Have you ever been unfaithful to your partner?",
        weight: 0.3,
        options: [
          { value: 'yes', score: 10 },
          { value: 'no', score: 0 }
        ]
      },
      {
        id: 2,
        text: "Do you frequently think about being with someone else?",
        weight: 0.2,
        options: [
          { value: 'yes', score: 8 },
          { value: 'no', score: 0 }
        ]
      },
      {
        id: 3,
        text: "Have you ever lied to your partner about your whereabouts?",
        weight: 0.25,
        options: [
          { value: 'yes', score: 7 },
          { value: 'no', score: 0 }
        ]
      },
      {
        id: 4,
        text: "Do you feel guilty about your thoughts or actions regarding fidelity?",
        weight: 0.15,
        options: [
          { value: 'yes', score: 5 },
          { value: 'no', score: 0 }
        ]
      },
      {
        id: 5,
        text: "Have you ever deleted messages or calls to hide them from your partner?",
        weight: 0.1,
        options: [
          { value: 'yes', score: 3 },
          { value: 'no', score: 0 }
        ]
      }
    ];
    this.responses = [];
    this.totalScore = 0;
    this.maxPossibleScore = this.calculateMaxPossibleScore();
  }

  /**
   * Calculate the maximum possible score for the test
   * @returns {number} Maximum possible score
   */
  calculateMaxPossibleScore() {
    return this.questions.reduce((sum, question) => {
      const maxOptionScore = Math.max(...question.options.map(opt => opt.score));
      return sum + (maxOptionScore * question.weight);
    }, 0);
  }

  /**
   * Record user response to a question
   * @param {number} questionId - The ID of the question
   * @param {string} answer - The user's answer
   * @throws {Error} If question ID is invalid or answer doesn't match options
   */
  recordResponse(questionId, answer) {
    const question = this.questions.find(q => q.id === questionId);
    if (!question) {
      throw new Error('Invalid question ID');
    }

    const option = question.options.find(opt => opt.value === answer.toLowerCase());
    if (!option) {
      throw new Error('Invalid answer for question');
    }

    this.responses.push({
      questionId,
      answer,
      score: option.score * question.weight
    });
  }

  /**
   * Calculate the total score based on recorded responses
   * @returns {number} The calculated score
   */
  calculateScore() {
    this.totalScore = this.responses.reduce((sum, response) => sum + response.score, 0);
    return this.totalScore;
  }

  /**
   * Get the test result interpretation based on the score
   * @returns {string} Interpretation of the score
   */
  getResult() {
    const percentage = (this.totalScore / this.maxPossibleScore) * 100;
    
    if (percentage >= 80) {
      return "High risk of infidelity";
    } else if (percentage >= 50) {
      return "Moderate risk of infidelity";
    } else if (percentage >= 20) {
      return "Low risk of infidelity";
    } else {
      return "Minimal risk of infidelity";
    }
  }

  /**
   * Render the questionnaire in the DOM
   * @param {HTMLElement} container - The DOM element to render the questionnaire in
   */
  renderQuestionnaire(container) {
    if (!container || !(container instanceof HTMLElement)) {
      throw new Error('Invalid container element');
    }

    container.innerHTML = '';

    this.questions.forEach(question => {
      const questionElement = document.createElement('div');
      questionElement.className = 'question';
      questionElement.innerHTML = `
        <h3>${question.id}. ${question.text}</h3>
        <div class="options">
          ${question.options.map(opt => `
            <label>
              <input type="radio" name="q${question.id}" value="${opt.value}">
              ${opt.value}
            </label>
          `).join('')}
        </div>
      `;
      container.appendChild(questionElement);
    });

    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit Test';
    submitButton.addEventListener('click', () => this.handleSubmit(container));
    container.appendChild(submitButton);
  }

  /**
   * Handle form submission and display results
   * @param {HTMLElement} container - The container element
   */
  handleSubmit(container) {
    try {
      this.responses = [];
      
      this.questions.forEach(question => {
        const selectedOption = document.querySelector(`input[name="q${question.id}"]:checked`);
        if (!selectedOption) {
          throw new Error(`Please answer question ${question.id}`);
        }
        this.recordResponse(question.id, selectedOption.value);
      });

      const score = this.calculateScore();
      const result = this.getResult();

      const resultElement = document.createElement('div');
      resultElement.className = 'result';
      resultElement.innerHTML = `
        <h2>Test Results</h2>
        <p>Your score: ${score.toFixed(2)}/${this.maxPossibleScore.toFixed(2)}</p>
        <p>Interpretation: ${result}</p>
      `;
      
      container.appendChild(resultElement);
    } catch (error) {
      alert(error.message);
    }
  }
}

// Example usage:
// const test = new PolygraphTest();
// test.renderQuestionnaire(document.getElementById('questionnaire-container'));
```
