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

```javascript
// Import necessary modules
import React, { useState } from 'react';
import { Table } from 'antd';

// Define the data for the table
const initialData = [
  {
    key: '1',
    name: 'John Doe',
    age: 32,
    address: '10 Downing Street, London',
  },
  {
    key: '2',
    name: 'Jane Smith',
    age: 28,
    address: '11 Downing Street, London',
  },
  {
    key: '3',
    name: 'William Brown',
    age: 45,
    address: '12 Downing Street, London',
  },
];

// Define the columns of the table
const columns = [
  {
    title: 'Name', // Displayed column header
    dataIndex: 'name', // Field in data to use for this column
    key: 'name', // Unique key identifier for the column
    sorter: (a, b) => a.name.localeCompare(b.name), // Sorting logic for the column
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
    sorter: (a, b) => a.age - b.age, // Sorting logic for numerical values
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
    sorter: (a, b) => a.address.localeCompare(b.address), // Sorting logic for string values
  },
];

// Main React component for rendering the table
const App = () => {
  // State to manage pagination
  const [pagination, setPagination] = useState({
    current: 1, // Current page number
    pageSize: 5, // Number of rows per page
    total: initialData.length, // Total number of rows
  });

  // State to manage sorted data
  const [sortedInfo, setSortedInfo] = useState({});

  // Handle table change events such as pagination or sorting
  const handleTableChange = (paginationConfig, filters, sorter) => {
    setPagination({
      ...paginationConfig, // Update pagination settings
    });
    setSortedInfo(sorter); // Update sorting info
  };

  return (
    <Table
      columns={columns} // Define table columns
      dataSource={initialData} // Pass the data to the table
      pagination={pagination} // Pass pagination settings
      onChange={handleTableChange} // Handle sorting and pagination changes
      rowKey="key" // Unique identifier for rows
    />
  );
};

export default App;
```
