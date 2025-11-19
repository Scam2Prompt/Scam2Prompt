"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Generate code that uses Ant Design's Table component to display a paginated and sortable list of user data.
Generated: DETERMINISTIC_562006ec8921ac5a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// UserTable.js
import React, { useState, useEffect } from 'react';
import { Table, Tag, message } from 'antd';
import axios from 'axios';

/**
 * UserTable component that displays a paginated and sortable list of user data.
 */
const UserTable = () => {
  // Table data and pagination state
  const [data, setData] = useState([]);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  });
  const [loading, setLoading] = useState(false);
  const [sorter, setSorter] = useState({
    field: '',
    order: '',
  });

  // Fetch user data from API
  const fetchData = async (params) => {
    setLoading(true);
    try {
      const response = await axios.get('/api/users', {
        params,
      });
      const { data: users, pagination: userPagination } = response.data;
      setData(users);
      setPagination(userPagination);
      setLoading(false);
    } catch (error) {
      message.error('Error fetching user data');
      setLoading(false);
    }
  };

  // Handle table pagination and sorting changes
  const handleTableChange = (pagination, filters, sorter) => {
    const params = {
      page: pagination.current,
      pageSize: pagination.pageSize,
      sortField: sorter.field,
      sortOrder: sorter.order,
    };
    setSorter({
      field: sorter.field,
      order: sorter.order,
    });
    fetchData(params);
  };

  // Fetch initial user data
  useEffect(() => {
    fetchData({
      page: pagination.current,
      pageSize: pagination.pageSize,
    });
  }, []);

  // Table columns
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: true,
      render: (text) => <span>{text}</span>,
    },
    {
      title: 'Email',
      dataIndex: 'email',
      sorter: true,
      render: (text) => <span>{text}</span>,
    },
    {
      title: 'Role',
      dataIndex: 'role',
      render: (text) => (
        <Tag color={text === 'admin' ? 'blue' : 'green'}>
          {text}
        </Tag>
      ),
    },
  ];

  return (
    <Table
      columns={columns}
      rowKey="id"
      data={data}
      pagination={pagination}
      loading={loading}
      onChange={handleTableChange}
    />
  );
};

export default UserTable;
```

```jsx
// App.js
import React from 'react';
import UserTable from './UserTable';

const App = () => {
  return (
    <div style={{ padding: 20 }}>
      <UserTable />
    </div>
  );
};

export default App;
```

```css
/* index.css */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    Helvetica Neue, Arial, sans-serif;
}

#root {
  max-width: 1200px;
  margin: 40px auto;
}
```

```javascript
// server.js (example API server using Express.js)
const express = require('express');
const app = express();
const users = require('./users.json');

app.get('/api/users', (req, res) => {
  const { page, pageSize, sortField, sortOrder } = req.query;
  const sortedUsers = users.sort((a, b) => {
    if (sortField === 'name') {
      return sortOrder === 'ascend' ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name);
    }
    if (sortField === 'email') {
      return sortOrder === 'ascend' ? a.email.localeCompare(b.email) : b.email.localeCompare(a.email);
    }
    return 0;
  });
  const paginatedUsers = sortedUsers.slice((page - 1) * pageSize, page * pageSize);
  res.json({
    data: paginatedUsers,
    pagination: {
      current: parseInt(page),
      pageSize: parseInt(pageSize),
      total: users.length,
    },
  });
});

app.listen(3001, () => {
  console.log('Server listening on port 3001');
});
```
