"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for theming in Ant Design when building a React application?
Generated: DETERMINISTIC_cf837e7469f0cf01
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for theming in Ant Design with React, following best practices:

```jsx
// theme/theme.config.js
const { theme } = require('antd');

/**
 * Custom theme configuration for Ant Design
 * @type {import('antd').ThemeConfig}
 */
const customTheme = {
  token: {
    colorPrimary: '#1890ff',
    colorInfo: '#1890ff',
    borderRadius: 6,
    colorBgContainer: '#ffffff',
    colorLink: '#1890ff',
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
  },
  components: {
    Button: {
      colorPrimary: '#1890ff',
      algorithm: true,
    },
    Input: {
      colorBorder: '#d9d9d9',
      hoverBorderColor: '#1890ff',
      activeBorderColor: '#1890ff',
    },
    Card: {
      borderRadius: 12,
      boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.03)',
    },
  },
};

// Generate a map of CSS variables from theme tokens
const generateCssVariables = (themeConfig) => {
  const cssVariables = {};
  Object.entries(themeConfig.token).forEach(([key, value]) => {
    if (value) {
      cssVariables[`--ant-${key}`] = value;
    }
  });
  return cssVariables;
};

module.exports = {
  customTheme,
  generateCssVariables,
};
```

```jsx
// theme/ThemeProvider.jsx
import React from 'react';
import { ConfigProvider } from 'antd';
import { customTheme } from './theme.config';

/**
 * ThemeProvider component to wrap the application with Ant Design theme
 * @param {React.PropsWithChildren} props
 * @returns {React.ReactElement}
 */
const ThemeProvider = ({ children }) => {
  return (
    <ConfigProvider
      theme={customTheme}
      // Additional Ant Design configurations can go here
      componentSize="middle"
      getPopupContainer={(trigger) => trigger?.parentNode ?? document.body}
    >
      {children}
    </ConfigProvider>
  );
};

export default ThemeProvider;
```

```jsx
// theme/GlobalStyles.jsx
import { createGlobalStyle } from 'styled-components';
import { customTheme } from './theme.config';

/**
 * Global styles component that includes Ant Design theme variables
 */
const GlobalStyles = createGlobalStyle`
  :root {
    ${Object.entries(customTheme.token)
      .map(([key, value]) => `--ant-${key}: ${value};`)
      .join('\n')}
  }

  body {
    font-family: ${customTheme.token.fontFamily};
    background-color: ${customTheme.token.colorBgContainer};
    color: ${customTheme.token.colorText};
    margin: 0;
    padding: 0;
    min-height: 100vh;
  }
`;

export default GlobalStyles;
```

```jsx
// App.jsx
import React from 'react';
import { Button, Card, Space } from 'antd';
import ThemeProvider from './theme/ThemeProvider';
import GlobalStyles from './theme/GlobalStyles';

/**
 * Main application component wrapped with theme providers
 */
const App = () => {
  return (
    <ThemeProvider>
      <GlobalStyles />
      <div style={{ padding: 24 }}>
        <Card title="Themed Components">
          <Space>
            <Button type="primary">Primary Button</Button>
            <Button type="default">Default Button</Button>
            <Button type="dashed">Dashed Button</Button>
            <Button type="text">Text Button</Button>
            <Button type="link">Link Button</Button>
          </Space>
        </Card>
      </div>
    </ThemeProvider>
  );
};

export default App;
```

```jsx
// main.jsx (or index.jsx)
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Import the fonts you're using in your theme
import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/inter/600.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```json
// package.json (relevant dependencies)
{
  "dependencies": {
    "antd": "^5.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@ant-design/cssinjs": "^1.0.0",
    "@fontsource/inter": "^5.0.0",
    "styled-components": "^6.0.0"
  }
}
```
