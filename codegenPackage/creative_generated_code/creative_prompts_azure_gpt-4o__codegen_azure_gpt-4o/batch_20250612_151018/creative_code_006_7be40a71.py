"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a React component that uses Ant Design's Tree component to display a hierarchical file structure with selectable nodes.
Generated: DETERMINISTIC_7be40a71558eda48
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components
import React, { useState } from 'react';
import { Tree, message } from 'antd';

// Ant Design Tree component expects data in a specific format
const initialTreeData = [
  {
    title: 'Folder 1',
    key: '0-0',
    children: [
      {
        title: 'File 1-1',
        key: '0-0-0',
      },
      {
        title: 'File 1-2',
        key: '0-0-1',
      },
    ],
  },
  {
    title: 'Folder 2',
    key: '0-1',
    children: [
      {
        title: 'Folder 2-1',
        key: '0-1-0',
        children: [
          {
            title: 'File 2-1-1',
            key: '0-1-0-0',
          },
        ],
      },
    ],
  },
];

const FileTree = () => {
  // State for selected keys
  const [selectedKeys, setSelectedKeys] = useState([]);

  /**
   * Event handler when tree nodes are selected
   * @param {array} keys - Array of selected node keys
   */
  const onSelect = (keys) => {
    setSelectedKeys(keys);

    // Display a message with the selected nodes
    if (keys.length > 0) {
      message.info(`Selected: ${keys.join(', ')}`);
    }
  };

  return (
    <div>
      <h3>File Tree</h3>
      <Tree
        showLine // Display lines to indicate hierarchy
        defaultExpandAll // Expand all nodes initially
        treeData={initialTreeData} // Hierarchical data for the tree
        selectedKeys={selectedKeys} // Controlled selected keys
        onSelect={onSelect} // Event handler for selection
      />
    </div>
  );
};

export default FileTree;
```
