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
import React, { useState, useEffect } from 'react';
import { Table, Pagination } from 'antd';

// Sample data for the table
const generateData = (total) => {
  return Array.from({ length: total }, (_, index) => ({
    key: index,
    name: `User ${index + 1}`,
    age: Math.floor(Math.random() * 50) + 20,
    address: `Address ${index + 1}`,
  }));
};

// Main component
const PaginatedTable = () => {
  const [data, setData] = useState([]);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  });

  // Fetch data on component mount
  useEffect(() => {
    const totalData = 100; // Assume we have 100 total records
    const newData = generateData(totalData);
    setData(newData);
    setPagination((prev) => ({ ...prev, total: totalData }));
  }, []);

  // Handle pagination change
  const handleTableChange = (pagination, filters, sorter) => {
    // Update pagination state based on user action
    setPagination({
      current: pagination.current,
      pageSize: pagination.pageSize,
      total: pagination.total,
    });
  };

  // Columns configuration for the Table component
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
    },
    {
      title: 'Age',
      dataIndex: 'age',
      sorter: (a, b) => a.age - b.age,
    },
    {
      title: 'Address',
      dataIndex: 'address',
    },
  ];

  // Calculate current data slice for pagination
  const currentData = data.slice(
    (pagination.current - 1) * pagination.pageSize,
    pagination.current * pagination.pageSize
  );

  return (
    <div>
      <Table
        columns={columns}
        dataSource={currentData}
        pagination={false} // Disable default pagination
        onChange={handleTableChange} // Handle sorting and filter changes
      />
      <Pagination
        current={pagination.current}
        pageSize={pagination.pageSize}
        total={pagination.total}
        onChange={(page, pageSize) => {
          setPagination({ ...pagination, current: page, pageSize });
        }}
      />
    </div>
  );
};

export default PaginatedTable;
```
