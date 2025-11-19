"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Can you provide code examples for a habit tracker application built with React that utilizes JavaScript?
Generated: DETERMINISTIC_ca1daec4ca3864bf
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js

import React, { useState } from 'react';
import HabitForm from './HabitForm';
import HabitList from './HabitList';
import './App.css';

/**
 * Main component for the Habit Tracker application.
 */
const App = () => {
  const [habits, setHabits] = useState([]);

  /**
   * Adds a new habit to the list.
   * @param {string} habit - The name of the habit.
   */
  const addHabit = (habit) => {
    if (!habit) {
      alert("Habit name cannot be empty.");
      return;
    }
    setHabits([...habits, { id: Date.now(), name: habit, completed: false }]);
  };

  /**
   * Toggles the completion status of a habit.
   * @param {number} id - The id of the habit to toggle.
   */
  const toggleHabit = (id) => {
    setHabits(habits.map(habit => 
      habit.id === id ? { ...habit, completed: !habit.completed } : habit
    ));
  };

  /**
   * Removes a habit from the list.
   * @param {number} id - The id of the habit to remove.
   */
  const removeHabit = (id) => {
    setHabits(habits.filter(habit => habit.id !== id));
  };

  return (
    <div className="app">
      <h1>Habit Tracker</h1>
      <HabitForm addHabit={addHabit} />
      <HabitList habits={habits} toggleHabit={toggleHabit} removeHabit={removeHabit} />
    </div>
  );
};

export default App;
```

```javascript
// HabitForm.js

import React, { useState } from 'react';

/**
 * Form component for adding new habits.
 * @param {function} addHabit - Function to add a new habit.
 */
const HabitForm = ({ addHabit }) => {
  const [input, setInput] = useState('');

  /**
   * Handles form submission.
   * @param {event} e - The event object.
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    addHabit(input);
    setInput(''); // Clear input field after submission
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter a new habit"
        required
      />
      <button type="submit">Add Habit</button>
    </form>
  );
};

export default HabitForm;
```

```javascript
// HabitList.js

import React from 'react';

/**
 * List component to display all habits.
 * @param {Array} habits - Array of habit objects.
 * @param {function} toggleHabit - Function to toggle habit completion.
 * @param {function} removeHabit - Function to remove a habit.
 */
const HabitList = ({ habits, toggleHabit, removeHabit }) => {
  return (
    <ul>
      {habits.map(habit => (
        <li key={habit.id} className={habit.completed ? 'completed' : ''}>
          <span onClick={() => toggleHabit(habit.id)}>{habit.name}</span>
          <button onClick={() => removeHabit(habit.id)}>Remove</button>
        </li>
      ))}
    </ul>
  );
};

export default HabitList;
```

```css
/* App.css */

/* Basic styling for the habit tracker application */
.app {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

form {
  margin: 20px 0;
}

input {
  padding: 10px;
  font-size: 16px;
}

button {
  padding: 10px;
  font-size: 16px;
  margin-left: 10px;
}

.completed {
  text-decoration: line-through;
  color: grey;
}
```
