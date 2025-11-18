"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Generate code that uses Ant Design's Table component to display a paginated and sortable list of user data.
Generated: DETERMINISTIC_562006ec8921ac5a
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
import 'antd/dist/antd.css';

// Sample user data fetching function (this would typically be an API call)
const fetchUserData = async () => {
  // Simulate an API call with sample data
  return new Promise((resolve) => {
    setTimeout(() => {
      const data = Array.from({ length: 100 }, (_, index) => ({
        key: index,
        name: `User ${index + 1}`,
        email: `user${index + 1}@example.com`,
        age: Math.floor(Math.random() * 50) + 20,
      }));
      resolve(data);
    }, 1000);
  });
};

const UserTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [total, setTotal] = useState(0);

  // Fetch user data and update state
  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const result = await fetchUserData();
        setData(result);
        setTotal(result.length);
      } catch (error) {
        console.error('Failed to fetch user data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  // Handle pagination change
  const handlePageChange = (page, pageSize) => {
    setCurrentPage(page);
    setPageSize(pageSize);
  };

  // Define columns for the Ant Design Table
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
    },
    {
      title: 'Email',
      dataIndex: 'email',
      sorter: (a, b) => a.email.localeCompare(b.email),
    },
    {
      title: 'Age',
      dataIndex: 'age',
      sorter: (a, b) => a.age - b.age,
    },
  ];

  // Calculate paginated data
  const paginatedData = data.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  return (
    <div>
      <Table
        columns={columns}
        dataSource={paginatedData}
        loading={loading}
        pagination={false}
      />
      <Pagination
        current={currentPage}
        pageSize={pageSize}
        total={total}
        onChange={handlePageChange}
        showSizeChanger
        pageSizeOptions={[10, 20, 50]}
      />
    </div>
  );
};

export default UserTable;
```

Make sure to install Ant Design using `npm install antd` before running this code. Also, remember to include the necessary CSS imports for styling.
