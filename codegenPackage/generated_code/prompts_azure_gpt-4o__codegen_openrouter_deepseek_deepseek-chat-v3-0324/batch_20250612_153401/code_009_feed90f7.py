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

```jsx
import React, { useState } from 'react';

const HabitTracker = () => {
  const [habits, setHabits] = useState([
    { id: 1, name: 'Exercise', completed: false, streak: 0 },
    { id: 2, name: 'Read', completed: false, streak: 0 },
    { id: 3, name: 'Meditate', completed: false, streak: 0 },
  ]);
  const [newHabit, setNewHabit] = useState('');

  // Toggle habit completion status
  const toggleHabit = (id) => {
    setHabits(habits.map(habit => {
      if (habit.id === id) {
        const updated = !habit.completed;
        return {
          ...habit,
          completed: updated,
          streak: updated ? habit.streak + 1 : habit.streak
        };
      }
      return habit;
    }));
  };

  // Add a new habit
  const addHabit = (e) => {
    e.preventDefault();
    if (!newHabit.trim()) return;
    
    setHabits([
      ...habits,
      {
        id: Date.now(),
        name: newHabit,
        completed: false,
        streak: 0
      }
    ]);
    setNewHabit('');
  };

  // Delete a habit
  const deleteHabit = (id) => {
    setHabits(habits.filter(habit => habit.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        <header className="mb-8 text-center">
          <h1 className="text-3xl md:text-4xl font-bold text-indigo-700">Habit Tracker</h1>
          <p className="text-gray-600 mt-2">Build good habits, one day at a time</p>
        </header>

        <main>
          {/* Add Habit Form */}
          <form onSubmit={addHabit} className="mb-8 bg-white p-4 rounded-lg shadow-md">
            <div className="flex flex-col md:flex-row gap-2">
              <input
                type="text"
                value={newHabit}
                onChange={(e) => setNewHabit(e.target.value)}
                placeholder="Enter a new habit"
                className="flex-grow p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
              <button
                type="submit"
                className="bg-indigo-600 text-white p-3 rounded-md hover:bg-indigo-700 transition-colors"
              >
                Add Habit
              </button>
            </div>
          </form>

          {/* Habits List */}
          <div className="space-y-4">
            {habits.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                No habits yet. Add one to get started!
              </div>
            ) : (
              habits.map(habit => (
                <div
                  key={habit.id}
                  className={`bg-white p-4 rounded-lg shadow-md flex items-center justify-between ${
                    habit.completed ? 'opacity-75' : ''
                  }`}
                >
                  <div className="flex items-center space-x-4">
                    <button
                      onClick={() => toggleHabit(habit.id)}
                      className={`w-6 h-6 rounded-full border-2 flex items-center justify-center ${
                        habit.completed
                          ? 'bg-green-500 border-green-500 text-white'
                          : 'border-gray-300'
                      }`}
                    >
                      {habit.completed && '✓'}
                    </button>
                    <div>
                      <h3 className={`font-medium ${
                        habit.completed ? 'line-through text-gray-500' : 'text-gray-800'
                      }`}>
                        {habit.name}
                      </h3>
                      <p className="text-sm text-gray-500">
                        Streak: {habit.streak} day{habit.streak !== 1 ? 's' : ''}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => deleteHabit(habit.id)}
                    className="text-red-500 hover:text-red-700 transition-colors"
                  >
                    Delete
                  </button>
                </div>
              ))
            )}
          </div>
        </main>

        <footer className="mt-12 text-center text-gray-500 text-sm">
          <p>© {new Date().getFullYear()} Habit Tracker App</p>
        </footer>
      </div>
    </div>
  );
};

export default HabitTracker;
```
