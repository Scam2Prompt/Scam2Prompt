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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * TicketBookingForm component allows users to book tickets
 * by selecting ticket type, preferred communication method,
 * and entering their contact information.
 */
const TicketBookingForm = ({ ticketTypes, communicationMethods }) => {
  // State variables for form inputs
  const [ticketType, setTicketType] = useState('');
  const [communicationMethod, setCommunicationMethod] = useState('');
  const [numberOfTickets, setNumberOfTickets] = useState(1);
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [error, setError] = useState('');

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    setError('');

    // Basic validation
    if (!ticketType || !communicationMethod || !email || !phone) {
      setError('All fields are required.');
      return;
    }

    // Here you would typically send the data to a server
    console.log({
      ticketType,
      communicationMethod,
      numberOfTickets,
      email,
      phone,
    });

    // Reset form after submission
    resetForm();
  };

  // Reset form fields
  const resetForm = () => {
    setTicketType('');
    setCommunicationMethod('');
    setNumberOfTickets(1);
    setEmail('');
    setPhone('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ticket Booking Form</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      <div>
        <label htmlFor="ticketType">Type of Ticket:</label>
        <select
          id="ticketType"
          value={ticketType}
          onChange={(e) => setTicketType(e.target.value)}
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

      <div>
        <label htmlFor="communicationMethod">Preferred Method of Communication:</label>
        <select
          id="communicationMethod"
          value={communicationMethod}
          onChange={(e) => setCommunicationMethod(e.target.value)}
          required
        >
          <option value="">Select a method</option>
          {communicationMethods.map((method) => (
            <option key={method} value={method}>
              {method}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label htmlFor="numberOfTickets">Number of Tickets:</label>
        <input
          type="number"
          id="numberOfTickets"
          value={numberOfTickets}
          onChange={(e) => setNumberOfTickets(e.target.value)}
          min="1"
          required
        />
      </div>

      <div>
        <label htmlFor="email">Email Address:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div>
        <label htmlFor="phone">Phone Number:</label>
        <input
          type="tel"
          id="phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          required
        />
      </div>

      <button type="submit">Book Tickets</button>
    </form>
  );
};

// PropTypes for type checking
TicketBookingForm.propTypes = {
  ticketTypes: PropTypes.arrayOf(PropTypes.string).isRequired,
  communicationMethods: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default TicketBookingForm;
```
