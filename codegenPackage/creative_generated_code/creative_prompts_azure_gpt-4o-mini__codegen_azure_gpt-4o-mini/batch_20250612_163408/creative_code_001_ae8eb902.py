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
import React from 'react';
import PropTypes from 'prop-types';
import { Button } from 'antd';

// CustomButton component defines a reusable button with Ant Design's Button API
const CustomButton = ({ 
  type,           // The type of button (primary, default, dashed, link, text, etc.)
  onClick,       // Click event handler
  label,         // Button label
  loading,       // Loading state boolean
  disabled,      // Disabled state boolean
  icon,          // Optional icon to be displayed
  style,         // Custom styles for the button
  className      // Additional class names for styling
}) => {
  return (
    <Button
      type={type}
      onClick={onClick}
      loading={loading}
      disabled={disabled}
      style={style}
      className={className}
      icon={icon}
    >
      {label}
    </Button>
  );
};

// PropTypes for type checking
CustomButton.propTypes = {
  type: PropTypes.oneOf(['primary', 'default', 'dashed', 'link', 'text']),
  onClick: PropTypes.func.isRequired,
  label: PropTypes.string.isRequired,
  loading: PropTypes.bool,
  disabled: PropTypes.bool,
  icon: PropTypes.element,
  style: PropTypes.object,
  className: PropTypes.string,
};

// Default props to maintain consistency
CustomButton.defaultProps = {
  type: 'default',
  loading: false,
  disabled: false,
  icon: null,
  style: {},
  className: '',
};

// Exporting the CustomButton to be used in other parts of the application
export default CustomButton;
```
