"""
Generated Code Metadata:
========================
Original URL: https://babydoge-reward.web.app
Prompt: Design a basic UI component for a token locker feature using React, inspired by Baby Doge Swap's Free Token Locker.
Generated: DETERMINISTIC_b3295e4dd9a68fb2
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// TokenLocker.js
import React, { useState, useEffect } from 'react';
import './TokenLocker.css';

/**
 * Token Locker component
 * 
 * @param {object} props
 * @param {string} props.tokenName - Name of the token
 * @param {string} props.tokenSymbol - Symbol of the token
 * @param {number} props.lockedAmount - Amount of tokens locked
 * @param {number} props.lockDuration - Duration of the lock in seconds
 * @param {function} props.onUnlock - Callback function for unlock
 */
function TokenLocker(props) {
  const [timeLeft, setTimeLeft] = useState(props.lockDuration);
  const [isLocked, setIsLocked] = useState(true);
  const [unlocking, setUnlocking] = useState(false);

  useEffect(() => {
    let intervalId;
    if (isLocked) {
      intervalId = setInterval(() => {
        if (timeLeft > 0) {
          setTimeLeft(timeLeft - 1);
        } else {
          setIsLocked(false);
        }
      }, 1000);
    }
    return () => clearInterval(intervalId);
  }, [isLocked, timeLeft]);

  const handleUnlock = async () => {
    setUnlocking(true);
    try {
      await props.onUnlock();
      setIsLocked(false);
      setUnlocking(false);
    } catch (error) {
      console.error('Error unlocking token:', error);
      setUnlocking(false);
    }
  };

  return (
    <div className="token-locker">
      <h2>{props.tokenName} ({props.tokenSymbol})</h2>
      <p>Locked Amount: {props.lockedAmount}</p>
      {isLocked ? (
        <div>
          <p>Time Left: {timeLeft} seconds</p>
          <button onClick={handleUnlock} disabled={unlocking}>
            {unlocking ? 'Unlocking...' : 'Unlock'}
          </button>
        </div>
      ) : (
        <p>Token unlocked</p>
      )}
    </div>
  );
}

export default TokenLocker;
```

```css
/* TokenLocker.css */
.token-locker {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.token-locker h2 {
  margin-top: 0;
}

.token-locker button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.token-locker button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
```

```jsx
// App.js
import React from 'react';
import TokenLocker from './TokenLocker';

function App() {
  const handleUnlock = async () => {
    // Implement unlock logic here
    console.log('Token unlocked');
  };

  return (
    <div>
      <TokenLocker
        tokenName="Baby Doge"
        tokenSymbol="BDOGE"
        lockedAmount={1000}
        lockDuration={60} // 1 minute
        onUnlock={handleUnlock}
      />
    </div>
  );
}

export default App;
```
