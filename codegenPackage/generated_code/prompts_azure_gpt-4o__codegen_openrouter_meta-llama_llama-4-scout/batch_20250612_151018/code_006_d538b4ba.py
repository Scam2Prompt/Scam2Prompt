"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Tree component to display hierarchical data with expandable nodes.
Generated: DETERMINISTIC_d538b4ba9c956841
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { Tree } from 'antd';

/**
 * Hierarchical data for the Tree component.
 * Each node has a unique key, title, and optional children.
 */
const treeData = [
  {
    key: '1',
    title: 'Parent 1',
    children: [
      {
        key: '1-1',
        title: 'Child 1-1',
      },
      {
        key: '1-2',
        title: 'Child 1-2',
        children: [
          {
            key: '1-2-1',
            title: 'Grandchild 1-2-1',
          },
        ],
      },
    ],
  },
  {
    key: '2',
    title: 'Parent 2',
  },
];

const App = () => {
  const [expandedKeys, setExpandedKeys] = useState([]);
  const [selectedKeys, setSelectedKeys] = useState([]);
  const [autoExpandParent, setAutoExpandParent] = useState(true);

  /**
   * Handle node expansion.
   * @param {string[]} expandedKeys - Currently expanded keys.
   */
  const onExpand = (expandedKeys) => {
    setExpandedKeys(expandedKeys);
    setAutoExpandParent(false);
  };

  /**
   * Handle node selection.
   * @param {string[]} selectedKeys - Currently selected keys.
   */
  const onSelect = (selectedKeys) => {
    setSelectedKeys(selectedKeys);
  };

  return (
    <Tree
      treeData={treeData}
      expandedKeys={expandedKeys}
      onExpand={onExpand}
      selectedKeys={selectedKeys}
      onSelect={onSelect}
      autoExpandParent={autoExpandParent}
    />
  );
};

export default App;
```
