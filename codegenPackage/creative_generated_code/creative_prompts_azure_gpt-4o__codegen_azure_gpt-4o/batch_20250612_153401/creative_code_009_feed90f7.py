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

```jsx
// App.jsx
import React from 'react';
import HabitTracker from './components/HabitTracker';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Main Application Wrapper */}
      <header className="bg-blue-600 text-white py-4">
        <h1 className="text-center text-2xl font-bold">Habit Tracker</h1>
      </header>
      
      <main className="p-4">
        {/* Habit Tracker Component */}
        <HabitTracker />
      </main>
    </div>
  );
}

export default App;

// components/HabitTracker.jsx
import React from 'react';

const HabitTracker = () => {
  // Example habits data
  const habits = [
    { id: 1, name: 'Drink Water', completed: true },
    { id: 2, name: 'Exercise', completed: false },
    { id: 3, name: 'Read a Book', completed: true },
  ];

  return (
    <div className="container mx-auto">
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {habits.map((habit) => (
          <div
            key={habit.id}
            className={`p-4 border rounded-lg shadow ${
              habit.completed ? 'bg-green-100' : 'bg-red-100'
            }`}
          >
            {/* Habit Name */}
            <h2 className="text-lg font-semibold">{habit.name}</h2>
            {/* Completion Status */}
            <p
              className={`text-sm ${
                habit.completed ? 'text-green-700' : 'text-red-700'
              }`}
            >
              {habit.completed ? 'Completed' : 'Pending'}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HabitTracker;

// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
};

// index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

// Required dependencies: React, Tailwind CSS
```
