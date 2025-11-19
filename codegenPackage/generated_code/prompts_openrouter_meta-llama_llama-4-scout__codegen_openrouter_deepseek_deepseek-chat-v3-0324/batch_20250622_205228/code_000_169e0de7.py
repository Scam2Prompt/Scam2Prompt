"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Write a React application that utilizes Node.js and MongoDB to create a user-centric web interface, inspired by Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_169e0de774bfd3cb
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a complete React application with Node.js backend and MongoDB integration, inspired by a portfolio-style application. The code is structured with best practices, error handling, and documentation.

### File Structure:
```
client/
  src/
    components/
      Header.js
      Projects.js
      ContactForm.js
    App.js
    index.js
    styles.css
server/
  models/
    User.js
    Project.js
  routes/
    userRoutes.js
    projectRoutes.js
  server.js
  config.js
```

### 1. Client-side (React)

#### `client/src/index.js`
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

#### `client/src/App.js`
```jsx
import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Projects from './components/Projects';
import ContactForm from './components/ContactForm';
import './styles.css';

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/projects')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch projects');
        return res.json();
      })
      .then(data => {
        setProjects(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="app">
      <Header />
      <main>
        {loading ? (
          <div className="loading">Loading...</div>
        ) : (
          <Projects projects={projects} />
        )}
      </main>
      <ContactForm />
    </div>
  );
}

export default App;
```

#### `client/src/components/Header.js`
```jsx
import React from 'react';

const Header = () => {
  return (
    <header className="header">
      <h1>Portfolio</h1>
      <nav>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>
  );
};

export default Header;
```

#### `client/src/components/Projects.js`
```jsx
import React from 'react';

const Projects = ({ projects }) => {
  return (
    <section id="projects" className="projects-section">
      <h2>My Projects</h2>
      <div className="projects-grid">
        {projects.map(project => (
          <div key={project._id} className="project-card">
            <h3>{project.title}</h3>
            <p>{project.description}</p>
            <a href={project.url} target="_blank" rel="noopener noreferrer">
              View Project
            </a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
```

#### `client/src/components/ContactForm.js`
```jsx
import React, { useState } from 'react';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Submission failed');

      setSubmitted(true);
      setFormData({ name: '', email: '', message: '' });
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <section id="contact" className="contact-section">
      <h2>Contact Me</h2>
      {submitted ? (
        <p className="success-message">Thank you for your message!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Your Name"
            required
          />
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Your Email"
            required
          />
          <textarea
            name="message"
            value={formData.message}
            onChange={handleChange}
            placeholder="Your Message"
            required
          />
          <button type="submit">Send Message</button>
        </form>
      )}
    </section>
  );
};

export default ContactForm;
```

#### `client/src/styles.css`
```css
/* Base Styles */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
  color: #333;
}

.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Header Styles */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid #eee;
}

.header h1 {
  margin: 0;
  font-size: 2rem;
}

.header nav a {
  margin-left: 20px;
  text-decoration: none;
  color: #333;
}

.header nav a:hover {
  color: #007bff;
}

/* Projects Section */
.projects-section {
  padding: 40px 0;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.project-card {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 5px;
  transition: transform 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.project-card h3 {
  margin-top: 0;
}

.project-card a {
  display: inline-block;
  margin-top: 10px;
  color: #007bff;
  text-decoration: none;
}

/* Contact Section */
.contact-section {
  padding: 40px 0;
}

.contact-section form {
  display: flex;
  flex-direction: column;
  max-width: 500px;
  margin: 0 auto;
}

.contact-section input,
.contact-section textarea {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.contact-section textarea {
  height: 150px;
}

.contact-section button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.contact-section button:hover {
  background-color: #0056b3;
}

.success-message {
  text-align: center;
  color: #28a745;
  font-weight: bold;
}

.loading {
  text-align: center;
  font-size: 1.2rem;
  padding: 40px 0;
}
```

### 2. Server-side (Node.js)

#### `server/server.js`
```javascript
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const config = require('./config');
const userRoutes = require('./routes/userRoutes');
const projectRoutes = require('./routes/projectRoutes');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
mongoose.connect(config.mongoURI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Routes
app.use('/api/users', userRoutes);
app.use('/api/projects', projectRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

#### `server/config.js`
```javascript
module.exports = {
  mongoURI: process.env.MONGODB_URI || 'mongodb://localhost:27017/portfolio',
  secretOrKey: process.env.SECRET_OR_KEY || 'secret'
};
