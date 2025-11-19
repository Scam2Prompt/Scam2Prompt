"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: Illustrate how to implement a user interface in React for booking medical consultations at Grupo Clínico IDET, including telemedicine options.
Generated: DETERMINISTIC_3980985394805ead
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './BookingForm.css'; // Import CSS for styling

// BookingForm component for medical consultation booking
const BookingForm = ({ clinics, onSubmit }) => {
    // State to manage form inputs
    const [selectedClinic, setSelectedClinic] = useState('');
    const [appointmentDate, setAppointmentDate] = useState('');
    const [isTelemedicine, setIsTelemedicine] = useState(false);
    const [error, setError] = useState('');

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        // Validate inputs
        if (!selectedClinic || !appointmentDate) {
            setError('Please select a clinic and a date for the appointment.');
            return;
        }
        // Clear error and call onSubmit prop with form data
        setError('');
        onSubmit({ selectedClinic, appointmentDate, isTelemedicine });
    };

    return (
        <div className="booking-form">
            <h2>Book a Medical Consultation</h2>
            {error && <div className="error-message">{error}</div>}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="clinic">Select Clinic:</label>
                    <select
                        id="clinic"
                        value={selectedClinic}
                        onChange={(e) => setSelectedClinic(e.target.value)}
                        required
                    >
                        <option value="">--Select a Clinic--</option>
                        {clinics.map((clinic) => (
                            <option key={clinic.id} value={clinic.id}>
                                {clinic.name}
                            </option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="date">Appointment Date:</label>
                    <input
                        type="date"
                        id="date"
                        value={appointmentDate}
                        onChange={(e) => setAppointmentDate(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>
                        <input
                            type="checkbox"
                            checked={isTelemedicine}
                            onChange={(e) => setIsTelemedicine(e.target.checked)}
                        />
                        Telemedicine Option
                    </label>
                </div>
                <button type="submit">Book Appointment</button>
            </form>
        </div>
    );
};

// PropTypes for type checking
BookingForm.propTypes = {
    clinics: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
        })
    ).isRequired,
    onSubmit: PropTypes.func.isRequired,
};

// Export the BookingForm component
export default BookingForm;
```

```javascript
// Example usage of BookingForm component
import React from 'react';
import ReactDOM from 'react-dom';
import BookingForm from './BookingForm';

// Sample clinic data
const clinics = [
    { id: '1', name: 'Clinica A' },
    { id: '2', name: 'Clinica B' },
    { id: '3', name: 'Clinica C' },
];

// Function to handle form submission
const handleBookingSubmit = (bookingData) => {
    console.log('Booking Data:', bookingData);
    // Here you would typically send the booking data to your server
};

// Render the BookingForm component
ReactDOM.render(
    <BookingForm clinics={clinics} onSubmit={handleBookingSubmit} />,
    document.getElementById('root')
);
```

```css
/* BookingForm.css */
.booking-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.form-group {
    margin-bottom: 15px;
}

.error-message {
    color: red;
    margin-bottom: 15px;
}
```
