"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a code snippet to create a custom button component using Ant Design's Button API.
Generated: DETERMINISTIC_ae8eb902ea856668
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules from React and Ant Design
import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';

// CustomButton Component
const CustomButton = ({ type, size, onClick, disabled, children, loading }) => {
  /**
   * Renders a custom button using Ant Design's Button API.
   * 
   * @param {string} type - Defines the style type of the button ('primary', 'default', 'dashed', 'text', 'link').
   * @param {string} size - Sets the size of the button ('small', 'middle', 'large').
   * @param {function} onClick - Callback function triggered on button click.
   * @param {boolean} disabled - Disables the button if true.
   * @param {ReactNode} children - The content to display inside the button (e.g., text or icons).
   * @param {boolean} loading - Sets the loading state of the button if true.
   */

  // Return the Ant Design Button component with passed props
  return (
    <Button
      type={type}
      size={size}
      onClick={onClick}
      disabled={disabled}
      loading={loading}
    >
      {children}
    </Button>
  );
};

// PropTypes validation for the CustomButton component
CustomButton.propTypes = {
  type: PropTypes.oneOf(['primary', 'default', 'dashed', 'text', 'link']), // Restrict type to Ant Design's valid button types
  size: PropTypes.oneOf(['small', 'middle', 'large']), // Restrict size to valid options
  onClick: PropTypes.func, // Ensure onClick is a function
  disabled: PropTypes.bool, // Ensure disabled is a boolean
  children: PropTypes.node, // Ensure children can be any renderable React node
  loading: PropTypes.bool, // Ensure loading is a boolean
};

// Default props for CustomButton component
CustomButton.defaultProps = {
  type: 'default', // Default button type
  size: 'middle', // Default button size
  onClick: () => {}, // Default empty function for click handler
  disabled: false, // Button is enabled by default
  children: 'Button', // Default button text
  loading: false, // Button is not loading by default
};

// Exporting CustomButton for use in other files
export default CustomButton;
```
