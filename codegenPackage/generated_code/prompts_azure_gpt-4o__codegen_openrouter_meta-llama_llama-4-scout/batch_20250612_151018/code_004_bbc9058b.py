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

```jsx
// Import necessary components and libraries
import React from 'react';
import { Button } from 'antd';
import { 
  FacebookOutlined, 
  TwitterOutlined, 
  GoogleOutlined 
} from '@ant-design/icons';

// Define a custom button component
const CustomButton = ({ 
  type, 
  icon, 
  size, 
  onClick, 
  children, 
  ...rest 
}) => {
  // Map icon types to Ant Design icons
  const iconMap = {
    facebook: <FacebookOutlined />,
    twitter: <TwitterOutlined />,
    google: <GoogleOutlined />,
  };

  // Validate props
  if (!['primary', 'secondary', 'default'].includes(type)) {
    console.error('Invalid button type. Must be one of: primary, secondary, default');
    throw new Error('Invalid button type');
  }

  if (!['large', 'middle', 'small'].includes(size)) {
    console.error('Invalid button size. Must be one of: large, middle, small');
    throw new Error('Invalid button size');
  }

  // Render the custom button
  return (
    <Button 
      type={type} 
      size={size} 
      onClick={onClick} 
      {...rest}
      icon={icon && iconMap[icon]}
    >
      {children}
    </Button>
  );
};

// Example usage
const App = () => {
  const handleClick = () => {
    console.log('Button clicked!');
  };

  return (
    <div>
      <CustomButton 
        type="primary" 
        icon="facebook" 
        size="large" 
        onClick={handleClick}
      >
        Facebook Login
      </CustomButton>

      <CustomButton 
        type="secondary" 
        icon="twitter" 
        size="middle" 
        onClick={handleClick}
      >
        Twitter Share
      </CustomButton>

      <CustomButton 
        type="default" 
        icon="google" 
        size="small" 
        onClick={handleClick}
      >
        Google Signin
      </CustomButton>
    </div>
  );
};

export default App;
```
