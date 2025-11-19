"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Table component to display a list of users with sorting and filtering features.
Generated: DETERMINISTIC_946a6657c85ab55d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { Table, Input, Button } from 'antd';

// Sample user data
const initialUsers = [
  { key: '1', name: 'John Doe', age: 32, email: 'john@example.com' },
  { key: '2', name: 'Jane Smith', age: 28, email: 'jane@example.com' },
  { key: '3', name: 'Mike Johnson', age: 45, email: 'mike@example.com' },
  { key: '4', name: 'Sarah Brown', age: 36, email: 'sarah@example.com' },
];

// Main component to display the user table
const UserTable = () => {
  const [searchText, setSearchText] = useState('');
  const [filteredData, setFilteredData] = useState(initialUsers);

  // Handle the search input change
  const handleSearch = (value) => {
    setSearchText(value);
    const filtered = initialUsers.filter(user =>
      user.name.toLowerCase().includes(value.toLowerCase())
    );
    setFilteredData(filtered);
  };

  // Define the columns for the Ant Design Table
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
      title: 'Email',
      dataIndex: 'email',
      sorter: (a, b) => a.email.localeCompare(b.email),
    },
  ];

  return (
    <div>
      <Input.Search
        placeholder="Search by name"
        onSearch={handleSearch}
        style={{ marginBottom: 16 }}
        allowClear
      />
      <Table
        columns={columns}
        dataSource={filteredData}
        pagination={{ pageSize: 5 }}
        rowKey="key"
      />
    </div>
  );
};

export default UserTable;
```
