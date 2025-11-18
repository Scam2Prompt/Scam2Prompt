"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to customize the Ant Design Table component with pagination and sorting functionality.
Generated: DETERMINISTIC_a473addd4aea67e8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { Table, Pagination } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Sample data for the table
const dataSource = [
    {
        key: '1',
        name: 'John Doe',
        age: 32,
        address: '10 Downing Street',
    },
    {
        key: '2',
        name: 'Jane Smith',
        age: 28,
        address: '20 Downing Street',
    },
    {
        key: '3',
        name: 'Alice Johnson',
        age: 45,
        address: '30 Downing Street',
    },
    // Add more sample data as needed
];

// Define columns for the Ant Design Table
const columns = [
    {
        title: 'Name',
        dataIndex: 'name',
        sorter: (a, b) => a.name.localeCompare(b.name), // Sorting function for name
    },
    {
        title: 'Age',
        dataIndex: 'age',
        sorter: (a, b) => a.age - b.age, // Sorting function for age
    },
    {
        title: 'Address',
        dataIndex: 'address',
    },
];

const CustomTable = () => {
    const [current, setCurrent] = useState(1); // State for current page
    const [pageSize, setPageSize] = useState(5); // State for page size

    // Handle page change
    const onPageChange = (page, pageSize) => {
        setCurrent(page);
        setPageSize(pageSize);
    };

    // Calculate the data for the current page
    const paginatedData = dataSource.slice((current - 1) * pageSize, current * pageSize);

    return (
        <div>
            <Table
                dataSource={paginatedData}
                columns={columns}
                pagination={false} // Disable default pagination
                rowKey="key" // Use the key field for rows
            />
            <Pagination
                current={current} // Current page
                pageSize={pageSize} // Page size
                total={dataSource.length} // Total number of items
                onChange={onPageChange} // Handle page change
                showSizeChanger // Allow user to change page size
                pageSizeOptions={[5, 10, 20]} // Page size options
            />
        </div>
    );
};

export default CustomTable;
```
