"""
Generated Code Metadata:
========================
Original URL: https://stoneage.com
Prompt: "Generate code to implement a Stoneage-themed UI component using React."
Generated: DETERMINISTIC_242b64c47c79a02f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './StoneageUI.css';

/**
 * Stoneage-themed UI component with customizable content and styling.
 * @param {Object} props - Component properties.
 * @param {string} props.title - Title text for the component.
 * @param {string} props.content - Main content text.
 * @param {string} [props.theme='default'] - Theme variant ('default', 'cave', 'forest').
 * @param {boolean} [props.showIcon=true] - Toggle for displaying stoneage icon.
 * @param {function} [props.onClick] - Click handler for the component.
 */
const StoneageUI = ({ title, content, theme = 'default', showIcon = true, onClick }) => {
  const handleClick = (e) => {
    if (onClick) {
      onClick(e);
    }
  };

  return (
    <div 
      className={`stoneage-ui ${theme}`}
      onClick={handleClick}
      role="button"
      tabIndex={0}
      aria-label="Stoneage themed component"
    >
      {showIcon && (
        <div className="stoneage-icon">
          <span role="img" aria-label="Caveman">🧔</span>
        </div>
      )}
      <div className="stoneage-content">
        <h2 className="stoneage-title">{title}</h2>
        <p className="stoneage-text">{content}</p>
      </div>
    </div>
  );
};

StoneageUI.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  theme: PropTypes.oneOf(['default', 'cave', 'forest']),
  showIcon: PropTypes.bool,
  onClick: PropTypes.func,
};

export default StoneageUI;
```

```css
/* StoneageUI.css */
.stoneage-ui {
  font-family: 'Courier New', monospace;
  border: 3px solid #8B4513;
  border-radius: 8px;
  padding: 20px;
  background-color: #F5DEB3;
  color: #5C4033;
  cursor: pointer;
  transition: all 0.3s ease;
  max-width: 500px;
  margin: 20px auto;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
}

.stoneage-ui:hover {
  transform: translateY(-2px);
  box-shadow: 7px 7px 20px rgba(0, 0, 0, 0.3);
}

.stoneage-ui.cave {
  background-color: #696969;
  color: #F5F5DC;
  border-color: #2F4F4F;
}

.stoneage-ui.forest {
  background-color: #556B2F;
  color: #F5F5DC;
  border-color: #8FBC8F;
}

.stoneage-icon {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 15px;
}

.stoneage-title {
  font-size: 1.5rem;
  margin: 0 0 10px 0;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.stoneage-text {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 600px) {
  .stoneage-ui {
    padding: 15px;
  }
  
  .stoneage-title {
    font-size: 1.2rem;
  }
}
```
