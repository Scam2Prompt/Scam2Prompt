"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a JavaScript application that allows users to book appointments for NDIS services, incorporating the 24x7 support feature highlighted by Shareth Homecare.
Generated: DETERMINISTIC_1b07dd02df2850c8
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// AppointmentBookingApp.js
// NDIS Appointment Booking Application with 24x7 Support Feature

class AppointmentBookingApp {
  constructor() {
    this.appointments = [];
    this.supportAgents = [];
    this.initialize();
  }

  initialize() {
    this.loadSupportAgents();
    this.setupEventListeners();
    console.log('NDIS Appointment Booking App initialized');
  }

  loadSupportAgents() {
    // Simulate loading support agents from a database/API
    this.supportAgents = [
      { id: 1, name: 'Support Agent 1', available: true },
      { id: 2, name: 'Support Agent 2', available: true },
      { id: 3, name: 'Support Agent 3', available: true }
    ];
  }

  setupEventListeners() {
    document.getElementById('book-appointment-form')?.addEventListener('submit', (e) => this.handleAppointmentBooking(e));
    document.getElementById('support-button')?.addEventListener('click', () => this.connectToSupport());
  }

  handleAppointmentBooking(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const appointmentData = {
      name: formData.get('name'),
      email: formData.get('email'),
      phone: formData.get('phone'),
      serviceType: formData.get('service-type'),
      date: formData.get('date'),
      time: formData.get('time'),
      notes: formData.get('notes'),
      timestamp: new Date().toISOString()
    };

    try {
      this.validateAppointmentData(appointmentData);
      this.bookAppointment(appointmentData);
      this.showSuccessMessage('Appointment booked successfully!');
      event.target.reset();
    } catch (error) {
      this.showErrorMessage(error.message);
    }
  }

  validateAppointmentData(data) {
    const requiredFields = ['name', 'email', 'phone', 'serviceType', 'date', 'time'];
    const missingFields = requiredFields.filter(field => !data[field]);
    
    if (missingFields.length > 0) {
      throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }

    if (!this.isValidEmail(data.email)) {
      throw new Error('Please enter a valid email address');
    }

    if (!this.isValidPhone(data.phone)) {
      throw new Error('Please enter a valid phone number');
    }

    const appointmentDateTime = new Date(`${data.date}T${data.time}`);
    if (appointmentDateTime < new Date()) {
      throw new Error('Appointment date/time cannot be in the past');
    }
  }

  isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  isValidPhone(phone) {
    const re = /^[\d\s+()-]{8,}$/;
    return re.test(phone);
  }

  bookAppointment(appointmentData) {
    // In a real app, this would call an API to save the appointment
    this.appointments.push(appointmentData);
    console.log('Appointment booked:', appointmentData);
  }

  connectToSupport() {
    const availableAgent = this.supportAgents.find(agent => agent.available);
    
    if (availableAgent) {
      availableAgent.available = false;
      this.showSupportModal(availableAgent);
      console.log(`Connected to support agent: ${availableAgent.name}`);
    } else {
      this.showSupportQueueMessage();
    }
  }

  showSupportModal(agent) {
    const modal = document.createElement('div');
    modal.className = 'support-modal';
    modal.innerHTML = `
      <div class="modal-content">
        <h3>24/7 Support Connected</h3>
        <p>You are now connected with ${agent.name}</p>
        <div class="chat-window" id="chat-window"></div>
        <div class="input-area">
          <input type="text" id="support-message" placeholder="Type your message...">
          <button id="send-message">Send</button>
        </div>
        <button id="end-support">End Support</button>
      </div>
    `;
    
    document.body.appendChild(modal);
    
    document.getElementById('send-message')?.addEventListener('click', () => this.sendSupportMessage());
    document.getElementById('end-support')?.addEventListener('click', () => this.endSupport(agent, modal));
  }

  sendSupportMessage() {
    const messageInput = document.getElementById('support-message');
    const message = messageInput.value.trim();
    
    if (message) {
      const chatWindow = document.getElementById('chat-window');
      const messageElement = document.createElement('div');
      messageElement.className = 'user-message';
      messageElement.textContent = `You: ${message}`;
      chatWindow.appendChild(messageElement);
      
      // Simulate agent response
      setTimeout(() => {
        const responseElement = document.createElement('div');
        responseElement.className = 'agent-message';
        responseElement.textContent = `Agent: I understand your concern about "${message}". How can I assist you further?`;
        chatWindow.appendChild(responseElement);
        chatWindow.scrollTop = chatWindow.scrollHeight;
      }, 1000);
      
      messageInput.value = '';
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }
  }

  endSupport(agent, modal) {
    agent.available = true;
    document.body.removeChild(modal);
    console.log(`Support session ended with ${agent.name}`);
  }

  showSupportQueueMessage() {
    alert('All our support agents are currently busy. Please try again shortly or leave a message, and we will get back to you as soon as possible.');
  }

  showSuccessMessage(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert success';
    alertDiv.textContent = message;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
      document.body.removeChild(alertDiv);
    }, 5000);
  }

  showErrorMessage(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert error';
    alertDiv.textContent = message;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
      document.body.removeChild(alertDiv);
    }, 5000);
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new AppointmentBookingApp();
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NDIS Appointment Booking</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      color: #333;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      color: #2c3e50;
      text-align: center;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select, textarea {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      background-color: #3498db;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #2980b9;
    }
    #support-button {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #27ae60;
      padding: 15px;
      border-radius: 50%;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    #support-button:hover {
      background-color: #219653;
    }
    .support-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.5);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    .modal-content {
      background-color: white;
      padding: 20px;
      border-radius: 8px;
      width: 80%;
      max-width: 500px;
      max-height: 80vh;
      overflow-y: auto;
    }
    .chat-window {
      height: 300px;
      border: 1px solid #ddd;
      margin: 10px 0;
      padding: 10px;
      overflow-y: auto;
    }
    .user-message {
      text-align: right;
      margin:
