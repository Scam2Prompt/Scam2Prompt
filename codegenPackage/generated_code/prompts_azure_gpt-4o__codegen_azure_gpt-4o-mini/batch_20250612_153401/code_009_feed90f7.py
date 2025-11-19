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

```javascript
// src/App.js
import React from 'react';
import HabitTracker from './components/HabitTracker';
import './App.css'; // Import Tailwind CSS

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <HabitTracker />
    </div>
  );
};

export default App;
```

```javascript
// src/components/HabitTracker.js
import React, { useState } from 'react';

// HabitTracker component to manage and display habits
const HabitTracker = () => {
  const [habits, setHabits] = useState([]);
  const [habitInput, setHabitInput] = useState('');

  // Function to add a new habit
  const addHabit = (e) => {
    e.preventDefault();
    if (!habitInput) return; // Prevent adding empty habits
    setHabits([...habits, { name: habitInput, completed: false }]);
    setHabitInput(''); // Clear input field
  };

  // Function to toggle habit completion
  const toggleHabit = (index) => {
    const updatedHabits = habits.map((habit, i) => 
      i === index ? { ...habit, completed: !habit.completed } : habit
    );
    setHabits(updatedHabits);
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md">
      <h1 className="text-2xl font-bold mb-4">Habit Tracker</h1>
      <form onSubmit={addHabit} className="flex mb-4">
        <input
          type="text"
          value={habitInput}
          onChange={(e) => setHabitInput(e.target.value)}
          className="border border-gray-300 rounded-l-md p-2 flex-grow"
          placeholder="Add a new habit"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white rounded-r-md p-2 hover:bg-blue-600"
        >
          Add
        </button>
      </form>
      <ul className="space-y-2">
        {habits.map((habit, index) => (
          <li
            key={index}
            className={`flex justify-between items-center p-2 border-b ${habit.completed ? 'line-through text-gray-500' : ''}`}
            onClick={() => toggleHabit(index)}
          >
            {habit.name}
            <span className="cursor-pointer text-blue-500 hover:text-blue-600">
              {habit.completed ? 'Undo' : 'Complete'}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HabitTracker;
```

```css
/* src/App.css */
/* Import Tailwind CSS styles */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```json
// package.json (relevant parts)
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "tailwindcss": "^3.0.0",
    "postcss": "^8.0.0",
    "autoprefixer": "^10.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

```bash
# Tailwind CSS setup commands
npx tailwindcss init -p
```

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
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

This code provides a responsive habit tracker app using React and Tailwind CSS, ensuring it is well-structured, documented, and ready for production.
