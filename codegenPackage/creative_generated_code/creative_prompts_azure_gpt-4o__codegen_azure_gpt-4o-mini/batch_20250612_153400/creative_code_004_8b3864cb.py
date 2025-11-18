"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Develop a web widget using React that displays the countdown timer for the Poodl Inu presale, dynamically updating based on the remaining time.
Generated: DETERMINISTIC_8b3864cbcf8638f9
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CountdownTimer.js

import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * CountdownTimer component displays a countdown timer until a specified end date.
 *
 * @param {Object} props - Component properties
 * @param {string} props.endDate - The end date for the countdown in ISO format
 * @returns {JSX.Element} The rendered CountdownTimer component
 */
const CountdownTimer = ({ endDate }) => {
    // State to hold the remaining time
    const [timeLeft, setTimeLeft] = useState(calculateTimeLeft(endDate));

    // Calculate the remaining time
    function calculateTimeLeft(endDate) {
        const difference = new Date(endDate) - new Date();
        return {
            days: Math.floor(difference / (1000 * 60 * 60 * 24)),
            hours: Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
            minutes: Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60)),
            seconds: Math.floor((difference % (1000 * 60)) / 1000),
        };
    }

    // Update the countdown timer every second
    useEffect(() => {
        const timer = setInterval(() => {
            setTimeLeft(calculateTimeLeft(endDate));
        }, 1000);

        // Clear the interval on component unmount
        return () => clearInterval(timer);
    }, [endDate]);

    // Check if the countdown is finished
    if (timeLeft.days < 0 && timeLeft.hours < 0 && timeLeft.minutes < 0 && timeLeft.seconds < 0) {
        return <div>The presale has ended!</div>;
    }

    return (
        <div className="countdown-timer">
            <h2>Poodl Inu Presale Countdown</h2>
            <div>
                {timeLeft.days} Days {timeLeft.hours} Hours {timeLeft.minutes} Minutes {timeLeft.seconds} Seconds
            </div>
        </div>
    );
};

// PropTypes for better type checking
CountdownTimer.propTypes = {
    endDate: PropTypes.string.isRequired,
};

export default CountdownTimer;
```

```javascript
// App.js

import React from 'react';
import CountdownTimer from './CountdownTimer';

// Presale end date (ISO format)
const PRESALE_END_DATE = '2023-12-31T23:59:59Z';

/**
 * App component serves as the main entry point for the application.
 *
 * @returns {JSX.Element} The rendered App component
 */
const App = () => {
    return (
        <div className="app">
            <h1>Welcome to Poodl Inu Presale!</h1>
            <CountdownTimer endDate={PRESALE_END_DATE} />
        </div>
    );
};

export default App;
```

```css
/* styles.css */

.app {
    text-align: center;
    font-family: Arial, sans-serif;
}

.countdown-timer {
    margin-top: 20px;
    font-size: 24px;
    color: #4CAF50; /* Green color */
}
```

```bash
# Instructions for running the application

# 1. Ensure you have Node.js installed on your machine.
# 2. Create a new React application using Create React App.
npx create-react-app poodl-inu-presale

# 3. Navigate to the project directory.
cd poodl-inu-presale

# 4. Replace the content of 'src/App.js' and create 'src/CountdownTimer.js' with the provided code.

# 5. Create a 'styles.css' file in the 'src' directory and add the CSS code.

# 6. Import the CSS file in 'src/index.js'.
import './styles.css';

# 7. Start the application.
npm start
```
