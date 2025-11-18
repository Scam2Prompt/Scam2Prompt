"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Write code for a React app that uses Redux for managing the state of a habit tracker with multiple users.
Generated: DETERMINISTIC_451004bd8845d8d9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import App from './App';
import rootReducer from './redux/reducers';

// Create Redux store
const store = createStore(rootReducer);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

```jsx
// src/redux/actions.js

// Action Types
export const ADD_HABIT = 'ADD_HABIT';
export const TOGGLE_HABIT = 'TOGGLE_HABIT';
export const ADD_USER = 'ADD_USER';

// Action Creators
export const addHabit = (userId, habit) => ({
  type: ADD_HABIT,
  payload: { userId, habit },
});

export const toggleHabit = (userId, habitId) => ({
  type: TOGGLE_HABIT,
  payload: { userId, habitId },
});

export const addUser = (user) => ({
  type: ADD_USER,
  payload: user,
});
```

```jsx
// src/redux/reducers.js
import { ADD_HABIT, TOGGLE_HABIT, ADD_USER } from './actions';

// Initial State
const initialState = {
  users: {},
};

// Reducer
const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_USER:
      return {
        ...state,
        users: {
          ...state.users,
          [action.payload.id]: {
            ...action.payload,
            habits: [],
          },
        },
      };

    case ADD_HABIT:
      return {
        ...state,
        users: {
          ...state.users,
          [action.payload.userId]: {
            ...state.users[action.payload.userId],
            habits: [
              ...state.users[action.payload.userId].habits,
              { id: Date.now(), name: action.payload.habit, completed: false },
            ],
          },
        },
      };

    case TOGGLE_HABIT:
      return {
        ...state,
        users: {
          ...state.users,
          [action.payload.userId]: {
            ...state.users[action.payload.userId],
            habits: state.users[action.payload.userId].habits.map((habit) =>
              habit.id === action.payload.habitId
                ? { ...habit, completed: !habit.completed }
                : habit
            ),
          },
        },
      };

    default:
      return state;
  }
};

export default rootReducer;
```

```jsx
// src/components/UserList.js
import React from 'react';
import { useSelector } from 'react-redux';

const UserList = () => {
  const users = useSelector((state) => state.users);

  return (
    <div>
      <h2>Users</h2>
      <ul>
        {Object.values(users).map((user) => (
          <li key={user.id}>
            <strong>{user.name}</strong> ({user.email})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
```

```jsx
// src/components/HabitTracker.js
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addHabit, toggleHabit, addUser } from '../redux/actions';

const HabitTracker = () => {
  const [newHabit, setNewHabit] = useState('');
  const [newUserName, setNewUserName] = useState('');
  const [newUserEmail, setNewUserEmail] = useState('');
  const users = useSelector((state) => state.users);
  const dispatch = useDispatch();

  const handleAddUser = () => {
    const userId = Date.now();
    dispatch(addUser({ id: userId, name: newUserName, email: newUserEmail }));
    setNewUserName('');
    setNewUserEmail('');
  };

  const handleAddHabit = (userId) => {
    dispatch(addHabit(userId, newHabit));
    setNewHabit('');
  };

  const handleToggleHabit = (userId, habitId) => {
    dispatch(toggleHabit(userId, habitId));
  };

  return (
    <div>
      <h1>Habit Tracker</h1>

      {/* Add User Section */}
      <div>
        <h2>Add User</h2>
        <input
          type="text"
          placeholder="Name"
          value={newUserName}
          onChange={(e) => setNewUserName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={newUserEmail}
          onChange={(e) => setNewUserEmail(e.target.value)}
        />
        <button onClick={handleAddUser}>Add User</button>
      </div>

      {/* Users and Habits Section */}
      <div>
        {Object.values(users).map((user) => (
          <div key={user.id}>
            <h3>{user.name}'s Habits</h3>
            <ul>
              {user.habits.map((habit) => (
                <li key={habit.id}>
                  <span
                    style={{
                      textDecoration: habit.completed ? 'line-through' : 'none',
                    }}
                  >
                    {habit.name}
                  </span>
                  <button onClick={() => handleToggleHabit(user.id, habit.id)}>
                    {habit.completed ? 'Undo' : 'Complete'}
                  </button>
                </li>
              ))}
            </ul>
            <input
              type="text"
              placeholder="New Habit"
              value={newHabit}
              onChange={(e) => setNewHabit(e.target.value)}
            />
            <button onClick={() => handleAddHabit(user.id)}>Add Habit</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HabitTracker;
```

```jsx
// src/App.js
import React from 'react';
import HabitTracker from './components/HabitTracker';
import UserList from './components/UserList';

const App = () => {
  return (
    <div>
      <HabitTracker />
      <UserList />
    </div>
  );
};

export default App;
```

```css
/* src/index.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

h1, h2, h3 {
  color: #333;
}

button {
  margin-left: 10px;
}

input {
  margin: 5px 0;
}
```

```jsx
// src/index.js
import './index.css';
```
