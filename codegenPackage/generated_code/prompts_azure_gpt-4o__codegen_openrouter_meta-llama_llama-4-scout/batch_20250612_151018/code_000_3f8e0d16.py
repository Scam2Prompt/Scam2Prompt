"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a React component that demonstrates a front-end feature similar to those described on Tim Mansell's portfolio website.
Generated: DETERMINISTIC_3f8e0d168d67f262
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// TypingText.js
import React, { useState, useEffect } from 'react';

/**
 * A React component that simulates a typing effect.
 * 
 * @param {Object} props
 * @param {string} props.text - The text to be typed.
 * @param {number} props.speed - The typing speed in milliseconds.
 * @param {function} props.onComplete - A callback function when typing is complete.
 */
const TypingText = ({ text, speed, onComplete }) => {
  const [displayText, setDisplayText] = useState('');
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      if (index < text.length) {
        setDisplayText(text.substring(0, index + 1));
        setIndex(index + 1);
      } else {
        clearInterval(intervalId);
        if (onComplete) onComplete();
      }
    }, speed);

    return () => clearInterval(intervalId);
  }, [index, text, speed, onComplete]);

  return (
    <span>
      {displayText}
      {index < text.length && <span className="cursor">|</span>}
    </span>
  );
};

export default TypingText;
```

```jsx
// AnimatedCursor.js
import React from 'react';

/**
 * A React component that simulates a animated cursor.
 * 
 * @param {Object} props
 * @param {string} props.className - The class name for the cursor element.
 */
const AnimatedCursor = ({ className }) => {
  return (
    <span className={`cursor ${className}`}>
      <span className="cursor-dot"></span>
      <span className="cursor-dot"></span>
      <span className="cursor-dot"></span>
    </span>
  );
};

export default AnimatedCursor;
```

```jsx
// Hero.js
import React from 'react';
import TypingText from './TypingText';
import AnimatedCursor from './AnimatedCursor';

/**
 * A React component that represents a hero section.
 */
const Hero = () => {
  const handleTypingComplete = () => {
    console.log('Typing complete!');
  };

  return (
    <section className="hero">
      <h1>
        <TypingText
          text="Welcome to my portfolio!"
          speed={100}
          onComplete={handleTypingComplete}
        />
      </h1>
      <AnimatedCursor className="hero-cursor" />
    </section>
  );
};

export default Hero;
```

```css
/* styles.css */
.cursor {
  position: relative;
}

.cursor-dot {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background-color: #333;
  animation: cursor-dot 1.5s infinite;
}

@keyframes cursor-dot {
  0% {
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.5);
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
  }
}

.hero {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 36px;
}

.hero-cursor {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

```jsx
// App.js
import React from 'react';
import Hero from './Hero';
import './styles.css';

const App = () => {
  return (
    <div>
      <Hero />
    </div>
  );
};

export default App;
```
