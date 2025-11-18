"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Provide example code for integrating Ant Design's DatePicker component with form validation in a React application.
Generated: DETERMINISTIC_77dc0b30b57f4b7f
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
import { Form, DatePicker, Button, message } from 'antd';
import moment from 'moment';

// Custom DatePicker component with form validation
const DatePickerForm = () => {
  // State to hold the selected date
  const [form] = Form.useForm();

  // Function to handle form submission
  const onFinish = (values) => {
    // Show success message with the selected date
    message.success(`Selected date: ${values.date.format('YYYY-MM-DD')}`);
  };

  // Function to handle form submission failure
  const onFinishFailed = (errorInfo) => {
    // Log the error info to the console for debugging
    console.error('Failed:', errorInfo);
  };

  return (
    <Form
      form={form}
      name="date_picker_form"
      layout="vertical"
      initialValues={{ date: null }} // Initialize date to null
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        name="date"
        label="Select Date"
        rules={[
          {
            required: true,
            message: 'Please select a date!', // Validation message
          },
          {
            type: 'object', // Ensure the value is an object (moment)
            message: 'Invalid date format!',
          },
        ]}
      >
        <DatePicker
          style={{ width: '100%' }} // Make DatePicker full width
          format="YYYY-MM-DD" // Display format for the date
          disabledDate={(current) => current && current < moment().endOf('day')} // Disable past dates
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

export default DatePickerForm;
```

Make sure to install the necessary packages by running:
```bash
npm install antd moment
```
