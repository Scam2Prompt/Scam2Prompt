"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to customize the Ant Design Table component with pagination and sorting functionality.
Generated: DETERMINISTIC_a473addd4aea67e8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary components and libraries
import React, { useState, useEffect } from 'react';
import { Table, Pagination } from 'antd';

/**
 * Customize Ant Design Table component with pagination and sorting functionality.
 */
const CustomTable = () => {
  // Define table columns
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
      sorter: (a, b) => a.age - b.age,
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
  ];

  // Define initial data and pagination
  const [data, setData] = useState([]);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  });

  // Fetch data from API or database
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Replace with actual API or database call
        const response = await new Promise((resolve) => {
          setTimeout(() => {
            resolve({
              data: [
                { name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
                { name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
                { name: 'Joe Black', age: 28, address: 'Sydney No. 1 Lake Park' },
                // Add more data here...
              ],
              total: 100,
            });
          }, 1000);
        });

        setData(response.data);
        setPagination((prevPagination) => ({
          ...prevPagination,
          total: response.total,
        }));
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  // Handle pagination changes
  const handlePaginationChange = (current, pageSize) => {
    setPagination((prevPagination) => ({
      ...prevPagination,
      current,
      pageSize,
    }));
  };

  // Handle sorting changes
  const handleTableChange = (pagination, filters, sorter) => {
    if (sorter) {
      // Update data based on sorting
      const sortedData = data.sort((a, b) => {
        if (sorter.order === 'ascend') {
          return a[sorter.field] - b[sorter.field];
        }
        return b[sorter.field] - a[sorter.field];
      });

      setData(sortedData);
    }
  };

  return (
    <div>
      <Table
        columns={columns}
        dataSource={data}
        pagination={pagination}
        onChange={handleTableChange}
        rowKey="key"
      />
      <Pagination
        {...pagination}
        onChange={handlePaginationChange}
        position={['bottomRight']}
      />
    </div>
  );
};

export default CustomTable;
```
