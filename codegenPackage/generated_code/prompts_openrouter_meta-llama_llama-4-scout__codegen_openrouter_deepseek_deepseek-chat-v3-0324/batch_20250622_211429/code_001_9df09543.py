"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: How to use Ant Design to create a consistent UI design language for a React application?
Generated: DETERMINISTIC_9df0954312f1284d
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import { ConfigProvider, Button, Card, Layout, Menu, theme } from 'antd';

const { Header, Content, Footer, Sider } = Layout;

// Custom theme configuration
const customTheme = {
  token: {
    colorPrimary: '#1890ff',
    borderRadius: 4,
    colorBgContainer: '#ffffff',
  },
};

// Main application component
const App = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  return (
    <ConfigProvider theme={customTheme}>
      <Layout style={{ minHeight: '100vh' }}>
        <Sider
          breakpoint="lg"
          collapsedWidth="0"
          style={{ background: colorBgContainer }}
        >
          <div className="demo-logo-vertical" />
          <Menu
            theme="light"
            mode="inline"
            defaultSelectedKeys={['1']}
            items={[
              { key: '1', label: 'Dashboard' },
              { key: '2', label: 'Users' },
              { key: '3', label: 'Settings' },
            ]}
          />
        </Sider>
        <Layout>
          <Header style={{ padding: 0, background: colorBgContainer }} />
          <Content style={{ margin: '24px 16px 0' }}>
            <div
              style={{
                padding: 24,
                minHeight: 360,
                background: colorBgContainer,
              }}
            >
              <Card title="Welcome to Ant Design">
                <p>This is a sample card component</p>
                <Button type="primary">Primary Button</Button>
              </Card>
            </div>
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
