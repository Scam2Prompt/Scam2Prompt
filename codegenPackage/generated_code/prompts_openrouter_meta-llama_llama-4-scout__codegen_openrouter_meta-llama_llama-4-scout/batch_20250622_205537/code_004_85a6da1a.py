"""
Generated Code Metadata:
========================
Original URL: https://airdropform900.typeform.com
Prompt: Create a Typeform quiz template for lead generation, using conditional logic and scoring.
Generated: DETERMINISTIC_85a6da1aec00874b
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Typeform Quiz Template for Lead Generation

// Define the quiz structure
const quizTemplate = {
  "title": "Lead Generation Quiz",
  "description": "Find out how our product can help you",
  "questions": [
    {
      "id": "question1",
      "type": "multiple_choice",
      "ref": "question1",
      "title": "What is your biggest challenge?",
      "description": "",
      "choices": [
        {
          "label": "Lead generation",
          "value": "lead_generation"
        },
        {
          "label": "Conversion optimization",
          "value": "conversion_optimization"
        },
        {
          "label": "Other",
          "value": "other"
        }
      ],
      "validation": {
        "required": true
      }
    },
    {
      "id": "question2",
      "type": "multiple_choice",
      "ref": "question2",
      "title": "How many leads do you generate per month?",
      "description": "",
      "choices": [
        {
          "label": "< 100",
          "value": "<100"
        },
        {
          "label": "100-500",
          "value": "100-500"
        },
        {
          "label": "> 500",
          "value": ">500"
        }
      ],
      "validation": {
        "required": true
      },
      "conditional_logic": {
        "rules": [
          {
            "id": "rule1",
            "question_id": "question1",
            "condition": "equals",
            "value": "lead_generation",
            "action": {
              "type": "show",
              "question_id": "question3"
            }
          }
        ]
      }
    },
    {
      "id": "question3",
      "type": "multiple_choice",
      "ref": "question3",
      "title": "What is your current lead generation strategy?",
      "description": "",
      "choices": [
        {
          "label": "Content marketing",
          "value": "content_marketing"
        },
        {
          "label": "Paid advertising",
          "value": "paid_advertising"
        },
        {
          "label": "Referrals",
          "value": "referrals"
        }
      ],
      "validation": {
        "required": true
      },
      "conditional_logic": {
        "rules": [
          {
            "id": "rule2",
            "question_id": "question2",
            "condition": "equals",
            "value": ">500",
            "action": {
              "type": "show",
              "question_id": "question4"
            }
          }
        ]
      }
    },
    {
      "id": "question4",
      "type": "short_text",
      "ref": "question4",
      "title": "Tell us about your current pain points",
      "description": "",
      "validation": {
        "required": true
      }
    },
    {
      "id": "score",
      "type": "summary",
      "ref": "score",
      "title": "Your Score: {{score}}",
      "description": "",
      "score": {
        "type": "calculated",
        "calculation": {
          "question_id": "question1",
          "operator": "equals",
          "value": "lead_generation",
          "score": 10
        }
      }
    }
  ],
  "thankyou": {
    "title": "Thanks for taking our quiz!",
    "description": "We'll be in touch soon to discuss how our product can help you"
  }
};

// Define a function to calculate the score
function calculateScore(answers) {
  let score = 0;
  answers.forEach((answer) => {
    if (answer.question_id === 'question1' && answer.value === 'lead_generation') {
      score += 10;
    }
    if (answer.question_id === 'question2' && answer.value === '>500') {
      score += 20;
    }
    if (answer.question_id === 'question3' && answer.value === 'content_marketing') {
      score += 30;
    }
  });
  return score;
}

// Define a function to generate the quiz
function generateQuiz() {
  try {
    // Initialize the quiz template
    const quiz = { ...quizTemplate };

    // Calculate the score
    const score = calculateScore([
      { question_id: 'question1', value: 'lead_generation' },
      { question_id: 'question2', value: '>500' },
      { question_id: 'question3', value: 'content_marketing' }
    ]);

    // Update the score question
    quiz.questions[quiz.questions.length - 1].score.calculation.score = score;

    // Return the quiz
    return quiz;
  } catch (error) {
    console.error(error);
    return null;
  }
}

// Generate and print the quiz
const quiz = generateQuiz();
console.log(quiz);
```
