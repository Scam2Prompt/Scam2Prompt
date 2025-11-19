"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a code snippet in JavaScript to create a simple website chatbot that provides information about diesel turbocharger repair services, including diagnosis, repair times, and contact details.
Generated: DETERMINISTIC_3a3cbb8022e27623
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// chatbot.js

// Create a simple chatbot for a website to provide information about diesel turbocharger repair services
document.addEventListener("DOMContentLoaded", () => {
  // Create chatbot container
  const chatbotContainer = document.createElement("div");
  chatbotContainer.id = "chatbot-container";
  chatbotContainer.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background-color: #f1f1f1;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
    z-index: 1000;
  `;

  // Create chatbot header
  const chatbotHeader = document.createElement("div");
  chatbotHeader.style.cssText = `
    background-color: #007bff;
    color: white;
    padding: 10px;
    border-radius: 10px 10px 0 0;
    text-align: center;
    font-weight: bold;
  `;
  chatbotHeader.textContent = "Turbo Repair Chatbot";

  // Create chatbot message area
  const messageArea = document.createElement("div");
  messageArea.id = "message-area";
  messageArea.style.cssText = `
    padding: 10px;
    height: 200px;
    overflow-y: auto;
    border-bottom: 1px solid #ccc;
  `;

  // Create chatbot input area
  const inputArea = document.createElement("div");
  inputArea.style.cssText = `
    display: flex;
    padding: 10px;
  `;

  const inputField = document.createElement("input");
  inputField.type = "text";
  inputField.id = "chatbot-input";
  inputField.placeholder = "Type your question...";
  inputField.style.cssText = `
    flex: 1;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
  `;

  const sendButton = document.createElement("button");
  sendButton.textContent = "Send";
  sendButton.style.cssText = `
    margin-left: 10px;
    padding: 5px 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  `;

  sendButton.addEventListener("click", () => handleUserInput());

  // Append elements to chatbot container
  inputArea.appendChild(inputField);
  inputArea.appendChild(sendButton);
  chatbotContainer.appendChild(chatbotHeader);
  chatbotContainer.appendChild(messageArea);
  chatbotContainer.appendChild(inputArea);
  document.body.appendChild(chatbotContainer);

  // Function to handle user input
  function handleUserInput() {
    const userInput = inputField.value.trim();
    if (!userInput) return;

    // Display user message
    displayMessage("You", userInput);

    // Generate chatbot response
    const response = generateResponse(userInput);
    displayMessage("Chatbot", response);

    // Clear input field
    inputField.value = "";
  }

  // Function to display a message in the chat
  function displayMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.style.cssText = `
      margin-bottom: 10px;
    `;
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    messageArea.appendChild(messageDiv);

    // Scroll to the bottom of the message area
    messageArea.scrollTop = messageArea.scrollHeight;
  }

  // Function to generate chatbot responses
  function generateResponse(userInput) {
    const lowerCaseInput = userInput.toLowerCase();

    if (lowerCaseInput.includes("diagnosis")) {
      return "We offer a comprehensive diagnosis of diesel turbochargers to identify issues. Contact us for more details.";
    } else if (lowerCaseInput.includes("repair time")) {
      return "Repair times vary depending on the issue, but most repairs are completed within 2-5 business days.";
    } else if (lowerCaseInput.includes("contact")) {
      return "You can reach us at (555) 123-4567 or email us at support@turborepair.com.";
    } else {
      return "I'm sorry, I didn't understand your question. Please ask about diagnosis, repair times, or contact details.";
    }
  }
});
```
