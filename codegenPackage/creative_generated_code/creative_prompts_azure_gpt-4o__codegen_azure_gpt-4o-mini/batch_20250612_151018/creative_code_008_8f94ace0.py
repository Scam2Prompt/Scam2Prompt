"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of integrating Ant Design's DatePicker component into a form with controlled state management.
Generated: DETERMINISTIC_8f94ace0c26664e5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';
import { Form, DatePicker, Button, message } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const DatePickerForm = () => {
  // State to hold the selected date
  const [selectedDate, setSelectedDate] = useState(null);

  // Handle form submission
  const onFinish = (values) => {
    if (selectedDate) {
      message.success(`Selected date: ${selectedDate.format('YYYY-MM-DD')}`);
    } else {
      message.error('Please select a date before submitting');
    }
  };

  // Handle date change
  const onDateChange = (date, dateString) => {
    setSelectedDate(date);
  };

  return (
    <Form onFinish={onFinish} layout="vertical">
      <Form.Item
        label="Select Date"
        name="date"
        rules={[{ required: true, message: 'Please select a date!' }]}
      >
        <DatePicker onChange={onDateChange} />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default DatePickerForm;
```
