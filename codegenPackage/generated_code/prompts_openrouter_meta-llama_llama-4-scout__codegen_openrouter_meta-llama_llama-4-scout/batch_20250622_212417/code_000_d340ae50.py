"""
Generated Code Metadata:
========================
Original URL: https://collab.host
Prompt: Write a code snippet for a UI component that implements a responsive design for a webinar registration form, incorporating elements such as date and time selection, speaker information, and attendee testimonials.
Generated: DETERMINISTIC_d340ae50a10deb7f
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// WebinarRegistrationForm.js
import React, { useState } from 'react';
import './WebinarRegistrationForm.css';

/**
 * Webinar Registration Form UI Component
 * 
 * @returns {JSX.Element} Webinar registration form
 */
function WebinarRegistrationForm() {
  // State to store form data
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    date: '',
    time: '',
    speaker: '',
  });

  // State to store error messages
  const [errors, setErrors] = useState({});

  // Handle form input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validateForm(formData);
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
    } else {
      // Call API to register attendee
      console.log('Registering attendee...');
      console.log(formData);
      // Reset form and errors
      setFormData({
        name: '',
        email: '',
        phone: '',
        date: '',
        time: '',
        speaker: '',
      });
      setErrors({});
    }
  };

  // Validate form data
  const validateForm = (data) => {
    const errors = {};
    if (!data.name) {
      errors.name = 'Name is required';
    }
    if (!data.email) {
      errors.email = 'Email is required';
    } else if (!validateEmail(data.email)) {
      errors.email = 'Invalid email address';
    }
    if (!data.phone) {
      errors.phone = 'Phone is required';
    }
    if (!data.date) {
      errors.date = 'Date is required';
    }
    if (!data.time) {
      errors.time = 'Time is required';
    }
    if (!data.speaker) {
      errors.speaker = 'Speaker is required';
    }
    return errors;
  };

  // Validate email address
  const validateEmail = (email) => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
  };

  return (
    <div className="webinar-registration-form">
      <h2>Webinar Registration Form</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
          {errors.name && <div className="error">{errors.name}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
          {errors.email && <div className="error">{errors.email}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="phone">Phone:</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
          />
          {errors.phone && <div className="error">{errors.phone}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="date">Date:</label>
          <input
            type="date"
            id="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
          />
          {errors.date && <div className="error">{errors.date}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="time">Time:</label>
          <input
            type="time"
            id="time"
            name="time"
            value={formData.time}
            onChange={handleChange}
          />
          {errors.time && <div className="error">{errors.time}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="speaker">Speaker:</label>
          <input
            type="text"
            id="speaker"
            name="speaker"
            value={formData.speaker}
            onChange={handleChange}
          />
          {errors.speaker && <div className="error">{errors.speaker}</div>}
        </div>
        <button type="submit">Register</button>
      </form>
      <div className="testimonials">
        <h3>Attendee Testimonials</h3>
        <ul>
          <li>
            <blockquote>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit
              amet nulla auctor, vestibulum magna sed, convallis ex.
            </blockquote>
            <cite>John Doe</cite>
          </li>
          <li>
            <blockquote>
              Pellentesque habitant morbi tristique senectus et netus et malesuada
              fames ac turpis egestas.
            </blockquote>
            <cite>Jane Smith</cite>
          </li>
        </ul>
      </div>
      <div className="speaker-info">
        <h3>Speaker Information</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet
          nulla auctor, vestibulum magna sed, convallis ex.
        </p>
      </div>
    </div>
  );
}

export default WebinarRegistrationForm;
```

```css
/* WebinarRegistrationForm.css */
.webinar-registration-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.webinar-registration-form h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 10px;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="tel"],
.form-group input[type="date"],
.form-group input[type="time"] {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.error {
  color: #f00;
  font-size: 12px;
  margin-top: 5px;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}

.testimonials {
  margin-top: 40px;
}

.testimonials h3 {
  margin-bottom: 20px;
}

.testimonials ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.testimonials li {
  margin-bottom: 20px;
}

.testimonials blockquote {
  background-color: #f9f9f9;
  padding: 10px;
  border-left: 5px solid #4CAF50;
}

.testimonials cite {
  display: block;
  margin-top: 10px;
  font-size: 14px;
}

.speaker-info {
  margin-top: 40px;
}

.speaker-info h3 {
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .webinar-registration-form {
    margin: 20px auto;
    padding: 10px;
  }
}

@media (max-width: 480px) {
  .webinar-registration-form {
    margin: 10px auto;
    padding: 5px;
  }
  .form-group input[type="text"],
  .form-group input[type="email"],
  .form-group input[type="tel"],
  .form-group input[type="date"],
  .form-group input[type="time"] {
    height: 30px;
  }
}
```
