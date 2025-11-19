"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Develop a simple chatbot script in JavaScript to handle customer inquiries and feedback for a restaurant, inspired by the contact and feedback forms on Restaurante y Coffee Shop San Carlos's website.
Generated: DETERMINISTIC_9be6ef8a9fb28de5
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.example.com/sancarlos": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Restaurant Chatbot Script
// Handles customer inquiries and feedback for a restaurant

class RestaurantChatbot {
  constructor() {
    this.responses = {
      greetings: [
        "Hello! Welcome to San Carlos Restaurant. How can I help you today?",
        "Hi there! Thanks for reaching out to San Carlos Restaurant. What can I do for you?",
        "Welcome! You've reached San Carlos Restaurant. How may I assist you?"
      ],
      menu: "Our menu includes a variety of dishes including seafood, steaks, and local specialties. You can view our full menu on our website.",
      hours: "We're open:\nMonday-Friday: 11am-10pm\nSaturday-Sunday: 10am-11pm",
      location: "We're located at 123 Main Street, San Carlos. Here's a link to our location: https://maps.example.com/sancarlos",
      reservation: "To make a reservation, please call us at (555) 123-4567 or book online through our website.",
      feedback: {
        positive: "Thank you for your positive feedback! We're glad you enjoyed your experience.",
        negative: "We're sorry to hear about your experience. Please email us at feedback@sancarlos.com so we can address your concerns.",
        neutral: "Thank you for your feedback. We appreciate all comments to help us improve."
      },
      fallback: "I'm sorry, I didn't understand that. Could you rephrase or ask about our menu, hours, location, reservations, or provide feedback?"
    };
  }

  // Process user input and return appropriate response
  processInput(input) {
    if (!input || typeof input !== 'string') {
      return "Please provide a valid message.";
    }

    const lowerInput = input.toLowerCase().trim();

    // Check for greetings
    if (this.isGreeting(lowerInput)) {
      return this.getRandomResponse(this.responses.greetings);
    }

    // Handle specific inquiries
    if (lowerInput.includes('menu') || lowerInput.includes('food') || lowerInput.includes('dish')) {
      return this.responses.menu;
    }

    if (lowerInput.includes('hour') || lowerInput.includes('open') || lowerInput.includes('close')) {
      return this.responses.hours;
    }

    if (lowerInput.includes('location') || lowerInput.includes('address') || lowerInput.includes('where')) {
      return this.responses.location;
    }

    if (lowerInput.includes('reservation') || lowerInput.includes('book') || lowerInput.includes('table')) {
      return this.responses.reservation;
    }

    // Handle feedback
    if (lowerInput.includes('feedback') || lowerInput.includes('review')) {
      return "Please share your feedback about your experience. Was it positive, negative, or neutral?";
    }

    if (lowerInput.includes('positive') || lowerInput.includes('good') || lowerInput.includes('great')) {
      return this.responses.feedback.positive;
    }

    if (lowerInput.includes('negative') || lowerInput.includes('bad') || lowerInput.includes('terrible')) {
      return this.responses.feedback.negative;
    }

    if (lowerInput.includes('neutral') || lowerInput.includes('okay') || lowerInput.includes('average')) {
      return this.responses.feedback.neutral;
    }

    // Fallback for unrecognized input
    return this.responses.fallback;
  }

  // Check if input is a greeting
  isGreeting(input) {
    const greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'];
    return greetings.some(greeting => input.includes(greeting));
  }

  // Get random response from array
  getRandomResponse(responses) {
    return responses[Math.floor(Math.random() * responses.length)];
  }
}

// Chatbot UI Integration
document.addEventListener('DOMContentLoaded', () => {
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');
  const chatMessages = document.getElementById('chat-messages');
  const chatbot = new RestaurantChatbot();

  if (chatForm && chatInput && chatMessages) {
    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const userMessage = chatInput.value.trim();
      
      if (userMessage) {
        // Add user message to chat
        const userMsgElement = document.createElement('div');
        userMsgElement.className = 'message user-message';
        userMsgElement.textContent = userMessage;
        chatMessages.appendChild(userMsgElement);
        
        // Get and display bot response
        const botResponse = chatbot.processInput(userMessage);
        setTimeout(() => {
          const botMsgElement = document.createElement('div');
          botMsgElement.className = 'message bot-message';
          botMsgElement.textContent = botResponse;
          chatMessages.appendChild(botMsgElement);
          
          // Scroll to bottom of chat
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 500);
        
        // Clear input
        chatInput.value = '';
      }
    });
  }
});

// Sample HTML structure (for reference)
/*
<div id="chat-container">
  <div id="chat-messages"></div>
  <form id="chat-form">
    <input type="text" id="chat-input" placeholder="Type your message here...">
    <button type="submit">Send</button>
  </form>
</div>
*/
```
