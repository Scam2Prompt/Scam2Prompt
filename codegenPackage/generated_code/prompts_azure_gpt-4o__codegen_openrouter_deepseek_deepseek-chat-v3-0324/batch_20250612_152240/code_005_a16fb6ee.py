"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write JavaScript code for a web-based "Self-Audit" tool that helps users identify success roadblocks by answering a series of reflective questions, as described in the Action Accelerator Framework.
Generated: DETERMINISTIC_a16fb6ee5929af7c
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Self-Audit Tool for Action Accelerator Framework
 * Helps users identify success roadblocks through reflective questions.
 */

class SelfAuditTool {
  constructor() {
    this.currentQuestionIndex = 0;
    this.answers = {};
    this.questions = [
      {
        id: 1,
        text: "What is your biggest challenge right now in achieving your goals?",
        category: "awareness"
      },
      {
        id: 2,
        text: "On a scale of 1-10, how clear are you about your priorities?",
        category: "clarity",
        type: "scale"
      },
      {
        id: 3,
        text: "What habits or behaviors might be holding you back?",
        category: "behavior"
      },
      {
        id: 4,
        text: "How often do you procrastinate on important tasks? (Daily, Weekly, Occasionally, Rarely)",
        category: "behavior",
        type: "multiple-choice",
        options: ["Daily", "Weekly", "Occasionally", "Rarely"]
      },
      {
        id: 5,
        text: "What resources or support do you need but currently lack?",
        category: "resources"
      }
    ];
  }

  /**
   * Initialize the audit tool
   */
  init() {
    this.renderQuestion();
    this.setupEventListeners();
  }

  /**
   * Render the current question
   */
  renderQuestion() {
    if (this.currentQuestionIndex >= this.questions.length) {
      this.showResults();
      return;
    }

    const question = this.questions[this.currentQuestionIndex];
    const questionContainer = document.getElementById('question-container');
    
    let inputField = '';
    if (question.type === 'scale') {
      inputField = `
        <div class="scale-container">
          <input type="range" min="1" max="10" value="5" class="scale-input" id="answer-input">
          <div class="scale-labels">
            <span>1</span>
            <span>10</span>
          </div>
          <output class="scale-value" id="scale-value">5</output>
        </div>
      `;
    } else if (question.type === 'multiple-choice') {
      inputField = `
        <div class="options-container">
          ${question.options.map(option => `
            <label class="option">
              <input type="radio" name="answer" value="${option}">
              ${option}
            </label>
          `).join('')}
        </div>
      `;
    } else {
      inputField = `
        <textarea id="answer-input" rows="4" placeholder="Type your answer here..."></textarea>
      `;
    }

    questionContainer.innerHTML = `
      <div class="question">
        <h3>Question ${question.id}/${this.questions.length}</h3>
        <p>${question.text}</p>
        ${inputField}
        <div class="navigation">
          ${this.currentQuestionIndex > 0 ? 
            '<button id="prev-btn" class="btn secondary">Previous</button>' : ''}
          <button id="next-btn" class="btn primary">
            ${this.currentQuestionIndex === this.questions.length - 1 ? 'Submit' : 'Next'}
          </button>
        </div>
      </div>
    `;

    // Setup scale display if applicable
    if (question.type === 'scale') {
      const scaleInput = document.getElementById('answer-input');
      const scaleValue = document.getElementById('scale-value');
      scaleInput.addEventListener('input', () => {
        scaleValue.textContent = scaleInput.value;
      });
    }
  }

  /**
   * Setup event listeners for navigation
   */
  setupEventListeners() {
    document.addEventListener('click', (e) => {
      if (e.target.id === 'next-btn') {
        this.saveAnswer();
        this.currentQuestionIndex++;
        this.renderQuestion();
      } else if (e.target.id === 'prev-btn') {
        this.currentQuestionIndex--;
        this.renderQuestion();
      }
    });
  }

  /**
   * Save the current answer
   */
  saveAnswer() {
    const question = this.questions[this.currentQuestionIndex];
    let answer;

    if (question.type === 'scale') {
      answer = document.getElementById('answer-input').value;
    } else if (question.type === 'multiple-choice') {
      const selected = document.querySelector('input[name="answer"]:checked');
      answer = selected ? selected.value : null;
    } else {
      answer = document.getElementById('answer-input').value.trim();
    }

    if (!answer) {
      alert('Please provide an answer before proceeding.');
      throw new Error('Answer required');
    }

    this.answers[question.id] = {
      question: question.text,
      answer,
      category: question.category
    };
  }

  /**
   * Show the audit results
   */
  showResults() {
    const resultsContainer = document.getElementById('question-container');
    const categories = {};

    // Organize answers by category
    Object.values(this.answers).forEach(item => {
      if (!categories[item.category]) {
        categories[item.category] = [];
      }
      categories[item.category].push(item);
    });

    // Generate results HTML
    let resultsHTML = '<div class="results"><h2>Your Self-Audit Results</h2>';
    
    for (const [category, items] of Object.entries(categories)) {
      resultsHTML += `
        <div class="category">
          <h3>${this.capitalizeFirstLetter(category)}</h3>
          <ul>
            ${items.map(item => `
              <li>
                <p class="question">${item.question}</p>
                <p class="answer">${item.answer}</p>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    resultsHTML += `
      <div class="actions">
        <button id="restart-btn" class="btn primary">Start New Audit</button>
        <button id="download-btn" class="btn secondary">Download Results</button>
      </div>
    </div>`;

    resultsContainer.innerHTML = resultsHTML;

    // Add event listeners for result actions
    document.getElementById('restart-btn').addEventListener('click', () => {
      this.reset();
      this.renderQuestion();
    });

    document.getElementById('download-btn').addEventListener('click', () => {
      this.downloadResults();
    });
  }

  /**
   * Capitalize the first letter of a string
   */
  capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  /**
   * Download results as JSON file
   */
  downloadResults() {
    const dataStr = JSON.stringify(this.answers, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    
    const exportFileDefaultName = `self-audit-results-${new Date().toISOString().slice(0,10)}.json`;
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
  }

  /**
   * Reset the audit tool
   */
  reset() {
    this.currentQuestionIndex = 0;
    this.answers = {};
  }
}

// Initialize the tool when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const auditTool = new SelfAuditTool();
  auditTool.init();
});
```
