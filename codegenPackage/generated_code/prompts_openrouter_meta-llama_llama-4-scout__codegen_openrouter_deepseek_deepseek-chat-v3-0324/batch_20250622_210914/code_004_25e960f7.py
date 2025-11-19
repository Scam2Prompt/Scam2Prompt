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
 * Goal Tracker Application Component
 * Allows users to create, track, and manage their goals
 */
const GoalTrackerApp = () => {
  const [goals, setGoals] = useState([]);
  const [newGoal, setNewGoal] = useState({
    title: '',
    description: '',
    targetDate: '',
    status: 'Not Started'
  });
  const [filter, setFilter] = useState('All');

  // Load goals from localStorage on component mount
  useEffect(() => {
    const savedGoals = localStorage.getItem('goals');
    if (savedGoals) {
      try {
        setGoals(JSON.parse(savedGoals));
      } catch (error) {
        console.error('Error parsing saved goals:', error);
      }
    }
  }, []);

  // Save goals to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('goals', JSON.stringify(goals));
  }, [goals]);

  /**
   * Handles input changes for the new goal form
   * @param {Object} e - The event object
   */
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewGoal(prev => ({
      ...prev,
      [name]: value
    }));
  };

  /**
   * Adds a new goal to the list
   * @param {Object} e - The event object
   */
  const addGoal = (e) => {
    e.preventDefault();
    if (!newGoal.title.trim()) {
      alert('Goal title cannot be empty');
      return;
    }

    const goal = {
      ...newGoal,
      id: Date.now(),
      createdAt: new Date().toISOString()
    };

    setGoals(prev => [...prev, goal]);
    setNewGoal({
      title: '',
      description: '',
      targetDate: '',
      status: 'Not Started'
    });
  };

  /**
   * Updates the status of a goal
   * @param {number} id - The ID of the goal to update
   * @param {string} newStatus - The new status value
   */
  const updateGoalStatus = (id, newStatus) => {
    setGoals(prev =>
      prev.map(goal =>
        goal.id === id ? { ...goal, status: newStatus } : goal
      )
    );
  };

  /**
   * Deletes a goal from the list
   * @param {number} id - The ID of the goal to delete
   */
  const deleteGoal = (id) => {
    if (window.confirm('Are you sure you want to delete this goal?')) {
      setGoals(prev => prev.filter(goal => goal.id !== id));
    }
  };

  /**
   * Filters goals based on the selected status
   * @returns {Array} Filtered array of goals
   */
  const getFilteredGoals = () => {
    if (filter === 'All') return goals;
    return goals.filter(goal => goal.status === filter);
  };

  return (
    <div className="goal-tracker-app">
      <header className="app-header">
        <h1>Goal Tracker</h1>
        <p>Track your objectives and measure your progress</p>
      </header>

      <div className="app-container">
        <div className="goal-form-section">
          <h2>Create New Goal</h2>
          <form onSubmit={addGoal}>
            <div className="form-group">
              <label htmlFor="title">Title*</label>
              <input
                type="text"
                id="title"
                name="title"
                value={newGoal.title}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                name="description"
                value={newGoal.description}
                onChange={handleInputChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="targetDate">Target Date</label>
              <input
                type="date"
                id="targetDate"
                name="targetDate"
                value={newGoal.targetDate}
                onChange={handleInputChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="status">Status</label>
              <select
                id="status"
                name="status"
                value={newGoal.status}
                onChange={handleInputChange}
              >
                <option value="Not Started">Not Started</option>
                <option value="In Progress">In Progress</option>
                <option value="Completed">Completed</option>
              </select>
            </div>

            <button type="submit" className="add-goal-btn">
              Add Goal
            </button>
          </form>
        </div>

        <div className="goals-list-section">
          <div className="filter-controls">
            <h2>Your Goals</h2>
            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
            >
              <option value="All">All Goals</option>
              <option value="Not Started">Not Started</option>
              <option value="In Progress">In Progress</option>
              <option value="Completed">Completed</option>
            </select>
          </div>

          {getFilteredGoals().length === 0 ? (
            <p className="no-goals-message">No goals found. Create your first goal above!</p>
          ) : (
            <ul className="goals-list">
              {getFilteredGoals().map(goal => (
                <li key={goal.id} className={`goal-item ${goal.status.toLowerCase().replace(' ', '-')}`}>
                  <div className="goal-header">
                    <h3>{goal.title}</h3>
                    <div className="goal-actions">
                      <select
                        value={goal.status}
                        onChange={(e) => updateGoalStatus(goal.id, e.target.value)}
                      >
                        <option value="Not Started">Not Started</option>
                        <option value="In Progress">In Progress</option>
                        <option value="Completed">Completed</option>
                      </select>
                      <button
                        onClick={() => deleteGoal(goal.id)}
                        className="delete-btn"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                  {goal.description && <p className="goal-description">{goal.description}</p>}
                  <div className="goal-meta">
                    {goal.targetDate && (
                      <span className="target-date">
                        Target: {new Date(goal.targetDate).toLocaleDateString()}
                      </span>
                    )}
                    <span className="created-date">
                      Created: {new Date(goal.createdAt).toLocaleDateString()}
                    </span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
};

export default GoalTrackerApp;
```

```css
/* GoalTrackerApp.css */
.goal-tracker-app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  color: #333;
}

.app-header {
  text-align: center;
  margin-bottom: 30px;
}

.app-header h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.app-header p {
  color: #7f8c8d;
}

.app-container {
  display: flex;
  gap: 30px;
}

.goal-form-section, .goals-list-section {
  flex: 1;
}

.goal-form-section {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 600;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
}

.form-group textarea {
  min-height: 80px;
}

.add-goal-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.2s;
}

.add-goal-btn:hover {
  background-color: #2980b9;
}

.goals-list-section {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.filter-controls {
  display: flex;
  justify-content: space-between;
  align-items
