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
// GoalTrackerApp.js
import React, { useState, useEffect } from 'react';
import './GoalTrackerApp.css';

/**
 * GoalTrackerApp Component
 * 
 * A simple goal-tracking application that allows users to set and track objectives.
 */
function GoalTrackerApp() {
  // State to store goals
  const [goals, setGoals] = useState(() => {
    const storedGoals = localStorage.getItem('goals');
    return storedGoals ? JSON.parse(storedGoals) : [];
  });

  // State to store new goal
  const [newGoal, setNewGoal] = useState('');
  const [newObjective, setNewObjective] = useState('');
  const [goalId, setGoalId] = useState(null);
  const [objectives, setObjectives] = useState({});

  // Effect to persist goals to local storage
  useEffect(() => {
    localStorage.setItem('goals', JSON.stringify(goals));
  }, [goals]);

  // Function to add goal
  const addGoal = () => {
    if (!newGoal) return;

    const goal = {
      id: Date.now(),
      text: newGoal,
      objectives: [],
      completed: false,
    };

    setGoals([...goals, goal]);
    setNewGoal('');
  };

  // Function to add objective
  const addObjective = () => {
    if (!newObjective || !goalId) return;

    const updatedGoals = goals.map((goal) => {
      if (goal.id === goalId) {
        return { ...goal, objectives: [...goal.objectives, newObjective] };
      }
      return goal;
    });

    setGoals(updatedGoals);
    setNewObjective('');
    setGoalId(null);
  };

  // Function to toggle goal completion
  const toggleGoalCompletion = (id) => {
    const updatedGoals = goals.map((goal) => {
      if (goal.id === id) {
        return { ...goal, completed: !goal.completed };
      }
      return goal;
    });

    setGoals(updatedGoals);
  };

  // Function to toggle objective completion
  const toggleObjectiveCompletion = (goalId, objective) => {
    const updatedGoals = goals.map((goal) => {
      if (goal.id === goalId) {
        const updatedObjectives = goal.objectives.map((obj) => {
          if (obj === objective) {
            return obj + ' (Completed)';
          }
          return obj;
        });

        return { ...goal, objectives: updatedObjectives };
      }
      return goal;
    });

    setGoals(updatedGoals);
  };

  // Function to delete goal
  const deleteGoal = (id) => {
    setGoals(goals.filter((goal) => goal.id !== id));
  };

  return (
    <div className="goal-tracker-app">
      <h1>Goal Tracker App</h1>

      {/* Add Goal Section */}
      <section>
        <h2>Add Goal</h2>
        <input
          type="text"
          value={newGoal}
          onChange={(e) => setNewGoal(e.target.value)}
          placeholder="Enter goal"
        />
        <button onClick={addGoal}>Add Goal</button>
      </section>

      {/* Goals List Section */}
      <section>
        <h2>Goals</h2>
        <ul>
          {goals.map((goal) => (
            <li key={goal.id}>
              <input
                type="checkbox"
                checked={goal.completed}
                onChange={() => toggleGoalCompletion(goal.id)}
              />
              <span style={{ textDecoration: goal.completed ? 'line-through' : 'none' }}>
                {goal.text}
              </span>

              {/* Objectives List */}
              <ul>
                {goal.objectives.map((objective, index) => (
                  <li key={index}>
                    <input
                      type="checkbox"
                      onChange={() => toggleObjectiveCompletion(goal.id, objective)}
                    />
                    <span>{objective.replace(' (Completed)', '')}</span>
                  </li>
                ))}
              </ul>

              {/* Add Objective Input */}
              <input
                type="text"
                value={newObjective}
                onChange={(e) => setNewObjective(e.target.value)}
                placeholder="Enter objective"
              />
              <button onClick={() => {
                setGoalId(goal.id);
                addObjective();
              }}>Add Objective</button>

              {/* Delete Goal Button */}
              <button onClick={() => deleteGoal(goal.id)}>Delete Goal</button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default GoalTrackerApp;
```

```css
/* GoalTrackerApp.css */
.goal-tracker-app {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.goal-tracker-app h1 {
  text-align: center;
}

.goal-tracker-app section {
  margin-bottom: 20px;
}

.goal-tracker-app h2 {
  margin-top: 0;
}

.goal-tracker-app input[type="text"] {
  width: 100%;
  height: 40px;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
}

.goal-tracker-app button {
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.goal-tracker-app button:hover {
  background-color: #3e8e41;
}

.goal-tracker-app ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.goal-tracker-app li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.goal-tracker-app li:last-child {
  border-bottom: none;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import GoalTrackerApp from './GoalTrackerApp';

ReactDOM.render(
  <React.StrictMode>
    <GoalTrackerApp />
  </React.StrictMode>,
  document.getElementById('root')
);
```
