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
// Define a class for the chatbot
class Chatbot {
  /**
   * Constructor to initialize the chatbot's knowledge base
   */
  constructor() {
    // Knowledge base for IELTS and PTE coaching
    this.ieltsPteCoaching = {
      "What is IELTS?": "IELTS (International English Language Testing System) is an English proficiency test required for admission to universities in English-speaking countries.",
      "What is PTE?": "PTE (Pearson Test of English) is another English proficiency test accepted by universities in English-speaking countries.",
      "How can I prepare for IELTS?": "You can prepare for IELTS by practicing with sample questions, taking a preparation course, or using online resources.",
    };

    // Knowledge base for study abroad services
    this.studyAbroadServices = {
      "How can I study abroad?": "To study abroad, you need to research universities, apply for admission, obtain a student visa, and arrange for accommodation and living expenses.",
      "What are the requirements for studying abroad?": "The requirements for studying abroad typically include English proficiency test scores (IELTS or PTE), academic transcripts, letters of recommendation, and a statement of purpose.",
    };

    // Knowledge base for visa assistance
    this.visaAssistance = {
      "How do I apply for a student visa?": "To apply for a student visa, you need to submit an application to the relevant embassy or consulate, providing required documents such as your passport, visa application form, and proof of financial support.",
      "What documents are required for a student visa?": "The required documents for a student visa typically include your passport, visa application form, proof of financial support, and academic documents.",
    };
  }

  /**
   * Method to handle user queries
   * @param {string} query - The user's question
   * @returns {string} The chatbot's response
   */
  respond(query) {
    // Convert query to lowercase for case-insensitive matching
    query = query.toLowerCase();

    // Check if the query matches a coaching-related question
    for (const question in this.ieltsPteCoaching) {
      if (query.includes(question.toLowerCase())) {
        return this.ieltsPteCoaching[question];
      }
    }

    // Check if the query matches a study abroad services-related question
    for (const question in this.studyAbroadServices) {
      if (query.includes(question.toLowerCase())) {
        return this.studyAbroadServices[question];
      }
    }

    // Check if the query matches a visa assistance-related question
    for (const question in this.visaAssistance) {
      if (query.includes(question.toLowerCase())) {
        return this.visaAssistance[question];
      }
    }

    // Default response if no match is found
    return "Sorry, I didn't understand your question. Please try rephrasing it or ask a different question.";
  }
}

// Create a new chatbot instance
const chatbot = new Chatbot();

// Example usage:
function main() {
  try {
    // Test the chatbot with some sample queries
    const queries = [
      "What is IELTS?",
      "How can I study abroad?",
      "What documents are required for a student visa?",
      "Invalid query to test default response",
    ];

    queries.forEach((query) => {
      console.log(`User: ${query}`);
      console.log(`Chatbot: ${chatbot.respond(query)}`);
      console.log(); // Empty line for readability
    });
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
