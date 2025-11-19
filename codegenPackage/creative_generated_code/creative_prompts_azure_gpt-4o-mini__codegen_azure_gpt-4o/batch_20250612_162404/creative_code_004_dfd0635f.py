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
// LoadingSpinner.jsx
import React from 'react';
import PropTypes from 'prop-types';
import './LoadingSpinner.css'; // Import the CSS for styling

/**
 * LoadingSpinner Component
 * A reusable loading spinner component that can be used across the application.
 *
 * Props:
 * - size: The size of the spinner (e.g., 'small', 'medium', 'large'). Default is 'medium'.
 * - color: The color of the spinner. Default is '#000' (black).
 *
 * Usage:
 * <LoadingSpinner size="large" color="#00f" />
 */
const LoadingSpinner = ({ size = 'medium', color = '#000' }) => {
  const spinnerSizes = {
    small: '20px',
    medium: '40px',
    large: '60px',
  };

  const spinnerSize = spinnerSizes[size] || spinnerSizes.medium;

  return (
    <div
      className="loading-spinner"
      style={{
        width: spinnerSize,
        height: spinnerSize,
        borderColor: `${color} transparent transparent transparent`,
      }}
    ></div>
  );
};

// Prop validation for reusable and reliable code
LoadingSpinner.propTypes = {
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  color: PropTypes.string,
};

export default LoadingSpinner;

// LoadingSpinner.css
/**
 * CSS for the LoadingSpinner Component
 * Creates a spinning animation for the loader.
 */

.loading-spinner {
  display: inline-block;
  border: 4px solid transparent; /* Border thickness */
  border-radius: 50%; /* Makes it circular */
  animation: spin 1.2s linear infinite; /* Spinning animation */
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
