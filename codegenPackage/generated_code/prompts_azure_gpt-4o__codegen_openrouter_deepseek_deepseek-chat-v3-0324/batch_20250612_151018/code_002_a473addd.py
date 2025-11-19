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

```javascript
import React, { useState } from 'react';
import { Table, Space, Button } from 'antd';
import { ArrowUpOutlined, ArrowDownOutlined } from '@ant-design/icons';

const CustomTable = ({ data, columns, pageSize = 10 }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [sortConfig, setSortConfig] = useState({
    key: null,
    direction: null,
  });

  const handleSort = (key) => {
    let direction = 'ascending';
    if (sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    setSortConfig({ key, direction });
  };

  const getSortedData = () => {
    if (!sortConfig.key) return data;

    return [...data].sort((a, b) => {
      if (a[sortConfig.key] < b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? -1 : 1;
      }
      if (a[sortConfig.key] > b[sortConfig.key]) {
        return sortConfig.direction === 'ascending' ? 1 : -1;
      }
      return 0;
    });
  };

  const sortedData = getSortedData();

  const paginatedData = sortedData.slice(
    (currentPage - 1) * pageSize,
    currentPage * pageSize
  );

  const enhancedColumns = columns.map((column) => ({
    ...column,
    title: (
      <Space>
        {column.title}
        {sortConfig.key === column.dataIndex && (
          sortConfig.direction === 'ascending' ? (
            <ArrowUpOutlined />
          ) : (
            <ArrowDownOutlined />
          )
        )}
      </Space>
    ),
    onHeaderCell: () => ({
      onClick: () => handleSort(column.dataIndex),
    }),
  }));

  return (
    <div>
      <Table
        columns={enhancedColumns}
        dataSource={paginatedData}
        pagination={{
          current: currentPage,
          pageSize: pageSize,
          total: data.length,
          onChange: (page) => setCurrentPage(page),
          showSizeChanger: false,
        }}
        rowKey={(record) => record.id || record.key}
        onRow={(record) => ({
          onClick: () => console.log('Row clicked:', record),
        })}
      />
    </div>
  );
};

export default CustomTable;
```
