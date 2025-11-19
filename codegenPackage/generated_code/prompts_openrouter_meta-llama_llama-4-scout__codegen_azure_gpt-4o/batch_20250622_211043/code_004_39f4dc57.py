"""
Generated Code Metadata:
========================
Original URL: https://celestia.top
Prompt: "Create a simple web app using React that allows architects to showcase their projects and collaborate with clients."
Generated: DETERMINISTIC_39f4dc57f898dfb0
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// File: App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Projects from './pages/Projects';
import Contact from './pages/Contact';
import NotFound from './pages/NotFound';

// Main App Component
const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
};

export default App;

// File: components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

// Navigation Bar Component
const Navbar = () => {
  return (
    <nav style={styles.navbar}>
      <Link to="/" style={styles.link}>Home</Link>
      <Link to="/projects" style={styles.link}>Projects</Link>
      <Link to="/contact" style={styles.link}>Contact</Link>
    </nav>
  );
};

const styles = {
  navbar: {
    display: 'flex',
    justifyContent: 'space-around',
    padding: '1rem',
    backgroundColor: '#333',
    color: '#fff',
  },
  link: {
    color: '#fff',
    textDecoration: 'none',
  },
};

export default Navbar;

// File: pages/Home.js
import React from 'react';

// Home Page Component
const Home = () => {
  return (
    <div style={styles.container}>
      <h1>Welcome to Architect Showcase</h1>
      <p>Explore projects and collaborate with clients.</p>
    </div>
  );
};

const styles = {
  container: {
    padding: '2rem',
    textAlign: 'center',
  },
};

export default Home;

// File: pages/Projects.js
import React, { useState, useEffect } from 'react';

// Projects Page Component
const Projects = () => {
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState(null);

  // Fetch projects from a mock API
  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch('/api/projects'); // Replace with actual API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch projects');
        }
        const data = await response.json();
        setProjects(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div style={styles.container}>
      <h1>Projects</h1>
      {error ? (
        <p style={styles.error}>{error}</p>
      ) : (
        <ul style={styles.list}>
          {projects.map((project) => (
            <li key={project.id} style={styles.listItem}>
              <h2>{project.name}</h2>
              <p>{project.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

const styles = {
  container: {
    padding: '2rem',
  },
  error: {
    color: 'red',
  },
  list: {
    listStyleType: 'none',
    padding: 0,
  },
  listItem: {
    marginBottom: '1rem',
    border: '1px solid #ccc',
    padding: '1rem',
    borderRadius: '5px',
  },
};

export default Projects;

// File: pages/Contact.js
import React, { useState } from 'react';

// Contact Page Component
const Contact = () => {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });
  const [success, setSuccess] = useState(false);

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate form submission
    console.log('Form submitted:', formData);
    setSuccess(true);
  };

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div style={styles.container}>
      <h1>Contact Us</h1>
      {success ? (
        <p style={styles.success}>Thank you for your message!</p>
      ) : (
        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="text"
            name="name"
            placeholder="Your Name"
            value={formData.name}
            onChange={handleChange}
            style={styles.input}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Your Email"
            value={formData.email}
            onChange={handleChange}
            style={styles.input}
            required
          />
          <textarea
            name="message"
            placeholder="Your Message"
            value={formData.message}
            onChange={handleChange}
            style={styles.textarea}
            required
          />
          <button type="submit" style={styles.button}>Send</button>
        </form>
      )}
    </div>
  );
};

const styles = {
  container: {
    padding: '2rem',
  },
  success: {
    color: 'green',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
  },
  input: {
    padding: '0.5rem',
    border: '1px solid #ccc',
    borderRadius: '5px',
  },
  textarea: {
    padding: '0.5rem',
    border: '1px solid #ccc',
    borderRadius: '5px',
    resize: 'none',
  },
  button: {
    padding: '0.5rem',
    backgroundColor: '#333',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
};

export default Contact;

// File: pages/NotFound.js
import React from 'react';

// Not Found Page Component
const NotFound = () => {
  return (
    <div style={styles.container}>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

const styles = {
  container: {
    padding: '2rem',
    textAlign: 'center',
  },
};

export default NotFound;

// File: index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the App component into the root element
ReactDOM.render(<App />, document.getElementById('root'));
```

### Notes:
1. This code assumes you have a React environment set up with `react-router-dom` installed.
2. Replace `/api/projects` in the `Projects` page with your actual API endpoint.
3. Add a mock backend or API for fetching projects if needed.
