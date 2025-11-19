"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-xprojecterc.pages.dev
Prompt: Illustrate how to implement a user interface component that shows the unlock time for staked assets in the X Project Staking app.
Generated: DETERMINISTIC_c16afb2a3a4d24c9
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import PropTypes from 'prop-types';
import dayjs from 'dayjs'; // For date formatting
import './UnlockTimeDisplay.css'; // Import styling

/**
 * UnlockTimeDisplay Component
 * Displays the unlock time for staked assets
 *
 * Props:
 * - unlockTimestamp (number): The UNIX timestamp representing the unlock time.
 */
const UnlockTimeDisplay = ({ unlockTimestamp }) => {
  // Convert the UNIX timestamp into a readable date format using dayjs
  const formattedDate = dayjs(unlockTimestamp * 1000).format('MMMM D, YYYY h:mm A');

  // Calculate time left in days, hours, and minutes
  const now = dayjs();
  const unlockTime = dayjs(unlockTimestamp * 1000);
  const timeLeft = unlockTime.diff(now);

  // Error handling for invalid timestamp
  if (isNaN(unlockTimestamp) || unlockTimestamp <= 0) {
    return <div className="error-message">Invalid unlock time. Please try again.</div>;
  }

  return (
    <div className="unlock-time-display">
      {/* Display the unlock time */}
      <h3 className="unlock-title">Unlock Time</h3>
      <p className="unlock-date">Your staked assets will unlock on:</p>
      <p className="unlock-date-formatted">{formattedDate}</p>

      {/* Countdown timer */}
      {timeLeft > 0 ? (
        <p className="unlock-countdown">
          Time remaining: {Math.floor(timeLeft / (1000 * 60 * 60 * 24))} days,{' '}
          {Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))} hours,{' '}
          {Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))} minutes
        </p>
      ) : (
        <p className="unlock-countdown">Your assets have unlocked!</p>
      )}
    </div>
  );
};

// Define prop types for the component
UnlockTimeDisplay.propTypes = {
  unlockTimestamp: PropTypes.number.isRequired,
};

// Export the component
export default UnlockTimeDisplay;

/*
 * UnlockTimeDisplay.css
 *
 * .unlock-time-display {
 *   padding: 16px;
 *   border: 1px solid #ccc;
 *   border-radius: 4px;
 *   background-color: #f9f9f9;
 *   max-width: 400px;
 *   margin: 0 auto;
 *   text-align: center;
 * }
 * 
 * .unlock-title {
 *   font-size: 1.5rem;
 *   margin-bottom: 8px;
 * }
 * 
 * .unlock-date, .unlock-date-formatted, .unlock-countdown {
 *   font-size: 1rem;
 *   margin: 4px 0;
 * }
 * 
 * .error-message {
 *   color: red;
 *   font-size: 1rem;
 *   text-align: center;
 * }
 */
```
