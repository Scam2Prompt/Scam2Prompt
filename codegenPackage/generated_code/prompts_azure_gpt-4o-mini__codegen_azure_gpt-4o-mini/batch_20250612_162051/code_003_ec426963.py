"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management tool using a library like React that incorporates features for tracking the design process phases mentioned on The Design Umbrella's site, such as discovery, design, development, and delivery.
Generated: DETERMINISTIC_ec4269637b58d32f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import './App.css'; // Importing CSS for styling

// Define the main App component
const App = () => {
  // State to manage the phases of the design process
  const [phases, setPhases] = useState([
    { name: 'Discovery', completed: false },
    { name: 'Design', completed: false },
    { name: 'Development', completed: false },
    { name: 'Delivery', completed: false },
  ]);

  // Function to toggle the completion status of a phase
  const togglePhaseCompletion = (index) => {
    setPhases((prevPhases) => {
      const newPhases = [...prevPhases];
      newPhases[index].completed = !newPhases[index].completed;
      return newPhases;
    });
  };

  // Function to render each phase
  const renderPhase = (phase, index) => (
    <div key={index} className={`phase ${phase.completed ? 'completed' : ''}`}>
      <span>{phase.name}</span>
      <button onClick={() => togglePhaseCompletion(index)}>
        {phase.completed ? 'Undo' : 'Complete'}
      </button>
    </div>
  );

  return (
    <div className="app">
      <h1>Project Management Tool</h1>
      <h2>Design Process Phases</h2>
      <div className="phases">
        {phases.map((phase, index) => renderPhase(phase, index))}
      </div>
    </div>
  );
};

// Export the App component as the default export
export default App;
```

```css
/* App.css - Basic styling for the project management tool */

.app {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.phases {
  margin-top: 20px;
}

.phase {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 10px;
  transition: background-color 0.3s;
}

.phase.completed {
  background-color: #d4edda;
  border-color: #c3e6cb;
}

button {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #007bff;
  color: white;
}
```

```javascript
// index.js - Entry point for the React application

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the App component into the root element
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```html
<!-- index.html - Basic HTML structure for the React application -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Management Tool</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
```

```json
// package.json - Basic configuration for the React application

{
  "name": "project-management-tool",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
