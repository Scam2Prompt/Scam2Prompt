"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a table using Ant Design's Table component, including sorting and pagination functionality.
Generated: DETERMINISTIC_54ba9ce5f5f0823c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';
import { Table, Pagination } from 'antd';

/**
 * Sample data for the table
 */
const sampleData = [
  { key: '1', name: 'John Doe', age: 32, address: '10 Downing St' },
  { key: '2', name: 'Jane Smith', age: 28, address: '20 Oxford St' },
  { key: '3', name: 'Sam Green', age: 45, address: '30 Park Ave' },
  { key: '4', name: 'Alice Brown', age: 23, address: '40 Elm St' },
  { key: '5', name: 'Bob White', age: 36, address: '50 Maple St' },
  // More sample data...
];

const App = () => {
  // State to manage current page and page size
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize] = useState(2); // Fixed page size for pagination

  // Function to handle page change
  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  // Function to compute paginated data
  const getPaginatedData = () => {
    const start = (currentPage - 1) * pageSize;
    return sampleData.slice(start, start + pageSize);
  };

  // Columns configuration for the Ant Design Table
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name), // Sorting function
      // Render sorting indicator
      sortDirections: ['ascend', 'descend', 'ascend'],
    },
    {
      title: 'Age',
      dataIndex: 'age',
      sorter: (a, b) => a.age - b.age, // Sorting function
      sortDirections: ['ascend', 'descend', 'ascend'],
    },
    {
      title: 'Address',
      dataIndex: 'address',
    },
  ];

  return (
    <div>
      <h2>User Table</h2>
      <Table
        columns={columns}
        dataSource={getPaginatedData()}
        pagination={false} // Disable default pagination
        rowKey="key" // Define a unique key for each row
      />
      <Pagination
        current={currentPage}
        pageSize={pageSize}
        total={sampleData.length}
        onChange={handlePageChange}
        showSizeChanger={false} // Hide page size changer
      />
    </div>
  );
};

export default App;
```

Make sure to have the appropriate Ant Design library installed in your project. You can install it with:

```bash
npm install antd
```

Also, ensure to import the Ant Design styles in your main entry file (e.g., `index.js` or `App.js`):

```js
import 'antd/dist/antd.css';
```
