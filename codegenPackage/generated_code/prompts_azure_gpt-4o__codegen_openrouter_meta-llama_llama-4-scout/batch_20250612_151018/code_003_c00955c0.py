"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Write code to customize the theme of an Ant Design application using the library's configuration options.
Generated: DETERMINISTIC_c00955c0a07f2811
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { ConfigProvider } from 'antd';
import enUS from 'antd/locale/en_US';
import zhCN from 'antd/locale/zh_CN';

// Define a function to customize the theme
function customizeTheme(config) {
  // Check if config is valid
  if (!config) {
    throw new Error('Config is required');
  }

  // Check if theme is specified
  if (!config.theme) {
    throw new Error('Theme is required');
  }

  // Define available themes
  const themes = {
    light: {
      primaryColor: '#1890ff',
    },
    dark: {
      primaryColor: '#141414',
    },
  };

  // Check if theme is valid
  if (!themes[config.theme]) {
    throw new Error(`Invalid theme: ${config.theme}`);
  }

  // Customize the theme
  const customize = {
    // Customize the primary color
    primaryColor: themes[config.theme].primaryColor,
  };

  return customize;
}

// Define a function to configure Ant Design
function configureAntDesign(config) {
  // Check if config is valid
  if (!config) {
    throw new Error('Config is required');
  }

  // Configure locale
  let locale;
  switch (config.locale) {
    case 'en-US':
      locale = enUS;
      break;
    case 'zh-CN':
      locale = zhCN;
      break;
    default:
      throw new Error(`Invalid locale: ${config.locale}`);
  }

  // Configure theme
  const customize = customizeTheme(config);

  // Return the configuration
  return {
    locale,
    theme: customize,
  };
}

// Usage example
const config = {
  theme: 'dark',
  locale: 'en-US',
};

const antDesignConfig = configureAntDesign(config);

const App = () => {
  return (
    <ConfigProvider
      locale={antDesignConfig.locale}
      theme={antDesignConfig.theme}
    >
      {/* Your Ant Design application */}
    </ConfigProvider>
  );
};

export default App;
```
