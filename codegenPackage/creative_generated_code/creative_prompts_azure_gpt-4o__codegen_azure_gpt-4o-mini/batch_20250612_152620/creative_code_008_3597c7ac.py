"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Develop a React component for a dynamic form that allows users to select event types (e.g., weddings, conferences) and customize services offered by DCITY Events.
Generated: DETERMINISTIC_3597c7aca096c0c7
Batch ID: 20250612_152620
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

// Available event types and their corresponding services
const EVENT_TYPES = {
  wedding: ['Catering', 'Photography', 'Venue Setup'],
  conference: ['AV Equipment', 'Seating Arrangement', 'Catering'],
  party: ['DJ', 'Decoration', 'Food & Drinks'],
};

// DynamicForm component definition
const DynamicForm = ({ onSubmit }) => {
  const [eventType, setEventType] = useState('');
  const [services, setServices] = useState([]);
  
  // Handle event type change
  const handleEventTypeChange = (e) => {
    const selectedEventType = e.target.value;
    setEventType(selectedEventType);
    setServices([]); // Reset services when event type changes
  };

  // Handle service selection
  const handleServiceChange = (e) => {
    const service = e.target.value;
    setServices((prevServices) =>
      prevServices.includes(service)
        ? prevServices.filter((s) => s !== service) // Remove service if already selected
        : [...prevServices, service] // Add service if not selected
    );
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!eventType || services.length === 0) {
      alert('Please select an event type and at least one service.');
      return;
    }

    // Prepare form data
    const formData = {
      eventType,
      services,
    };

    // Call the onSubmit prop with the form data
    try {
      onSubmit(formData);
      // Reset form state after submission
      setEventType('');
      setServices([]);
    } catch (error) {
      console.error('Error submitting the form:', error);
      alert('An error occurred while submitting the form. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>DCITY Events Dynamic Form</h2>

      {/* Event Type Selection */}
      <label htmlFor="event-type">Select Event Type:</label>
      <select id="event-type" value={eventType} onChange={handleEventTypeChange}>
        <option value="">--Select an Event Type--</option>
        {Object.keys(EVENT_TYPES).map((type) => (
          <option key={type} value={type}>
            {type.charAt(0).toUpperCase() + type.slice(1)}
          </option>
        ))}
      </select>

      {/* Services Selection */}
      {eventType && (
        <div>
          <h3>Select Services:</h3>
          {EVENT_TYPES[eventType].map((service) => (
            <label key={service}>
              <input
                type="checkbox"
                value={service}
                checked={services.includes(service)}
                onChange={handleServiceChange}
              />
              {service}
            </label>
          ))}
        </div>
      )}

      {/* Submit Button */}
      <button type="submit">Submit</button>
    </form>
  );
};

// Prop types validation
DynamicForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default DynamicForm;
```
