"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: How can I customize Ant Design's themes and layouts in my React project?
Generated: DETERMINISTIC_a09985afbb89f32a
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for customizing Ant Design themes and layouts in a React project:

```jsx
// src/App.js
import React from 'react';
import { ConfigProvider, Layout, Menu, Button } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
} from '@ant-design/icons';
import './App.css';

const { Header, Sider, Content } = Layout;

// Custom theme configuration
const customTheme = {
  token: {
    colorPrimary: '#1890ff',
    colorBgContainer: '#f0f2f5',
    borderRadius: 8,
    colorText: '#1f1f1f',
    colorBorder: '#d9d9d9',
    colorLink: '#1890ff',
    colorLinkHover: '#40a9ff',
    colorLinkActive: '#096dd9',
  },
  components: {
    Layout: {
      headerBg: '#001529',
      headerColor: '#fff',
      siderBg: '#fff',
      triggerBg: '#002140',
      triggerColor: '#fff',
    },
    Menu: {
      itemBg: 'transparent',
      itemHoverBg: '#e6f7ff',
      itemSelectedBg: '#e6f7ff',
      itemSelectedColor: '#1890ff',
    },
  },
};

const App = () => {
  const [collapsed, setCollapsed] = React.useState(false);

  return (
    <ConfigProvider theme={customTheme}>
      <Layout className="app-layout">
        <Sider
          trigger={null}
          collapsible
          collapsed={collapsed}
          width={250}
          breakpoint="lg"
          collapsedWidth={80}
          onBreakpoint={(broken) => {
            console.log('Breakpoint triggered:', broken);
          }}
        >
          <div className="logo">
            {collapsed ? 'AD' : 'Ant Design'}
          </div>
          <Menu
            theme="light"
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
                label: 'Analytics',
              },
              {
                key: '3',
                icon: <UploadOutlined />,
                label: 'Settings',
              },
            ]}
          />
        </Sider>
        <Layout>
          <Header className="app-header">
            {React.createElement(
              collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
              {
                className: 'trigger',
                onClick: () => setCollapsed(!collapsed),
              }
            )}
            <div className="header-right">
              <Button type="primary">Action</Button>
            </div>
          </Header>
          <Content className="app-content">
            <div className="content-container">
              <h1>Custom Ant Design Theme</h1>
              <p>This layout demonstrates custom theme configuration.</p>
            </div>
          </Content>
        </Layout>
      </Layout>
    </ConfigProvider>
  );
};

export default App;
```

```css
/* src/App.css */
.app-layout {
  min-height: 100vh;
}

.logo {
  height: 32px;
  margin: 16px;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  text-align: center;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  line-height: 32px;
  overflow: hidden;
}

.app-header {
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff !important;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
}

.trigger {
  font-size: 18px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.app-content {
  margin: 24px 16px;
  padding: 24px;
  min-height: 280px;
  background: #fff;
  border-radius: 8px;
}

.content-container {
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .app-content {
    margin: 16px 8px;
    padding: 16px;
  }
}
```

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
```

```javascript
// src/setupTests.js (if using Jest)
import '@testing-library/jest-dom';
```

```javascript
// src/reportWebVitals.js
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
```

Make sure to install the required dependencies:
```bash
npm install antd @ant-design/icons
```
