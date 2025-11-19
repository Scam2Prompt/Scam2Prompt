"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the key components of the Ant Design library for building modern web applications?
Generated: DETERMINISTIC_1c317c0bef81333c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-commented code example demonstrating key Ant Design components in a React application:

```jsx
import React from 'react';
import {
  // Layout Components
  Layout,
  Menu,
  // General UI Components
  Button,
  Card,
  Table,
  Form,
  Input,
  Select,
  // Feedback Components
  Modal,
  message,
  notification,
  // Navigation
  Breadcrumb,
  // Data Entry
  DatePicker,
  Checkbox,
  Radio,
  Upload,
  // Data Display
  Badge,
  Tag,
  Tooltip,
  // Feedback
  Alert,
  Spin,
  Progress,
  // Other
  ConfigProvider,
  theme
} from 'antd';
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  UploadOutlined,
  UserOutlined,
  VideoCameraOutlined
} from '@ant-design/icons';

const { Header, Sider, Content, Footer } = Layout;
const { Option } = Select;
const { TextArea } = Input;

// Example form component
const ExampleForm = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log('Form values:', values);
    message.success('Form submitted successfully!');
  };

  const onFinishFailed = (errorInfo) => {
    console.error('Form submission failed:', errorInfo);
    notification.error({
      message: 'Submission Error',
      description: 'Please check the form for errors.'
    });
  };

  return (
    <Form
      form={form}
      name="basic"
      layout="vertical"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[{ required: true, message: 'Please input your username!' }]}
      >
        <Input prefix={<UserOutlined />} placeholder="Username" />
      </Form.Item>

      <Form.Item
        label="Email"
        name="email"
        rules={[{ type: 'email', message: 'Please enter a valid email!' }]}
      >
        <Input placeholder="Email" />
      </Form.Item>

      <Form.Item
        label="Select Field"
        name="select"
        rules={[{ required: true, message: 'Please select an option!' }]}
      >
        <Select placeholder="Select an option">
          <Option value="option1">Option 1</Option>
          <Option value="option2">Option 2</Option>
          <Option value="option3">Option 3</Option>
        </Select>
      </Form.Item>

      <Form.Item name="remember" valuePropName="checked">
        <Checkbox>Remember me</Checkbox>
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

// Example table component
const ExampleTable = () => {
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      render: (text) => <a>{text}</a>,
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
    {
      title: 'Tags',
      key: 'tags',
      dataIndex: 'tags',
      render: (_, { tags }) => (
        <>
          {tags.map((tag) => {
            let color = tag.length > 5 ? 'geekblue' : 'green';
            return (
              <Tag color={color} key={tag}>
                {tag.toUpperCase()}
              </Tag>
            );
          })}
        </>
      ),
    },
    {
      title: 'Action',
      key: 'action',
      render: (_, record) => (
        <Button type="link" onClick={() => message.info(`Action on ${record.name}`)}>
          Action
        </Button>
      ),
    },
  ];

  const data = [
    {
      key: '1',
      name: 'John Brown',
      age: 32,
      address: 'New York No. 1 Lake Park',
      tags: ['nice', 'developer'],
    },
    {
      key: '2',
      name: 'Jim Green',
      age: 42,
      address: 'London No. 1 Lake Park',
      tags: ['cool'],
    },
  ];

  return <Table columns={columns} dataSource={data} />;
};

// Main App component
const App = () => {
  const [collapsed, setCollapsed] = React.useState(false);
  const [loading, setLoading] = React.useState(false);

  const toggleLoading = () => {
    setLoading(true);
    setTimeout(() => setLoading(false), 2000);
  };

  return (
    <ConfigProvider
      theme={{
        algorithm: theme.defaultAlgorithm,
        token: {
          colorPrimary: '#1890ff',
        },
      }}
    >
      <Layout style={{ minHeight: '100vh' }}>
        <Sider trigger={null} collapsible collapsed={collapsed}>
          <div className="logo" />
          <Menu
            theme="dark"
            mode="inline"
            defaultSelectedKeys={['1']}
            items={[
              {
                key: '1',
                icon: <UserOutlined />,
                label: 'Dashboard',
              },
              {
                key: '2',
                icon: <VideoCameraOutlined />,
                label: 'Videos',
              },
              {
                key: '3',
                icon: <UploadOutlined />,
                label: 'Upload',
              },
            ]}
          />
        </Sider>
        <Layout>
          <Header style={{ padding: 0, background: '#fff' }}>
            <Button
              type="text"
              icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
              onClick={() => setCollapsed(!collapsed)}
              style={{
                fontSize: '16px',
                width: 64,
                height: 64,
              }}
            />
          </Header>
          <Content
            style={{
              margin: '24px 16px',
              padding: 24,
              minHeight: 280,
              background: '#fff',
            }}
          >
            <Breadcrumb
              items={[
                { title: 'Home' },
                { title: 'Application' },
                { title: 'Dashboard' },
              ]}
            />
            <div style={{ margin: '16px 0' }}>
              <Alert
                message="Welcome to Ant Design"
                description="This is a demo showcasing key Ant Design components."
                type="info"
                showIcon
                closable
              />
            </div>

            <Spin spinning={loading}>
              <Card
                title="Example Form"
                extra={
                  <Button onClick={toggleLoading}>
                    {loading ? 'Loading...' : 'Reload'}
                  </Button>
                }
                style={{ marginBottom: 24 }}
              >
                <ExampleForm />
              </Card>

              <Card title="Data Table">
                <ExampleTable />
              </Card>
            </Spin>
          </Content>
          <Footer style={{ textAlign: 'center' }}>
            Ant Design ©{new Date().getFullYear()} Created by Ant UED
          </Footer>
        </Layout>
      </Layout>
    </ConfigProvider>
  );
};

export default App;
```
