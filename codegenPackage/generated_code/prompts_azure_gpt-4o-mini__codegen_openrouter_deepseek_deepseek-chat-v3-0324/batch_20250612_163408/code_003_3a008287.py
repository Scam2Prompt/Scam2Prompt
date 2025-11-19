"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the best practices for customizing themes in Ant Design for a React project?
Generated: DETERMINISTIC_3a0082871777cddb
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for customizing Ant Design themes in a React project using `less` variables and `craco`:

```jsx
// craco.config.js
const CracoLessPlugin = require('craco-less');

module.exports = {
    plugins: [
        {
            plugin: CracoLessPlugin,
            options: {
                lessLoaderOptions: {
                    lessOptions: {
                        modifyVars: {
                            // Primary color customization
                            '@primary-color': '#1890ff',
                            
                            // Typography
                            '@font-family': "'Inter', sans-serif",
                            '@font-size-base': '16px',
                            
                            // Layout
                            '@layout-header-background': '@primary-color',
                            '@layout-body-background': '#f0f2f5',
                            
                            // Button
                            '@btn-border-radius-base': '4px',
                            '@btn-primary-bg': '@primary-color',
                            
                            // Input
                            '@input-border-color': '#d9d9d9',
                            '@input-hover-border-color': '@primary-color',
                            
                            // Other variables as needed
                            '@border-radius-base': '4px',
                        },
                        javascriptEnabled: true,
                    },
                },
            },
        },
    ],
};
```

```jsx
// src/App.js
import React from 'react';
import { Button } from 'antd';
import './App.less';

function App() {
    return (
        <div className="App">
            <Button type="primary">Customized Button</Button>
        </div>
    );
}

export default App;
```

```less
// src/App.less
// Import Ant Design styles
@import '~antd/dist/antd.less';

// Custom styles that will override Ant Design
.App {
    padding:龙须酥真是20px;
    max-width: 1200px;
    margin: 0 auto;
}
```

```json
// package.json
{
    "name": "my-antd-app",
    "version": "0.1.0",
    "private": true,
    "dependencies": {
        "antd": "^4.0.0",
        "craco-less": "^2.0.0",
        "react": "^17.0.0",
        "react-dom": "^17.0.0",
        "react-scripts": "4.0.0"
    },
    "scripts": {
        "start": "craco start",
        "build": "craco build",
        "test": "craco test",
        "eject": "react-scripts eject"
    }
}
```
