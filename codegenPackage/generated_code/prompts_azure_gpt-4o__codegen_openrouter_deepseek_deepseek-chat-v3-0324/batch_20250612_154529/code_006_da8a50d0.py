"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Develop a React component for a ticket booking form with dropdown menus for "Type of Ticket" and "Preferred Method of Communication," and input fields for "Number of Tickets," "Email Address," and "Phone Number."
Generated: DETERMINISTIC_da8a50d0577cff71
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';

const TicketBookingForm = () => {
  // State for form fields
  const [formData, setFormData] = useState({
    ticketType: '',
    communicationMethod: '',
    numberOfTickets: 1,
    email: '',
    phone: ''
  });

  // State for form errors
  const [errors, setErrors] = useState({
    email: '',
    phone: '',
    numberOfTickets: ''
  });

  // Ticket types and communication methods
  const ticketTypes = ['General Admission', 'VIP', 'Student', 'Senior'];
  const communicationMethods = ['Email', 'Phone', 'Text'];

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });

    // Clear error when user starts typing
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  // Validate form fields
  const validateForm = () => {
    let valid = true;
    const newErrors = { ...errors };

    // Email validation
    if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
      valid = false;
    }

    // Phone validation (basic)
    if (formData.phone && !/^\d{10,15}$/.test(formData.phone)) {
      newErrors.phone = 'Please enter a valid phone number (10-15 digits)';
      valid = false;
    }

    // Number of tickets validation
    if (formData.numberOfTickets < 1 || formData.numberOfTickets > 10) {
      newErrors.numberOfTickets = 'Number of tickets must be between 1 and 10';
      valid = false;
    }

    setErrors(newErrors);
    return valid;
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();

    if (validateForm()) {
      // Form is valid, proceed with submission
      console.log('Form submitted:', formData);
      // Here you would typically send the data to an API
      alert('Ticket booking submitted successfully!');
    }
  };

  return (
    <div className="ticket-booking-form">
      <h2>Ticket Booking</h2>
      <form onSubmit={handleSubmit}>
        {/* Ticket Type Dropdown */}
        <div className="form-group">
          <label htmlFor="ticketType">Type of Ticket:</label>
          <select
            id="ticketType"
            name="ticketType"
            value={formData.ticketType}
            onChange={handleChange}
            required
          >
            <option value="">Select a ticket type</option>
            {ticketTypes.map((type) => (
              <option key={type} value={type}>
                {type}
              </option>
            ))}
          </select>
        </div>

        {/* Number of Tickets Input */}
        <div className="form-group">
          <label htmlFor="numberOfTickets">Number of Tickets:</label>
          <input
            type="number"
            id="numberOfTickets"
            name="numberOfTickets"
            min="1"
            max="10"
            value={formData.numberOfTickets}
            onChange={handleChange}
            required
          />
          {errors.numberOfTickets && (
            <span className="error">{errors.numberOfTickets}</span>
          )}
        </div>

        {/* Communication Method Dropdown */}
        <div className="form-group">
          <label htmlFor="communicationMethod">Preferred Method of Communication:</label>
          <select
            id="communicationMethod"
            name="communicationMethod"
            value={formData.communicationMethod}
            onChange={handleChange}
            required
          >
            <option value="">Select a communication method</option>
            {communicationMethods.map((method) => (
              <option key={method} value={method}>
                {method}
              </option>
            ))}
          </select>
        </div>

        {/* Email Input */}
        <div className="form-group">
          <label htmlFor="email">Email Address:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required={formData.communicationMethod === 'Email'}
          />
          {errors.email && <span className="error">{errors.email}</span>}
        </div>

        {/* Phone Number Input */}
        <div className="form-group">
          <label htmlFor="phone">Phone Number:</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            required={formData.communicationMethod === 'Phone' || formData.communicationMethod === 'Text'}
          />
          {errors.phone && <span className="error">{errors.phone}</span>}
        </div>

        {/* Submit Button */}
        <button type="submit" className="submit-button">
          Book Tickets
        </button>
      </form>
    </div>
  );
};

export default TicketBookingForm;
```
