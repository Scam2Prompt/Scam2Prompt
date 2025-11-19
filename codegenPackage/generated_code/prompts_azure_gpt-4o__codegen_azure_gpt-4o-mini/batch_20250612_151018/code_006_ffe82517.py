"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Write code to integrate Ant Design's DatePicker component with a Form to select and validate a date range.
Generated: DETERMINISTIC_ffe82517c77e1a5c
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
import { Form, DatePicker, Button, message } from 'antd';
import moment from 'moment';

// DateRangePickerForm component for selecting and validating a date range
const DateRangePickerForm = () => {
  const [form] = Form.useForm();

  // Function to handle form submission
  const onFinish = (values) => {
    const { dateRange } = values;
    if (dateRange && dateRange.length === 2) {
      const startDate = dateRange[0].format('YYYY-MM-DD');
      const endDate = dateRange[1].format('YYYY-MM-DD');
      message.success(`Selected Date Range: ${startDate} to ${endDate}`);
    }
  };

  // Function to validate the date range
  const validateDateRange = (_, value) => {
    if (!value || value.length < 2) {
      return Promise.reject(new Error('Please select a date range!'));
    }
    const [start, end] = value;
    if (end.isBefore(start)) {
      return Promise.reject(new Error('End date cannot be before start date!'));
    }
    return Promise.resolve();
  };

  return (
    <Form
      form={form}
      layout="vertical"
      onFinish={onFinish}
      style={{ maxWidth: 400, margin: 'auto' }}
    >
      <Form.Item
        name="dateRange"
        label="Select Date Range"
        rules={[{ validator: validateDateRange }]}
      >
        <DatePicker.RangePicker
          format="YYYY-MM-DD"
          disabledDate={(current) => current && current > moment().endOf('day')}
        />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default DateRangePickerForm;
```
