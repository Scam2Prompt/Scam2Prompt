"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Develop a web application using React that showcases the various humanitarian activities of Indological India, including health care and education.
Generated: DETERMINISTIC_79dbe4211fffb483
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

// Components
import Home from './components/Home';
import Healthcare from './components/Healthcare';
import Education from './components/Education';
import About from './components/About';
import Contact from './components/Contact';
import NotFound from './components/NotFound';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="header">
          <nav className="navbar">
            <div className="logo">
              <Link to="/">Indological India</Link>
            </div>
            <ul className="nav-links">
              <li><Link to="/">Home</Link></li>
              <li><Link to="/healthcare">Healthcare</Link></li>
              <li><Link to="/education">Education</Link></li>
              <li><Link to="/about">About Us</Link></li>
              <li><Link to="/contact">Contact</Link></li>
            </ul>
          </nav>
        </header>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/healthcare" element={<Healthcare />} />
            <Route path="/education" element={<Education />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>

        <footer className="footer">
          <p>&copy; {new Date().getFullYear()} Indological India. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
```

```javascript
// components/Home.js
import React from 'react';

const Home = () => {
  return (
    <div className="home">
      <section className="hero">
        <h1>Welcome to Indological India</h1>
        <p>Transforming lives through healthcare and education initiatives</p>
      </section>

      <section className="highlights">
        <div className="highlight-card">
          <h2>Healthcare Programs</h2>
          <p>Providing medical care to underserved communities across India.</p>
        </div>
        <div className="highlight-card">
          <h2>Education Initiatives</h2>
          <p>Empowering youth through quality education and skill development.</p>
        </div>
      </section>
    </div>
  );
};

export default Home;
```

```javascript
// components/Healthcare.js
import React from 'react';

const Healthcare = () => {
  return (
    <div className="healthcare">
      <h1>Healthcare Initiatives</h1>
      <div className="programs">
        <div className="program-card">
          <h2>Rural Health Camps</h2>
          <p>Mobile medical units providing free checkups and medicines in remote areas.</p>
        </div>
        <div className="program-card">
          <h2>Maternal Health</h2>
          <p>Prenatal and postnatal care for mothers in underserved communities.</p>
        </div>
        <div className="program-card">
          <h2>Disease Prevention</h2>
          <p>Awareness campaigns and vaccination drives for preventable diseases.</p>
        </div>
      </div>
    </div>
  );
};

export default Healthcare;
```

```javascript
// components/Education.js
import React from 'react';

const Education = () => {
  return (
    <div className="education">
      <h1>Education Programs</h1>
      <div className="programs">
        <div className="program-card">
          <h2>School Adoption</h2>
          <p>Improving infrastructure and quality of education in government schools.</p>
        </div>
        <div className="program-card">
          <h2>Scholarships</h2>
          <p>Financial support for meritorious students from underprivileged backgrounds.</p>
        </div>
        <div className="program-card">
          <h2>Digital Literacy</h2>
          <p>Training programs to bridge the digital divide in rural areas.</p>
        </div>
      </div>
    </div>
  );
};

export default Education;
```

```javascript
// components/About.js
import React from 'react';

const About = () => {
  return (
    <div className="about">
      <h1>About Indological India</h1>
      <section className="mission">
        <h2>Our Mission</h2>
        <p>
          To create sustainable impact through healthcare and education initiatives,
          empowering communities across India to break the cycle of poverty.
        </p>
      </section>
      <section className="history">
        <h2>Our History</h2>
        <p>
          Founded in 2010, Indological India has impacted over 1 million lives
          through its various humanitarian programs.
        </p>
      </section>
    </div>
  );
};

export default About;
```

```javascript
// components/Contact.js
import React, { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real app, you would send this data to a backend
    alert('Thank you for your message! We will get back to you soon.');
    setFormData({
      name: '',
      email: '',
      message: ''
    });
  };

  return (
    <div className="contact">
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="message">Message:</label>
          <textarea
            id="message"
            name="message"
            value={formData.message}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Send Message</button>
      </form>
    </div>
  );
};

export default Contact;
```

```javascript
// components/NotFound.js
import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = () => {
  return (
    <div className="not-found">
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for doesn't exist or has been moved.</p>
      <Link to="/" className="home-link">Return to Home</Link>
    </div>
  );
};

export default NotFound;
```

```css
/* App.css */
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --accent-color: #e74c3c;
  --light-color: #ecf0f1;
  --dark-color: #2c3e50;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--dark-color);
}

.App {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  background-color: var(--primary-color);
  color: white;
  padding: 1rem 0;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.logo a {
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
}

.nav-links {
  display: flex;
  list-style: none;
}

.nav-links li {
  margin-left: 1.5rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: var(--secondary-color);
}

.main-content {
  flex: 1;
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.footer {
  background-color: var(--primary-color);
  color:
