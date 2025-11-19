"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate a React component using Ant Design's UI design language.
Generated: DETERMINISTIC_ec7925510f57c9c9
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { 
  Button, 
  Form, 
  Input, 
  Card, 
  message, 
  Space,
  Typography 
} from 'antd';

const { Title } = Typography;

/**
 * UserProfileForm - A React component for displaying and editing user profile information
 * using Ant Design components.
 * 
 * Features:
 * - Form validation
 * - Success/error feedback
 * - Responsive layout
 */
const UserProfileForm = () => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

  /**
   * Handle form submission
   * @param {Object} values - Form field values
   */
  const handleSubmit = async (values) => {
    try {
      setLoading(true);
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      message.success('Profile updated successfully!');
    } catch (error) {
      message.error('Failed to update profile. Please try again.');
      console.error('Submission error:', error);
    } finally {
      setLoading(false);
    }
  };

  /**
   * Handle form reset
   */
  const handleReset = () => {
    form.resetFields();
  };

  return (
    <Card 
      title={<Title level={4}>User Profile</Title>}
      style={{ maxWidth: 600, margin: '0 auto' }}
    >
      <Form
        form={form}
        layout="vertical"
        onFinish={handleSubmit}
        initialValues={{
          name: 'John Doe',
          email: 'john.doe@example.com',
          bio: 'Software developer with 5 years of experience'
        }}
      >
        <Form.Item
          label="Full Name"
          name="name"
          rules={[
            { required: true, message: 'Please input your name!' },
            { min: 2, message: 'Name must be at least 2 characters' }
          ]}
        >
          <Input placeholder="Enter your full name" />
        </Form.Item>

        <Form.Item
          label="Email"
          name="email"
          rules={[
            { required: true, message: 'Please input your email!' },
            { type: 'email', message: 'Please enter a valid email' }
          ]}
        >
          <Input placeholder="Enter your email address" />
        </Form.Item>

        <Form.Item
          label="Bio"
          name="bio"
          rules={[
            { max: 200, message: 'Bio cannot exceed 200 characters' }
          ]}
        >
          <Input.TextArea rows={4} placeholder="Tell us about yourself" />
        </Form.Item>

        <Form.Item>
          <Space>
            <Button 
              type="primary" 
              htmlType="submit" 
              loading={loading}
            >
              Save Changes
            </Button>
            <Button 
              htmlType="button" 
              onClick={handleReset}
            >
              Reset
            </Button>
          </Space>
        </Form.Item>
      </Form>
    </Card>
  );
};

export default UserProfileForm;
```
