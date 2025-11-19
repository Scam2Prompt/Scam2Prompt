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

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * NFTBiddingTimer component displays a live countdown timer for NFT auctions.
 * @param {Object} props - Component props
 * @param {string} props.endTime - ISO string representing the auction end time
 * @param {function} props.onTimerEnd - Callback when timer reaches zero
 * @param {string} [props.className] - Additional CSS class for styling
 */
const NFTBiddingTimer = ({ endTime, onTimerEnd, className = '' }) => {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0
  });
  const [hasEnded, setHasEnded] = useState(false);

  useEffect(() => {
    const calculateTimeLeft = () => {
      const endDate = new Date(endTime);
      const now = new Date();
      const difference = endDate - now;

      if (difference <= 0) {
        setHasEnded(true);
        if (onTimerEnd) onTimerEnd();
        return {
          days: 0,
          hours: 0,
          minutes: 0,
          seconds: 0
        };
      }

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
      const minutes = Math.floor((difference / 1000 / 60) % 60);
      const seconds = Math.floor((difference / 1000) % 60);

      return { days, hours, minutes, seconds };
    };

    const timer = setInterval(() => {
      setTimeLeft(calculateTimeLeft());
    }, 1000);

    // Initial calculation
    setTimeLeft(calculateTimeLeft());

    return () => clearInterval(timer);
  }, [endTime, onTimerEnd]);

  if (hasEnded) {
    return <div className={`nft-timer ended ${className}`}>Auction Ended</div>;
  }

  return (
    <div className={`nft-timer ${className}`}>
      {timeLeft.days > 0 && <span>{timeLeft.days} D's </span>}
      {timeLeft.hours > 0 && <span>{timeLeft.hours} H's </span>}
      {timeLeft.minutes > 0 && <span>{timeLeft.minutes} Min's </span>}
      <span>{timeLeft.seconds} Sec</span>
    </div>
  );
};

NFTBiddingTimer.propTypes = {
  endTime: PropTypes.string.isRequired,
  onTimerEnd: PropTypes.func,
  className: PropTypes.string
};

export default NFTBiddingTimer;
```
