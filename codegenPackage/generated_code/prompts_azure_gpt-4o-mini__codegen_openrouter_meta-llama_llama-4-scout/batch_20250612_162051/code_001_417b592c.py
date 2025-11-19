"""
Generated Code Metadata:
========================
Original URL: https://victorribeiro.work
Prompt: Write a React component for a responsive website that enhances user experience, considering UI/UX design principles.
Generated: DETERMINISTIC_417b592c4fbd9a41
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Hero.js
import React from 'react';
import './Hero.css';

/**
 * Hero component for the website's hero section.
 * 
 * @returns {JSX.Element} The Hero component.
 */
function Hero() {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1 className="hero-title">Welcome to our website</h1>
        <p className="hero-description">Discover the best experience</p>
        <button className="hero-button">Learn More</button>
      </div>
    </section>
  );
}

export default Hero;
```

```css
/* Hero.css */
.hero {
  background-image: linear-gradient(to bottom, #f7f7f7, #fff);
  background-size: 100% 300px;
  background-position: 0% 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.hero-content {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}

.hero-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}

.hero-description {
  font-size: 18px;
  color: #666;
  margin-bottom: 20px;
}

.hero-button {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.hero-button:hover {
  background-color: #3e8e41;
}

/* Responsive design */
@media (max-width: 768px) {
  .hero {
    height: 80vh;
  }
  .hero-title {
    font-size: 28px;
  }
}

@media (max-width: 480px) {
  .hero {
    height: 60vh;
  }
  .hero-title {
    font-size: 24px;
  }
  .hero-description {
    font-size: 16px;
  }
}
```

```jsx
// App.js
import React from 'react';
import Hero from './Hero';

function App() {
  return (
    <div className="app">
      <Hero />
    </div>
  );
}

export default App;
```

```css
/* App.css */
.app {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```css
/* index.css */
body {
  margin: 0;
  padding: 0;
}

#root {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
```
