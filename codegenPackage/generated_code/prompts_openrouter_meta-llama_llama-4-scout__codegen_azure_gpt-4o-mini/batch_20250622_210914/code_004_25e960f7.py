"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Create a simple goal-tracking application using a JavaScript library like React, with features to set and track objectives, similar to those described on the Norbert Gabriel Management Consulting website.
Generated: DETERMINISTIC_25e960f7bdb8b752
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Importing CSS for styling

// GoalTrackingApp Component
const GoalTrackingApp = () => {
  // State to hold goals
  const [goals, setGoals] = useState([]);
  const [goalInput, setGoalInput] = useState('');

  // Function to handle input change
  const handleInputChange = (event) => {
    setGoalInput(event.target.value);
  };

  // Function to add a new goal
  const addGoal = (event) => {
    event.preventDefault(); // Prevent form submission
    if (goalInput.trim() === '') {
      alert('Please enter a valid goal.'); // Error handling for empty input
      return;
    }
    const newGoal = {
      id: Date.now(), // Unique ID for each goal
      text: goalInput,
      completed: false,
    };
    setGoals([...goals, newGoal]); // Update goals state
    setGoalInput(''); // Clear input field
  };

  // Function to toggle goal completion status
  const toggleGoalCompletion = (id) => {
    setGoals(goals.map(goal => 
      goal.id === id ? { ...goal, completed: !goal.completed } : goal
    ));
  };

  // Function to delete a goal
  const deleteGoal = (id) => {
    setGoals(goals.filter(goal => goal.id !== id)); // Remove goal from state
  };

  return (
    <div className="goal-tracking-app">
      <h1>Goal Tracking Application</h1>
      <form onSubmit={addGoal}>
        <input
          type="text"
          value={goalInput}
          onChange={handleInputChange}
          placeholder="Enter your goal"
        />
        <button type="submit">Add Goal</button>
      </form>
      <ul>
        {goals.map(goal => (
          <li key={goal.id} className={goal.completed ? 'completed' : ''}>
            <span onClick={() => toggleGoalCompletion(goal.id)}>
              {goal.text}
            </span>
            <button onClick={() => deleteGoal(goal.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Render the application
ReactDOM.render(<GoalTrackingApp />, document.getElementById('root'));
```

```css
/* index.css - Basic styling for the goal tracking application */

body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 20px;
}

.goal-tracking-app {
  max-width: 600px;
  margin: auto;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

form {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  border: none;
  background-color: #28a745;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.completed {
  text-decoration: line-through;
  color: #6c757d;
}
```

Make sure to create an `index.html` file with a root div for the React app to render into:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Goal Tracking App</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js"></script>
</body>
</html>
```

This code provides a simple goal-tracking application using React, with features to add, complete, and delete goals.
