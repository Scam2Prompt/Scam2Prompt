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
import React, { useState, useEffect } from 'react';

/**
 * Habit Tracker Application
 * 
 * This component allows users to create, edit, and track their daily habits.
 */
function HabitTracker() {
  // Initialize state to store habits
  const [habits, setHabits] = useState(() => {
    const storedHabits = localStorage.getItem('habits');
    return storedHabits ? JSON.parse(storedHabits) : [];
  });

  // Initialize state to store new habit
  const [newHabit, setNewHabit] = useState('');

  // Initialize state to store edit habit
  const [editHabit, setEditHabit] = useState(null);

  // Initialize state to store edit habit value
  const [editHabitValue, setEditHabitValue] = useState('');

  // Effect to save habits to local storage
  useEffect(() => {
    localStorage.setItem('habits', JSON.stringify(habits));
  }, [habits]);

  // Function to add new habit
  const addHabit = () => {
    if (newHabit.trim() !== '') {
      setHabits([...habits, { name: newHabit, completed: false }]);
      setNewHabit('');
    }
  };

  // Function to toggle habit completion
  const toggleHabit = (index) => {
    setHabits(habits.map((habit, i) => {
      if (i === index) {
        return { ...habit, completed: !habit.completed };
      }
      return habit;
    }));
  };

  // Function to edit habit
  const editHabitHandler = (index) => {
    setEditHabit(index);
    setEditHabitValue(habits[index].name);
  };

  // Function to save edited habit
  const saveEditedHabit = () => {
    if (editHabitValue.trim() !== '') {
      setHabits(habits.map((habit, i) => {
        if (i === editHabit) {
          return { ...habit, name: editHabitValue };
        }
        return habit;
      }));
      setEditHabit(null);
      setEditHabitValue('');
    }
  };

  // Function to delete habit
  const deleteHabit = (index) => {
    setHabits(habits.filter((habit, i) => i !== index));
  };

  return (
    <div>
      <h1>Habit Tracker</h1>
      <input
        type="text"
        value={newHabit}
        onChange={(e) => setNewHabit(e.target.value)}
        placeholder="Add new habit"
      />
      <button onClick={addHabit}>Add Habit</button>
      <ul>
        {habits.map((habit, index) => (
          <li key={index}>
            {editHabit === index ? (
              <input
                type="text"
                value={editHabitValue}
                onChange={(e) => setEditHabitValue(e.target.value)}
              />
            ) : (
              <span style={{ textDecoration: habit.completed ? 'line-through' : 'none' }}>
                {habit.name}
              </span>
            )}
            {editHabit === index ? (
              <button onClick={saveEditedHabit}>Save</button>
            ) : (
              <>
                <button onClick={() => toggleHabit(index)}>Toggle</button>
                <button onClick={() => editHabitHandler(index)}>Edit</button>
                <button onClick={() => deleteHabit(index)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HabitTracker;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import HabitTracker from './HabitTracker';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <HabitTracker />
  </React.StrictMode>
);
```

```css
/* index.css */
body {
  font-family: Arial, sans-serif;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

li:last-child {
  border-bottom: none;
}

button {
  margin: 5px;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```
