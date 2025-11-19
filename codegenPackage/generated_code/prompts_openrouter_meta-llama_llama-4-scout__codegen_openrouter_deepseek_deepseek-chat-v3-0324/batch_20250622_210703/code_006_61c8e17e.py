"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Develop a simple web application using a library like React or Angular to promote an eye care business, incorporating features like appointment scheduling and newsletter subscription.
Generated: DETERMINISTIC_61c8e17e301196f2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [appointmentSuccess, setAppointmentSuccess] = useState(false);
  const [subscriptionSuccess, setSubscriptionSuccess] = useState(false);

  const handleAppointmentSubmit = (e) => {
    e.preventDefault();
    // In a real app, you would send this data to a backend API
    console.log({ name, email, phone, date, time });
    setAppointmentSuccess(true);
    setName('');
    setEmail('');
    setPhone('');
    setDate('');
    setTime('');
  };

  const handleSubscriptionSubmit = (e) => {
    e.preventDefault();
    // In a real app, you would send this data to a backend API
    console.log({ email, isSubscribed });
    setSubscriptionSuccess(true);
    setEmail('');
    setIsSubscribed(false);
  };

  return (
    <div className="App">
      <header className="header">
        <h1>ClearVision Eye Care</h1>
        <p>Professional eye care services for your whole family</p>
      </header>

      <main className="main-content">
        <section className="services">
          <h2>Our Services</h2>
          <ul>
            <li>Comprehensive Eye Exams</li>
            <li>Contact Lens Fittings</li>
            <li>Glasses Prescription</li>
            <li>Dry Eye Treatment</li>
            <li>Pediatric Eye Care</li>
          </ul>
        </section>

        <section className="appointment">
          <h2>Book an Appointment</h2>
          {appointmentSuccess ? (
            <div className="success-message">
              <p>Your appointment has been scheduled successfully!</p>
              <button onClick={() => setAppointmentSuccess(false)}>Book Another Appointment</button>
            </div>
          ) : (
            <form onSubmit={handleAppointmentSubmit}>
              <div className="form-group">
                <label htmlFor="name">Full Name:</label>
                <input
                  type="text"
                  id="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="email">Email:</label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="phone">Phone Number:</label>
                <input
                  type="tel"
                  id="phone"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="date">Preferred Date:</label>
                <input
                  type="date"
                  id="date"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="time">Preferred Time:</label>
                <input
                  type="time"
                  id="time"
                  value={time}
                  onChange={(e) => setTime(e.target.value)}
                  required
                />
              </div>
              <button type="submit">Schedule Appointment</button>
            </form>
          )}
        </section>

        <section className="newsletter">
          <h2>Subscribe to Our Newsletter</h2>
          {subscriptionSuccess ? (
            <div className="success-message">
              <p>Thank you for subscribing to our newsletter!</p>
              <button onClick={() => setSubscriptionSuccess(false)}>Subscribe Again</button>
            </div>
          ) : (
            <form onSubmit={handleSubscriptionSubmit}>
              <div className="form-group">
                <label htmlFor="newsletter-email">Email:</label>
                <input
                  type="email"
                  id="newsletter-email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label>
                  <input
                    type="checkbox"
                    checked={isSubscribed}
                    onChange={(e) => setIsSubscribed(e.target.checked)}
                  />
                  I agree to receive promotional emails
                </label>
              </div>
              <button type="submit">Subscribe</button>
            </form>
          )}
        </section>
      </main>

      <footer className="footer">
        <p>© {new Date().getFullYear()} ClearVision Eye Care. All rights reserved.</p>
        <p>Contact: info@clearvision.com | Phone: (123) 456-7890</p>
      </footer>
    </div>
  );
}

export default App;
```

```css
/* App.css */
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
  color: #333;
}

.App {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  background-color: #4a90e2;
  color: white;
  padding: 2rem;
  text-align: center;
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
}

.header p {
  margin: 0.5rem 0 0;
  font-size: 1.2rem;
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.services {
  margin-bottom: 2rem;
}

.services ul {
  list-style-type: none;
  padding: 0;
}

.services li {
  background-color: #f4f4f4;
  margin: 0.5rem 0;
  padding: 1rem;
  border-radius: 4px;
}

.appointment, .newsletter {
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.appointment h2, .newsletter h2 {
  margin-top: 0;
  color: #4a90e2;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="tel"],
.form-group input[type="date"],
.form-group input[type="time"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group input[type="checkbox"] {
  margin-right: 0.5rem;
}

button {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #357ab8;
}

.success-message {
  background-color: #d4edda;
  color: #155724;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.success-message p {
  margin: 0 0 1rem;
}

.footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}

.footer p {
  margin: 0.5rem 0;
}

@media (min-width: 768px) {
  .main-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .services {
    grid-column: span 2;
  }
}
```
