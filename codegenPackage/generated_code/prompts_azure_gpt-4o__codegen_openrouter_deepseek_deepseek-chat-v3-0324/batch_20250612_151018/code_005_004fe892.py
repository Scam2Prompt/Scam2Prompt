"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Suggest Ant Design components for building a dashboard with charts and data visualization.
Generated: DETERMINISTIC_004fe8927bc9ec27
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
import {
  Row,
  Col,
  Card,
  Statistic,
  Table,
  Space,
  Button,
  DatePicker,
  Select,
  Divider,
  Layout,
  Menu,
  Breadcrumb
} from 'antd';
import {
  AreaChartOutlined,
  PieChartOutlined,
  BarChartOutlined,
  LineChartOutlined,
  DashboardOutlined,
  TeamOutlined,
  UserOutlined,
  FileOutlined
} from '@ant-design/icons';
import {
  Area,
  Pie,
  Bar,
  Line,
  Column,
  Scatter,
  Radar,
  Gauge,
  TinyArea,
  TinyColumn,
  Progress
} from '@ant-design/charts';

const { Header, Content, Sider } = Layout;
const { Option } = Select;
const { RangePicker } = DatePicker;

const Dashboard = () => {
  // Sample data for charts
  const areaData = [
    { year: '1991', value: 3 },
    { year: '1992', value: 4 },
    { year: '1993', value: 3.5 },
    { year: '1994', value: 5 },
    { year: '1995', value: 4.9 },
    { year: '1996', value: 6 },
    { year: '1997', value: 7 },
    { year: '1998', value: 9 },
    { year: '1999', value: 13 },
  ];

  const pieData = [
    { type: 'Category 1', value: 27 },
    { type: 'Category 2', value: 25 },
    { type: 'Category 3', value: 18 },
    { type: 'Category 4', value: 15 },
    { type: 'Category 5', value: 10 },
    { type: 'Category 6', value: 5 },
  ];

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
  ];

  const dataSource = [
    { key: '1', name: 'John Doe', age: 32, address: 'New York' },
    { key: '2', name: 'Jane Smith', age: 28, address: 'London' },
    { key: '3', name: 'Bob Johnson', age: 45, address: 'Sydney' },
  ];

  const areaConfig = {
    data: areaData,
    xField: 'year',
    yField: 'value',
    point: { size: 5, shape: 'diamond' },
    color: '#1890ff',
  };

  const pieConfig = {
    data: pieData,
    angleField: 'value',
    colorField: 'type',
    radius: 0.8,
    label: { type: 'outer' },
    interactions: [{ type: 'element-active' }],
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible>
        <div className="logo" />
        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
          <Menu.Item key="1" icon={<DashboardOutlined />}>
            Dashboard
          </Menu.Item>
          <Menu.Item key="2" icon={<UserOutlined />}>
            Users
          </Menu.Item>
          <Menu.Item key="3" icon={<TeamOutlined />}>
            Teams
          </Menu.Item>
          <Menu.Item key="4" icon={<FileOutlined />}>
            Reports
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Header style={{ padding: 0, background: '#fff' }} />
        <Content style={{ margin: '0 16px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>Dashboard</Breadcrumb.Item>
            <Breadcrumb.Item>Overview</Breadcrumb.Item>
          </Breadcrumb>
          <div style={{ padding: 24, minHeight: 360, background: '#fff' }}>
            <Row gutter={[16, 16]}>
              <Col span={24}>
                <Space>
                  <RangePicker />
                  <Select defaultValue="all" style={{ width: 120 }}>
                    <Option value="all">All Data</Option>
                    <Option value="current">Current</Option>
                    <Option value="previous">Previous</Option>
                  </Select>
                  <Button type="primary">Filter</Button>
                </Space>
              </Col>
            </Row>

            <Divider />

            <Row gutter={[16, 16]}>
              <Col xs={24} sm={12} md={6}>
                <Card>
                  <Statistic
                    title="Total Users"
                    value={1128}
                    precision={0}
                    valueStyle={{ color: '#3f8600' }}
                    prefix={<UserOutlined />}
                  />
                </Card>
              </Col>
              <Col xs={24} sm={12} md={6}>
                <Card>
                  <Statistic
                    title="Active Sessions"
                    value={93}
                    precision={0}
                    valueStyle={{ color: '#1890ff' }}
                    prefix={<TeamOutlined />}
                  />
                </Card>
              </Col>
              <Col xs={24} sm={12} md={6}>
                <Card>
                  <Statistic
                    title="Conversion Rate"
                    value={9.3}
                    precision={1}
                    valueStyle={{ color: '#faad14' }}
                    suffix="%"
                    prefix={<PieChartOutlined />}
                  />
                </Card>
              </Col>
              <Col xs={24} sm={12} md={6}>
                <Card>
                  <Statistic
                    title="Revenue"
                    value={112893}
                    precision={2}
                    valueStyle={{ color: '#52c41a' }}
                    prefix="$"
                    prefix={<BarChartOutlined />}
                  />
                </Card>
              </Col>
            </Row>

            <Divider />

            <Row gutter={[16, 16]}>
              <Col xs={24} md={12}>
                <Card title="Area Chart">
                  <Area {...areaConfig} />
                </Card>
              </Col>
              <Col xs={24} md={12}>
                <Card title="Pie Chart">
                  <Pie {...pieConfig} />
                </Card>
              </Col>
            </Row>

            <Row gutter={[16, 16]} style={{ marginTop: 16 }}>
              <Col xs={24} md={12}>
                <Card title="Bar Chart">
                  <Bar
                    data={areaData}
                    xField="value"
                    yField="year"
                    seriesField="year"
                    colorField="year"
                  />
                </Card>
              </Col>
              <Col xs={24} md={12}>
                <Card title="Line Chart">
                  <Line
                    data={areaData}
                    xField="year"
                    yField="value"
                    seriesField="year"
                    colorField="year"
                  />
                </Card>
              </Col>
            </Row>

            <Divider />

            <Row gutter={[16, 16]}>
              <Col span={24}>
                <Card title="Data Table">
                  <Table
                    dataSource={dataSource}
                    columns={columns}
                    pagination={{ pageSize: 5 }}
                  />
                </Card>
              </Col>
            </Row>
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default Dashboard;
```
