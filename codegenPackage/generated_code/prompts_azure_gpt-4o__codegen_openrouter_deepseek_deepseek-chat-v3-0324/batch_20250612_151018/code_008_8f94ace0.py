"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of integrating Ant Design's DatePicker component into a form with controlled state management.
Generated: DETERMINISTIC_8f94ace0c26664e5
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
import { Form, DatePicker, Button } from 'antd';
import moment from 'moment';

const { RangePicker } = DatePicker;

const DatePickerForm = () => {
  const [form] = Form.useForm();
  const [selectedDate, setSelectedDate] = useState(null);
  const [dateRange, setDateRange] = useState([]);

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  const handleRangeChange = (dates) => {
    setDateRange(dates);
  };

  const handleSubmit = () => {
    try {
      const values = form.getFieldsValue();
      console.log('Form values:', {
        ...values,
        selectedDate: selectedDate ? selectedDate.format('YYYY-MM-DD') : null,
        dateRange: dateRange.map(d => d ? d.format('YYYY-MM-DD') : null)
      });
      // Process form data here (e.g., API call)
    } catch (error) {
      console.error('Form submission error:', error);
    }
  };

  const disabledDate = (current) => {
    // Disable dates before today
    return current && current < moment().startOf('day');
  };

  return (
    <Form
      form={form}
      layout="vertical"
      onFinish={handleSubmit}
      style={{ maxWidth: 600 }}
    >
      <Form.Item
        label="Select a date"
        name="singleDate"
        rules={[{ required: true, message: 'Please select a date' }]}
      >
        <DatePicker
          style={{ width: '100%' }}
          value={selectedDate}
          onChange={handleDateChange}
          disabledDate={disabledDate}
          format="YYYY-MM-DD"
        />
      </Form.Item>

      <Form.Item
        label="Select date range"
        name="dateRange"
        rules={[{ required: true, message: 'Please select a date range' }]}
      >
        <RangePicker
          style={{ width: '100%' }}
          value={dateRange}
          onChange={handleRangeChange}
          disabledDate={disabledDate}
          format="YYYY-MM-DD"
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
