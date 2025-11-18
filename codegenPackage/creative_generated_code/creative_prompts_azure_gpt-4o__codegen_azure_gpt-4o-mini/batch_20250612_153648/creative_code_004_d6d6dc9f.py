"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Write code to display active and past raffles dynamically on a webpage, using data fetched from a backend API.
Generated: DETERMINISTIC_d6d6dc9f38c52c40
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// RaffleDisplay.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

/**
 * RaffleDisplay component fetches and displays active and past raffles from the backend API.
 */
const RaffleDisplay = () => {
    const [activeRaffles, setActiveRaffles] = useState([]);
    const [pastRaffles, setPastRaffles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch raffles from API
    const fetchRaffles = async () => {
        try {
            const response = await axios.get('/api/raffles'); // Replace with your actual API endpoint
            const { active, past } = response.data;

            if (!Array.isArray(active) || !Array.isArray(past)) {
                throw new Error('Invalid data format from the API');
            }

            setActiveRaffles(active);
            setPastRaffles(past);
        } catch (err) {
            setError(err.message || 'Error fetching raffle data');
        } finally {
            setLoading(false);
        }
    };

    // useEffect hook to fetch data on component mount
    useEffect(() => {
        fetchRaffles();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h1>Active Raffles</h1>
            {activeRaffles.length > 0 ? (
                <ul>
                    {activeRaffles.map((raffle) => (
                        <li key={raffle.id}>{raffle.title}</li>
                    ))}
                </ul>
            ) : (
                <p>No active raffles at the moment.</p>
            )}

            <h1>Past Raffles</h1>
            {pastRaffles.length > 0 ? (
                <ul>
                    {pastRaffles.map((raffle) => (
                        <li key={raffle.id}>{raffle.title} - {new Date(raffle.date).toLocaleDateString()}</li>
                    ))}
                </ul>
            ) : (
                <p>No past raffles found.</p>
            )}
        </div>
    );
};

export default RaffleDisplay;
```

```css
/* RaffleDisplay.css */
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #f4f4f4;
    margin: 8px 0;
    padding: 10px;
    border-radius: 4px;
}
```

```javascript
// App.js
import React from 'react';
import RaffleDisplay from './RaffleDisplay';
import './RaffleDisplay.css';

/**
 * Main App component that renders the RaffleDisplay component.
 */
const App = () => {
    return (
        <div>
            <h1>Raffle Management System</h1>
            <RaffleDisplay />
        </div>
    );
};

export default App;
```

```json
// package.json
{
  "name": "raffle-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "axios": "^0.21.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

Remember to create a backend API that responds with the expected data format for this code to function correctly.
