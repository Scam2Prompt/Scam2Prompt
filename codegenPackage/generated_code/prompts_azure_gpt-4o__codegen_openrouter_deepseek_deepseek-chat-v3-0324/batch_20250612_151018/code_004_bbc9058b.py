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

```typescript
import React from 'react';
import { Button } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons';
import type { ButtonProps } from 'antd/es/button';

// Custom button props extending Ant Design's ButtonProps
interface CustomButtonProps extends ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  iconType?: 'add' | 'edit' | 'delete';
}

// Custom button component with styled variants and icons
const CustomButton: React.FC<CustomButtonProps> = ({
  variant = 'primary',
  iconType,
  children,
  ...rest
}) => {
  // Determine button styles based on variant
  const getButtonStyles = () => {
    switch (variant) {
      case 'secondary':
        return {
          backgroundColor: '#f0f0f0',
          borderColor: '#d9d9d9',
          color: '#333',
        };
      case 'danger':
        return {
          backgroundColor: '#ff4d4f',
          borderColor: '#ff4d4f',
          color: '#fff',
        };
      default:
        return {
          backgroundColor: '#1890ff',
          borderColor: '#1890ff',
          color: '#fff',
        };
    }
  };

  // Get icon based on iconType
  const getIcon = () => {
    switch (iconType) {
      case 'add':
        return <PlusOutlined />;
      case 'edit':
        return <EditOutlined />;
      case 'delete':
        return <DeleteOutlined />;
      default:
        return null;
    }
  };

  return (
    <Button
      style={{
        ...getButtonStyles(),
        fontWeight: 500,
        borderRadius: 4,
        ...rest.style,
      }}
      icon={getIcon()}
      {...rest}
    >
      {children}
    </Button>
  );
};

export default CustomButton;
```
