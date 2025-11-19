"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a React component that demonstrates a unique front-end feature inspired by Tim Mansell's portfolio, such as dynamic rendering or state management.
Generated: DETERMINISTIC_328f7b4181538713
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * DynamicTextReveal component that animates text reveal on scroll.
 * Inspired by Tim Mansell's portfolio animations.
 */
const DynamicTextReveal = ({ text, speed = 50, threshold = 0.2 }) => {
  const [revealedText, setRevealedText] = useState('');
  const [isVisible, setIsVisible] = useState(false);
  const [animationComplete, setAnimationComplete] = useState(false);
  const elementRef = React.useRef(null);

  // Handle intersection observer for scroll-based triggering
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !animationComplete) {
          setIsVisible(true);
        }
      },
      { threshold }
    );

    if (elementRef.current) {
      observer.observe(elementRef.current);
    }

    return () => {
      if (elementRef.current) {
        observer.unobserve(elementRef.current);
      }
    };
  }, [threshold, animationComplete]);

  // Handle text reveal animation
  useEffect(() => {
    if (!isVisible) return;

    let currentIndex = 0;
    const interval = setInterval(() => {
      if (currentIndex < text.length) {
        setRevealedText((prev) => prev + text[currentIndex]);
        currentIndex++;
      } else {
        clearInterval(interval);
        setAnimationComplete(true);
      }
    }, speed);

    return () => clearInterval(interval);
  }, [isVisible, text, speed]);

  return (
    <div ref={elementRef} className="dynamic-text-reveal">
      <span className="revealed-text">{revealedText}</span>
      {!animationComplete && (
        <span className="cursor" aria-hidden="true">
          |
        </span>
      )}
    </div>
  );
};

DynamicTextReveal.propTypes = {
  text: PropTypes.string.isRequired,
  speed: PropTypes.number,
  threshold: PropTypes.number,
};

export default DynamicTextReveal;
```
