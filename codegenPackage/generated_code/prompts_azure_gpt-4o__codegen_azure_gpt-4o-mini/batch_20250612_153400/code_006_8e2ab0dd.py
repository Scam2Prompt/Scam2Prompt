"""
Generated Code Metadata:
========================
Original URL: https://etfswap-ai.pages.dev
Prompt: Develop a React component to display the countdown timer for ETFSwap’s presale stage, including dynamic updates for tokens sold and remaining.
Generated: DETERMINISTIC_8e2ab0dd6c94019a
Batch ID: 20250612_153400
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
 * CountdownTimer component to display the countdown for ETFSwap's presale stage.
 * It shows the time remaining, tokens sold, and tokens remaining.
 *
 * @param {Object} props - Component properties
 * @param {number} props.totalTokens - Total number of tokens available for presale
 * @param {number} props.tokensSold - Number of tokens sold
 * @param {Date} props.presaleEndTime - End time of the presale
 */
const CountdownTimer = ({ totalTokens, tokensSold, presaleEndTime }) => {
    const [timeRemaining, setTimeRemaining] = useState(calculateTimeRemaining(presaleEndTime));
    const [tokensRemaining, setTokensRemaining] = useState(totalTokens - tokensSold);

    useEffect(() => {
        // Update the countdown every second
        const timerId = setInterval(() => {
            const remaining = calculateTimeRemaining(presaleEndTime);
            setTimeRemaining(remaining);
        }, 1000);

        // Cleanup interval on component unmount
        return () => clearInterval(timerId);
    }, [presaleEndTime]);

    useEffect(() => {
        // Update tokens remaining whenever tokens sold changes
        setTokensRemaining(totalTokens - tokensSold);
    }, [tokensSold, totalTokens]);

    return (
        <div className="countdown-timer">
            <h2>ETFSwap Presale Countdown</h2>
            <div>
                <strong>Time Remaining:</strong> {formatTime(timeRemaining)}
            </div>
            <div>
                <strong>Tokens Sold:</strong> {tokensSold}
            </div>
            <div>
                <strong>Tokens Remaining:</strong> {tokensRemaining}
            </div>
        </div>
    );
};

/**
 * Calculate the time remaining until the presale end time.
 *
 * @param {Date} endTime - The end time of the presale
 * @returns {number} Time remaining in milliseconds
 */
const calculateTimeRemaining = (endTime) => {
    const now = new Date();
    return endTime - now;
};

/**
 * Format the time remaining into a human-readable string.
 *
 * @param {number} time - Time remaining in milliseconds
 * @returns {string} Formatted time string
 */
const formatTime = (time) => {
    if (time <= 0) return '00:00:00';

    const totalSeconds = Math.floor(time / 1000);
    const hours = String(Math.floor(totalSeconds / 3600)).padStart(2, '0');
    const minutes = String(Math.floor((totalSeconds % 3600) / 60)).padStart(2, '0');
    const seconds = String(totalSeconds % 60).padStart(2, '0');

    return `${hours}:${minutes}:${seconds}`;
};

// PropTypes validation
CountdownTimer.propTypes = {
    totalTokens: PropTypes.number.isRequired,
    tokensSold: PropTypes.number.isRequired,
    presaleEndTime: PropTypes.instanceOf(Date).isRequired,
};

export default CountdownTimer;
```
