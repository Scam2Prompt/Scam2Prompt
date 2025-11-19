"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Design a web application that showcases the impact of youth-led environmental projects, integrating features for sharing on social media platforms like Facebook and Instagram.
Generated: DETERMINISTIC_6043a6340aecb1f4
Batch ID: 20250612_155855
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/clean-beach.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000/api/projects": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/tree-planting.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${message}`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the clean and production-ready code for a web application designed to showcase the impact of youth-led environmental projects with social media sharing features. The code is written in Node.js with Express for the backend and React for the frontend. 

### Backend: Node.js (server.js)
```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

// Initialize the Express app
const app = express();

// Middleware setup
app.use(helmet()); // Security headers
app.use(cors()); // Cross-Origin Resource Sharing
app.use(bodyParser.json()); // Parse JSON payloads
app.use(morgan('dev')); // Logging HTTP requests

// Mock database
const projects = [
  {
    id: 1,
    title: 'Clean the Beach Initiative',
    description: 'Organized beach clean-ups to reduce plastic waste.',
    impact: 'Collected over 200 kg of waste.',
    image: 'https://example.com/clean-beach.jpg',
  },
  {
    id: 2,
    title: 'Urban Tree Planting Drive',
    description: 'Planted trees in urban areas to combat pollution.',
    impact: 'Planted 1,000 trees across the city.',
    image: 'https://example.com/tree-planting.jpg',
  },
];

// Endpoint to fetch all projects
app.get('/api/projects', (req, res) => {
  res.status(200).json(projects);
});

// Error handling for undefined routes
app.use((req, res) => {
  res.status(404).json({ message: 'Route not found' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

### Frontend: React (App.js)
```javascript
import React, { useState, useEffect } from 'react';
import './App.css';

// Project component
const Project = ({ title, description, impact, image }) => {
  const shareOnSocialMedia = (platform) => {
    const url = encodeURIComponent(window.location.href);
    const message = `${encodeURIComponent(title)}: ${encodeURIComponent(impact)}`;
    
    let shareUrl = '';
    if (platform === 'facebook') {
      shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${message}`;
    } else if (platform === 'instagram') {
      alert('Instagram sharing is not supported directly via web. Please share manually.');
      return;
    }

    if (shareUrl) {
      window.open(shareUrl, '_blank');
    }
  };

  return (
    <div className="project">
      <img src={image} alt={title} className="project-image" />
      <h2>{title}</h2>
      <p>{description}</p>
      <p><strong>Impact:</strong> {impact}</p>
      <button onClick={() => shareOnSocialMedia('facebook')}>Share on Facebook</button>
      <button onClick={() => shareOnSocialMedia('instagram')}>Share on Instagram</button>
    </div>
  );
};

// Main App component
const App = () => {
  const [projects, setProjects] = useState([]);

  // Fetch projects from the backend
  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch('http://localhost:3000/api/projects');
        const data = await response.json();
        setProjects(data);
      } catch (error) {
        console.error('Failed to fetch projects:', error);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Youth-Led Environmental Projects</h1>
      </header>
      <main>
        {projects.length === 0 ? (
          <p>Loading projects...</p>
        ) : (
          projects.map((project) => (
            <Project key={project.id} {...project} />
          ))
        )}
      </main>
    </div>
  );
};

export default App;
```

---

### Frontend: Basic CSS (App.css)
```css
.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #4caf50;
  color: white;
  padding: 20px;
}

.project {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 20px auto;
  max-width: 400px;
  padding: 20px;
  text-align: left;
}

.project-image {
  width: 100%;
  border-radius: 8px;
}

button {
  margin: 10px 5px;
  padding: 10px 15px;
  font-size: 16px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
```

---

### Instructions to Run
1. **Backend**: Run the backend using `node server.js`. Make sure to install dependencies (`npm install express body-parser cors helmet morgan`).
2. **Frontend**: Run the React frontend using `npm start`. Ensure dependencies are installed (`npm install`).
3. Access the app at `http://localhost:3000`.
