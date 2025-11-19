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

```jsx
// Import necessary components and libraries
import React, { useState, useEffect } from 'react';
import { Table, Pagination } from 'antd';

// Define the column structure for the table
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

// Define the data source for the table
const initialData = [
  { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
  { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
  { key: '3', name: 'Joe Black', age: 28, address: 'Sydney No. 1 Lake Park' },
  { key: '4', name: 'Jill White', age: 35, address: 'Melbourne No. 1 Lake Park' },
  { key: '5', name: 'John Smith', age: 40, address: 'Paris No. 1 Lake Park' },
];

// Table component with sorting and pagination functionality
const MyTable = () => {
  const [data, setData] = useState(initialData);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 5,
    total: initialData.length,
  });
  const [sorter, setSorter] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Simulate API call to fetch data
        const response = initialData;
        setData(response);
        setPagination((prevPagination) => ({
          ...prevPagination,
          total: response.length,
        }));
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, []);

  const handleTableChange = (pagination, filters, sorter) => {
    setPagination(pagination);
    setSorter(sorter);

    const sortedData = initialData.sort((a, b) => {
      if (sorter.columnKey === 'name') {
        return sorter.order === 'ascend'
          ? a.name.localeCompare(b.name)
          : b.name.localeCompare(a.name);
      } else if (sorter.columnKey === 'age') {
        return sorter.order === 'ascend' ? a.age - b.age : b.age - a.age;
      }
      return 0;
    });

    const paginatedData = sortedData.slice(
      (pagination.current - 1) * pagination.pageSize,
      pagination.current * pagination.pageSize
    );

    setData(paginatedData);
  };

  return (
    <div>
      <Table
        columns={columns}
        dataSource={data}
        pagination={pagination}
        onChange={handleTableChange}
        rowKey={(record) => record.key}
      />
      <Pagination
        {...pagination}
        onChange={(current) =>
          setPagination((prevPagination) => ({ ...prevPagination, current }))
        }
        onShowSizeChange={(current, pageSize) =>
          setPagination((prevPagination) => ({
            ...prevPagination,
            current,
            pageSize,
          }))
        }
      />
    </div>
  );
};

export default MyTable;
```
