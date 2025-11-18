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
// Import necessary modules and components
import React from 'react';
import { Tree } from 'antd';

// Sample hierarchical data for the Tree component
const treeData = [
  {
    title: 'Parent Node 1',
    key: '0-0',
    children: [
      {
        title: 'Child Node 1-1',
        key: '0-0-0',
      },
      {
        title: 'Child Node 1-2',
        key: '0-0-1',
        children: [
          {
            title: 'Leaf Node 1-2-1',
            key: '0-0-1-0',
          },
          {
            title: 'Leaf Node 1-2-2',
            key: '0-0-1-1',
          },
        ],
      },
    ],
  },
  {
    title: 'Parent Node 2',
    key: '0-1',
    children: [
      {
        title: 'Child Node 2-1',
        key: '0-1-0',
      },
      {
        title: 'Child Node 2-2',
        key: '0-1-1',
      },
    ],
  },
];

// Functional component rendering the Ant Design Tree
const TreeExample = () => {
  // Callback for handling node selection
  const onSelect = (selectedKeys, info) => {
    console.log('Selected keys:', selectedKeys);
    console.log('Node info:', info);
  };

  // Callback for handling node expansion
  const onExpand = (expandedKeys) => {
    console.log('Expanded keys:', expandedKeys);
  };

  return (
    <div style={{ margin: '20px' }}>
      {/* Ant Design Tree component */}
      <Tree
        showLine={true} // Enables visual connection lines between nodes
        showIcon={true} // Shows icons next to nodes
        defaultExpandAll={true} // Expands all nodes by default
        treeData={treeData} // Pass hierarchical data
        onSelect={onSelect} // Selection callback
        onExpand={onExpand} // Expansion callback
      />
    </div>
  );
};

export default TreeExample;
```
