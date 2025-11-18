"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Generate code for a React app that uses Material-UI to design a habit tracker interface with a calendar view for tracking habits.
Generated: DETERMINISTIC_bd2837be2557c4ad
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.jsx - Main File
import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import HabitTracker from './HabitTracker';

// Create a Material-UI theme for consistent styling
const theme = createTheme({
  palette: {
    primary: {
      main: '#4caf50', // Green color for the primary theme
    },
    secondary: {
      main: '#f50057', // Pink color for the secondary theme
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
  },
});

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline /> {/* Sets up baseline styles */}
      <HabitTracker /> {/* Main Habit Tracker Component */}
    </ThemeProvider>
  );
};

export default App;
```

```jsx
// HabitTracker.jsx - Habit Tracker Component
import React, { useState } from 'react';
import { Box, Typography, Grid, Checkbox, Button, TextField } from '@mui/material';
import Calendar from 'react-calendar'; // React Calendar package for calendar view
import 'react-calendar/dist/Calendar.css'; // Import default calendar styles

const HabitTracker = () => {
  const [date, setDate] = useState(new Date()); // State for calendar date
  const [habits, setHabits] = useState([]); // State for habit list
  const [habitInput, setHabitInput] = useState(''); // State for new habit input

  // Handle date change in the calendar
  const handleDateChange = (selectedDate) => {
    setDate(selectedDate);
  };

  // Handle adding a new habit
  const handleAddHabit = () => {
    if (habitInput.trim()) {
      setHabits([...habits, { name: habitInput, completed: false }]);
      setHabitInput('');
    }
  };

  // Toggle completion status of a habit
  const toggleHabitCompletion = (index) => {
    const updatedHabits = habits.map((habit, i) =>
      i === index ? { ...habit, completed: !habit.completed } : habit
    );
    setHabits(updatedHabits);
  };

  return (
    <Box sx={{ p: 3 }}>
      {/* Header Section */}
      <Typography variant="h4" gutterBottom>
        Habit Tracker
      </Typography>

      {/* Calendar Section */}
      <Box sx={{ mb: 3 }}>
        <Calendar onChange={handleDateChange} value={date} />
        <Typography align="center" sx={{ mt: 1 }}>
          Selected Date: {date.toDateString()}
        </Typography>
      </Box>

      {/* Habit Input Section */}
      <Box sx={{ display: 'flex', mb: 2 }}>
        <TextField
          label="New Habit"
          variant="outlined"
          fullWidth
          value={habitInput}
          onChange={(e) => setHabitInput(e.target.value)}
          sx={{ mr: 2 }}
        />
        <Button variant="contained" color="primary" onClick={handleAddHabit}>
          Add Habit
        </Button>
      </Box>

      {/* Habit List Section */}
      <Box>
        {habits.length === 0 ? (
          <Typography color="textSecondary">No habits added yet.</Typography>
        ) : (
          <Grid container spacing={2}>
            {habits.map((habit, index) => (
              <Grid item xs={12} key={index}>
                <Box
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                    border: '1px solid #e0e0e0',
                    borderRadius: 2,
                    p: 2,
                  }}
                >
                  <Checkbox
                    color="primary"
                    checked={habit.completed}
                    onChange={() => toggleHabitCompletion(index)}
                  />
                  <Typography
                    variant="body1"
                    sx={{
                      textDecoration: habit.completed ? 'line-through' : 'none',
                      flexGrow: 1,
                    }}
                  >
                    {habit.name}
                  </Typography>
                </Box>
              </Grid>
            ))}
          </Grid>
        )}
      </Box>
    </Box>
  );
};

export default HabitTracker;
```

```json
// package.json - Dependencies for the app
{
  "name": "habit-tracker",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@emotion/react": "^11.11.0",
    "@emotion/styled": "^11.11.0",
    "@mui/material": "^5.14.0",
    "react": "^18.2.0",
    "react-calendar": "^3.8.0",
    "react-dom": "^18.2.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

```bash
# Installation Instructions
npm install @mui/material @emotion/react @emotion/styled react-calendar
```

```css
/* App.css - Additional optional styling */
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #f5f5f5;
}
.react-calendar {
  display: block;
  margin: auto;
}
```
