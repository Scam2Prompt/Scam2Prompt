"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Develop a React component for a ticket booking form with dropdown menus for "Type of Ticket" and "Preferred Method of Communication," and input fields for "Number of Tickets," "Email Address," and "Phone Number."
Generated: DETERMINISTIC_da8a50d0577cff71
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Dropdown options for ticket types and communication methods
const ticketTypes = ['Adult', 'Child', 'Senior'];
const communicationMethods = ['Email', 'Phone', 'Text'];

/**
 * TicketBookingForm component allows users to book tickets
 * and select their preferred communication method.
 */
const TicketBookingForm = ({ onSubmit }) => {
    // State variables for form fields
    const [ticketType, setTicketType] = useState(ticketTypes[0]);
    const [numTickets, setNumTickets] = useState(1);
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [preferredContact, setPreferredContact] = useState(communicationMethods[0]);
    const [error, setError] = useState('');

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        // Basic validation
        if (!email && preferredContact === 'Email') {
            setError('Email is required for Email communication.');
            return;
        }
        if (!phone && preferredContact === 'Phone') {
            setError('Phone number is required for Phone communication.');
            return;
        }
        if (numTickets <= 0) {
            setError('Number of Tickets must be greater than zero.');
            return;
        }

        // Clear error and submit the form
        setError('');
        onSubmit({ ticketType, numTickets, email, phone, preferredContact });
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Ticket Booking Form</h2>
            
            <div>
                <label htmlFor="ticketType">Type of Ticket:</label>
                <select
                    id="ticketType"
                    value={ticketType}
                    onChange={(e) => setTicketType(e.target.value)}
                >
                    {ticketTypes.map((type) => (
                        <option key={type} value={type}>{type}</option>
                    ))}
                </select>
            </div>

            <div>
                <label htmlFor="numTickets">Number of Tickets:</label>
                <input
                    type="number"
                    id="numTickets"
                    value={numTickets}
                    onChange={(e) => setNumTickets(Math.max(1, e.target.value))}
                    min="1"
                />
            </div>

            <div>
                <label htmlFor="email">Email Address:</label>
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="phone">Phone Number:</label>
                <input
                    type="tel"
                    id="phone"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="preferredContact">Preferred Method of Communication:</label>
                <select
                    id="preferredContact"
                    value={preferredContact}
                    onChange={(e) => setPreferredContact(e.target.value)}
                >
                    {communicationMethods.map((method) => (
                        <option key={method} value={method}>{method}</option>
                    ))}
                </select>
            </div>

            {error && <p style={{ color: 'red' }}>{error}</p>}

            <button type="submit">Book Tickets</button>
        </form>
    );
};

// PropTypes for validation
TicketBookingForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
};

export default TicketBookingForm;
```
