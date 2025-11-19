"""
Generated Code Metadata:
========================
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Write code for a React app that uses Redux for managing the state of a habit tracker with multiple users.
Generated: DETERMINISTIC_451004bd8845d8d9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/store/store.js
import { configureStore } from '@reduxjs/toolkit';
import habitsReducer from '../features/habits/habitsSlice';
import usersReducer from '../features/users/usersSlice';

export const store = configureStore({
  reducer: {
    habits: habitsReducer,
    users: usersReducer
  }
});

// src/features/habits/habitsSlice.js
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  habits: [],
  status: 'idle',
  error: null
};

const habitsSlice = createSlice({
  name: 'habits',
  initialState,
  reducers: {
    addHabit: (state, action) => {
      state.habits.push(action.payload);
    },
    updateHabit: (state, action) => {
      const { id, updates } = action.payload;
      const habitIndex = state.habits.findIndex(habit => habit.id === id);
      if (habitIndex !== -1) {
        state.habits[habitIndex] = { ...state.habits[habitIndex], ...updates };
      }
    },
    deleteHabit: (state, action) => {
      state.habits = state.habits.filter(habit => habit.id !== action.payload);
    },
    markComplete: (state, action) => {
      const { habitId, date } = action.payload;
      const habit = state.habits.find(h => h.id === habitId);
      if (habit) {
        if (!habit.completedDates) habit.completedDates = [];
        habit.completedDates.push(date);
      }
    }
  }
});

export const { addHabit, updateHabit, deleteHabit, markComplete } = habitsSlice.actions;
export default habitsSlice.reducer;

export const selectAllHabits = state => state.habits.habits;
export const selectHabitsByUser = userId => state => 
  state.habits.habits.filter(habit => habit.userId === userId);

// src/features/users/usersSlice.js
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  users: [
    { id: '1', name: 'User 1' },
    { id: '2', name: 'User 2' }
  ],
  currentUser: null,
  status: 'idle',
  error: null
};

const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    setCurrentUser: (state, action) => {
      state.currentUser = action.payload;
    },
    addUser: (state, action) => {
      state.users.push(action.payload);
    }
  }
});

export const { setCurrentUser, addUser } = usersSlice.actions;
export default usersSlice.reducer;

export const selectAllUsers = state => state.users.users;
export const selectCurrentUser = state => state.users.currentUser;

// src/features/habits/HabitForm.js
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addHabit } from './habitsSlice';

const HabitForm = () => {
  const [name, setName] = useState('');
  const [frequency, setFrequency] = useState('daily');
  const dispatch = useDispatch();
  const currentUser = useSelector(selectCurrentUser);

  const handleSubmit = e => {
    e.preventDefault();
    if (!name.trim()) return;
    
    const newHabit = {
      id: Date.now().toString(),
      name,
      frequency,
      userId: currentUser.id,
      completedDates: []
    };
    
    dispatch(addHabit(newHabit));
    setName('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="Habit name"
        required
      />
      <select value={frequency} onChange={e => setFrequency(e.target.value)}>
        <option value="daily">Daily</option>
        <option value="weekly">Weekly</option>
        <option value="monthly">Monthly</option>
      </select>
      <button type="submit">Add Habit</button>
    </form>
  );
};

export default HabitForm;

// src/features/habits/HabitList.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { deleteHabit, markComplete } from './habitsSlice';
import { selectHabitsByUser } from './habitsSlice';
import { selectCurrentUser } from '../users/usersSlice';

const HabitList = () => {
  const currentUser = useSelector(selectCurrentUser);
  const habits = useSelector(selectHabitsByUser(currentUser?.id));
  const dispatch = useDispatch();

  const handleDelete = id => {
    dispatch(deleteHabit(id));
  };

  const handleMarkComplete = habitId => {
    const today = new Date().toISOString().split('T')[0];
    dispatch(markComplete({ habitId, date: today }));
  };

  return (
    <div>
      <h2>Your Habits</h2>
      {habits.length === 0 ? (
        <p>No habits yet. Add one to get started!</p>
      ) : (
        <ul>
          {habits.map(habit => (
            <li key={habit.id}>
              <h3>{habit.name}</h3>
              <p>Frequency: {habit.frequency}</p>
              <p>
                Completed: {habit.completedDates?.length || 0} times
              </p>
              <button onClick={() => handleMarkComplete(habit.id)}>
                Mark Complete Today
              </button>
              <button onClick={() => handleDelete(habit.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default HabitList;

// src/features/users/UserSelector.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setCurrentUser } from './usersSlice';
import { selectAllUsers } from './usersSlice';

const UserSelector = () => {
  const users = useSelector(selectAllUsers);
  const dispatch = useDispatch();

  const handleUserChange = e => {
    const userId = e.target.value;
    const user = users.find(u => u.id === userId);
    dispatch(setCurrentUser(user || null));
  };

  return (
    <div>
      <h2>Select User</h2>
      <select onChange={handleUserChange}>
        <option value="">-- Select User --</option>
        {users.map(user => (
          <option key={user.id} value={user.id}>
            {user.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default UserSelector;

// src/features/users/AddUserForm.js
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addUser } from './usersSlice';

const AddUserForm = () => {
  const [name, setName] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = e => {
    e.preventDefault();
    if (!name.trim()) return;
    
    const newUser = {
      id: Date.now().toString(),
      name
    };
    
    dispatch(addUser(newUser));
    setName('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="User name"
        required
      />
      <button type="submit">Add User</button>
    </form>
  );
};

export default AddUserForm;

// src/app/App.js
import React from 'react';
import { Provider } from 'react-redux';
import { store } from '../store/store';
import UserSelector from '../features/users/UserSelector';
import AddUserForm from '../features/users/AddUserForm';
import HabitForm from '../features/habits/HabitForm';
import HabitList from '../features/habits/HabitList';

const App = () => {
  return (
    <Provider store={store}>
      <div className="app">
        <h1>Habit Tracker</h1>
        <UserSelector />
        <AddUserForm />
        <HabitForm />
        <HabitList />
      </div>
    </Provider>
  );
};

export default App;

// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './app/App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
