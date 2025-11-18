"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of how to use Ant Design's Table component to display paginated data with sorting functionality.
Generated: DETERMINISTIC_7dd05057acc7f63e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary components and modules from React and Ant Design
import React, { useState } from 'react';
import { Table, message } from 'antd';

// Sample data for the table
const sampleData = [
  { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
  { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
  { key: '3', name: 'Joe Black', age: 32, address: 'Sidney No. 1 Lake Park' },
  { key: '4', name: 'Jane White', age: 28, address: 'Boston No. 1 Lake Park' },
];

// Ant Design Table Component with pagination and sorting
const PaginatedSortableTable = () => {
  // State to manage pagination and sorting
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 2,
  });
  const [sorter, setSorter] = useState({});

  // Columns configuration with sorting enabled
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
      sortOrder: sorter.columnKey === 'name' && sorter.order,
    },
    {
      title: 'Age',
      dataIndex: 'age',
      sorter: (a, b) => a.age - b.age,
      sortOrder: sorter.columnKey === 'age' && sorter.order,
    },
    {
      title: 'Address',
      dataIndex: 'address',
    },
  ];

  // Handle table changes (pagination, sorter, etc.)
  const handleTableChange = (newPagination, filters, newSorter) => {
    try {
      // Update pagination state
      setPagination(newPagination);

      // Update sorter state
      setSorter(newSorter);

    } catch (error) {
      // Display an error message if something goes wrong
      message.error('An error occurred while updating the table settings.');
      console.error(error);
    }
  };

  return (
    <Table
      columns={columns} // Set table columns
      dataSource={sampleData} // Provide the data for the table
      pagination={pagination} // Set pagination state
      onChange={handleTableChange} // Handle table changes (pagination/sorting)
    />
  );
};

export default PaginatedSortableTable;
```
