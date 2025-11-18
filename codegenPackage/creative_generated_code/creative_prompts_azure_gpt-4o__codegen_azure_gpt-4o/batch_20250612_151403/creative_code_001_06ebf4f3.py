"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Generate a React.js web development project that incorporates responsive design principles as described by DigiTech Care India.
Generated: DETERMINISTIC_06ebf4f3321fb20a
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/index.js
// Entry point for the React.js application

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

// Create a React root and render the main App component
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```javascript
// File: src/App.js
// Main application component

import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ResponsiveGrid from "./components/ResponsiveGrid";

// App component that renders the application layout
function App() {
  return (
    <div>
      <Header />
      <main>
        <ResponsiveGrid />
      </main>
      <Footer />
    </div>
  );
}

export default App;
```

```javascript
// File: src/components/Header.js
// Header component

import React from "react";
import "./Header.css";

// Functional component for the header
function Header() {
  return (
    <header className="header">
      <h1 className="header-title">DigiTech Care India</h1>
      <nav className="header-nav">
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
```

```css
/* File: src/components/Header.css */
/* Styles for Header component */

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
}

.header-title {
  font-size: 1.5rem;
}

.header-nav ul {
  list-style: none;
  display: flex;
  gap: 15px;
}

.header-nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.header-nav a:hover {
  text-decoration: underline;
}
```

```javascript
// File: src/components/Footer.js
// Footer component

import React from "react";
import "./Footer.css";

// Functional component for the footer
function Footer() {
  return (
    <footer className="footer">
      <p>© 2023 DigiTech Care India. All rights reserved.</p>
    </footer>
  );
}

export default Footer;
```

```css
/* File: src/components/Footer.css */
/* Styles for Footer component */

.footer {
  text-align: center;
  padding: 20px;
  background-color: #f1f1f1;
  color: #333;
}
```

```javascript
// File: src/components/ResponsiveGrid.js
// Responsive grid layout component

import React from "react";
import "./ResponsiveGrid.css";

// Functional component for a responsive grid
function ResponsiveGrid() {
  const items = Array.from({ length: 12 }, (_, index) => `Item ${index + 1}`);

  return (
    <div className="grid-container">
      {items.map((item, index) => (
        <div key={index} className="grid-item">
          {item}
        </div>
      ))}
    </div>
  );
}

export default ResponsiveGrid;
```

```css
/* File: src/components/ResponsiveGrid.css */
/* Styles for ResponsiveGrid component */

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 10px;
  padding: 20px;
}

.grid-item {
  background-color: #007bff;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
```

```css
/* File: src/index.css */
/* Global styles */

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
}

main {
  padding: 20px;
}
```

```html
<!-- File: public/index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DigiTech Care India</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

```json
// File: package.json
{
  "name": "digitech-care-india",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

This code defines a responsive React.js project structure with components adhering to responsive design principles. It's ready to be run using `npm start`.
