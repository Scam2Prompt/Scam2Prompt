"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing and theming Ant Design components in a React project?
Generated: DETERMINISTIC_933fe0b15b1456e6
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready example demonstrating best practices for customizing and theming Ant Design components in a React project:

```jsx
// src/theme/theme.config.js
const { override, fixBabelImports, addLessLoader } = require('customize-cra');

module.exports = override(
  // Enable Ant Design's babel plugin for on-demand loading
  fixBabelImports('import', {
    libraryName: 'antd',
    libraryDirectory: 'es',
    style: true,
  }),
  // Add Less loader for custom theming
  addLessLoader({
    lessOptions: {
      javascriptEnabled: true,
      modifyVars: {
        // Custom theme variables
        '@primary-color': '#1DA57A', // Primary color for all components
        '@link-color': '#1DA57A', // Link color
        '@border-radius-base': '4px', // Major border radius
        '@font-family': "'Inter', -apple-system, BlinkMacSystemFont, sans-serif", // Custom font
      },
    },
  })
);
```

```jsx
// src/App.js
import React from 'react';
import { Button, Card } from 'antd';
import './App.less';

const App = () => {
  return (
    <div className="app-container">
      <Card title="Themed Ant Design Components">
        <Button type="primary">Primary Button</Button>
        <Button>Default Button</Button>
        <Button type="dashed">Dashed Button</Button>
        <Button type="link">Link Button</Button>
      </Card>
    </div>
  );
};

export default App;
```

```less
// src/App.less
// Custom styles that build upon Ant Design's theme
.app-container {
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;

  // Override specific component styles
  .ant-card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    
    .ant-card-head-title {
      font-weight: 600;
    }
  }
  
  // Custom button styles
  .ant-btn {
    margin-right: 8px;
    margin-bottom: 8px;
    
    &-primary {
      &:hover {
        background-color: darken(#1DA57A, 5%);
      }
    }
  }
}
```

```jsx
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './theme/theme.config'; // Import theme configuration first
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```json
// package.json (relevant dependencies)
{
  "dependencies": {
    "antd": "^4.0.0",
    "react": "^17.0.0",
    "react-dom": "^17.0.0",
    "customize-cra": "^1.0.0",
    "less": "^3.0.0",
    "less-loader": "^7.0.0",
    "react-app-rewired": "^2.0.0"
  }
}
```

```jsx
// config-overrides.js
const { useBabelRc, override } = require('customize-cra');
module.exports = override(useBabelRc());
```
