"""
Generated Code Metadata:
========================
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Can you provide code examples for a habit tracker application built with React that utilizes JavaScript?
Generated: DETERMINISTIC_ca1daec4ca3864bf
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HabitTracker.js
import React, { useState } from 'react';

// HabitTracker component
const HabitTracker = () => {
  // State to hold the list of habits
  const [habits, setHabits] = useState([]);
  // State to hold the new habit input
  const [newHabit, setNewHabit] = useState('');

  // Function to handle adding a new habit
  const addHabit = (e) => {
    e.preventDefault();
    if (!newHabit.trim()) {
      alert('Please enter a habit.'); // Error handling for empty input
      return;
    }
    setHabits([...habits, { id: Date.now(), name: newHabit, completed: false }]);
    setNewHabit(''); // Clear input after adding
  };

  // Function to toggle the completion status of a habit
  const toggleHabit = (id) => {
    setHabits(habits.map(habit => 
      habit.id === id ? { ...habit, completed: !habit.completed } : habit
    ));
  };

  // Function to delete a habit
  const deleteHabit = (id) => {
    setHabits(habits.filter(habit => habit.id !== id));
  };

  return (
    <div className="habit-tracker">
      <h1>Habit Tracker</h1>
      <form onSubmit={addHabit}>
        <input
          type="text"
          value={newHabit}
          onChange={(e) => setNewHabit(e.target.value)}
          placeholder="Enter a new habit"
        />
        <button type="submit">Add Habit</button>
      </form>
      <ul>
        {habits.map(habit => (
          <li key={habit.id} className={habit.completed ? 'completed' : ''}>
            <span onClick={() => toggleHabit(habit.id)}>{habit.name}</span>
            <button onClick={() => deleteHabit(habit.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HabitTracker;

// App.js
import React from 'react';
import HabitTracker from './HabitTracker';
import './App.css'; // Importing CSS for styling

// Main App component
const App = () => {
  return (
    <div className="app">
      <HabitTracker />
    </div>
  );
};

export default App;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css'; // Importing global styles

// Rendering the App component into the root element
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* App.css */
.habit-tracker {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}

.completed {
  text-decoration: line-through;
  color: gray;
}

button {
  margin-left: 10px;
}
```

```css
/* index.css */
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 20px;
}
```
