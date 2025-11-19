"""
Generated Code Metadata:
========================
Original URL: https://manta.zone
Prompt: How can I implement a basic copyright notice for my web application, similar to the one on manta.zone?
Generated: DETERMINISTIC_77d6d866761c34f8
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a basic copyright notice component in a web application:

```html
<!-- CopyrightNotice.vue -->
<template>
  <footer class="copyright-notice">
    <div class="container">
      <p class="copyright-text">
        &copy; {{ currentYear }} {{ companyName }}. All rights reserved.
        <span v-if="showVersion" class="version">v{{ appVersion }}</span>
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'CopyrightNotice',
  props: {
    companyName: {
      type: String,
      required: true,
      default: 'Your Company'
    },
    showVersion: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      appVersion: process.env.VUE_APP_VERSION || '1.0.0'
    }
  },
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
.copyright-notice {
  padding: 1rem 0;
  text-align: center;
  font-size: 0.875rem;
  color: #666;
  background-color: transparent;
}

.copyright-notice .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.version {
  margin-left: 0.5rem;
  font-weight: 600;
}
</style>
```

For a React implementation:

```jsx
// CopyrightNotice.jsx
import React from 'react';
import PropTypes from 'prop-types';

const CopyrightNotice = ({ companyName, showVersion }) => {
  const currentYear = new Date().getFullYear();
  const appVersion = process.env.REACT_APP_VERSION || '1.0.0';

  return (
    <footer className="copyright-notice">
      <div className="container">
        <p className="copyright-text">
          &copy; {currentYear} {companyName}. All rights reserved.
          {showVersion && <span className="version">v{appVersion}</span>}
        </p>
      </div>
    </footer>
  );
};

CopyrightNotice.propTypes = {
  companyName: PropTypes.string.isRequired,
  showVersion: PropTypes.bool
};

CopyrightNotice.defaultProps = {
  companyName: 'Your Company',
  showVersion: false
};

export default CopyrightNotice;

// CopyrightNotice.css
.copyright-notice {
  padding: 1rem 0;
  text-align: center;
  font-size: 0.875rem;
  color: #666;
  background-color: transparent;
}

.copyright-notice .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.version {
  margin-left: 0.5rem;
  font-weight: 600;
}
```

For a plain HTML/CSS/JS implementation:

```html
<!-- copyright-notice.html -->
<footer class="copyright-notice">
  <div class="container">
    <p class="copyright-text">
      &copy; <span id="current-year"></span> <span id="company-name">Your Company</span>. All rights reserved.
      <span id="version" class="version"></span>
    </p>
  </div>
</footer>

<style>
.copyright-notice {
  padding: 1rem 0;
  text-align: center;
  font-size: 0.875rem;
  color: #666;
  background-color: transparent;
}

.copyright-notice .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.version {
  margin-left: 0.5rem;
  font-weight: 600;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  try {
    // Set current year
    document.getElementById('current-year').textContent = new Date().getFullYear();
    
    // Optional: Set company name from config
    const config = window.appConfig || {};
    if (config.companyName) {
      document.getElementById('company-name').textContent = config.companyName;
    }
    
    // Optional: Show version if enabled
    if (config.showVersion) {
      const version = config.appVersion || '1.0.0';
      document.getElementById('version').textContent = `v${version}`;
    } else {
      document.getElementById('version').style.display = 'none';
    }
  } catch (error) {
    console.error('Error initializing copyright notice:', error);
  }
});
</script>
```
