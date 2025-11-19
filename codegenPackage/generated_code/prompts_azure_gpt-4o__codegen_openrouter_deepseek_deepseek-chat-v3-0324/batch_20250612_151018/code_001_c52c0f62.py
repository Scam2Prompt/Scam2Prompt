"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Recommend Ant Design components for building a responsive dashboard layout in React, including navigation and data visualization.
Generated: DETERMINISTIC_c52c0f62a87bdfbc
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import { Layout, Menu, Card, Row, Col, Statistic, Table, Space, Button } from 'antd';
import {
  DashboardOutlined,
  UserOutlined,
  FileOutlined,
  BarChartOutlined,
  SettingOutlined,
  ArrowUpOutlined,
  ArrowDownOutlined,
} from '@ant-design/icons';
import { Line, Pie } from '@ant-design/charts';

const { Header, Content, Sider } = Layout;

const Dashboard = () => {
  // Sample data for charts
  const lineData = [
    { month: 'Jan', value: 120 },
    { month: 'Feb', value: 200 },
    { month: 'Mar', value: 150 },
    { month: 'Apr', value: 80 },
    { month: 'May', value: 70 },
    { month: 'Jun', value: 110 },
    { month: 'Jul', value: 130 },
  ];

  const pieData = [
    { type: 'Category A', value: 27 },
    { type: 'Category B', value: 25 },
    { type: 'Category C', value: 18 },
    { type: 'Category D', value: 15 },
    { type: 'Category E', value: 10 },
    { type: 'Category F', value: 5 },
  ];

  // Sample table data
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
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
      title: 'Action',
      key: 'action',
      render: (_, record) => (
        <Space size="middle">
          <Button type="link">Edit</Button>
          <Button type="link" danger>Delete</Button>
        </Space>
      ),
    },
  ];

  const data = [
    { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
    { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
    { key: '3', name: 'Joe Black', age: 32, address: 'Sidney No. 1 Lake Park' },
  ];

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider breakpoint="lg" collapsedWidth="0">
        <div className="logo" style={{ height: '32px', margin: '16px', background: 'rgba(255, 255, 255, 0.2)' }} />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
          <Menu.Item key="1" icon={<DashboardOutlined />}>
            Dashboard
          </Menu.Item>
          <Menu.Item key="2" icon={<UserOutlined />}>
            Users
          </Menu.Item>
          <Menu.Item key="3" icon={<FileOutlined />}>
            Files
          </Menu.Item>
          <Menu.Item key="4" icon={<BarChartOutlined />}>
            Reports
          </Menu.Item>
          <Menu.Item key="5" icon={<SettingOutlined />}>
            Settings
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout>
        <Header style={{ padding: 0, background: '#fff' }} />
        <Content style={{ margin: '24px 16px 0' }}>
          <div style={{ padding: 24, minHeight: 360, background: '#fff' }}>
            {/* Stats Cards */}
            <Row gutter={16}>
              <Col span={6}>
                <Card>
                  <Statistic
                    title="Active Users"
                    value={1128}
                    precision={0}
                    valueStyle={{ color: '#3f8600' }}
                    prefix={<ArrowUpOutlined />}
                  />
                </Card>
              </Col>
              <Col span={6}>
                <Card>
                  <Statistic
                    title="Total Revenue"
                    value={8846}
                    precision={2}
                    valueStyle={{ color: '#3f8600' }}
                    prefix="$"
                  />
                </Card>
              </Col>
              <Col span={6}>
                <Card>
                  <Statistic
                    title="Tasks Completed"
                    value={93}
                    precision={0}
                    valueStyle={{ color: '#3f8600' }}
                    suffix="/ 100"
                  />
                </Card>
              </Col>
              <Col span={6}>
                <Card>
                  <Statistic
                    title="Error Rate"
                    value={2.5}
                    precision={2}
                    valueStyle={{ color: '#cf1322' }}
                    prefix={<ArrowDownOutlined />}
                    suffix="%"
                  />
                </Card>
              </Col>
            </Row>

            {/* Charts */}
            <Row gutter={16} style={{ marginTop: 24 }}>
              <Col span={16}>
                <Card title="Monthly Performance">
                  <Line
                    data={lineData}
                    xField="month"
                    yField="value"
                    point={{ size: 5, shape: 'diamond' }}
                    color="#1890ff"
                  />
                </Card>
              </Col>
              <Col span={8}>
                <Card title="Revenue Distribution">
                  <Pie
                    data={pieData}
                    angleField="value"
                    colorField="type"
                    radius={0.8}
                    label={{
                      type: 'outer',
                      content: '{name} {percentage}',
                    }}
                  />
                </Card>
              </Col>
            </Row>

            {/* Data Table */}
            <Card style={{ marginTop: 24 }} title="Recent Activities">
              <Table columns={columns} dataSource={data} />
            </Card>
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default Dashboard;
```
