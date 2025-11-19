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
// HabitTrackerApp.jsx
import React, { useState } from "react";
import HabitList from "./HabitList";
import AddHabitForm from "./AddHabitForm";

// Main Habit Tracker Application Component
const HabitTrackerApp = () => {
  const [habits, setHabits] = useState([]);

  // Handle adding a new habit to the list
  const addHabit = (habitName) => {
    if (!habitName.trim()) return; // Validate input
    const newHabit = { id: Date.now(), name: habitName, completed: false };
    setHabits([...habits, newHabit]);
  };

  // Handle toggling the completion status of a habit
  const toggleHabitCompletion = (id) => {
    const updatedHabits = habits.map((habit) =>
      habit.id === id ? { ...habit, completed: !habit.completed } : habit
    );
    setHabits(updatedHabits);
  };

  // Handle deleting a habit
  const deleteHabit = (id) => {
    const filteredHabits = habits.filter((habit) => habit.id !== id);
    setHabits(filteredHabits);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Habit Tracker</h1>
      <AddHabitForm addHabit={addHabit} />
      <HabitList
        habits={habits}
        toggleHabitCompletion={toggleHabitCompletion}
        deleteHabit={deleteHabit}
      />
    </div>
  );
};

export default HabitTrackerApp;
```

```javascript
// AddHabitForm.jsx
import React, { useState } from "react";

// Component for adding a new habit
const AddHabitForm = ({ addHabit }) => {
  const [habitName, setHabitName] = useState("");

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    addHabit(habitName); // Call parent handler to add habit
    setHabitName(""); // Reset input field
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <input
        type="text"
        placeholder="Enter new habit"
        value={habitName}
        onChange={(e) => setHabitName(e.target.value)}
        style={{ padding: "10px", width: "200px" }}
      />
      <button type="submit" style={{ padding: "10px", marginLeft: "10px" }}>
        Add Habit
      </button>
    </form>
  );
};

export default AddHabitForm;
```

```javascript
// HabitList.jsx
import React from "react";

// Component for displaying the list of habits
const HabitList = ({ habits, toggleHabitCompletion, deleteHabit }) => {
  if (habits.length === 0) {
    return <p>No habits added yet. Start by adding a new habit!</p>;
  }

  return (
    <ul style={{ listStyleType: "none", padding: 0 }}>
      {habits.map((habit) => (
        <li
          key={habit.id}
          style={{
            display: "flex",
            alignItems: "center",
            padding: "10px 0",
            borderBottom: "1px solid #ccc",
          }}
        >
          <span
            style={{
              textDecoration: habit.completed ? "line-through" : "none",
              flex: 1,
              cursor: "pointer",
            }}
            onClick={() => toggleHabitCompletion(habit.id)}
          >
            {habit.name}
          </span>
          <button
            style={{ backgroundColor: "red", color: "white", padding: "5px" }}
            onClick={() => deleteHabit(habit.id)}
          >
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
};

export default HabitList;
```

```javascript
// index.js
import React from "react";
import ReactDOM from "react-dom";
import HabitTrackerApp from "./HabitTrackerApp";

// Render the Habit Tracker Application to the DOM
ReactDOM.render(
  <React.StrictMode>
    <HabitTrackerApp />
  </React.StrictMode>,
  document.getElementById("root")
);
```

```javascript
// package.json (script for dependencies reference, not runnable code)
{
  "name": "habit-tracker-app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "^5.0.0"
  }
}
```
