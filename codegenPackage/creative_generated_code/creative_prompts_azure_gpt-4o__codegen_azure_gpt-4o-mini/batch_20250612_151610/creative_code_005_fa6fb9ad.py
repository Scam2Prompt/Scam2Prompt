"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neftyartstudio.com
Prompt: Develop a React component for displaying live bidding timers for NFTs listed on the Neftyartstudio marketplace, such as "87 D's 23 H's 38 Min's 27 Sec."
Generated: DETERMINISTIC_fa6fb9ad5ebb4c67
Batch ID: 20250612_151610
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
 * Timer component to display live auction countdown for NFTs.
 * @param {Object} props - The properties passed to the component.
 * @param {number} props.endTime - The end time of the auction in milliseconds.
 * @returns {JSX.Element} The rendered Timer component.
 */
const LiveBiddingTimer = ({ endTime }) => {
    const [timeLeft, setTimeLeft] = useState(calculateTimeLeft(endTime));

    useEffect(() => {
        // Update the timer every second
        const timerId = setInterval(() => {
            const newTimeLeft = calculateTimeLeft(endTime);
            setTimeLeft(newTimeLeft);
        }, 1000);

        // Clear the interval on component unmount
        return () => clearInterval(timerId);
    }, [endTime]);

    /**
     * Calculates the time left until the auction ends.
     * @param {number} targetTime - The end time of the auction in milliseconds.
     * @returns {Object} An object containing days, hours, minutes, and seconds.
     */
    const calculateTimeLeft = (targetTime) => {
        const now = Date.now();
        const difference = targetTime - now;

        if (difference <= 0) {
            return { days: 0, hours: 0, minutes: 0, seconds: 0 };
        }

        const seconds = Math.floor((difference / 1000) % 60);
        const minutes = Math.floor((difference / 1000 / 60) % 60);
        const hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
        const days = Math.floor(difference / (1000 * 60 * 60 * 24));

        return { days, hours, minutes, seconds };
    };

    return (
        <div className="live-bidding-timer">
            {timeLeft.days} D's {timeLeft.hours} H's {timeLeft.minutes} Min's {timeLeft.seconds} Sec's
        </div>
    );
};

// PropTypes for type-checking
LiveBiddingTimer.propTypes = {
    endTime: PropTypes.number.isRequired,
};

export default LiveBiddingTimer;
```
