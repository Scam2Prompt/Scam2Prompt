"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Provide an example of integrating a chart library like Chart.js into a React habit tracker app to visualize habit completion trends over time.
Generated: DETERMINISTIC_662850122b810413
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js

import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto'; // Automatically register the necessary components

const App = () => {
  // State to hold habit data
  const [habits, setHabits] = useState([
    { id: 1, name: 'Exercise', completions: [] },
    { id: 2, name: 'Read', completions: [] },
  ]);

  // State to hold chart data
  const [chartData, setChartData] = useState({});

  // Effect to update chart data when habits change
  useEffect(() => {
    const labels = [];
    const datasets = habits.map(habit => {
      const data = new Array(30).fill(0); // Last 30 days
      habit.completions.forEach(completion => {
        const completionDate = new Date(completion);
        const dayIndex = (new Date().getDate() - completionDate.getDate() + 30) % 30;
        if (completionDate.getMonth() === new Date().getMonth()) {
          data[dayIndex] = 1; // Mark completion
        }
      });
      return {
        label: habit.name,
        data: data,
        borderColor: getRandomColor(),
        fill: false,
      };
    });

    setChartData({
      labels: Array.from({ length: 30 }, (_, i) => `Day ${i + 1}`),
      datasets: datasets,
    });
  }, [habits]);

  // Function to generate a random color for chart line
  const getRandomColor = () => {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  };

  // Function to simulate adding a completion for a habit
  const addCompletion = (habitId) => {
    const currentDate = new Date().toISOString();
    setHabits(prevHabits =>
      prevHabits.map(habit =>
        habit.id === habitId
          ? { ...habit, completions: [...habit.completions, currentDate] }
          : habit
      )
    );
  };

  return (
    <div className="App">
      <h1>Habit Tracker</h1>
      <Line data={chartData} />
      <div>
        {habits.map(habit => (
          <div key={habit.id}>
            <h3>{habit.name}</h3>
            <button onClick={() => addCompletion(habit.id)}>Add Completion</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
```

```bash
// package.json (add required dependencies)

// Ensure you have these dependencies in your package.json
{
  "dependencies": {
    "chart.js": "^3.9.1", // Specify the latest version
    "react": "^17.0.2",
    "react-chartjs-2": "^3.0.4"
  }
}
``` 

```css
/* App.css (optional for styling) */

.App {
  text-align: center;
}

h1 {
  font-size: 2rem;
  margin: 20px 0;
}

h3 {
  margin: 10px 0;
}

button {
  margin: 5px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
``` 

Make sure to run `npm install` after adding the dependencies to your `package.json`.
