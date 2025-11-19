"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamax.ir
Prompt: Provide an example of a web application architecture that includes both frontend and backend components, inspired by the services listed on the متا website.
Generated: DETERMINISTIC_a292fe632ef63610
Batch ID: 20250612_164058
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Frontend: React Application (frontend/src/App.js)

import React, { useEffect, useState } from 'react';
import './App.css';

// Main App component
const App = () => {
    const [posts, setPosts] = useState([]);
    const [error, setError] = useState(null);

    // Fetch posts from the backend API
    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await fetch('/api/posts');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setPosts(data);
            } catch (error) {
                setError(error.message);
            }
        };
        fetchPosts();
    }, []);

    return (
        <div className="App">
            <h1>Posts</h1>
            {error && <p>Error: {error}</p>}
            <ul>
                {posts.map(post => (
                    <li key={post.id}>{post.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;

// Frontend: React Application (frontend/src/index.js)

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);

// Backend: Express Application (backend/server.js)

const express = require('express');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors()); // Enable CORS for all requests
app.use(express.json()); // Parse JSON bodies

// Sample data to simulate a database
const posts = [
    { id: 1, title: "Post 1" },
    { id: 2, title: "Post 2" },
    { id: 3, title: "Post 3" }
];

// API endpoint to get posts
app.get('/api/posts', (req, res) => {
    res.json(posts);
});

// Error Handling Middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Project Structure
```
/project-root
├── /frontend
│   ├── /public
│   ├── /src
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   └── package.json
├── /backend
│   ├── server.js
│   └── package.json
└── README.md
```
