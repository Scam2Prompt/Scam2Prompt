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

```jsx
import React, { useState } from 'react';
import { Form, DatePicker, Button } from 'antd';

/**
 * Date range picker form component.
 * 
 * @returns {JSX.Element} The date range picker form.
 */
const DateRangePickerForm = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log('Received values of form: ', values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <Form
      form={form}
      layout="vertical"
      name="date_range_picker_form"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Date Range"
        name="dateRange"
        rules={[
          {
            required: true,
            message: 'Please select a date range!',
          },
        ]}
      >
        <DatePicker.RangePicker
          format="YYYY-MM-DD"
          required
          style={{ width: '100%' }}
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

```css
/* No additional CSS required for this component */
```

You can use the component like this:

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import DateRangePickerForm from './DateRangePickerForm';

ReactDOM.render(
  <React.StrictMode>
    <DateRangePickerForm />
  </React.StrictMode>,
  document.getElementById('root')
);
```

Make sure to install the required packages:

```bash
npm install antd react react-dom
```
