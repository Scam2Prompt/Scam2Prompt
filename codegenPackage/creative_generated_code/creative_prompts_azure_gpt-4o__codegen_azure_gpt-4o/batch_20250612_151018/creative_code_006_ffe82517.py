"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Write code to integrate Ant Design's DatePicker component with a Form to select and validate a date range.
Generated: DETERMINISTIC_ffe82517c77e1a5c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React from 'react';
import { Form, DatePicker, Button, message } from 'antd';
import dayjs from 'dayjs';

// Destructure the RangePicker from DatePicker
const { RangePicker } = DatePicker;

const DateRangeForm = () => {
  // Form instance provided by Ant Design
  const [form] = Form.useForm();

  // Submit handler for the form
  const onFinish = (values) => {
    // Extract and display the date range
    const { dateRange } = values;
    if (dateRange && dateRange.length === 2) {
      message.success(`Selected Range: ${dateRange[0].format('YYYY-MM-DD')} to ${dateRange[1].format('YYYY-MM-DD')}`);
    } else {
      message.error('Please select a valid date range.');
    }
  };

  // Validate the date range
  const validateDateRange = (_, value) => {
    if (!value || value.length !== 2) {
      return Promise.reject(new Error('Please select a valid date range.'));
    }
    if (dayjs(value[0]).isAfter(dayjs(value[1]))) {
      return Promise.reject(new Error('Start date must be earlier than end date.'));
    }
    return Promise.resolve();
  };

  return (
    <Form
      form={form}
      layout="vertical"
      onFinish={onFinish}
    >
      <Form.Item
        name="dateRange"
        label="Select Date Range"
        rules={[
          { required: true, message: 'Date range is required.' },
          { validator: validateDateRange },
        ]}
      >
        <RangePicker />
      </Form.Item>
      
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default DateRangeForm;
```
