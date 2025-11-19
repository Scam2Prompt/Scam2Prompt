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
import React, { useState } from 'react';

// HabitTracker component to manage and display habits
const HabitTracker = () => {
    // State to hold habit list and input for new habit
    const [habits, setHabits] = useState([]);
    const [habitInput, setHabitInput] = useState("");

    // Function to handle changes in the input field
    const handleInputChange = (e) => {
        setHabitInput(e.target.value);
    };

    // Function to add a new habit to the list
    const addHabit = (e) => {
        e.preventDefault(); // Prevent default form submission behavior
        if (habitInput.trim() === "") {
            alert("Habit cannot be empty!"); // Alert if input is empty
            return;
        }

        // Add the new habit to the list
        setHabits([...habits, { name: habitInput, completed: false }]);
        setHabitInput(""); // Clear the input field
    };

    // Function to toggle the completion status of a habit
    const toggleHabitCompletion = (index) => {
        const updatedHabits = habits.map((habit, i) => {
            if (i === index) {
                return { ...habit, completed: !habit.completed }; // Toggle completion
            }
            return habit;
        });
        setHabits(updatedHabits); // Update the habits state
    };

    // Function to remove a habit from the list
    const removeHabit = (index) => {
        const updatedHabits = habits.filter((_, i) => i !== index); // Filter out the habit at the given index
        setHabits(updatedHabits); // Update the habits state
    };

    return (
        <div>
            <h1>Habit Tracker</h1>
            <form onSubmit={addHabit}>
                <input
                    type="text"
                    value={habitInput}
                    onChange={handleInputChange}
                    placeholder="Enter a new habit"
                />
                <button type="submit">Add Habit</button>
            </form>
            <ul>
                {habits.map((habit, index) => (
                    <li key={index}>
                        <span
                            style={{ textDecoration: habit.completed ? 'line-through' : 'none' }}
                            onClick={() => toggleHabitCompletion(index)} // Toggle completion on click
                        >
                            {habit.name}
                        </span>
                        <button onClick={() => removeHabit(index)}>Remove</button> {/* Remove habit button */}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HabitTracker;

// Usage: Import and render <HabitTracker /> in your main application component.
```
