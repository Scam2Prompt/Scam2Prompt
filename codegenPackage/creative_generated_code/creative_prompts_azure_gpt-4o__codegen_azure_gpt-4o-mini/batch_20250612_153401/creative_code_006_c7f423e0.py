"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://habit-tracker-ten-pearl.vercel.app
Prompt: Recommend a React library for implementing drag-and-drop functionality to reorder habits in a habit tracker app.
Generated: DETERMINISTIC_c7f423e0c390d191
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import './HabitTracker.css'; // Optional: Add CSS for styling

// Component for individual Habit item
const HabitItem = ({ habit, index, moveHabit }) => {
  const [{ isDragging }, drag] = useDrag({
    type: 'HABIT',
    item: { index },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  return (
    <div
      ref={drag}
      className={`habit-item ${isDragging ? 'dragging' : ''}`}
      style={{ opacity: isDragging ? 0.5 : 1 }}
    >
      {habit}
    </div>
  );
};

// Component to render the list of habits with drag-and-drop functionality
const HabitList = ({ habits, setHabits }) => {
  const [, drop] = useDrop({
    accept: 'HABIT',
    hover(item, monitor) {
      const dragIndex = item.index;
      const hoverIndex = index;

      // Don't replace items with themselves
      if (dragIndex === hoverIndex) return;

      // Perform the reordering
      const updatedHabits = [...habits];
      const [movedHabit] = updatedHabits.splice(dragIndex, 1);
      updatedHabits.splice(hoverIndex, 0, movedHabit);

      // Update the state with the new habits order
      setHabits(updatedHabits);
      item.index = hoverIndex; // Update index for the dragged item
    },
  });

  return (
    <div ref={drop} className="habit-list">
      {habits.map((habit, index) => (
        <HabitItem key={habit} habit={habit} index={index} moveHabit={moveHabit} />
      ))}
    </div>
  );
};

// Main Habit Tracker component
const HabitTracker = () => {
  const [habits, setHabits] = useState(['Exercise', 'Read', 'Meditate', 'Cook']);

  return (
    <DndProvider backend={HTML5Backend}>
      <h1>Habit Tracker</h1>
      <HabitList habits={habits} setHabits={setHabits} />
    </DndProvider>
  );
};

// Export the Habit Tracker component
export default HabitTracker;
```

```css
/* HabitTracker.css */
/* Basic styles for habit tracker */

.habit-list {
  width: 300px;
  margin: 0 auto;
}

.habit-item {
  padding: 10px;
  margin: 5px 0;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: move;
}

.dragging {
  background-color: #d0ffd0; /* Highlight dragged item */
}
``` 

```bash
# Add required dependencies
npm install react-dnd react-dnd-html5-backend
```
