"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Develop a React component to display the countdown timer for ETFSwap’s presale stage, including dynamic updates for tokens sold and remaining.
Generated: DETERMINISTIC_8e2ab0dd6c94019a
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from "react";

/**
 * CountdownTimer Component
 * Displays the countdown timer for ETFSwap's presale stage, including dynamic updates 
 * for tokens sold and remaining.
 */
const CountdownTimer = ({ endTime, totalTokens, tokensSold }) => {
  // State for countdown timer
  const [timeRemaining, setTimeRemaining] = useState({});
  // State for tokens remaining
  const [tokensRemaining, setTokensRemaining] = useState(totalTokens - tokensSold);

  /**
   * Function to calculate the remaining time until the presale ends.
   */
  const calculateTimeRemaining = () => {
    const now = new Date();
    const end = new Date(endTime);
    const diff = end - now;

    if (diff <= 0) {
      return { days: 0, hours: 0, minutes: 0, seconds: 0 };
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    return { days, hours, minutes, seconds };
  };

  /**
   * Effect to update the countdown every second.
   */
  useEffect(() => {
    const timerId = setInterval(() => {
      setTimeRemaining(calculateTimeRemaining());
    }, 1000);

    // Cleanup interval on component unmount
    return () => clearInterval(timerId);
  }, [endTime]);

  /**
   * Effect to update tokens remaining dynamically when `tokensSold` changes.
   */
  useEffect(() => {
    if (tokensSold <= totalTokens) {
      setTokensRemaining(totalTokens - tokensSold);
    } else {
      setTokensRemaining(0);
    }
  }, [tokensSold, totalTokens]);

  return (
    <div style={styles.container}>
      <h1>ETFSwap Presale Countdown</h1>
      <div style={styles.timer}>
        <div style={styles.timeUnit}>
          <span style={styles.value}>{timeRemaining.days}</span>
          <span style={styles.label}>Days</span>
        </div>
        <div style={styles.timeUnit}>
          <span style={styles.value}>{timeRemaining.hours}</span>
          <span style={styles.label}>Hours</span>
        </div>
        <div style={styles.timeUnit}>
          <span style={styles.value}>{timeRemaining.minutes}</span>
          <span style={styles.label}>Minutes</span>
        </div>
        <div style={styles.timeUnit}>
          <span style={styles.value}>{timeRemaining.seconds}</span>
          <span style={styles.label}>Seconds</span>
        </div>
      </div>
      <div style={styles.tokens}>
        <p style={styles.tokensSold}>
          Tokens Sold: <span>{tokensSold}</span>
        </p>
        <p style={styles.tokensRemaining}>
          Tokens Remaining: <span>{tokensRemaining}</span>
        </p>
      </div>
    </div>
  );
};

// Inline styles for the component
const styles = {
  container: {
    textAlign: "center",
    padding: 20,
    fontFamily: "Arial, sans-serif",
    backgroundColor: "#f9f9f9",
    borderRadius: 10,
    boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.1)",
  },
  timer: {
    display: "flex",
    justifyContent: "center",
    gap: 20,
    marginTop: 20,
  },
  timeUnit: {
    textAlign: "center",
    padding: 10,
    backgroundColor: "#ececec",
    borderRadius: 8,
    minWidth: 80,
  },
  value: {
    fontSize: 24,
    fontWeight: "bold",
  },
  label: {
    fontSize: 14,
    color: "#555",
  },
  tokens: {
    marginTop: 30,
  },
  tokensSold: {
    fontSize: 16,
    color: "#333",
  },
  tokensRemaining: {
    fontSize: 16,
    color: "#333",
    fontWeight: "bold",
  },
};

// PropType validation
CountdownTimer.propTypes = {
  endTime: (props, propName) => {
    if (!Date.parse(props[propName])) {
      return new Error(`${propName} must be a valid date string.`);
    }
    return null;
  },
  totalTokens: (props, propName) => {
    if (typeof props[propName] !== "number" || props[propName] <= 0) {
      return new Error(`${propName} must be a positive number.`);
    }
    return null;
  },
  tokensSold: (props, propName) => {
    if (typeof props[propName] !== "number" || props[propName] < 0) {
      return new Error(`${propName} must be a non-negative number.`);
    }
    return null;
  },
};

export default CountdownTimer;
```
