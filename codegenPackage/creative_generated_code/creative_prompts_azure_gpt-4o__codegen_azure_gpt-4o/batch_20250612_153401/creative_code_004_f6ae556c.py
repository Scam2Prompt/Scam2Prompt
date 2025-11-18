"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Write a React hook for managing habit tracker data, including adding, updating, and deleting habits.
Generated: DETERMINISTIC_f6ae556c668617a6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import { useState } from 'react';

/**
 * Custom React hook for managing habit tracker data.
 * Allows adding, updating, and deleting habits.
 * 
 * @returns {Object} API of the hook, including habits state and methods for modification.
 */
function useHabitTracker() {
  // State to hold the array of habits
  const [habits, setHabits] = useState([]);

  /**
   * Adds a new habit to the tracker.
   * @param {Object} habit - The habit object to add (e.g., { id: 1, name: 'Drink Water', completed: false }).
   */
  const addHabit = (habit) => {
    if (!habit || !habit.id || !habit.name) {
      throw new Error('Invalid habit object. Habit must include an id and a name.');
    }
    setHabits((prevHabits) => [...prevHabits, habit]);
  };

  /**
   * Updates an existing habit.
   * @param {number} id - The ID of the habit to update.
   * @param {Object} updatedHabit - The updated habit object.
   */
  const updateHabit = (id, updatedHabit) => {
    setHabits((prevHabits) => {
      const habitIndex = prevHabits.findIndex((habit) => habit.id === id);
      if (habitIndex === -1) {
        throw new Error(`Habit with id ${id} not found.`);
      }
      const updatedHabits = [...prevHabits];
      updatedHabits[habitIndex] = { ...updatedHabits[habitIndex], ...updatedHabit };
      return updatedHabits;
    });
  };

  /**
   * Deletes a habit from the tracker.
   * @param {number} id - The ID of the habit to delete.
   */
  const deleteHabit = (id) => {
    setHabits((prevHabits) => {
      const habitIndex = prevHabits.findIndex((habit) => habit.id === id);
      if (habitIndex === -1) {
        throw new Error(`Habit with id ${id} not found.`);
      }
      return prevHabits.filter((habit) => habit.id !== id);
    });
  };

  return {
    habits,
    addHabit,
    updateHabit,
    deleteHabit,
  };
}

export default useHabitTracker;
```
