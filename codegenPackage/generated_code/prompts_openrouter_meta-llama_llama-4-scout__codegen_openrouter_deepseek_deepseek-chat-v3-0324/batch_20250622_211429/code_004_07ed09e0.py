"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing Ant Design's theme and styles in a React project?
Generated: DETERMINISTIC_07ed09e0e164b757
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// 1. Customizing Ant Design Theme using modifyVars in craco.config.js
const CracoLessPlugin = require('craco-less');

module.exports = {
  plugins: [
    {
      plugin: CracoLessPlugin,
      options: {
        lessLoaderOptions: {
          lessOptions: {
            modifyVars: {
              // Customize theme variables
              '@primary-color': '#1DA57A', // Primary color for all components
              '@link-color': '#1DA57A', // Link color
              '@border-radius-base': '4px', // Major border radius
              '@font-family': "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
              '@text-color': '#333', // Major text color
            },
            javascriptEnabled: true,
          },
        },
      },
    },
  ],
};

// 2. Customizing styles with CSS-in-JS (using styled-components)
import styled from 'styled-components';
import { Button } from 'antd';

export const CustomButton = styled(Button)`
  background-color: ${props => props.type === 'primary' ? '#1DA57A' : '#fff'};
  border-color: #1DA57A;
  color: ${props => props.type === 'primary' ? '#fff' : '#1DA57A'};
  
  &:hover {
    background-color: ${props => props.type === 'primary' ? '#0d8d6a' : '#f5f5f5'};
    border-color: #0d8d6a;
    color: ${props => props.type === 'primary' ? '#fff' : '#0d8d6a'};
  }
`;

// 3. Overriding component styles with less file
// Create a file: src/styles/antd-overrides.less
/*
@import '~antd/dist/antd.less';

// Override styles
.ant-btn {
  font-weight: 500;
}

.ant-layout-header {
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.ant-menu {
  border-bottom: none;
}
*/

// 4. Using ConfigProvider for component-level theming
import { ConfigProvider } from 'antd';

function App() {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#1DA57A',
          borderRadius: 4,
          colorBgContainer: '#ffffff',
        },
        components: {
          Button: {
            colorPrimary: '#1DA57A',
            algorithm: true, // Enable algorithm
          },
          Table: {
            headerBg: '#fafafa',
            headerColor: '#333',
          },
        },
      }}
    >
      {/* Your app components */}
    </ConfigProvider>
  );
}

// 5. Dynamic theme switching
import { useState } from 'react';
import { ConfigProvider, Button, Switch } from 'antd';

function ThemeSwitcher() {
  const [isDark, setIsDark] = useState(false);

  const theme = {
    token: {
      colorPrimary: isDark ? '#1890ff' : '#1DA57A',
      colorBgBase: isDark ? '#1f1f1f' : '#ffffff',
      colorTextBase: isDark ? '#ffffff' : '#333333',
    },
  };

  return (
    <ConfigProvider theme={theme}>
      <Switch
        checked={isDark}
        onChange={setIsDark}
        checkedChildren="Dark"
        unCheckedChildren="Light"
      />
      <Button type="primary">Primary Button</Button>
    </ConfigProvider>
  );
}
```
