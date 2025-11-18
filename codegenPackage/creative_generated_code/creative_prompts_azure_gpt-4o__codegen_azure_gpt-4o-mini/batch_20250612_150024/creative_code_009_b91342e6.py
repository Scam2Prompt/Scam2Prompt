"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m-wisemonkey.pages.dev
Prompt: Create a frontend component to display a "high-risk investment" disclaimer dynamically, as seen on the "Wise Monky" website.
Generated: DETERMINISTIC_b91342e6602ef3d1
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './HighRiskDisclaimer.css'; // Importing CSS for styling

/**
 * HighRiskDisclaimer component displays a dynamic disclaimer for high-risk investments.
 * 
 * @param {Object} props - The component props.
 * @param {boolean} props.isVisible - Determines if the disclaimer should be visible.
 * 
 * @returns {JSX.Element} The rendered component.
 */
const HighRiskDisclaimer = ({ isVisible }) => {
  const [showDisclaimer, setShowDisclaimer] = useState(isVisible);

  // Effect to handle visibility of the disclaimer
  useEffect(() => {
    setShowDisclaimer(isVisible);
  }, [isVisible]);

  // Function to close the disclaimer
  const closeDisclaimer = () => {
    setShowDisclaimer(false);
  };

  // Render the disclaimer
  return (
    <>
      {showDisclaimer && (
        <div className="high-risk-disclaimer">
          <div className="disclaimer-content">
            <h2>Disclaimer</h2>
            <p>
              Investing in financial markets involves a high level of risk and may not be suitable for all investors. 
              Past performance is not indicative of future results. Please invest responsibly.
            </p>
            <button onClick={closeDisclaimer} className="close-button">
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
};

// PropType validation
HighRiskDisclaimer.propTypes = {
  isVisible: PropTypes.bool.isRequired
};

export default HighRiskDisclaimer;
```

```css
/* HighRiskDisclaimer.css */

.high-risk-disclaimer {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #ffcc00;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.disclaimer-content {
  font-family: Arial, sans-serif;
  color: #333;
}

.close-button {
  background-color: #d9534f;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.close-button:hover {
  background-color: #c9302c;
}
```
