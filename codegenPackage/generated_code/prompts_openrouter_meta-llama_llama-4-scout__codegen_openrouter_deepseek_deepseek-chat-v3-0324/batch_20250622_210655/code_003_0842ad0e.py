"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Design a simple form using React that mirrors the patient review and rating form on the Móricz Dental website, including fields for doctor's name, rating service, and detailed feedback.
Generated: DETERMINISTIC_0842ad0ed1d31e1f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';

const PatientReviewForm = () => {
  const [formData, setFormData] = useState({
    doctorName: '',
    service: '',
    rating: 0,
    feedback: '',
    name: '',
    email: '',
    consent: false
  });

  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitSuccess, setSubmitSuccess] = useState(false);

  const doctors = [
    'Dr. Móricz Zsolt',
    'Dr. Kovács Anna',
    'Dr. Nagy Péter',
    'Dr. Szabó Eszter'
  ];

  const services = [
    'General Dentistry',
    'Cosmetic Dentistry',
    'Orthodontics',
    'Dental Implants',
    'Teeth Whitening'
  ];

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.doctorName) newErrors.doctorName = 'Please select a doctor';
    if (!formData.service) newErrors.service = 'Please select a service';
    if (formData.rating === 0) newErrors.rating = 'Please provide a rating';
    if (!formData.feedback.trim()) newErrors.feedback = 'Feedback is required';
    if (!formData.name.trim()) newErrors.name = 'Name is required';
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email';
    }
    if (!formData.consent) newErrors.consent = 'You must agree to the terms';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) return;

    setIsSubmitting(true);
    
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      setSubmitSuccess(true);
      setFormData({
        doctorName: '',
        service: '',
        rating: 0,
        feedback: '',
        name: '',
        email: '',
        consent: false
      });
    } catch (error) {
      console.error('Submission error:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleRatingChange = (value) => {
    setFormData(prev => ({ ...prev, rating: value }));
  };

  if (submitSuccess) {
    return (
      <div className="success-message">
        <h2>Thank You!</h2>
        <p>Your review has been submitted successfully.</p>
        <button onClick={() => setSubmitSuccess(false)}>Submit another review</button>
      </div>
    );
  }

  return (
    <div className="patient-review-form">
      <h2>Patient Review Form</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="doctorName">Doctor:</label>
          <select
            id="doctorName"
            name="doctorName"
            value={formData.doctorName}
            onChange={handleChange}
            className={errors.doctorName ? 'error' : ''}
          >
            <option value="">Select a doctor</option>
            {doctors.map(doctor => (
              <option key={doctor} value={doctor}>{doctor}</option>
            ))}
          </select>
          {errors.doctorName && <span className="error-message">{errors.doctorName}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="service">Service:</label>
          <select
            id="service"
            name="service"
            value={formData.service}
            onChange={handleChange}
            className={errors.service ? 'error' : ''}
          >
            <option value="">Select a service</option>
            {services.map(service => (
              <option key={service} value={service}>{service}</option>
            ))}
          </select>
          {errors.service && <span className="error-message">{errors.service}</span>}
        </div>

        <div className="form-group">
          <label>Rating:</label>
          <div className="rating-container">
            {[1, 2, 3, 4, 5].map((star) => (
              <span
                key={star}
                className={`rating-star ${star <= formData.rating ? 'filled' : ''}`}
                onClick={() => handleRatingChange(star)}
              >
                ★
              </span>
            ))}
          </div>
          {errors.rating && <span className="error-message">{errors.rating}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="feedback">Your Feedback:</label>
          <textarea
            id="feedback"
            name="feedback"
            value={formData.feedback}
            onChange={handleChange}
            rows="5"
            className={errors.feedback ? 'error' : ''}
          />
          {errors.feedback && <span className="error-message">{errors.feedback}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="name">Your Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className={errors.name ? 'error' : ''}
          />
          {errors.name && <span className="error-message">{errors.name}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="email">Your Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className={errors.email ? 'error' : ''}
          />
          {errors.email && <span className="error-message">{errors.email}</span>}
        </div>

        <div className="form-group checkbox-group">
          <input
            type="checkbox"
            id="consent"
            name="consent"
            checked={formData.consent}
            onChange={handleChange}
            className={errors.consent ? 'error' : ''}
          />
          <label htmlFor="consent">
            I agree that my review may be published on the website
          </label>
          {errors.consent && <span className="error-message">{errors.consent}</span>}
        </div>

        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Submit Review'}
        </button>
      </form>
    </div>
  );
};

export default PatientReviewForm;
```
