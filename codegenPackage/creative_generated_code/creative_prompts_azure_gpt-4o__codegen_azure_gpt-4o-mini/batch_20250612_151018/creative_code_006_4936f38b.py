"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Create a React form using Ant Design's Form and Input components, with custom validation rules for email and password fields.
Generated: DETERMINISTIC_4936f38ba672cbc1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Form, Input, Button } from 'antd';

// Custom validation rules
const validateEmail = (email) => {
    // Basic email regex for validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
};

const validatePassword = (password) => {
    // Password must be at least 8 characters long
    return password.length >= 8;
};

const CustomForm = () => {
    // Form submission handler
    const onFinish = (values) => {
        console.log('Success:', values);
    };

    // Form submission error handler
    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };

    return (
        <Form
            name="custom_form"
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
            layout="vertical"
            style={{ maxWidth: 400, margin: '0 auto' }}
        >
            <Form.Item
                label="Email"
                name="email"
                rules={[
                    {
                        required: true,
                        message: 'Please input your email!',
                    },
                    {
                        validator: (_, value) =>
                            validateEmail(value)
                                ? Promise.resolve()
                                : Promise.reject(new Error('The input is not a valid email!')),
                    },
                ]}
            >
                <Input placeholder="Enter your email" />
            </Form.Item>

            <Form.Item
                label="Password"
                name="password"
                rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                    {
                        validator: (_, value) =>
                            validatePassword(value)
                                ? Promise.resolve()
                                : Promise.reject(new Error('Password must be at least 8 characters long!')),
                    },
                ]}
            >
                <Input.Password placeholder="Enter your password" />
            </Form.Item>

            <Form.Item>
                <Button type="primary" htmlType="submit">
                    Submit
                </Button>
            </Form.Item>
        </Form>
    );
};

export default CustomForm;
```
