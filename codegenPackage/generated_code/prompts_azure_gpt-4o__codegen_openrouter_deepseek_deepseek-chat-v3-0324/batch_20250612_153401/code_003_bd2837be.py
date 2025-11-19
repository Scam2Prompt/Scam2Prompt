"""
Generated Code Metadata:
========================
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Generate code for a React app that uses Material-UI to design a habit tracker interface with a calendar view for tracking habits.
Generated: DETERMINISTIC_bd2837be2557c4ad
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  Grid,
  Paper,
  Button,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Box,
  CircularProgress
} from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { Calendar, dateFnsLocalizer } from 'react-big-calendar';
import format from 'date-fns/format';
import parse from 'date-fns/parse';
import startOfWeek from 'date-fns/startOfWeek';
import getDay from 'date-fns/getDay';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import AddIcon from '@mui/icons-material/Add';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';

const locales = {
  'en-US': require('date-fns/locale/en-US')
};

const localizer = dateFnsLocalizer({
  format,
  parse,
  startOfWeek,
  getDay,
  locales,
});

const HabitTracker = () => {
  const [habits, setHabits] = useState([]);
  const [events, setEvents] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [currentHabit, setCurrentHabit] = useState({
    id: '',
    name: '',
    frequency: 'daily',
    color: '#1976d2'
  });
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const frequencyOptions = [
    { value: 'daily', label: 'Daily' },
    { value: 'weekly', label: 'Weekly' },
    { value: 'monthly', label: 'Monthly' }
  ];

  const colorOptions = [
    { value: '#1976d2', label: 'Blue' },
    { value: '#d32f2f', label: 'Red' },
    { value: '#388e3c', label: 'Green' },
    { value: '#ffa000', label: 'Orange' },
    { value: '#7b1fa2', label: 'Purple' }
  ];

  useEffect(() => {
    // Simulate loading habits from an API
    const fetchHabits = async () => {
      try {
        setLoading(true);
        // Mock API call
        await new Promise(resolve => setTimeout(resolve, 1000));
        const mockHabits = [
          { id: '1', name: 'Exercise', frequency: 'daily', color: '#388e3c' },
          { id: '2', name: 'Read', frequency: 'daily', color: '#1976d2' },
          { id: '3', name: 'Meditate', frequency: 'weekly', color: '#7b1fa2' }
        ];
        setHabits(mockHabits);
        generateEvents(mockHabits);
      } catch (err) {
        setError('Failed to load habits');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchHabits();
  }, []);

  const generateEvents = (habitsList) => {
    const newEvents = [];
    habitsList.forEach(habit => {
      // Generate events for the current month
      const startDate = new Date();
      const endDate = new Date();
      endDate.setMonth(startDate.getMonth() + 1);

      // Simple event generation logic
      if (habit.frequency === 'daily') {
        for (let d = new Date(startDate); d <= endDate; d.setDate(d.getDate() + 1)) {
          newEvents.push({
            id: `${habit.id}-${d.toISOString()}`,
            title: habit.name,
            start: new Date(d),
            end: new Date(d),
            allDay: true,
            habitId: habit.id,
            color: habit.color
          });
        }
      } else if (habit.frequency === 'weekly') {
        for (let d = new Date(startDate); d <= endDate; d.setDate(d.getDate() + 7)) {
          newEvents.push({
            id: `${habit.id}-${d.toISOString()}`,
            title: habit.name,
            start: new Date(d),
            end: new Date(d),
            allDay: true,
            habitId: habit.id,
            color: habit.color
          });
        }
      } else if (habit.frequency === 'monthly') {
        for (let d = new Date(startDate); d <= endDate; d.setMonth(d.getMonth() + 1)) {
          newEvents.push({
            id: `${habit.id}-${d.toISOString()}`,
            title: habit.name,
            start: new Date(d),
            end: new Date(d),
            allDay: true,
            habitId: habit.id,
            color: habit.color
          });
        }
      }
    });
    setEvents(newEvents);
  };

  const handleOpenDialog = (habit = null) => {
    if (habit) {
      setCurrentHabit(habit);
    } else {
      setCurrentHabit({
        id: '',
        name: '',
        frequency: 'daily',
        color: '#1976d2'
      });
    }
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCurrentHabit(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = () => {
    try {
      if (!currentHabit.name.trim()) {
        throw new Error('Habit name is required');
      }

      if (currentHabit.id) {
        // Update existing habit
        const updatedHabits = habits.map(habit =>
          habit.id === currentHabit.id ? currentHabit : habit
        );
        setHabits(updatedHabits);
        generateEvents(updatedHabits);
      } else {
        // Add new habit
        const newHabit = {
          ...currentHabit,
          id: Date.now().toString()
        };
        const updatedHabits = [...habits, newHabit];
        setHabits(updatedHabits);
        generateEvents(updatedHabits);
      }
      handleCloseDialog();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDeleteHabit = (id) => {
    try {
      const updatedHabits = habits.filter(habit => habit.id !== id);
      setHabits(updatedHabits);
      generateEvents(updatedHabits);
    } catch (err) {
      setError('Failed to delete habit');
      console.error(err);
    }
  };

  const eventStyleGetter = (event) => {
    return {
      style: {
        backgroundColor: event.color,
        borderRadius: '4px',
        opacity: 0.8,
        color: 'white',
        border: '0px',
        display: 'block'
      }
    };
  };

  return (
    <LocalizationProvider dateAdapter={AdapterDateFns}>
      <div>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Habit Tracker
            </Typography>
          </Toolbar>
        </AppBar>

        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          {error && (
            <Paper sx={{ p: 2, mb: 2, backgroundColor: '#ffebee' }}>
              <Typography color="error">{error}</Typography>
            </Paper>
          )}

          <Grid container spacing={3}>
            <Grid item xs={12} md={4}>
              <Paper sx={{ p: 2 }}>
                <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
                  <Typography variant="h6">My Habits</Typography>
                  <Button
                    variant="contained"
                    startIcon={<AddIcon />}
                    onClick={() => handleOpenDialog()}
                  >
                    Add Habit
                  </Button>
                </Box>

                {loading ? (
                  <Box display="flex" justifyContent="center" mt={2}>
                    <CircularProgress />
                  </Box>
                ) : (
                  <div>
                    {habits.map(habit => (
                      <Paper
                        key={habit.id}
                        sx={{
                          p: 2,
                          mb: 2,
                          backgroundColor: habit.color,
                          color: 'white',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center'
                        }}
                      >
                        <Typography>{habit.name}</Typography>
                        <div>
                          <IconButton
                            size="small"
