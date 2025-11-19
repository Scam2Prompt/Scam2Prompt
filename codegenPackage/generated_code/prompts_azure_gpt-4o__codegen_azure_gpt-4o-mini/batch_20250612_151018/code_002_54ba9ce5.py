"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a table using Ant Design's Table component, including sorting and pagination functionality.
Generated: DETERMINISTIC_54ba9ce5f5f0823c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Table, Pagination } from 'antd';

// Sample data for the table
const dataSource = [
  { key: '1', name: 'John Doe', age: 32, address: '10 Downing St' },
  { key: '2', name: 'Jane Smith', age: 28, address: '20 Main St' },
  { key: '3', name: 'Sam Green', age: 45, address: '30 Elm St' },
  // Add more data as needed
];

// Columns configuration for the Ant Design Table
const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    sorter: (a, b) => a.name.localeCompare(b.name), // Sorting by name
  },
  {
    title: 'Age',
    dataIndex: 'age',
    sorter: (a, b) => a.age - b.age, // Sorting by age
  },
  {
    title: 'Address',
    dataIndex: 'address',
  },
];

const App = () => {
  // State for pagination
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 5; // Number of items per page

  // Function to handle page change
  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  // Calculate the data to be displayed on the current page
  const paginatedData = dataSource.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  return (
    <div>
      <Table
        dataSource={paginatedData}
        columns={columns}
        pagination={false} // Disable default pagination
        rowKey="key" // Unique key for each row
      />
      <Pagination
        current={currentPage}
        pageSize={pageSize}
        total={dataSource.length}
        onChange={handlePageChange} // Handle page change
        showSizeChanger={false} // Disable page size changer
      />
    </div>
  );
};

export default App;
```
