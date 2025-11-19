"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Generate a sample Docusaurus layout that reuses React components for a consistent header and footer across pages.
Generated: DETERMINISTIC_88314bc388485f6d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Importing CSS for styling

/**
 * Header component that renders the navigation bar.
 * @returns {JSX.Element} The header element with navigation links.
 */
const Header = () => {
    return (
        <header className="app-header">
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

```javascript
// src/components/Footer.js
import React from 'react';
import './Footer.css'; // Importing CSS for styling

/**
 * Footer component that renders the footer section.
 * @returns {JSX.Element} The footer element with copyright information.
 */
const Footer = () => {
    return (
        <footer className="app-footer">
            <p>&copy; {new Date().getFullYear()} My Company. All rights reserved.</p>
        </footer>
    );
};

export default Footer;
```

```javascript
// src/layouts/MainLayout.js
import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import './MainLayout.css'; // Importing CSS for layout styling

/**
 * MainLayout component that wraps the page content with a header and footer.
 * @param {Object} props - The props object.
 * @param {JSX.Element} props.children - The child components to render within the layout.
 * @returns {JSX.Element} The layout with header, content, and footer.
 */
const MainLayout = ({ children }) => {
    return (
        <div className="main-layout">
            <Header />
            <main className="content">
                {children}
            </main>
            <Footer />
        </div>
    );
};

export default MainLayout;
```

```javascript
// src/pages/Home.js
import React from 'react';
import MainLayout from '../layouts/MainLayout';

/**
 * Home page component.
 * @returns {JSX.Element} The home page content.
 */
const Home = () => {
    return (
        <MainLayout>
            <h1>Welcome to My Website</h1>
            <p>This is the home page content.</p>
        </MainLayout>
    );
};

export default Home;
```

```javascript
// src/pages/About.js
import React from 'react';
import MainLayout from '../layouts/MainLayout';

/**
 * About page component.
 * @returns {JSX.Element} The about page content.
 */
const About = () => {
    return (
        <MainLayout>
            <h1>About Us</h1>
            <p>This is the about page content.</p>
        </MainLayout>
    );
};

export default About;
```

```javascript
// src/pages/Contact.js
import React from 'react';
import MainLayout from '../layouts/MainLayout';

/**
 * Contact page component.
 * @returns {JSX.Element} The contact page content.
 */
const Contact = () => {
    return (
        <MainLayout>
            <h1>Contact Us</h1>
            <p>This is the contact page content.</p>
        </MainLayout>
    );
};

export default Contact;
```

```javascript
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

/**
 * Main application component that sets up routing.
 * @returns {JSX.Element} The main application with routes.
 */
const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/about" component={About} />
                <Route path="/contact" component={Contact} />
            </Switch>
        </Router>
    );
};

export default App;
```

```css
/* src/components/Header.css */
.app-header {
    background-color: #282c34;
    padding: 20px;
    color: white;
}

.app-header nav ul {
    list-style-type: none;
    padding: 0;
}

.app-header nav ul li {
    display: inline;
    margin-right: 20px;
}

/* src/components/Footer.css */
.app-footer {
    background-color: #282c34;
    padding: 10px;
    color: white;
    text-align: center;
}

/* src/layouts/MainLayout.css */
.main-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.content {
    flex: 1;
    padding: 20px;
}
```

```json
// package.json (snippet)
{
  "name": "my-docusaurus-app",
  "version": "1.0.0",
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.2.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

This code provides a complete Docusaurus layout with reusable React components for a consistent header and footer across pages. Each component is well-documented, and the layout is structured for maintainability and scalability.
