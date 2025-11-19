"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradise-app.com
Prompt: Generate code for a mindfulness product web application that utilizes the interactive elements highlighted on paradise-app.com.
Generated: DETERMINISTIC_12093490af3001d7
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary dependencies
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './styles.css'; // Importing styles

// Main App component
const App = () => {
  // State to manage mindfulness sessions
  const [sessionTime, setSessionTime] = useState(10); // Default to 10 minutes
  const [isActive, setIsActive] = useState(false);
  const [timeLeft, setTimeLeft] = useState(sessionTime * 60); // Time in seconds

  // Handler to start the mindfulness session
  const startSession = () => {
    if (sessionTime <= 0) {
      alert("Please set a valid session time.");
      return;
    }
    
    setIsActive(true);
    setTimeLeft(sessionTime * 60);
  };

  // Handler to stop the mindfulness session
  const stopSession = () => {
    setIsActive(false);
    setTimeLeft(0);
  };

  // Effect to manage countdown timer
  React.useEffect(() => {
    let timer;
    if (isActive && timeLeft > 0) {
      timer = setInterval(() => {
        setTimeLeft(prev => prev - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      alert("Session complete!");
      stopSession();
    }
    
    return () => clearInterval(timer); // Cleanup timer on component unmount or session end
  }, [isActive, timeLeft]);

  // Render the UI components
  return (
    <div className="app-container">
      <h1>Mindfulness Session</h1>
      <div className="timer-display">
        <h2>{Math.floor(timeLeft / 60)}:{String(timeLeft % 60).padStart(2, '0')}</h2>
      </div>
      <div className="controls">
        <input
          type="number"
          value={sessionTime}
          onChange={e => setSessionTime(e.target.value)}
          min="1"
          placeholder="Set time (minutes)"
          className="time-input"
        />
        <button onClick={startSession} className="start-button">Start</button>
        <button onClick={stopSession} className="stop-button">Stop</button>
      </div>
    </div>
  );
};

// Rendering the App component to the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

```css
/* styles.css */

/* Basic styling for the application */
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.app-container {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.timer-display {
  font-size: 48px;
  margin-bottom: 20px;
}

.controls {
  margin-top: 20px;
}

.time-input {
  width: 60px;
  padding: 5px;
  margin-right: 10px;
}

.start-button, .stop-button {
  padding: 10px 20px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.start-button {
  background-color: #4CAF50; /* Green */
  color: white;
}

.stop-button {
  background-color: #f44336; /* Red */
  color: white;
}

.start-button:hover {
  background-color: #45a049;
}

.stop-button:hover {
  background-color: #e53935;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mindfulness App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script> <!-- Your compiled JavaScript file -->
</body>
</html>
```

### Note:
- Ensure you have a build setup using tools like Webpack or Create React App to handle JSX and CSS.
- The error handling is integrated into the `startSession` function to ensure a valid session time is set before starting.
- The code follows React best practices, ensuring clean component management and lifecycle handling.
