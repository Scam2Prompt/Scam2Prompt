"""
Generated Code Metadata:
========================
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Provide an example of integrating a chart library like Chart.js into a React habit tracker app to visualize habit completion trends over time.
Generated: DETERMINISTIC_662850122b810413
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// HabitTracker.js
import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';

/**
 * Habit Tracker component that displays a line chart of habit completion trends.
 */
function HabitTracker() {
  // Initialize state to store habit data
  const [habitData, setHabitData] = useState({
    labels: [],
    datasets: [{
      label: 'Habit Completion',
      data: [],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  });

  // Mock API call to fetch habit data
  useEffect(() => {
    const fetchHabitData = async () => {
      try {
        // Replace with actual API endpoint
        const response = await new Promise((resolve) => {
          setTimeout(() => {
            resolve({
              data: [
                { date: '2022-01-01', completed: 3 },
                { date: '2022-01-02', completed: 2 },
                { date: '2022-01-03', completed: 4 },
                { date: '2022-01-04', completed: 1 },
                { date: '2022-01-05', completed: 3 },
              ]
            });
          }, 1000);
        });

        const labels = response.data.map((entry) => entry.date);
        const data = response.data.map((entry) => entry.completed);

        setHabitData({
          labels,
          datasets: [{
            label: 'Habit Completion',
            data,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
          }]
        });
      } catch (error) {
        console.error('Error fetching habit data:', error);
      }
    };

    fetchHabitData();
  }, []);

  // Chart options
  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };

  return (
    <div>
      <h2>Habit Tracker</h2>
      <Line data={habitData} options={chartOptions} />
    </div>
  );
}

export default HabitTracker;
```

```jsx
// App.js
import React from 'react';
import HabitTracker from './HabitTracker';

function App() {
  return (
    <div className="App">
      <HabitTracker />
    </div>
  );
}

export default App;
```

```css
/* index.css */
body {
  font-family: Arial, sans-serif;
}

.App {
  text-align: center;
  margin-top: 50px;
}
```

```bash
# package.json
{
  "name": "habit-tracker",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "chart.js": "^3.9.1",
    "react": "^18.2.0",
    "react-chartjs-2": "^4.3.1",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
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
  }
}
```
