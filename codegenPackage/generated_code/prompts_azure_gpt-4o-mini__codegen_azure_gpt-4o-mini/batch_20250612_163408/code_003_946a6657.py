"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Table component to display a list of users with sorting and filtering features.
Generated: DETERMINISTIC_946a6657c85ab55d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Table, Input, Button } from 'antd';

// Sample data for users
const initialData = [
  { key: '1', name: 'John Doe', age: 32, address: '10 Downing St' },
  { key: '2', name: 'Jane Smith', age: 28, address: '20 Main St' },
  { key: '3', name: 'Alice Johnson', age: 45, address: '30 Elm St' },
  { key: '4', name: 'Bob Brown', age: 36, address: '40 Oak St' },
];

// Main component to display the user table
const UserTable = () => {
  const [data, setData] = useState(initialData);
  const [searchText, setSearchText] = useState('');

  // Function to handle search input change
  const handleSearch = (e) => {
    setSearchText(e.target.value);
  };

  // Function to filter data based on search text
  const filteredData = data.filter((user) =>
    user.name.toLowerCase().includes(searchText.toLowerCase())
  );

  // Columns configuration for the Ant Design Table
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
      filters: [
        { text: '10 Downing St', value: '10 Downing St' },
        { text: '20 Main St', value: '20 Main St' },
        { text: '30 Elm St', value: '30 Elm St' },
        { text: '40 Oak St', value: '40 Oak St' },
      ],
      onFilter: (value, record) => record.address.includes(value),
    },
  ];

  return (
    <div>
      <Input
        placeholder="Search by name"
        value={searchText}
        onChange={handleSearch}
        style={{ marginBottom: 16 }}
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
