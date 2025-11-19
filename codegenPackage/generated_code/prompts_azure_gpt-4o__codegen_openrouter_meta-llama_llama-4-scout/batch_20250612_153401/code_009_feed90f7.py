"""
Generated Code Metadata:
========================
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Create a responsive layout for a habit tracker app using React and Tailwind CSS, ensuring it works well on both desktop and mobile devices.
Generated: DETERMINISTIC_feed90f71aa20b85
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// HabitTrackerApp.js
import React, { useState } from 'react';
import './HabitTrackerApp.css';

/**
 * Habit Tracker App component.
 * 
 * @returns {JSX.Element} The Habit Tracker App component.
 */
function HabitTrackerApp() {
  // State to store habits
  const [habits, setHabits] = useState([
    { id: 1, name: 'Exercise', completed: false },
    { id: 2, name: 'Meditate', completed: false },
    { id: 3, name: 'Read', completed: false },
  ]);

  // Function to toggle habit completion
  const toggleHabitCompletion = (id) => {
    setHabits((prevHabits) =>
      prevHabits.map((habit) =>
        habit.id === id ? { ...habit, completed: !habit.completed } : habit
      )
    );
  };

  return (
    <div className="max-w-4xl mx-auto p-4 sm:p-6 md:p-8 mt-10 bg-white rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">Habit Tracker</h1>
      <ul>
        {habits.map((habit) => (
          <li
            key={habit.id}
            className={`py-2 ${
              habit.completed ? 'bg-green-100' : 'bg-gray-100'
            } rounded-lg mb-2`}
          >
            <span
              className={`px-4 py-2 ${
                habit.completed ? 'text-green-600' : 'text-gray-600'
              }`}
            >
              {habit.name}
            </span>
            <button
              className={`ml-2 px-4 py-2 ${
                habit.completed ? 'bg-red-500' : 'bg-blue-500'
              } text-white rounded-lg hover:bg-red-700 hover:bg-blue-700`}
              onClick={() => toggleHabitCompletion(habit.id)}
            >
              {habit.completed ? 'Not Completed' : 'Completed'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HabitTrackerApp;
```

```css
/* HabitTrackerApp.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import HabitTrackerApp from './HabitTrackerApp';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <HabitTrackerApp />
  </React.StrictMode>
);
```

```bash
#tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
