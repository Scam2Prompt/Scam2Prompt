"""
Generated Code Metadata:
========================
Original URL: https://neftyartstudio.com
Prompt: Develop a React component for displaying live bidding timers for NFTs listed on the Neftyartstudio marketplace, such as "87 D's 23 H's 38 Min's 27 Sec."
Generated: DETERMINISTIC_fa6fb9ad5ebb4c67
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * CountdownTimer component displays a live bidding timer for NFTs.
 * 
 * @param {Object} props - Component properties
 * @param {number} props.endTime - The end time of the auction in milliseconds
 * @returns {JSX.Element} The rendered countdown timer
 */
const CountdownTimer = ({ endTime }) => {
    const [timeLeft, setTimeLeft] = useState({ days: 0, hours: 0, minutes: 0, seconds: 0 });

    useEffect(() => {
        // Function to calculate the time left until the auction ends
        const calculateTimeLeft = () => {
            const now = new Date().getTime();
            const distance = endTime - now;

            if (distance < 0) {
                // Auction has ended
                return { days: 0, hours: 0, minutes: 0, seconds: 0 };
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            return { days, hours, minutes, seconds };
        };

        // Update the timer every second
        const timerId = setInterval(() => {
            setTimeLeft(calculateTimeLeft());
        }, 1000);

        // Cleanup interval on component unmount
        return () => clearInterval(timerId);
    }, [endTime]);

    return (
        <div className="countdown-timer">
            <span>{timeLeft.days} D's </span>
            <span>{timeLeft.hours} H's </span>
            <span>{timeLeft.minutes} Min's </span>
            <span>{timeLeft.seconds} Sec</span>
        </div>
    );
};

// PropTypes for type checking
CountdownTimer.propTypes = {
    endTime: PropTypes.number.isRequired,
};

export default CountdownTimer;
```
