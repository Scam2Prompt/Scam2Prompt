"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: How can I create a habit tracker using React that requires JavaScript to function properly?
Generated: DETERMINISTIC_fc628d115cb5bc46
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: HabitTrackerApp.jsx

import React, { useState } from 'react';

// Functional component for individual habit item
const HabitItem = ({ habit, toggleCompletion, deleteHabit }) => {
  return (
    <div style={styles.habitItem}>
      <span
        style={{
          textDecoration: habit.completed ? 'line-through' : 'none',
          cursor: 'pointer',
        }}
        onClick={() => toggleCompletion(habit.id)}
      >
        {habit.name}
      </span>
      <button style={styles.deleteButton} onClick={() => deleteHabit(habit.id)}>
        Delete
      </button>
    </div>
  );
};

// Main Habit Tracker App component
const HabitTrackerApp = () => {
  // State to manage habits
  const [habits, setHabits] = useState([]);
  const [newHabit, setNewHabit] = useState('');

  // Function to add a new habit
  const addHabit = () => {
    if (!newHabit.trim()) {
      alert('Habit name cannot be empty');
      return;
    }

    const newHabitObj = {
      id: Date.now(), // Unique ID for each habit
      name: newHabit.trim(),
      completed: false,
    };

    setHabits([...habits, newHabitObj]);
    setNewHabit(''); // Clear the input field
  };

  // Function to toggle the completion status of a habit
  const toggleCompletion = (id) => {
    setHabits(
      habits.map((habit) =>
        habit.id === id ? { ...habit, completed: !habit.completed } : habit
      )
    );
  };

  // Function to delete a habit
  const deleteHabit = (id) => {
    setHabits(habits.filter((habit) => habit.id !== id));
  };

  return (
    <div style={styles.container}>
      <h1>Habit Tracker</h1>
      <div style={styles.inputContainer}>
        <input
          type="text"
          value={newHabit}
          onChange={(e) => setNewHabit(e.target.value)}
          placeholder="Enter a new habit"
          style={styles.inputField}
        />
        <button onClick={addHabit} style={styles.addButton}>
          Add Habit
        </button>
      </div>
      <div style={styles.habitsList}>
        {habits.length > 0 ? (
          habits.map((habit) => (
            <HabitItem
              key={habit.id}
              habit={habit}
              toggleCompletion={toggleCompletion}
              deleteHabit={deleteHabit}
            />
          ))
        ) : (
          <p>No habits added yet. Start tracking!</p>
        )}
      </div>
    </div>
  );
};

// CSS-in-JS styles for components
const styles = {
  container: {
    maxWidth: '600px',
    margin: '0 auto',
    padding: '20px',
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
  },
  inputContainer: {
    marginBottom: '20px',
  },
  inputField: {
    padding: '10px',
    width: '70%',
    marginRight: '10px',
    fontSize: '16px',
  },
  addButton: {
    padding: '10px 15px',
    fontSize: '16px',
    cursor: 'pointer',
  },
  habitsList: {
    marginTop: '20px',
    textAlign: 'left',
  },
  habitItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '10px',
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
  },
  deleteButton: {
    padding: '5px 10px',
    fontSize: '14px',
    cursor: 'pointer',
    color: '#fff',
    backgroundColor: '#f44336',
    border: 'none',
    borderRadius: '4px',
  },
};

// Export the component
export default HabitTrackerApp;

// Usage:
// Import and render <HabitTrackerApp /> in your main React application file (e.g., App.jsx or index.jsx).
```
