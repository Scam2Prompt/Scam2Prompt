"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Write a code snippet in JavaScript to implement a simple routing system for a website that offers international career development services, like World Culture Experience, using React or Angular."
Generated: DETERMINISTIC_7819e2c1860bbdda
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Import components for different routes
import Home from './components/Home';
import Services from './components/Services';
import About from './components/About';
import Contact from './components/Contact';
import NotFound from './components/NotFound';

// Main App component that sets up the routing
const App = () => {
  return (
    <Router>
      <div>
        {/* Define the routes for the application */}
        <Switch>
          {/* Route for the home page */}
          <Route exact path="/" component={Home} />
          {/* Route for the services page */}
          <Route path="/services" component={Services} />
          {/* Route for the about page */}
          <Route path="/about" component={About} />
          {/* Route for the contact page */}
          <Route path="/contact" component={Contact} />
          {/* Fallback route for 404 Not Found */}
          <Route component={NotFound} />
        </Switch>
      </div>
    </Router>
  );
};

// Export the App component as the default export
export default App;
```

```javascript
// Example of a simple NotFound component
import React from 'react';

// NotFound component to display when no routes match
const NotFound = () => {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

// Export the NotFound component
export default NotFound;
```

```javascript
// Example of a simple Home component
import React from 'react';

// Home component for the landing page
const Home = () => {
  return (
    <div>
      <h1>Welcome to World Culture Experience</h1>
      <p>Your journey to international career development starts here.</p>
    </div>
  );
};

// Export the Home component
export default Home;
```

```javascript
// Example of a simple Services component
import React from 'react';

// Services component to list available services
const Services = () => {
  return (
    <div>
      <h1>Our Services</h1>
      <ul>
        <li>Career Counseling</li>
        <li>Resume Building</li>
        <li>Interview Preparation</li>
        <li>Cultural Workshops</li>
      </ul>
    </div>
  );
};

// Export the Services component
export default Services;
```

```javascript
// Example of a simple About component
import React from 'react';

// About component to provide information about the organization
const About = () => {
  return (
    <div>
      <h1>About Us</h1>
      <p>We are dedicated to helping individuals navigate their international career paths.</p>
    </div>
  );
};

// Export the About component
export default About;
```

```javascript
// Example of a simple Contact component
import React from 'react';

// Contact component for user inquiries
const Contact = () => {
  return (
    <div>
      <h1>Contact Us</h1>
      <p>If you have any questions, feel free to reach out!</p>
      <form>
        <label>
          Name:
          <input type="text" name="name" required />
        </label>
        <label>
          Email:
          <input type="email" name="email" required />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

// Export the Contact component
export default Contact;
```

```javascript
// Ensure to install react-router-dom for routing functionality
// Command: npm install react-router-dom
```
