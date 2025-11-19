"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Generate a sample Docusaurus layout that reuses React components for a consistent header and footer across pages.
Generated: DETERMINISTIC_88314bc388485f6d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// src/components/Header.js

import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Assuming you have some CSS to style the header

/**
 * Header component to be reused across pages.
 * This component contains the navigation links.
 */
const Header = () => {
  return (
    <header className="site-header">
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
```

```jsx
// src/components/Footer.js

import React from 'react';
import './Footer.css'; // Assuming you have some CSS to style the footer

/**
 * Footer component to be reused across pages.
 * This component contains copyright and other links.
 */
const Footer = () => {
  return (
    <footer className="site-footer">
      <p>&copy; {new Date().getFullYear()} Your Company. All rights reserved.</p>
      <p><a href="/privacy">Privacy Policy</a></p>
    </footer>
  );
};

export default Footer;
```

```jsx
// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import './App.css'; // Main application CSS file

/**
 * Main application component that sets up the Docusaurus layout.
 * It includes the Header, Footer and routes for different pages.
 */
const App = () => {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <main>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/contact" component={Contact} />
            {/* Add more routes here as needed */}
          </Switch>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
```

```jsx
// src/pages/Home.js

import React from 'react';

/**
 * Home page component.
 */
const Home = () => {
  return (
    <div>
      <h1>Welcome to Our Site</h1>
      <p>This is the home page.</p>
    </div>
  );
};

export default Home;
```

```jsx
// src/pages/About.js

import React from 'react';

/**
 * About page component.
 */
const About = () => {
  return (
    <div>
      <h1>About Us</h1>
      <p>This is the about page.</p>
    </div>
  );
};

export default About;
```

```jsx
// src/pages/Contact.js

import React from 'react';

/**
 * Contact page component.
 */
const Contact = () => {
  return (
    <div>
      <h1>Contact Us</h1>
      <p>This is the contact page.</p>
    </div>
  );
};

export default Contact;
```

```css
/* src/components/Header.css */

/* Basic styling for the header */
.site-header {
  background-color: #f8f9fa;
  padding: 20px;
}

.site-header nav ul {
  list-style: none;
  padding: 0;
}

.site-header nav ul li {
  display: inline;
  margin-right: 15px;
}
```

```css
/* src/components/Footer.css */

/* Basic styling for the footer */
.site-footer {
  background-color: #f1f1f1;
  text-align: center;
  padding: 10px;
}
```

```css
/* src/App.css */

/* Main application styles */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}
```
