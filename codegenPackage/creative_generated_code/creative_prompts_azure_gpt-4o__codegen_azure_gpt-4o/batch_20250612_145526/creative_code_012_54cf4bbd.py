"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Generate code in React.js for displaying EarthMeta's token presale countdown timer and dynamically updating the EMT price based on the next stage.
Generated: DETERMINISTIC_54cf4bbdb58deed1
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';

// Function to calculate the remaining time until the presale ends
const calculateTimeLeft = (endDate) => {
  const now = new Date();
  const difference = endDate - now;
  
  if (difference <= 0) {
    return null; // Presale ended
  }

  const timeLeft = {
    days: Math.floor(difference / (1000 * 60 * 60 * 24)),
    hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
    minutes: Math.floor((difference / 1000 / 60) % 60),
    seconds: Math.floor((difference / 1000) % 60),
  };

  return timeLeft;
};

const PresaleCountdown = () => {
  // Sample presale stages with their respective end dates and EMT prices
  const presaleStages = [
    { stage: 1, endDate: new Date('2023-11-15T00:00:00'), price: 0.05 },
    { stage: 2, endDate: new Date('2023-11-20T00:00:00'), price: 0.07 },
    { stage: 3, endDate: new Date('2023-11-25T00:00:00'), price: 0.1 },
  ];

  // State for the current presale stage
  const [currentStage, setCurrentStage] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);

  useEffect(() => {
    const updateStageAndTimer = () => {
      const now = new Date();
      const activeStage = presaleStages.find(stage => now < stage.endDate);
      
      if (activeStage) {
        setCurrentStage(activeStage);
        setTimeLeft(calculateTimeLeft(activeStage.endDate));
      } else {
        setCurrentStage(null); // No active stage
        setTimeLeft(null);
      }
    };

    updateStageAndTimer();

    // Update the countdown timer every second
    const intervalId = setInterval(updateStageAndTimer, 1000);

    return () => clearInterval(intervalId); // Cleanup on component unmount
  }, [presaleStages]);

  // Render the timer and EMT price
  return (
    <div style={{ textAlign: 'center', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>EarthMeta Token Presale</h1>
      {currentStage ? (
        <>
          <h2>Stage {currentStage.stage}</h2>
          <p>Current EMT Price: ${currentStage.price.toFixed(2)}</p>
          {timeLeft ? (
            <div style={{ fontSize: '1.5rem', margin: '10px 0' }}>
              <p>Time Left:</p>
              <p>
                {timeLeft.days}d {timeLeft.hours}h {timeLeft.minutes}m {timeLeft.seconds}s
              </p>
            </div>
          ) : (
            <p>Calculating time left...</p>
          )}
        </>
      ) : (
        <h2>Presale has ended</h2>
      )}
    </div>
  );
};

export default PresaleCountdown;
```
