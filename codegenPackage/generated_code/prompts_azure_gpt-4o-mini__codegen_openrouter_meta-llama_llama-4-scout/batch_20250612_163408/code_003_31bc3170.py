"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: How can I implement a responsive design for a front-end engineer's portfolio using React, as seen in Tim Mansell's site?
Generated: DETERMINISTIC_31bc3170b2a6daa1
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Responsive Portfolio Website using React**
=====================================================

### `index.js`
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

### `App.js`
```javascript
import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Projects from './components/Projects';
import Footer from './components/Footer';
import './App.css';

function App() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    window.addEventListener('resize', () => setWidth(window.innerWidth));
    return () => window.removeEventListener('resize', () => setWidth(window.innerWidth));
  }, []);

  return (
    <div className="app">
      <Navbar width={width} />
      <Hero width={width} />
      <Projects width={width} />
      <Footer />
    </div>
  );
}

export default App;
```

### `components/Navbar.js`
```javascript
import React from 'react';
import './Navbar.css';

function Navbar({ width }) {
  return (
    <nav className={`navbar ${width < 768 ? 'mobile' : ''}`}>
      <ul>
        <li><a href="#hero">Home</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

### `components/Hero.js`
```javascript
import React from 'react';
import './Hero.css';

function Hero({ width }) {
  return (
    <section id="hero" className={`hero ${width < 768 ? 'mobile' : ''}`}>
      <h1>Welcome to my portfolio!</h1>
      <p>I'm a front-end engineer with a passion for building responsive websites.</p>
    </section>
  );
}

export default Hero;
```

### `components/Projects.js`
```javascript
import React from 'react';
import Project from './Project';
import './Projects.css';

function Projects({ width }) {
  const projects = [
    {
      id: 1,
      title: 'Project 1',
      description: 'This is a project I worked on.',
      image: 'project1.jpg',
    },
    {
      id: 2,
      title: 'Project 2',
      description: 'This is another project I worked on.',
      image: 'project2.jpg',
    },
  ];

  return (
    <section id="projects" className={`projects ${width < 768 ? 'mobile' : ''}`}>
      <h2>My Projects</h2>
      <div className="project-grid">
        {projects.map((project) => (
          <Project key={project.id} project={project} />
        ))}
      </div>
    </section>
  );
}

export default Projects;
```

### `components/Project.js`
```javascript
import React from 'react';
import './Project.css';

function Project({ project }) {
  return (
    <div className="project">
      <img src={project.image} alt={project.title} />
      <h3>{project.title}</h3>
      <p>{project.description}</p>
    </div>
  );
}

export default Project;
```

### `components/Footer.js`
```javascript
import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <p>&copy; 2023 My Portfolio</p>
    </footer>
  );
}

export default Footer;
```

### `App.css`
```css
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.navbar {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

.navbar ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

.navbar li {
  margin-right: 20px;
}

.navbar a {
  color: #fff;
  text-decoration: none;
}

.hero {
  background-image: linear-gradient(to bottom, #333, #555);
  background-size: 100% 300px;
  background-position: 0% 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}

.hero h1 {
  font-size: 48px;
}

.projects {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.project {
  background-color: #f7f7f7;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.footer {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
  clear: both;
}

/* Mobile styles */
.navbar.mobile {
  flex-direction: column;
}

.navbar.mobile ul {
  flex-direction: column;
}

.navbar.mobile li {
  margin-right: 0;
  margin-bottom: 10px;
}

.hero.mobile {
  height: 50vh;
}

.project-grid.mobile {
  grid-template-columns: 1fr;
}
```

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
