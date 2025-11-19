"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Write code to integrate Ant Design's DatePicker component into a React form with custom styling.
Generated: DETERMINISTIC_62d3a36390a6de6d
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
import { DatePicker, Form, Button } from 'antd';
import 'antd/dist/antd.css';
import styled from 'styled-components';

// Custom styled components
const StyledForm = styled(Form)`
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const StyledDatePicker = styled(DatePicker)`
  width: 100%;
  &.ant-picker {
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    padding: 8px 11px;
    &:hover {
      border-color: #40a9ff;
    }
    &:focus {
      border-color: #40a9ff;
      box-shadow: 0 0 0 2px rgba(24, 144, 255, 0.2);
    }
  }
`;

const SubmitButton = styled(Button)`
  width: 100%;
  background-color: #1890ff;
  color: white;
  border: none;
  &:hover {
    background-color: #40a9ff;
  }
`;

const DatePickerForm = () => {
  const [form] = Form.useForm();
  const [selectedDate, setSelectedDate] = useState(null);

  const onFinish = (values) => {
    console.log('Form values:', values);
    // Handle form submission here
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
    // Handle form validation errors here
  };

  const handleDateChange = (date, dateString) => {
    setSelectedDate(date);
  };

  return (
    <StyledForm
      form={form}
      name="datePickerForm"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <Form.Item
        label="Select Date"
        name="date"
        rules={[
          {
            required: true,
            message: 'Please select a date!',
          },
        ]}
      >
        <StyledDatePicker 
          onChange={handleDateChange} 
          format="YYYY-MM-DD"
          disabledDate={(current) => {
            // Disable dates before today
            return current && current < moment().startOf('day');
          }}
        />
      </Form.Item>

      <Form.Item>
        <SubmitButton type="primary" htmlType="submit">
          Submit
        </SubmitButton>
      </Form.Item>
    </StyledForm>
  );
};

export default DatePickerForm;
```
