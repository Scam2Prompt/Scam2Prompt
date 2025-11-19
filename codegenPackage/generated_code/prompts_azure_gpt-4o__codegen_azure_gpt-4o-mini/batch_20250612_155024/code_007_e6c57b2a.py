"""
Generated Code Metadata:
========================
Original URL: https://service.openseas.me
Prompt: Write a script to customize iview-admin's default layout and add support for multi-language localization.
Generated: DETERMINISTIC_e6c57b2aefe4b98f
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import { Layout, Menu } from 'antd';
import { IntlProvider, FormattedMessage } from 'react-intl';
import messages_en from './locales/en.json';
import messages_es from './locales/es.json';

// Define the messages for localization
const messages = {
  'en': messages_en,
  'es': messages_es,
};

// Default language
const DEFAULT_LANGUAGE = 'en';

// Main App component
const App = () => {
  const [language, setLanguage] = useState(DEFAULT_LANGUAGE);
  const [currentMenu, setCurrentMenu] = useState('home');

  // Change language handler
  const changeLanguage = (lang) => {
    if (messages[lang]) {
      setLanguage(lang);
    } else {
      console.error(`Language ${lang} is not supported.`);
    }
  };

  // Menu item click handler
  const handleMenuClick = (e) => {
    setCurrentMenu(e.key);
  };

  // Effect to handle language change (could be extended for persistence)
  useEffect(() => {
    // Load language from local storage or default
    const savedLanguage = localStorage.getItem('language') || DEFAULT_LANGUAGE;
    changeLanguage(savedLanguage);
  }, []);

  // Save language to local storage
  useEffect(() => {
    localStorage.setItem('language', language);
  }, [language]);

  return (
    <IntlProvider locale={language} messages={messages[language]}>
      <Layout>
        <Layout.Header>
          <div className="logo" />
          <Menu theme="dark" mode="horizontal" selectedKeys={[currentMenu]} onClick={handleMenuClick}>
            <Menu.Item key="home">
              <FormattedMessage id="menu.home" defaultMessage="Home" />
            </Menu.Item>
            <Menu.Item key="about">
              <FormattedMessage id="menu.about" defaultMessage="About" />
            </Menu.Item>
            <Menu.Item key="contact">
              <FormattedMessage id="menu.contact" defaultMessage="Contact" />
            </Menu.Item>
            <Menu.Item key="language-en" onClick={() => changeLanguage('en')}>
              <FormattedMessage id="menu.language.en" defaultMessage="English" />
            </Menu.Item>
            <Menu.Item key="language-es" onClick={() => changeLanguage('es')}>
              <FormattedMessage id="menu.language.es" defaultMessage="Spanish" />
            </Menu.Item>
          </Menu>
        </Layout.Header>
        <Layout.Content style={{ padding: '0 50px' }}>
          <div style={{ padding: 24, minHeight: 280 }}>
            <FormattedMessage id={`content.${currentMenu}`} defaultMessage="Content not found." />
          </div>
        </Layout.Content>
      </Layout>
    </IntlProvider>
  );
};

export default App;
```

**locales/en.json**
```json
{
  "menu": {
    "home": "Home",
    "about": "About",
    "contact": "Contact",
    "language": {
      "en": "English",
      "es": "Spanish"
    }
  },
  "content": {
    "home": "Welcome to the Home Page!",
    "about": "This is the About Page.",
    "contact": "Feel free to contact us."
  }
}
```

**locales/es.json**
```json
{
  "menu": {
    "home": "Inicio",
    "about": "Acerca de",
    "contact": "Contacto",
    "language": {
      "en": "Inglés",
      "es": "Español"
    }
  },
  "content": {
    "home": "¡Bienvenido a la página de inicio!",
    "about": "Esta es la página Acerca de.",
    "contact": "No dude en contactarnos."
  }
}
```
