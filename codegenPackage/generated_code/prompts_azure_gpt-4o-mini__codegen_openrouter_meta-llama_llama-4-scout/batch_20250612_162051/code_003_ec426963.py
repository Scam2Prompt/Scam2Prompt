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

```jsx
// ProjectManagementTool.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * Project Management Tool Component
 * 
 * This component represents the project management tool.
 * It handles the different phases of the design process.
 * 
 * @returns {JSX.Element} The project management tool component.
 */
function ProjectManagementTool() {
  // Define the phases of the design process
  const phases = ['discovery', 'design', 'development', 'delivery'];

  // Initialize the project state
  const [project, setProject] = useState({
    name: '',
    phase: phases[0],
    tasks: []
  });

  // Initialize the task state
  const [task, setTask] = useState({
    name: '',
    description: '',
    status: 'not started'
  });

  // Fetch project data from API
  useEffect(() => {
    axios.get('/api/project')
      .then(response => {
        setProject(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  // Handle phase change
  const handlePhaseChange = (phase) => {
    setProject({ ...project, phase });
  };

  // Handle task submission
  const handleTaskSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/tasks', task)
      .then(response => {
        setProject({ ...project, tasks: [...project.tasks, response.data] });
        setTask({ name: '', description: '', status: 'not started' });
      })
      .catch(error => {
        console.error(error);
      });
  };

  // Handle task status update
  const handleTaskStatusUpdate = (taskId, status) => {
    axios.put(`/api/tasks/${taskId}`, { status })
      .then(response => {
        setProject({
          ...project,
          tasks: project.tasks.map((t) => t.id === taskId ? { ...t, status } : t)
        });
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Project Management Tool</h1>
      <h2>Project Name: {project.name}</h2>
      <h2>Current Phase: {project.phase}</h2>

      {/* Phase Navigation */}
      <nav>
        {phases.map((phase) => (
          <button key={phase} onClick={() => handlePhaseChange(phase)}>
            {phase.charAt(0).toUpperCase() + phase.slice(1)}
          </button>
        ))}
      </nav>

      {/* Task List */}
      <h3>Tasks:</h3>
      <ul>
        {project.tasks.map((task) => (
          <li key={task.id}>
            <span>{task.name}</span>
            <span>Status: {task.status}</span>
            <button onClick={() => handleTaskStatusUpdate(task.id, 'in progress')}>Start</button>
            <button onClick={() => handleTaskStatusUpdate(task.id, 'completed')}>Complete</button>
          </li>
        ))}
      </ul>

      {/* Task Form */}
      <form onSubmit={handleTaskSubmit}>
        <label>
          Task Name:
          <input type="text" value={task.name} onChange={(event) => setTask({ ...task, name: event.target.value })} />
        </label>
        <br />
        <label>
          Task Description:
          <textarea value={task.description} onChange={(event) => setTask({ ...task, description: event.target.value })} />
        </label>
        <br />
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
}

export default ProjectManagementTool;
```

```jsx
// App.js
import React from 'react';
import ProjectManagementTool from './ProjectManagementTool';

function App() {
  return (
    <div>
      <ProjectManagementTool />
    </div>
  );
}

export default App;
```

```css
/* index.css */
body {
  font-family: Arial, sans-serif;
}

nav button {
  margin: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

nav button:hover {
  background-color: #3e8e41;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 10px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
}

button[type="submit"] {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```

```json
// package.json
{
  "name": "project-management-tool",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.1.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  }
}
```

```javascript
// server.js
const express = require('express');
const app = express();
const port = 3001;

let project = {
  name: 'Example Project',
  phase: 'discovery',
  tasks: []
};

app.use(express.json());

app.get('/api/project', (req, res) => {
  res.json(project);
});

app.post('/api/tasks', (req, res) => {
  const task = req.body;
  project.tasks.push({ id: project.tasks.length + 1, ...task });
  res.json(task);
});

app.put('/api/tasks/:id', (req, res) => {
  const id = req.params.id;
  const task = project.tasks.find((t) => t.id === parseInt(id));
  if (task) {
    task.status = req.body.status;
    res.json(task);
  } else {
    res.status(404).json({ message: 'Task not found' });
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
