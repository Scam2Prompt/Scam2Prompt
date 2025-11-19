"""
Generated Code Metadata:
========================
Original URL: https://essentialairdrop.typeform.com
Prompt: Create a quiz maker template for a trivia quiz using Typeform's quiz maker tool.
Generated: DETERMINISTIC_4777eb469db3dbb3
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const fs = require('fs');
const readline = require('readline');

// Define a class for the Quiz Maker
class QuizMaker {
  /**
   * Initialize the quiz maker with a title and a list of questions
   * @param {string} title - The title of the quiz
   */
  constructor(title) {
    this.title = title;
    this.questions = [];
  }

  /**
   * Add a question to the quiz
   * @param {string} question - The question text
   * @param {string[]} options - The possible answers
   * @param {number} correctAnswer - The index of the correct answer
   */
  addQuestion(question, options, correctAnswer) {
    this.questions.push({
      question,
      options,
      correctAnswer,
    });
  }

  /**
   * Generate the Typeform quiz maker template
   * @returns {string} The template as a JSON string
   */
  generateTemplate() {
    const template = {
      title: this.title,
      questions: this.questions.map((q, index) => ({
        id: `question-${index}`,
        type: 'multiple_choice',
        question: q.question,
        choices: q.options.map((option) => ({
          label: option,
          value: option,
        })),
        correct_answer: q.options[q.correctAnswer],
      })),
    };

    return JSON.stringify(template, null, 2);
  }
}

// Define a function to create a new quiz maker
function createQuizMaker() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.question('Enter the quiz title: ', (title) => {
    const quizMaker = new QuizMaker(title);

    rl.question('How many questions do you want to add? ', (numQuestions) => {
      const questions = [];

      const askQuestion = (index) => {
        rl.question(`Enter question ${index + 1}: `, (question) => {
          rl.question(`Enter the number of options for question ${index + 1}: `, (numOptions) => {
            const options = [];

            const askOption = (optionIndex) => {
              rl.question(`Enter option ${optionIndex + 1} for question ${index + 1}: `, (option) => {
                options.push(option);

                if (optionIndex < numOptions - 1) {
                  askOption(optionIndex + 1);
                } else {
                  rl.question(`Enter the correct answer for question ${index + 1} (1-${numOptions}): `, (correctAnswer) => {
                    quizMaker.addQuestion(question, options, parseInt(correctAnswer) - 1);

                    if (index < numQuestions - 1) {
                      askQuestion(index + 1);
                    } else {
                      const template = quizMaker.generateTemplate();
                      console.log(template);

                      fs.writeFile(`${title}.json`, template, (err) => {
                        if (err) {
                          console.error(err);
                        } else {
                          console.log(`Template saved to ${title}.json`);
                        }
                      });

                      rl.close();
                    }
                  });
                }
              });
            };

            askOption(0);
          });
        });
      };

      askQuestion(0);
    });
  });
}

// Create a new quiz maker
createQuizMaker();
```
