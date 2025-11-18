"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-app.pages.dev
Prompt: Write a React component for the BCB Staking v2 platform that displays the countdown timer for Pool 1, showing the remaining days, hours, minutes, and seconds until the pool ends.
Generated: DETERMINISTIC_9da57c463fbe5317
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * CountdownTimer component to display the remaining time for a staking pool.
 * 
 * @param {Object} props - Component props.
 * @param {Date} props.endDate - The end date of the staking pool.
 */
const CountdownTimer = ({ endDate }) => {
    const [timeRemaining, setTimeRemaining] = useState({});

    useEffect(() => {
        const calculateTimeRemaining = () => {
            const now = new Date();
            const distance = new Date(endDate) - now;

            // Check if the countdown has ended
            if (distance < 0) {
                setTimeRemaining({ days: 0, hours: 0, minutes: 0, seconds: 0 });
                return;
            }

            // Calculate remaining time
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            setTimeRemaining({ days, hours, minutes, seconds });
        };

        // Initial calculation
        calculateTimeRemaining();

        // Update the countdown every second
        const intervalId = setInterval(calculateTimeRemaining, 1000);

        // Cleanup interval on component unmount
        return () => clearInterval(intervalId);
    }, [endDate]);

    return (
        <div className="countdown-timer">
            <h2>Pool Countdown</h2>
            <div>
                <span>{timeRemaining.days} Days </span>
                <span>{timeRemaining.hours} Hours </span>
                <span>{timeRemaining.minutes} Minutes </span>
                <span>{timeRemaining.seconds} Seconds </span>
            </div>
        </div>
    );
};

// PropTypes for type-checking
CountdownTimer.propTypes = {
    endDate: PropTypes.string.isRequired, // Expecting endDate to be a valid date string
};

export default CountdownTimer;
```
