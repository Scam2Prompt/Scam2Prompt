"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet in JavaScript to create a simple website for a cleaning and disinfection service company, including features like service descriptions, contact information, and a quote request form.
Generated: DETERMINISTIC_fe34d8924e5a54c8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CleaningServiceWebsite.js
class CleaningServiceWebsite {
  constructor() {
    this.services = [
      {
        id: 1,
        name: "Residential Cleaning",
        description: "Thorough cleaning of homes including dusting, vacuuming, and sanitizing surfaces.",
        priceRange: "$100 - $300"
      },
      {
        id: 2,
        name: "Commercial Cleaning",
        description: "Professional cleaning for offices and business spaces with eco-friendly products.",
        priceRange: "$200 - $500"
      },
      {
        id: 3,
        name: "Deep Disinfection",
        description: "Specialized disinfection service using hospital-grade disinfectants.",
        priceRange: "$150 - $400"
      }
    ];
    
    this.contactInfo = {
      phone: "(555) 123-4567",
      email: "contact@cleaningservice.com",
      address: "123 Clean Street, Sanitized City, 12345"
    };
    
    this.init();
  }
  
  init() {
    this.renderHeader();
    this.renderServices();
    this.renderContactInfo();
    this.renderQuoteForm();
    this.setupEventListeners();
  }
  
  renderHeader() {
    const header = document.createElement('header');
    header.innerHTML = `
      <h1>Professional Cleaning & Disinfection Services</h1>
      <p>Your trusted partner for spotless spaces</p>
    `;
    document.body.appendChild(header);
  }
  
  renderServices() {
    const section = document.createElement('section');
    section.className = 'services';
    section.innerHTML = '<h2>Our Services</h2>';
    
    const servicesList = document.createElement('div');
    servicesList.className = 'service-list';
    
    this.services.forEach(service => {
      const serviceCard = document.createElement('div');
      serviceCard.className = 'service-card';
      serviceCard.innerHTML = `
        <h3>${service.name}</h3>
        <p>${service.description}</p>
        <span class="price">${service.priceRange}</span>
      `;
      servicesList.appendChild(serviceCard);
    });
    
    section.appendChild(servicesList);
    document.body.appendChild(section);
  }
  
  renderContactInfo() {
    const section = document.createElement('section');
    section.className = 'contact';
    section.innerHTML = `
      <h2>Contact Us</h2>
      <div class="contact-details">
        <p><strong>Phone:</strong> ${this.contactInfo.phone}</p>
        <p><strong>Email:</strong> ${this.contactInfo.email}</p>
        <p><strong>Address:</strong> ${this.contactInfo.address}</p>
      </div>
    `;
    document.body.appendChild(section);
  }
  
  renderQuoteForm() {
    const section = document.createElement('section');
    section.className = 'quote-form';
    section.innerHTML = `
      <h2>Request a Quote</h2>
      <form id="quoteRequestForm">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
          <label for="phone">Phone:</label>
          <input type="tel" id="phone" name="phone">
        </div>
        <div class="form-group">
          <label for="service">Service Needed:</label>
          <select id="service" name="service" required>
            <option value="">Select a service</option>
            ${this.services.map(service => `<option value="${service.id}">${service.name}</option>`).join('')}
          </select>
        </div>
        <div class="form-group">
          <label for="message">Additional Information:</label>
          <textarea id="message" name="message" rows="4"></textarea>
        </div>
        <button type="submit">Request Quote</button>
      </form>
    `;
    document.body.appendChild(section);
  }
  
  setupEventListeners() {
    const form = document.getElementById('quoteRequestForm');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        this.handleFormSubmission();
      });
    }
  }
  
  handleFormSubmission() {
    const form = document.getElementById('quoteRequestForm');
    const formData = new FormData(form);
    const data = {};
    
    for (const [key, value] of formData.entries()) {
      data[key] = value;
    }
    
    try {
      // In a real application, you would send this data to a server
      console.log('Form submitted:', data);
      alert('Thank you for your request! We will contact you shortly.');
      form.reset();
    } catch (error) {
      console.error('Error submitting form:', error);
      alert('There was an error submitting your request. Please try again.');
    }
  }
}

// Initialize the website when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new CleaningServiceWebsite();
});

// Basic CSS styles (would normally be in a separate file)
const style = document.createElement('style');
style.textContent = `
  body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
    color: #333;
  }
  header {
    text-align: center;
    margin-bottom: 30px;
  }
  section {
    margin-bottom: 40px;
    padding: 20px;
    border-radius: 5px;
    background: #f9f9f9;
  }
  .service-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }
  .service-card {
    padding: 15px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
  .price {
    font-weight: bold;
    color: #2a7f62;
  }
  .form-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input, textarea, select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  button {
    background: #2a7f62;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  button:hover {
    background: #1e6b50;
  }
`;
document.head.appendChild(style);
```
