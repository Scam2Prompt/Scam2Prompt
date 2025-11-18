"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to customize the Ant Design Table component with pagination and sorting functionality.
Generated: DETERMINISTIC_a473addd4aea67e8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and components from React and Ant Design
import React, { useState } from 'react';
import { Table } from 'antd';

// Sample data for the table
const dataSource = [
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
    name: 'Michael Brown',
    age: 45,
    address: '12 Downing Street, London',
  },
];

// Define columns with sorting functionality
const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
    sorter: (a, b) => a.name.localeCompare(b.name), // Sorting by name (alphabetically)
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
    sorter: (a, b) => a.age - b.age, // Sorting by age (numerically)
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
    sorter: (a, b) => a.address.localeCompare(b.address), // Sorting by address (alphabetically)
  },
];

const CustomTable = () => {
  // State for handling pagination
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 5, // Number of rows per page
  });

  // Function to handle table changes (pagination, sorting, filtering)
  const handleTableChange = (newPagination, filters, sorter) => {
    setPagination(newPagination); // Update pagination state
    // Additional processing can be added here for filters/sorter if needed
  };

  return (
    <Table
      dataSource={dataSource} // Set data for the table
      columns={columns} // Provide column definitions
      pagination={pagination} // Enable pagination with current state
      onChange={handleTableChange} // Handle changes (pagination/sorting/filtering)
      rowKey="key" // Set unique key for each row (important for performance)
    />
  );
};

export default CustomTable;
```
