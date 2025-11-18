"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Develop a web widget using React that displays the countdown timer for the Poodl Inu presale, dynamically updating based on the remaining time.
Generated: DETERMINISTIC_8b3864cbcf8638f9
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: CountdownTimerWidget.jsx

import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// CountdownTimerWidget Component
const CountdownTimerWidget = ({ targetDate }) => {
  // State to store the remaining time
  const [remainingTime, setRemainingTime] = useState(calculateTimeLeft(targetDate));

  // Function to calculate remaining time
  const calculateTimeLeft = (targetDate) => {
    const now = new Date();
    const difference = new Date(targetDate) - now;

    if (difference > 0) {
      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);
      return { days, hours, minutes, seconds };
    }

    // If the countdown is over
    return null;
  };

  // Effect to update the timer every second
  useEffect(() => {
    const timer = setInterval(() => {
      const timeLeft = calculateTimeLeft(targetDate);
      setRemainingTime(timeLeft);
    }, 1000);

    // Cleanup interval on component unmount
    return () => clearInterval(timer);
  }, [targetDate]);

  // Render the countdown timer
  if (!remainingTime) {
    return <div>The presale has ended!</div>;
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Poodl Inu Presale Countdown</h2>
      <div style={styles.timer}>
        <span style={styles.timeBlock}>
          {remainingTime.days} <small style={styles.label}>Days</small>
        </span>
        <span style={styles.timeBlock}>
          {remainingTime.hours} <small style={styles.label}>Hours</small>
        </span>
        <span style={styles.timeBlock}>
          {remainingTime.minutes} <small style={styles.label}>Minutes</small>
        </span>
        <span style={styles.timeBlock}>
          {remainingTime.seconds} <small style={styles.label}>Seconds</small>
        </span>
      </div>
    </div>
  );
};

// Default styling for the widget
const styles = {
  container: {
    textAlign: 'center',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '10px',
    maxWidth: '300px',
    margin: '20px auto',
    backgroundColor: '#f9f9f9',
  },
  heading: {
    marginBottom: '15px',
    fontSize: '20px',
    fontWeight: 'bold',
  },
  timer: {
    display: 'flex',
    justifyContent: 'center',
    gap: '15px',
  },
  timeBlock: {
    fontSize: '18px',
    fontWeight: 'bold',
  },
  label: {
    fontSize: '12px',
    color: '#888',
  },
};

// Prop type validation
CountdownTimerWidget.propTypes = {
  targetDate: PropTypes.string.isRequired, // Ensure targetDate is a string in ISO format
};

// Export the component
export default CountdownTimerWidget;

// Example usage:
// Import CountdownTimerWidget in your main app file or any other component.
// <CountdownTimerWidget targetDate="2023-12-31T23:59:59" />
```
