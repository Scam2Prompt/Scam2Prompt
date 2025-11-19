"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: What are the key features of Ant Design, a popular React UI library?
Generated: DETERMINISTIC_ecbbbe70f00b7976
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Key Features of Ant Design React UI Library
 * 
 * This component demonstrates the key features of Ant Design,
 * a popular React UI library.
 */
import React from 'react';
import { 
  Button, 
  Card, 
  Row, 
  Col,
  Table,
  Form,
  Input,
  Select,
  Modal,
  notification,
  Space,
  Typography 
} from 'antd';

const { Title, Text } = Typography;
const { Option } = Select;

const AntDesignFeatures = () => {
  const [form] = Form.useForm();
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleOk = () => {
    setIsModalVisible(false);
    notification.success({
      message: 'Action Completed',
      description: 'Modal action was successfully processed.',
    });
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const dataSource = [
    {
      key: '1',
      feature: 'Enterprise-class UI',
      description: 'Professional UI design for enterprise applications',
    },
    {
      key: '2',
      feature: 'Rich Components',
      description: '50+ high-quality React components out of the box',
    },
    {
      key: '3',
      feature: 'Theme Customization',
      description: 'Customizable design system with theme support',
    },
    {
      key: '4',
      feature: 'Internationalization',
      description: 'Supports dozens of languages out of the box',
    },
    {
      key: '5',
      feature: 'TypeScript Support',
      description: 'First-class TypeScript support',
    },
    {
      key: '6',
      feature: 'Responsive Design',
      description: 'Works well on mobile, tablet, and desktop',
    },
  ];

  const columns = [
    {
      title: 'Feature',
      dataIndex: 'feature',
      key: 'feature',
    },
    {
      title: 'Description',
      dataIndex: 'description',
      key: 'description',
    },
  ];

  return (
    <div style={{ padding: 24 }}>
      <Title level={2}>Ant Design Key Features</Title>
      <Text type="secondary">
        A comprehensive React UI library for enterprise applications
      </Text>

      <Row gutter={16} style={{ marginTop: 24 }}>
        <Col span={24}>
          <Card title="Core Features">
            <Table 
              dataSource={dataSource} 
              columns={columns} 
              pagination={false}
              bordered
            />
          </Card>
        </Col>
      </Row>

      <Row gutter={16} style={{ marginTop: 24 }}>
        <Col span={12}>
          <Card title="Component Example">
            <Space direction="vertical" size="middle">
              <Button type="primary">Primary Button</Button>
              <Button>Default Button</Button>
              <Button type="dashed">Dashed Button</Button>
              <Button type="text">Text Button</Button>
              <Button type="link">Link Button</Button>
            </Space>
          </Card>
        </Col>
        <Col span={12}>
          <Card title="Form Example">
            <Form form={form} layout="vertical">
              <Form.Item name="username" label="Username">
                <Input placeholder="Enter username" />
              </Form.Item>
              <Form.Item name="role" label="Role">
                <Select placeholder="Select a role">
                  <Option value="admin">Admin</Option>
                  <Option value="user">User</Option>
                  <Option value="guest">Guest</Option>
                </Select>
              </Form.Item>
              <Form.Item>
                <Button type="primary" onClick={showModal}>
                  Open Modal
                </Button>
              </Form.Item>
            </Form>
          </Card>
        </Col>
      </Row>

      <Modal 
        title="Ant Design Modal" 
        visible={isModalVisible} 
        onOk={handleOk} 
        onCancel={handleCancel}
      >
        <p>This is a modal dialog demonstrating Ant Design's modal component.</p>
      </Modal>
    </div>
  );
};

export default AntDesignFeatures;
```
e size="middle">
                  <Button type="primary">Primary Button</Button>
                  <Button>Default Button</Button>
                  <Button type="dashed">Dashed Button</Button>
                  <Button type="text">Text Button</Button>
                  <Button type="link">Link Button</Button>
                </Space>
              </Card>

              {/* Form Components */}
              <Card title="Form Components">
                <Form
                  {...layout}
                  form={form}
                  name="control-hooks"
                  onFinish={onFinish}
                  onFinishFailed={onFinishFailed}
                >
                  <Form.Item
                    name="username"
                    label="Username"
                    rules={[{ required: true, message: 'Please input your username!' }]}
                  >
                    <Input />
                  </Form.Item>
                  <Form.Item
                    name="gender"
                    label="Gender"
                    rules={[{ required: true }]}
                  >
                    <Select
                      placeholder="Select a option and change input text above"
                      onChange={onGenderChange}
                      allowClear
                    >
                      <Option value="male">male</Option>
                      <Option value="female">female</Option>
                      <Option value="other">other</Option>
                    </Select>
                  </Form.Item>
                  <Form.Item {...tailLayout}>
                    <Button type="primary" htmlType="submit">
                      Submit
                    </Button>
                  </Form.Item>
                </Form>
              </Card>

              {/* Data Display */}
              <Card title="Data Display">
                <Row gutter={16}>
                  <Col span={12}>
                    <Title level={4}>Table</Title>
                    <Table dataSource={dataSource} columns={columns} />
                  </Col>
                  <Col span={12}>
                    <Title level={4}>Cards & Avatars</Title>
                    <Card
                      cover={
                        <img
                          alt="example"
                          src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
                        />
                      }
                      actions={[
                        <SmileOutlined key="like" />,
                        <SolutionOutlined key="edit" />,
                      ]}
                    >
                      <Card.Meta
                        avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
                        title="Card Title"
                        description="This is the description"
                      />
                    </Card>
                  </Col>
                </Row>
              </Card>

              {/* Feedback Components */}
              <Card title="Feedback Components">
                <Space size="middle">
                  <Button type="primary" onClick={showModal}>
                    Open Modal
                  </Button>
                  <Button onClick={() => message.info('This is a normal message')}>
                    Show Message
                  </Button>
                  <Badge count={5}>
                    <Avatar shape="square" size="large" icon={<UserOutlined />} />
                  </Badge>
                </Space>
                <Modal
                  title="Basic Modal"
                  visible={visible}
                  onOk={handleOk}
                  onCancel={handleCancel}
                >
                  <p>Some contents...</p>
                  <p>Some contents...</p>
                  <p>Some contents...</p>
                </Modal>
              </Card>

              {/* Navigation Components */}
              <Card title="Navigation Components">
                <Tabs defaultActiveKey="1">
                  <TabPane tab="Tab 1" key="1">
                    Content of Tab Pane 1
                  </TabPane>
                  <TabPane tab="Tab 2" key="2">
                    Content of Tab Pane 2
                  </TabPane>
                </Tabs>
                <Steps current={1}>
                  <Step title="Finished" description="This is a description." />
                  <Step title="In Progress" subTitle="Left 00:00:08" description="This is a description." />
                  <Step title="Waiting" description="This is a description." />
                </Steps>
              </Card>

              {/* Data Entry */}
              <Card title="Data Entry">
                <DatePicker />
                <Dragger {...uploadProps}>
                  <p className="ant-upload-drag-icon">
                    <InboxOutlined />
                  </p>
                  <p className="ant-upload-text">Click or drag file to this area to upload</p>
                  <p className="ant-upload-hint">
                    Support for a single or bulk upload.
                  </p>
                </Dragger>
              </Card>
            </Space>
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          Ant Design ©2022 Created by Ant UED
        </Footer>
      </Layout>
    </Layout>
  );
};

export default AntDesignDemo;
```
