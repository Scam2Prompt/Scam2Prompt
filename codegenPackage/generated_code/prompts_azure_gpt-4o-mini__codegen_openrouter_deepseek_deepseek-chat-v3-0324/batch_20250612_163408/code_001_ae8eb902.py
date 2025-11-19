"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a code snippet to create a custom button component using Ant Design's Button API.
Generated: DETERMINISTIC_ae8eb902ea856668
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';

/**
 * CustomButton Component
 * 
 * @param {Object} props - Component props
 * @param {string} props.type - Button type (primary, dashed, text, link, default)
 * @param {string} props.shape - Button shape (circle, round)
 * @param {string} props.size - Button size (large, middle, small)
 * @param {boolean} props.disabled - Disabled state
 * @param {boolean} props.loading - Loading state
 * @param {string} props.icon - Icon component
 * @param {function} props.onClick - Click handler
 * @param {ReactNode} props.children - Button content
 * @param {string} props.className - Additional CSS class
 * @param {Object} props.style - Inline styles
 * @returns {React.Element} Custom Button component
 */
const CustomButton = ({
  type = 'default',
  shape,
  size = 'middle',
  disabled = false,
  loading = false,
  icon,
  onClick,
  children,
  className = '',
  style = {},
  ...restProps
}) => {
  /**
   * Handle button click
   * @param {Event} e - Click event
   */
  const handleClick = (e) => {
    if (disabled || loading) return;
    onClick && onClick(e);
  };

  return (
    <Button
      type={type}
      shape={shape}
      size={size}
      disabled={disabled}
      loading={loading}
      icon={icon}
      onClick={handleClick}
      className={`custom-button ${className}`}
      style={style}
      {...restProps}
    >
      {children}
    </Button>
  );
};

CustomButton.propTypes = {
  type: PropTypes.oneOf(['primary', 'dashed', 'text', 'link', 'default']),
  shape: PropTypes.oneOf(['circle', 'round']),
  size: PropTypes.oneOf(['large', 'middle', 'small']),
  disabled: PropTypes.bool,
  loading: PropTypes.bool,
  icon: PropTypes.element,
  onClick: PropTypes.func,
  children: PropTypes.node,
  className: PropTypes.string,
  style: PropTypes.object,
};

export default CustomButton;
```
