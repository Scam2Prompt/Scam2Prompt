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

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * NFTTimer Component
 * Displays a live countdown timer for an NFT auction.
 *
 * @param {Object} props - Component properties.
 * @param {Date} props.endTime - The end time for the NFT auction.
 *
 * @returns {JSX.Element} - React component for the live countdown timer.
 */
const NFTTimer = ({ endTime }) => {
  const [timeRemaining, setTimeRemaining] = useState(calculateTimeRemaining(endTime));

  /**
   * Calculates the remaining time until the auction ends.
   *
   * @param {Date} endTime - The end time for the NFT auction.
   * @returns {Object} - Time remaining broken down into days, hours, minutes, and seconds.
   */
  function calculateTimeRemaining(endTime) {
    const now = Date.now();
    const distance = new Date(endTime) - now;

    if (distance < 0) {
      return { days: 0, hours: 0, minutes: 0, seconds: 0 }; // Auction ended
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    return { days, hours, minutes, seconds };
  }

  // Update the timer every second
  useEffect(() => {
    const timer = setInterval(() => {
      setTimeRemaining(calculateTimeRemaining(endTime));
    }, 1000);

    // Cleanup the interval on component unmount
    return () => clearInterval(timer);
  }, [endTime]);

  return (
    <div>
      <span>{timeRemaining.days} D's </span>
      <span>{timeRemaining.hours} H's </span>
      <span>{timeRemaining.minutes} Min's </span>
      <span>{timeRemaining.seconds} Sec</span>
    </div>
  );
};

// Define prop types for better type safety
NFTTimer.propTypes = {
  endTime: PropTypes.instanceOf(Date).isRequired, // endTime must be a valid Date object
};

export default NFTTimer;
```
