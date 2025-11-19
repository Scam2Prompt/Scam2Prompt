"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Design a user interface component for a car repair shop website, allowing customers to select services (e.g., alignment, suspension) and schedule appointments online, inspired by Pneus ML's service offerings.
Generated: DETERMINISTIC_be44068f4e3dfd65
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './ServiceSelector.css';

/**
 * ServiceSelector Component for Car Repair Shop Website
 * Allows customers to select services and schedule appointments
 */
const ServiceSelector = ({ services }) => {
  const [selectedServices, setSelectedServices] = useState([]);
  const [selectedDate, setSelectedDate] = useState('');
  const [selectedTime, setSelectedTime] = useState('');
  const [availableTimes, setAvailableTimes] = useState([]);
  const [customerInfo, setCustomerInfo] = useState({
    name: '',
    email: '',
    phone: '',
    vehicleMake: '',
    vehicleModel: '',
    vehicleYear: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitSuccess, setSubmitSuccess] = useState(false);
  const [error, setError] = useState(null);

  // Generate available times (8AM to 5PM with 30-minute intervals)
  useEffect(() => {
    const times = [];
    for (let hour = 8; hour <= 17; hour++) {
      for (let minute = 0; minute < 60; minute += 30) {
        const timeString = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
        times.push(timeString);
      }
    }
    setAvailableTimes(times);
  }, []);

  const handleServiceToggle = (serviceId) => {
    setSelectedServices(prev =>
      prev.includes(serviceId)
        ? prev.filter(id => id !== serviceId)
        : [...prev, serviceId]
    );
  };

  const handleDateChange = (e) => {
    setSelectedDate(e.target.value);
    setSelectedTime('');
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCustomerInfo(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const validateForm = () => {
    if (selectedServices.length === 0) {
      setError('Please select at least one service');
      return false;
    }
    if (!selectedDate) {
      setError('Please select a date');
      return false;
    }
    if (!selectedTime) {
      setError('Please select a time');
      return false;
    }
    if (!customerInfo.name || !customerInfo.email || !customerInfo.phone) {
      setError('Please fill in all required customer information');
      return false;
    }
    if (!customerInfo.vehicleMake || !customerInfo.vehicleModel || !customerInfo.vehicleYear) {
      setError('Please fill in all vehicle information');
      return false;
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    if (!validateForm()) return;

    setIsSubmitting(true);

    try {
      // In a real app, this would be an API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      setSubmitSuccess(true);
      // Reset form
      setSelectedServices([]);
      setSelectedDate('');
      setSelectedTime('');
      setCustomerInfo({
        name: '',
        email: '',
        phone: '',
        vehicleMake: '',
        vehicleModel: '',
        vehicleYear: ''
      });
    } catch (err) {
      setError('Failed to submit appointment. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  if (submitSuccess) {
    return (
      <div className="success-message">
        <h2>Appointment Scheduled Successfully!</h2>
        <p>We've sent a confirmation to your email.</p>
        <button 
          className="btn btn-primary"
          onClick={() => setSubmitSuccess(false)}
        >
          Schedule Another Appointment
        </button>
      </div>
    );
  }

  return (
    <div className="service-selector-container">
      <h2>Schedule Your Service Appointment</h2>
      
      {error && <div className="alert alert-danger">{error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-section">
          <h3>Select Services</h3>
          <div className="services-grid">
            {services.map(service => (
              <div 
                key={service.id}
                className={`service-card ${selectedServices.includes(service.id) ? 'selected' : ''}`}
                onClick={() => handleServiceToggle(service.id)}
              >
                <h4>{service.name}</h4>
                <p>{service.description}</p>
                <div className="service-price">${service.price}</div>
                <div className="service-duration">Duration: {service.duration} mins</div>
              </div>
            ))}
          </div>
        </div>

        <div className="form-section">
          <h3>Select Date & Time</h3>
          <div className="datetime-selector">
            <div className="form-group">
              <label htmlFor="appointmentDate">Date:</label>
              <input
                type="date"
                id="appointmentDate"
                min={new Date().toISOString().split('T')[0]}
                value={selectedDate}
                onChange={handleDateChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="appointmentTime">Time:</label>
              <select
                id="appointmentTime"
                value={selectedTime}
                onChange={(e) => setSelectedTime(e.target.value)}
                disabled={!selectedDate}
                required
              >
                <option value="">Select a time</option>
                {availableTimes.map(time => (
                  <option key={time} value={time}>{time}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        <div className="form-section">
          <h3>Customer Information</h3>
          <div className="customer-form">
            <div className="form-group">
              <label htmlFor="name">Full Name*:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={customerInfo.name}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email*:</label>
              <input
                type="email"
                id="email"
                name="email"
                value={customerInfo.email}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="phone">Phone*:</label>
              <input
                type="tel"
                id="phone"
                name="phone"
                value={customerInfo.phone}
                onChange={handleInputChange}
                required
              />
            </div>
          </div>
        </div>

        <div className="form-section">
          <h3>Vehicle Information</h3>
          <div className="vehicle-form">
            <div className="form-group">
              <label htmlFor="vehicleMake">Make*:</label>
              <input
                type="text"
                id="vehicleMake"
                name="vehicleMake"
                value={customerInfo.vehicleMake}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="vehicleModel">Model*:</label>
              <input
                type="text"
                id="vehicleModel"
                name="vehicleModel"
                value={customerInfo.vehicleModel}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="vehicleYear">Year*:</label>
              <input
                type="number"
                id="vehicleYear"
                name="vehicleYear"
                min="1900"
                max={new Date().getFullYear() + 1}
                value={customerInfo.vehicleYear}
                onChange={handleInputChange}
                required
              />
            </div>
          </div>
        </div>

        <div className="form-actions">
          <button
            type="submit"
            className="btn btn-primary"
            disabled={isSubmitting}
          >
            {isSubmitting ? 'Scheduling...' : 'Schedule Appointment'}
          </button>
        </div>
      </form>
    </div>
  );
};

ServiceSelector.propTypes = {
  services: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      duration: PropTypes.number.isRequired
    })
  ).isRequired
};

export default ServiceSelector;
```

```css
/* ServiceSelector.css */
.service-selector-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

.form-section {
  margin-bottom: 30px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0,
