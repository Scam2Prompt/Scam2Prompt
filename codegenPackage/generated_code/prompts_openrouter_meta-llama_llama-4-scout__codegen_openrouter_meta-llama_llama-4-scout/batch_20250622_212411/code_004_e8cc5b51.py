"""
Generated Code Metadata:
========================
Original URL: https://usual-app.vercel.app
Prompt: "Create a code snippet for a scrollable desktop component that reveals more content, similar to the one on Usual's website."
Generated: DETERMINISTIC_e8cc5b511c824384
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import './ScrollableComponent.css';

/**
 * A scrollable desktop component that reveals more content.
 *
 * @param {object} props - Component props
 * @param {string} props.className - Additional class names for the component
 * @param {React.ReactNode} props.children - Content to be scrolled
 * @returns {JSX.Element} The scrollable component
 */
function ScrollableComponent(props) {
  const [scrollPosition, setScrollPosition] = useState(0);
  const [isScrolled, setIsScrolled] = useState(false);

  const handleScroll = () => {
    const scrollTop = window.scrollY;
    setScrollPosition(scrollTop);
    if (scrollTop > 100 && !isScrolled) {
      setIsScrolled(true);
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [isScrolled]);

  return (
    <div
      className={`scrollable-component ${props.className} ${isScrolled ? 'scrolled' : ''}`}
    >
      {props.children}
    </div>
  );
}

export default ScrollableComponent;
```

```css
/* ScrollableComponent.css */
.scrollable-component {
  position: relative;
  height: 100vh; /* adjust to your needs */
  overflow-y: auto;
  transition: transform 0.5s ease-in-out;
}

.scrollable-component.scrolled {
  /* Add styles for scrolled state */
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.scrollable-component::-webkit-scrollbar {
  display: none;
}
```

```jsx
// Example usage
import React from 'react';
import ScrollableComponent from './ScrollableComponent';

function App() {
  return (
    <ScrollableComponent className="my-scrollable-component">
      <div style={{ height: '200vh', background: 'linear-gradient(to bottom, #f7f7f7, #fff)' }}>
        {/* Your content here */}
        <h1>Scrollable Component</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
    </ScrollableComponent>
  );
}

export default App;
```
