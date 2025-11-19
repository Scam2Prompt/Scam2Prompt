"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management tool using a library like React that incorporates features for tracking the design process phases mentioned on The Design Umbrella's site, such as discovery, design, development, and delivery.
Generated: DETERMINISTIC_ec4269637b58d32f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState } from 'react';
import './App.css'; // Import CSS for styling

// Define the phases of the design process
const phases = [
  { id: 1, name: 'Discovery', description: 'Understanding client needs and project requirements.' },
  { id: 2, name: 'Design', description: 'Creating wireframes and prototypes.' },
  { id: 3, name: 'Development', description: 'Building the actual product.' },
  { id: 4, name: 'Delivery', description: 'Final testing and launching the product.' },
];

// Main App Component
const App = () => {
  // State to hold the progress of each phase
  const [phaseProgress, setPhaseProgress] = useState(phases.map(phase => ({ ...phase, completed: false })));

  // Function to toggle phase completion
  const togglePhaseCompletion = (id) => {
    setPhaseProgress(prevProgress =>
      prevProgress.map(phase =>
        phase.id === id ? { ...phase, completed: !phase.completed } : phase
      )
    );
  };

  return (
    <div className="app">
      <h1>Project Management Tool</h1>
      <div className="phases">
        {phaseProgress.map(phase => (
          <div key={phase.id} className={`phase ${phase.completed ? 'completed' : ''}`}>
            <h2>{phase.name}</h2>
            <p>{phase.description}</p>
            <button onClick={() => togglePhaseCompletion(phase.id)}>
              {phase.completed ? 'Undo' : 'Complete'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
```

```css
/* App.css */

.app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
}

.phases {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.phase {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 15px;
  margin: 10px;
  width: 300px;
  transition: background-color 0.3s;
}

.phase.completed {
  background-color: #d4edda; /* Light green background for completed phases */
  border-color: #c3e6cb; /* Darker border for completed phases */
}

button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #007bff; /* Change background color on hover */
  color: white; /* Change text color on hover */
}
```

```json
// package.json (only necessary parts)

{
  "name": "project-management-tool",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "5.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
``` 

**Instructions:**
1. Create a new directory for the project.
2. Inside the directory, run `npx create-react-app project-management-tool`.
3. Replace the contents of `src/App.js` with the provided React code.
4. Create a `src/App.css` file and add the provided CSS styles.
5. Update `package.json` with the necessary dependencies if required.
6. Run the project using `npm start`.
