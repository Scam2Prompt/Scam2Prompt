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

```javascript
import React, { useState } from 'react';
import { Tree, message } from 'antd';

// Sample data for the hierarchical file structure
const treeData = [
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
        title: 'File 2-1',
        key: '0-1-0',
      },
      {
        title: 'Folder 2-2',
        key: '0-1-1',
        children: [
          {
            title: 'File 2-2-1',
            key: '0-1-1-0',
          },
        ],
      },
    ],
  },
];

const FileTree = () => {
  const [selectedKeys, setSelectedKeys] = useState([]);

  // Function to handle tree node selection
  const onSelect = (selectedKeysValue) => {
    setSelectedKeys(selectedKeysValue);
    if (selectedKeysValue.length > 0) {
      const selectedNode = selectedKeysValue[0];
      message.info(`Selected: ${selectedNode}`);
    }
  };

  return (
    <Tree
      treeData={treeData}
      onSelect={onSelect}
      selectedKeys={selectedKeys}
      defaultExpandAll
    />
  );
};

export default FileTree;
```
