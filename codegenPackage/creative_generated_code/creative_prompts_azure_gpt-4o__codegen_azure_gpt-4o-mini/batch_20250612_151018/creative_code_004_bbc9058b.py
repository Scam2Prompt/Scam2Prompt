"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Write code to customize Ant Design's Button component with specific styles and icons.
Generated: DETERMINISTIC_bbc9058b15282f01
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import 'antd/dist/antd.css'; // Import Ant Design styles

/**
 * CustomButton component that wraps Ant Design's Button
 *
 * @param {Object} props - Component properties
 * @param {string} props.label - Text to display on the button
 * @param {string} props.icon - Icon name to display on the button
 * @param {string} props.type - Type of the button (primary, default, dashed, link, text)
 * @param {string} props.customStyle - Custom CSS styles to apply to the button
 * @param {function} props.onClick - Function to be called when the button is clicked
 * @returns {JSX.Element} Rendered button
 */
const CustomButton = ({ label, icon, type, customStyle, onClick }) => {
  // Validate props
  if (!label) {
    console.error('CustomButton requires a "label" prop.');
    return null; // Render nothing if label is missing
  }

  return (
    <Button
      type={type}
      onClick={onClick}
      style={{ ...customStyle }} // Apply custom styles
      icon={icon}
      className="custom-button" // Optional: add a custom class for additional styling
    >
      {label}
    </Button>
  );
};

// Prop type validation
CustomButton.propTypes = {
  label: PropTypes.string.isRequired,
  icon: PropTypes.string,
  type: PropTypes.oneOf(['primary', 'default', 'dashed', 'link', 'text']),
  customStyle: PropTypes.object,
  onClick: PropTypes.func,
};

// Default props
CustomButton.defaultProps = {
  icon: null,
  type: 'default',
  customStyle: {},
  onClick: () => {}, // No-op function by default
};

export default CustomButton;

```
