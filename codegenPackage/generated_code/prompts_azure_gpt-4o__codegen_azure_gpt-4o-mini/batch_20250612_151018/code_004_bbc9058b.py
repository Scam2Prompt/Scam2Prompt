"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Write code to customize Ant Design's Button component with specific styles and icons.
Generated: DETERMINISTIC_bbc9058b15282f01
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import 'antd/dist/antd.css'; // Import Ant Design styles

/**
 * CustomButton component that wraps Ant Design's Button
 * to provide additional styling and icon support.
 *
 * @param {Object} props - Component properties
 * @param {string} props.label - The text to display on the button
 * @param {string} props.icon - The icon type to display on the button
 * @param {string} props.customStyle - Additional custom styles for the button
 * @param {function} props.onClick - Function to call on button click
 * @param {boolean} props.disabled - Flag to disable the button
 * @returns {JSX.Element} Rendered CustomButton component
 */
const CustomButton = ({ label, icon, customStyle, onClick, disabled }) => {
  // Validate props
  if (typeof label !== 'string') {
    console.error('Invalid prop: label must be a string');
    return null;
  }

  return (
    <Button
      type="primary"
      icon={icon}
      style={{ ...defaultStyle, ...customStyle }} // Merge default and custom styles
      onClick={onClick}
      disabled={disabled}
    >
      {label}
    </Button>
  );
};

// Default styles for the button
const defaultStyle = {
  borderRadius: '5px',
  padding: '10px 20px',
};

// Prop types validation
CustomButton.propTypes = {
  label: PropTypes.string.isRequired,
  icon: PropTypes.string,
  customStyle: PropTypes.object,
  onClick: PropTypes.func,
  disabled: PropTypes.bool,
};

// Default props
CustomButton.defaultProps = {
  icon: null,
  customStyle: {},
  onClick: () => {},
  disabled: false,
};

export default CustomButton;
```
