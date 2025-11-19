"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-11.pages.dev
Prompt: Create a React loading spinner component that can be reused across different parts of an application.
Generated: DETERMINISTIC_dfd0635fabfb61c3
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Spinner.js

import React from 'react';
import PropTypes from 'prop-types';
import './Spinner.css'; // Assuming you have a separate CSS file for styles

const Spinner = ({ size = 'medium', color = '#000', isLoading = true }) => {
  // Early return if not loading
  if (!isLoading) return null;

  return (
    <div className={`spinner spinner--${size}`} style={{ borderColor: color }}>
      <div className="spinner__dot"></div>
      <div className="spinner__dot"></div>
      <div className="spinner__dot"></div>
    </div>
  );
};

// Prop type validations
Spinner.propTypes = {
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  color: PropTypes.string,
  isLoading: PropTypes.bool,
};

export default Spinner;
```

```css
/* Spinner.css */

.spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.spinner--small {
  width: 30px;
  height: 30px;
}

.spinner--medium {
  width: 50px;
  height: 50px;
}

.spinner--large {
  width: 70px;
  height: 70px;
}

.spinner__dot {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: currentColor;
  animation: spin 1s infinite ease-in-out;
}

.spinner__dot:nth-child(1) {
  animation-delay: -0.2s;
}

.spinner__dot:nth-child(2) {
  animation-delay: -0.1s;
}

@keyframes spin {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
```

### Usage Example

```javascript
// App.js

import React from 'react';
import Spinner from './Spinner';

const App = () => {
  const [loading, setLoading] = React.useState(true);

  // Simulate a data fetch
  React.useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false); // Stop loading after 3 seconds
    }, 3000);
    
    return () => clearTimeout(timer); // Cleanup on unmount
  }, []);

  return (
    <div className="app">
      <h1>Loading Spinner Example</h1>
      <Spinner size="large" color="#3498db" isLoading={loading} />
    </div>
  );
};

export default App;
```
