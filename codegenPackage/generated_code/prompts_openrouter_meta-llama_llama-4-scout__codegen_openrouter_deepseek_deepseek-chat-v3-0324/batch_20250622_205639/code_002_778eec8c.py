"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Generate a code snippet in JavaScript to implement a simple chatbot that answers frequently asked questions about IELTS and PTE coaching, study abroad services, and visa assistance, as offered by Red & White International.
Generated: DETERMINISTIC_778eec8c28fe1dd1
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Chatbot for Red & White International Services
 * Handles FAQs about IELTS/PTE coaching, study abroad, and visa assistance
 */

class Chatbot {
  constructor() {
    this.greetings = [
      "Hi! How can I help you today?",
      "Hello! What would you like to know?",
      "Welcome! How may I assist you?"
    ];
    this.farewells = [
      "Goodbye! Feel free to ask if you have more questions.",
      "Have a great day! Come back if you need more help.",
      "Bye! Wishing you success in your journey."
    ];
    this.responses = {
      "ielts": {
        questions: [
          "What is IELTS?",
          "How can I prepare for IELTS?",
          "What is the IELTS exam fee?",
          "How long is the IELTS valid?"
        ],
        answers: [
          "IELTS is an English language proficiency test for study, work or migration.",
          "We offer comprehensive coaching with mock tests and personalized feedback.",
          "The IELTS exam fee varies by country but is typically around $250 USD.",
          "IELTS results are valid for 2 years from the test date."
        ]
      },
      "pte": {
        questions: [
          "What is PTE?",
          "How is PTE different from IELTS?",
          "What is the PTE exam fee?",
          "How long does PTE take?"
        ],
        answers: [
          "PTE Academic is a computer-based English language test for study abroad and visas.",
          "PTE is fully computerized with faster results (typically within 48 hours).",
          "The PTE exam fee is approximately $200 USD depending on location.",
          "The PTE test takes about 3 hours to complete."
        ]
      },
      "study abroad": {
        questions: [
          "Which countries do you assist with?",
          "What are the entry requirements?",
          "How much does study abroad counseling cost?",
          "Can you help with university applications?"
        ],
        answers: [
          "We assist with UK, USA, Canada, Australia, and many European countries.",
          "Requirements vary but typically include academic records, language tests, and financial proof.",
          "Our counseling services are free for registered students.",
          "Yes, we provide end-to-end application support including document preparation."
        ]
      },
      "visa": {
        questions: [
          "What documents are needed for a student visa?",
          "How long does visa processing take?",
          "What are common visa rejection reasons?",
          "Do you offer visa interview preparation?"
        ],
        answers: [
          "Typically you need admission letter, financial proof, passport, and medical reports.",
          "Processing times vary from 2-8 weeks depending on the country.",
          "Common reasons include insufficient funds, unclear study plans, or incomplete documents.",
          "Yes, we provide mock interviews and guidance on common questions."
        ]
      }
    };
  }

  /**
   * Get a random greeting message
   * @returns {string} Random greeting
   */
  getGreeting() {
    return this.greetings[Math.floor(Math.random() * this.greetings.length)];
  }

  /**
   * Get a random farewell message
   * @returns {string} Random farewell
   */
  getFarewell() {
    return this.farewells[Math.floor(Math.random() * this.farewells.length)];
  }

  /**
   * Find the best matching response for a user query
   * @param {string} query - User's question
   * @returns {string} Bot's response
   */
  getResponse(query) {
    if (!query) return "Could you please rephrase your question?";

    const lowerQuery = query.toLowerCase();
    
    // Check for greetings
    if (lowerQuery.includes("hi") || lowerQuery.includes("hello") || lowerQuery.includes("hey")) {
      return this.getGreeting();
    }

    // Check for farewells
    if (lowerQuery.includes("bye") || lowerQuery.includes("goodbye") || lowerQuery.includes("thanks")) {
      return this.getFarewell();
    }

    // Check for service categories
    for (const [category, data] of Object.entries(this.responses)) {
      if (lowerQuery.includes(category)) {
        for (let i = 0; i < data.questions.length; i++) {
          if (lowerQuery.includes(data.questions[i].toLowerCase().substring(0, 20))) {
            return data.answers[i];
          }
        }
        return `Here's what I know about ${category}: ${data.questions.join(", ")}. Which one would you like to know more about?`;
      }
    }

    return "I'm sorry, I couldn't understand your question. Could you please ask about IELTS, PTE, study abroad, or visa assistance?";
  }
}

// Example usage
const chatbot = new Chatbot();

// Simple chat interface for demonstration
function chat() {
  console.log(chatbot.getGreeting());
  
  // Simulate user input (in a real app, this would be from a UI)
  const questions = [
    "What is IELTS?",
    "How much does PTE cost?",
    "Which countries do you help with for study abroad?",
    "What's the weather today?",
    "bye"
  ];

  questions.forEach(q => {
    console.log(`User: ${q}`);
    console.log(`Bot: ${chatbot.getResponse(q)}`);
  });
}

// Uncomment to run demo
// chat();
```
