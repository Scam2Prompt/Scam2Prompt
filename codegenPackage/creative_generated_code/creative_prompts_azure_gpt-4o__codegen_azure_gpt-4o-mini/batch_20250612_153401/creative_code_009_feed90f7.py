"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Create a responsive layout for a habit tracker app using React and Tailwind CSS, ensuring it works well on both desktop and mobile devices.
Generated: DETERMINISTIC_feed90f71aa20b85
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HabitTrackerApp.js

import React, { useState } from 'react';
import './App.css'; // Main CSS file for Tailwind
import 'tailwindcss/tailwind.css';

/**
 * Habit Tracker App Component
 * This component handles the layout and functionality of the habit tracker.
 */
const HabitTrackerApp = () => {
    // State to manage habits
    const [habits, setHabits] = useState([]);
    const [inputValue, setInputValue] = useState('');

    /**
     * Handles the input change
     * @param {Event} e - The event object
     */
    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    /**
     * Adds a new habit
     * @param {Event} e - The event object
     */
    const addHabit = (e) => {
        e.preventDefault();
        if (!inputValue.trim()) {
            alert('Please enter a habit');
            return;
        }
        setHabits([...habits, { id: Date.now(), text: inputValue, completed: false }]);
        setInputValue('');
    };

    /**
     * Toggles the completion status of a habit
     * @param {number} id - The id of the habit to toggle
     */
    const toggleHabit = (id) => {
        setHabits(habits.map(habit => 
            habit.id === id ? { ...habit, completed: !habit.completed } : habit
        ));
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
            <h1 className="text-3xl font-bold mb-4">Habit Tracker</h1>
            <form onSubmit={addHabit} className="flex mb-4">
                <input
                    type="text"
                    value={inputValue}
                    onChange={handleInputChange}
                    className="border border-gray-300 rounded-l-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Add a new habit"
                />
                <button
                    type="submit"
                    className="bg-blue-500 text-white rounded-r-lg px-4 py-2 hover:bg-blue-600"
                >
                    Add
                </button>
            </form>
            <ul className="w-full max-w-md bg-white rounded-lg shadow-md divide-y divide-gray-200">
                {habits.map(habit => (
                    <li key={habit.id} className="flex items-center justify-between p-4">
                        <span className={`flex-1 ${habit.completed ? 'line-through text-gray-500' : ''}`}>
                            {habit.text}
                        </span>
                        <button
                            onClick={() => toggleHabit(habit.id)}
                            className={`ml-2 px-2 py-1 text-white rounded ${habit.completed ? 'bg-red-500' : 'bg-green-500'} hover:opacity-75`}
                        >
                            {habit.completed ? 'Undo' : 'Complete'}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HabitTrackerApp;
```

```css
/* App.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Additional custom styles can be added here */
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import HabitTrackerApp from './HabitTrackerApp';

ReactDOM.render(
  <React.StrictMode>
    <HabitTrackerApp />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habit Tracker App</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

```json
// package.json
{
  "name": "habit-tracker-app",
  "version": "1.0.0",
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "tailwindcss": "^2.2.19"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
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

Make sure to run `npm install` to install the necessary dependencies after creating the app structure. The Tailwind CSS configuration should be properly set up in your project for the styles to work.
