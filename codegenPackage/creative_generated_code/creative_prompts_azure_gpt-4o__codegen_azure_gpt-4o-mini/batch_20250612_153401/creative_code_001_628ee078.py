"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Recommend libraries or APIs that can be integrated into a React app for storing habit tracking data persistently, such as using Firebase or localStorage.
Generated: DETERMINISTIC_628ee078eaad9b31
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// habitTracker.js

import React, { useState, useEffect } from 'react';
import firebase from 'firebase/app';
import 'firebase/firestore'; // Import Firestore for database functionality

// Firebase configuration object
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase app
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

// Firestore database reference
const db = firebase.firestore();

/**
 * Custom hook to manage habit tracking data
 * @returns {object} An object containing habits data and functions to manipulate it
 */
const useHabitTracker = () => {
    const [habits, setHabits] = useState([]);

    // Fetch habits from Firestore on component mount
    useEffect(() => {
        const fetchHabits = async () => {
            try {
                const snapshot = await db.collection('habits').get();
                const habitsData = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
                setHabits(habitsData);
            } catch (error) {
                console.error("Error fetching habits:", error);
            }
        };

        fetchHabits();
    }, []);

    /**
     * Add a new habit to the Firestore database
     * @param {object} habit - The habit object to add
     */
    const addHabit = async (habit) => {
        try {
            const docRef = await db.collection('habits').add(habit);
            setHabits([...habits, { id: docRef.id, ...habit }]);
        } catch (error) {
            console.error("Error adding habit:", error);
        }
    };

    /**
     * Delete a habit from the Firestore database
     * @param {string} id - The ID of the habit to delete
     */
    const deleteHabit = async (id) => {
        try {
            await db.collection('habits').doc(id).delete();
            setHabits(habits.filter(habit => habit.id !== id));
        } catch (error) {
            console.error("Error deleting habit:", error);
        }
    };

    return { habits, addHabit, deleteHabit };
};

/**
 * HabitTracker component to display and manage habits
 */
const HabitTracker = () => {
    const { habits, addHabit, deleteHabit } = useHabitTracker();
    const [newHabit, setNewHabit] = useState('');

    // Handle form submission for adding a new habit
    const handleSubmit = (e) => {
        e.preventDefault();
        if (newHabit.trim()) {
            addHabit({ name: newHabit });
            setNewHabit('');
        }
    };

    return (
        <div>
            <h1>Habit Tracker</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={newHabit}
                    onChange={(e) => setNewHabit(e.target.value)}
                    placeholder="Enter a new habit"
                />
                <button type="submit">Add Habit</button>
            </form>
            <ul>
                {habits.map(habit => (
                    <li key={habit.id}>
                        {habit.name}
                        <button onClick={() => deleteHabit(habit.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HabitTracker;
```

Make sure to replace the placeholders in the `firebaseConfig` object with your actual Firebase project credentials before running this code.
