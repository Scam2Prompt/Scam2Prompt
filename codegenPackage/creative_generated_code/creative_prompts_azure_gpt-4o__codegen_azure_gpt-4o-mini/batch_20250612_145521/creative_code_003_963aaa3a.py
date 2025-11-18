"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Develop a feature in a React app that displays tokenomics data (e.g., presale allocation, liquidity, marketing percentages) dynamically, using the structure outlined in the GoodEgg tokenomics section.
Generated: DETERMINISTIC_963aaa3ad238f242
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './Tokenomics.css'; // Assuming a CSS file for styles

// Tokenomics component to display token distribution percentages
const Tokenomics = ({ tokenData }) => {
  const [data, setData] = useState([]);

  // Fetch tokenomics data from the passed prop
  useEffect(() => {
    if (tokenData && tokenData.length > 0) {
      setData(tokenData);
    } else {
      console.error('Invalid token data provided');
    }
  }, [tokenData]);

  // Error handling for empty or invalid data
  if (!data.length) {
    return <div className="tokenomics-error">No tokenomics data available</div>;
  }

  return (
    <div className="tokenomics-container">
      <h2>Tokenomics Overview</h2>
      <div className="tokenomics-list">
        {data.map((item) => (
          <div key={item.id} className="tokenomics-item">
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <div className="tokenomics-percentage">
              <span>{item.percentage}%</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// PropTypes for validation
Tokenomics.propTypes = {
  tokenData: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      description: PropTypes.string,
      percentage: PropTypes.number.isRequired,
    })
  ).isRequired,
};

export default Tokenomics;
```

```css
/* Tokenomics.css */

.tokenomics-container {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.tokenomics-list {
  display: flex;
  flex-direction: column;
}

.tokenomics-item {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background-color: #fff;
}

.tokenomics-percentage {
  font-size: 1.5em;
  font-weight: bold;
  color: #4caf50;
}

.tokenomics-error {
  color: red;
  text-align: center;
  font-weight: bold;
}
```
