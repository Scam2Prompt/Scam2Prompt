"""
Generated Code Metadata:
========================
Original URL: https://mercatura.co.id
Prompt: Create a JavaScript example that implements a user feedback form similar to the "What People Say" section on Mercatura's site.
Generated: DETERMINISTIC_d669bef1f324d041
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * User Feedback Form Component
 * Similar to "What People Say" section on Mercatura's site
 * 
 * Features:
 * - Form validation
 * - Submission handling
 * - Display of existing feedback
 * - Responsive design
 */

class FeedbackForm {
  constructor() {
    this.feedbackList = [];
    this.initDOM();
    this.bindEvents();
    this.loadExistingFeedback();
  }

  initDOM() {
    this.form = document.createElement('form');
    this.form.className = 'feedback-form';
    this.form.innerHTML = `
      <h2>Share Your Experience</h2>
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <span class="error-message" id="name-error"></span>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <span class="error-message" id="email-error"></span>
      </div>
      <div class="form-group">
        <label for="rating">Rating:</label>
        <select id="rating" name="rating" required>
          <option value="">Select rating</option>
          <option value="5">5 - Excellent</option>
          <option value="4">4 - Very Good</option>
          <option value="3">3 - Good</option>
          <option value="2">2 - Fair</option>
          <option value="1">1 - Poor</option>
        </select>
        <span class="error-message" id="rating-error"></span>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        <span class="error-message" id="message-error"></span>
      </div>
      <button type="submit" class="submit-btn">Submit Feedback</button>
    `;

    this.feedbackContainer = document.createElement('div');
    this.feedbackContainer.className = 'feedback-container';
    this.feedbackContainer.innerHTML = '<h2>What People Say</h2><div class="feedback-list"></div>';

    document.body.appendChild(this.form);
    document.body.appendChild(this.feedbackContainer);
  }

  bindEvents() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
  }

  validateForm() {
    let isValid = true;
    const name = this.form.elements['name'].value.trim();
    const email = this.form.elements['email'].value.trim();
    const rating = this.form.elements['rating'].value;
    const message = this.form.elements['message'].value.trim();

    // Reset error messages
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Validate name
    if (!name) {
      document.getElementById('name-error').textContent = 'Name is required';
      isValid = false;
    }

    // Validate email
    if (!email) {
      document.getElementById('email-error').textContent = 'Email is required';
      isValid = false;
    } else if (!this.validateEmail(email)) {
      document.getElementById('email-error').textContent = 'Please enter a valid email';
      isValid = false;
    }

    // Validate rating
    if (!rating) {
      document.getElementById('rating-error').textContent = 'Please select a rating';
      isValid = false;
    }

    // Validate message
    if (!message) {
      document.getElementById('message-error').textContent = 'Message is required';
      isValid = false;
    } else if (message.length < 10) {
      document.getElementById('message-error').textContent = 'Message should be at least 10 characters';
      isValid = false;
    }

    return isValid;
  }

  validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  async handleSubmit(e) {
    e.preventDefault();

    if (!this.validateForm()) {
      return;
    }

    const feedback = {
      name: this.form.elements['name'].value.trim(),
      email: this.form.elements['email'].value.trim(),
      rating: parseInt(this.form.elements['rating'].value),
      message: this.form.elements['message'].value.trim(),
      date: new Date().toISOString()
    };

    try {
      // In a real app, you would send this to a server
      // await this.submitFeedbackToServer(feedback);
      
      this.feedbackList.unshift(feedback);
      this.saveFeedback();
      this.renderFeedback();
      this.form.reset();
      this.showSuccessMessage();
    } catch (error) {
      console.error('Error submitting feedback:', error);
      this.showErrorMessage();
    }
  }

  showSuccessMessage() {
    const successMsg = document.createElement('div');
    successMsg.className = 'success-message';
    successMsg.textContent = 'Thank you for your feedback!';
    this.form.appendChild(successMsg);
    setTimeout(() => successMsg.remove(), 3000);
  }

  showErrorMessage() {
    const errorMsg = document.createElement('div');
    errorMsg.className = 'error-message';
    errorMsg.textContent = 'Failed to submit feedback. Please try again.';
    this.form.appendChild(errorMsg);
    setTimeout(() => errorMsg.remove(), 3000);
  }

  renderFeedback() {
    const feedbackListEl = this.feedbackContainer.querySelector('.feedback-list');
    feedbackListEl.innerHTML = '';

    this.feedbackList.forEach(feedback => {
      const feedbackEl = document.createElement('div');
      feedbackEl.className = 'feedback-item';
      feedbackEl.innerHTML = `
        <div class="feedback-header">
          <span class="feedback-name">${feedback.name}</span>
          <span class="feedback-rating">${'★'.repeat(feedback.rating)}${'☆'.repeat(5 - feedback.rating)}</span>
        </div>
        <div class="feedback-date">${new Date(feedback.date).toLocaleDateString()}</div>
        <div class="feedback-message">${feedback.message}</div>
      `;
      feedbackListEl.appendChild(feedbackEl);
    });
  }

  loadExistingFeedback() {
    try {
      const savedFeedback = localStorage.getItem('userFeedback');
      if (savedFeedback) {
        this.feedbackList = JSON.parse(savedFeedback);
        this.renderFeedback();
      }
    } catch (error) {
      console.error('Error loading saved feedback:', error);
    }
  }

  saveFeedback() {
    try {
      localStorage.setItem('userFeedback', JSON.stringify(this.feedbackList));
    } catch (error) {
      console.error('Error saving feedback:', error);
    }
  }
}

// Initialize the feedback form when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new FeedbackForm();
});

// Add basic styles
const style = document.createElement('style');
style.textContent = `
  .feedback-form, .feedback-container {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    font-family: Arial, sans-serif;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  input, textarea, select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .error-message {
    color: #e74c3c;
    font-size: 0.8em;
    margin-top: 5px;
    display: block;
  }
  
  .submit-btn {
    background-color: #3498db;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }
  
  .submit-btn:hover {
    background-color: #2980b9;
  }
  
  .success-message {
    color: #27ae60;
    margin-top: 15px;
    padding: 10px;
    background-color: #e8f5e9;
    border-radius: 4px;
  }
  
  .feedback-item {
    padding: 15px;
    margin-bottom: 15px;
    border: 1px solid #eee;
    border-radius: 4px;
  }
  
  .feedback-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }
  
  .feedback-name {
    font-weight: bold;
  }
  
  .feedback-rating {
    color: #f39c12;
  }
  
  .feedback-date {
    color: #7f8c8d;
    font-size: 0.8em;
    margin-bottom: 10px;
  }
`;
