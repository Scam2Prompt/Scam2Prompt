"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Tree component to display hierarchical data with expandable nodes.
Generated: DETERMINISTIC_d538b4ba9c956841
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
import { Tree } from 'antd';

// Sample hierarchical data
const treeData = [
  {
    title: 'Root 1',
    key: '0-0',
    children: [
      {
        title: 'Child 1-1',
        key: '0-0-0',
        children: [
          {
            title: 'Leaf 1-1-1',
            key: '0-0-0-0',
          },
          {
            title: 'Leaf 1-1-2',
            key: '0-0-0-1',
          },
        ],
      },
      {
        title: 'Child 1-2',
        key: '0-0-1',
      },
    ],
  },
  {
    title: 'Root 2',
    key: '0-1',
    children: [
      {
        title: 'Child 2-1',
        key: '0-1-0',
      },
    ],
  },
];

// TreeComponent to display the hierarchical data
const TreeComponent = () => {
  // Handle tree node selection
  const onSelect = (selectedKeys, info) => {
    console.log('Selected:', selectedKeys, info);
  };

  // Handle tree node expansion
  const onExpand = (expandedKeys) => {
    console.log('Expanded:', expandedKeys);
  };

  return (
    <Tree
      showLine // Display lines connecting nodes
      treeData={treeData} // Set the data for the tree
      onSelect={onSelect} // Event handler for node selection
      onExpand={onExpand} // Event handler for node expansion
    />
  );
};

// Main application component
const App = () => {
  return (
    <div style={{ padding: '20px' }}>
      <h2>Ant Design Tree Example</h2>
      <TreeComponent />
    </div>
  );
};

// Export the main application component
export default App;
```

Make sure to install `antd` in your project by running:
```bash
npm install antd
```

Also, don't forget to import the Ant Design styles in your main entry file (e.g., `index.js` or `App.js`):
```javascript
import 'antd/dist/antd.css';
```
