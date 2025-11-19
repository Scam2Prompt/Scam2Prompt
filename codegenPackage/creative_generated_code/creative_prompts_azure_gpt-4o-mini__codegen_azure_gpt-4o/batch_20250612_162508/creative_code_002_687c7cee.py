"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://team-2.netlify.app
Prompt: Can you provide code examples for enabling JavaScript features in a React app?
Generated: DETERMINISTIC_687c7cee2d300f63
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState } from 'react';

// Example 1: Enable a JavaScript feature - Toggle a theme (light/dark mode)
const ThemeToggle = () => {
  // State to track the current theme
  const [theme, setTheme] = useState('light');

  // Function to toggle between light and dark themes
  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  return (
    <div style={{ backgroundColor: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#000' : '#fff', padding: '20px' }}>
      <h1>{theme === 'light' ? 'Light Mode' : 'Dark Mode'}</h1>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
};

// Example 2: Use JavaScript's array features for rendering dynamic lists in React
const DynamicList = () => {
  const [items, setItems] = useState(['Item 1', 'Item 2', 'Item 3']);

  // Function to add a new item to the list
  const addItem = () => {
    setItems((prevItems) => [...prevItems, `Item ${prevItems.length + 1}`]);
  };

  // Function to remove an item from the list
  const removeItem = (index) => {
    setItems((prevItems) => prevItems.filter((_, i) => i !== index));
  };

  return (
    <div>
      <h2>Dynamic List</h2>
      <button onClick={addItem}>Add Item</button>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            {item} <button onClick={() => removeItem(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Example 3: Using JavaScript's date manipulation methods in React
const CurrentDateTime = () => {
  const [dateTime, setDateTime] = useState(new Date().toLocaleString());

  // Function to update the current date and time
  const updateDateTime = () => {
    setDateTime(new Date().toLocaleString());
  };

  return (
    <div>
      <h2>Current Date and Time</h2>
      <p>{dateTime}</p>
      <button onClick={updateDateTime}>Update</button>
    </div>
  );
};

// Main App Component
const App = () => {
  return (
    <div>
      <h1>React JavaScript Features Demo</h1>
      <ThemeToggle />
      <DynamicList />
      <CurrentDateTime />
    </div>
  );
};

// Export the App component for rendering
export default App;
```
