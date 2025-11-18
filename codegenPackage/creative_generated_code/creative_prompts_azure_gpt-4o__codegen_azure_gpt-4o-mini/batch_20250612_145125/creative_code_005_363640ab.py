"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptosdegenflip.vercel.app
Prompt: Write code to display a countdown timer for a presale event on a blockchain-based dApp, using the Aptos ecosystem.
Generated: DETERMINISTIC_363640abe08bcc1f
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from the Aptos ecosystem
import { AptosClient, AptosAccount } from "aptos";
import React, { useEffect, useState } from "react";

// Define the CountdownTimer component
const CountdownTimer = ({ endTime }) => {
  // State to hold the remaining time
  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft(endTime));

  // Function to calculate the time left until the event
  function calculateTimeLeft(endTime) {
    const difference = +new Date(endTime) - +new Date();
    return difference > 0 ? difference : 0;
  }

  // Update the countdown every second
  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft(calculateTimeLeft(endTime));
    }, 1000);

    // Clear the timer when the component unmounts
    return () => clearInterval(timer);
  }, [endTime]);

  // Convert milliseconds to a human-readable format
  const formatTimeLeft = (milliseconds) => {
    const totalSeconds = Math.floor(milliseconds / 1000);
    const days = Math.floor(totalSeconds / (3600 * 24));
    const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    return {
      days,
      hours,
      minutes,
      seconds,
    };
  };

  // Format the time left for display
  const { days, hours, minutes, seconds } = formatTimeLeft(timeLeft);

  return (
    <div>
      <h1>Presale Countdown</h1>
      {timeLeft > 0 ? (
        <div>
          <p>{days} Days</p>
          <p>{hours} Hours</p>
          <p>{minutes} Minutes</p>
          <p>{seconds} Seconds</p>
        </div>
      ) : (
        <p>Presale has started!</p>
      )}
    </div>
  );
};

// Main App component
const App = () => {
  // Set the presale end time (Example: set for 1 day from now)
  const presaleEndTime = new Date(Date.now() + 24 * 60 * 60 * 1000);

  return (
    <div>
      <CountdownTimer endTime={presaleEndTime} />
    </div>
  );
};

// Render the App
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```
