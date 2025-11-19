"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Write a JavaScript code snippet to implement a chatbot for customer support on a Jordanian company's website, using IDEX Marketing's digital marketing services as a reference."
Generated: DETERMINISTIC_0cde93bcb3576c9b
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Customer Support Chatbot for Jordanian Company
 * Integrated with IDEX Marketing's digital marketing services
 */

class Chatbot {
  constructor() {
    this.messages = [];
    this.isActive = false;
    this.initElements();
    this.bindEvents();
    this.loadGreeting();
  }

  initElements() {
    this.chatbotContainer = document.createElement('div');
    this.chatbotContainer.className = 'chatbot-container';
    
    this.chatbotHeader = document.createElement('div');
    this.chatbotHeader.className = 'chatbot-header';
    this.chatbotHeader.textContent = 'IDEX Marketing Support';
    
    this.chatbotBody = document.createElement('div');
    this.chatbotBody.className = 'chatbot-body';
    
    this.chatbotFooter = document.createElement('div');
    this.chatbotFooter.className = 'chatbot-footer';
    
    this.inputField = document.createElement('input');
    this.inputField.type = 'text';
    this.inputField.placeholder = 'Type your message here...';
    this.inputField.className = 'chatbot-input';
    
    this.sendButton = document.createElement('button');
    this.sendButton.className = 'chatbot-send';
    this.sendButton.textContent = 'Send';
    
    this.toggleButton = document.createElement('button');
    this.toggleButton.className = 'chatbot-toggle';
    this.toggleButton.textContent = 'Chat';
    
    this.chatbotFooter.appendChild(this.inputField);
    this.chatbotFooter.appendChild(this.sendButton);
    
    this.chatbotContainer.appendChild(this.chatbotHeader);
    this.chatbotContainer.appendChild(this.chatbotBody);
    this.chatbotContainer.appendChild(this.chatbotFooter);
    
    document.body.appendChild(this.chatbotContainer);
    document.body.appendChild(this.toggleButton);
    
    this.addStyles();
  }

  bindEvents() {
    this.toggleButton.addEventListener('click', () => this.toggleChat());
    this.sendButton.addEventListener('click', () => this.handleSend());
    this.inputField.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.handleSend();
    });
  }

  toggleChat() {
    this.isActive = !this.isActive;
    this.chatbotContainer.style.display = this.isActive ? 'block' : 'none';
    this.toggleButton.textContent = this.isActive ? 'Close' : 'Chat';
  }

  handleSend() {
    const message = this.inputField.value.trim();
    if (!message) return;
    
    this.addMessage(message, 'user');
    this.inputField.value = '';
    
    setTimeout(() => {
      this.processResponse(message);
    }, 500);
  }

  addMessage(text, sender) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${sender}`;
    messageElement.textContent = text;
    this.chatbotBody.appendChild(messageElement);
    this.chatbotBody.scrollTop = this.chatbotBody.scrollHeight;
    this.messages.push({ text, sender });
  }

  processResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    let response = '';

    if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
      response = 'مرحبا! كيف يمكنني مساعدتك اليوم؟';
    } 
    else if (lowerMessage.includes('service') || lowerMessage.includes('services')) {
      response = 'نحن في IDEX Marketing نقدم خدمات التسويق الرقمي بما في ذلك إدارة وسائل التواصل الاجتماعي، تحسين محركات البحث، الإعلانات المدفوعة، وتصميم المواقع. هل ترغب في معرفة المزيد عن خدمة معينة؟';
    }
    else if (lowerMessage.includes('contact') || lowerMessage.includes('reach')) {
      response = 'يمكنك التواصل معنا على الهاتف: +962 6 1234567 أو عبر البريد الإلكتروني: info@idexmarketing.com';
    }
    else if (lowerMessage.includes('price') || lowerMessage.includes('cost')) {
      response = 'تختلف الأسعار حسب الخدمة المطلوبة. هل يمكنك تحديد الخدمة التي تهتم بها؟';
    }
    else if (lowerMessage.includes('thank') || lowerMessage.includes('shukran')) {
      response = 'العفو! نحن دائما هنا لمساعدتك. هل هناك أي شيء آخر تحتاجه؟';
    }
    else {
      response = 'آسف، لم أفهم سؤالك. هل يمكنك إعادة صياغته؟ أو يمكنك كتابة "خدمات" لمعرفة المزيد عن خدماتنا.';
    }

    this.addMessage(response, 'bot');
  }

  loadGreeting() {
    setTimeout(() => {
      this.addMessage('مرحبا! أنا مساعد IDEX Marketing. كيف يمكنني مساعدتك اليوم؟', 'bot');
    }, 1000);
  }

  addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .chatbot-container {
        position: fixed;
        bottom: 80px;
        right: 20px;
        width: 300px;
        height: 400px;
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        display: none;
        flex-direction: column;
        z-index: 1000;
        font-family: 'Arial', sans-serif;
      }
      
      .chatbot-header {
        padding: 15px;
        background: #2c3e50;
        color: white;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        font-weight: bold;
      }
      
      .chatbot-body {
        flex: 1;
        padding: 15px;
        overflow-y: auto;
      }
      
      .chatbot-footer {
        padding: 10px;
        display: flex;
        border-top: 1px solid #eee;
      }
      
      .chatbot-input {
        flex: 1;
        padding: 8px;
        border: 1px solid #ddd;
        border-radius: 4px;
        outline: none;
      }
      
      .chatbot-send {
        margin-left: 10px;
        padding: 8px 15px;
        background: #2c3e50;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      
      .chatbot-send:hover {
        background: #34495e;
      }
      
      .chatbot-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        padding: 10px 20px;
        background: #2c3e50;
        color: white;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        z-index: 1000;
      }
      
      .message {
        margin-bottom: 10px;
        padding: 8px 12px;
        border-radius: 18px;
        max-width: 80%;
      }
      
      .message.user {
        background: #e3f2fd;
        margin-left: auto;
        border-bottom-right-radius: 0;
      }
      
      .message.bot {
        background: #f1f1f1;
        margin-right: auto;
        border-bottom-left-radius: 0;
      }
    `;
    document.head.appendChild(style);
  }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new Chatbot();
});
```
