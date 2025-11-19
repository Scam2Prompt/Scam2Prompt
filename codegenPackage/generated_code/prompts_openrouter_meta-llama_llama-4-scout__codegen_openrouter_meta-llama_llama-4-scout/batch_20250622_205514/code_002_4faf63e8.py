"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Generate a code snippet in JavaScript to create a simple chatbot that provides information on hypertension, its risks, and management strategies, based on the content available on Payidar Evde Sağlık Hizmetleri website.
Generated: DETERMINISTIC_4faf63e86dc13c14
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const readline = require('readline');

// Define a class for the chatbot
class HypertensionChatbot {
  /**
   * Constructor to initialize the chatbot's knowledge base
   */
  constructor() {
    // Knowledge base for hypertension
    this.knowledgeBase = {
      definition: 'Hypertension, also known as high blood pressure, is a condition in which the blood pressure in the arteries is persistently elevated.',
      risks: [
        'Increased risk of heart disease and stroke',
        'Kidney disease and kidney failure',
        'Vision loss and blindness',
        'Cognitive impairment and dementia'
      ],
      managementStrategies: [
        'Regular exercise, such as walking or jogging',
        'Healthy diet, low in salt and sugar',
        'Stress management techniques, such as meditation or deep breathing',
        'Monitoring and managing stress'
      ]
    };
  }

  /**
   * Method to provide information on hypertension
   * @param {string} topic - The topic of interest (definition, risks, management)
   * @returns {string} The relevant information
   */
  getInformation(topic) {
    switch (topic) {
      case 'definition':
        return this.knowledgeBase.definition;
      case 'risks':
        return this.knowledgeBase.risks.join('\n');
      case 'management':
      case 'management strategies':
        return this.knowledgeBase.managementStrategies.join('\n');
      default:
        return 'Sorry, I did not understand your request. Please try again.';
    }
  }
}

// Create a new chatbot instance
const chatbot = new HypertensionChatbot();

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to start the chatbot
function startChatbot() {
  console.log('Welcome to the Hypertension Chatbot!');
  console.log('Type "quit" to exit.');

  // Recursive function to handle user input
  function handleInput() {
    rl.question('What would you like to know about hypertension? (definition, risks, management strategies) ', (input) => {
      if (input.toLowerCase() === 'quit') {
        console.log('Goodbye!');
        rl.close();
      } else {
        const response = chatbot.getInformation(input.toLowerCase());
        console.log(response);
        handleInput();
      }
    });
  }

  handleInput();
}

// Start the chatbot
startChatbot();
```
