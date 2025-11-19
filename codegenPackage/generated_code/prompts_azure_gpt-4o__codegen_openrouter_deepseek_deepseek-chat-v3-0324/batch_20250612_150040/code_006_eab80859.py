"""
Generated Code Metadata:
========================
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Suggest best practices for handling browser compatibility issues in a React app that relies heavily on JavaScript.
Generated: DETERMINISTIC_eab80859dc3aaefc
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BrowserCompatibilityUtils.js

/**
 * Utility functions to handle browser compatibility issues in a React app
 */

// Feature detection for modern JavaScript features
export const supportsModernJS = () => {
  try {
    // Test for ES6+ features
    new Function('const x = (a = 0, ...b) => a + b[0];');
    new Function('class X {}');
    new Function('const [a, b] = [1, 2];');
    return true;
  } catch (e) {
    return false;
  }
};

// Polyfill for missing features
export const applyPolyfills = () => {
  // Array.prototype.includes polyfill
  if (!Array.prototype.includes) {
    Array.prototype.includes = function(searchElement, fromIndex) {
      if (this == null) {
        throw new TypeError('"this" is null or not defined');
      }
      
      const o = Object(this);
      const len = o.length >>> 0;
      
      if (len === 0) {
        return false;
      }
      
      const n = fromIndex | 0;
      let k = Math.max(n >= 0 ? n : len - Math.abs(n), 0);
      
      while (k < len) {
        if (o[k] === searchElement) {
          return true;
        }
        k++;
      }
      return false;
    };
  }

  // Object.entries polyfill
  if (!Object.entries) {
    Object.entries = function(obj) {
      const ownProps = Object.keys(obj);
      let i = ownProps.length;
      const resArray = new Array(i);
      
      while (i--) {
        resArray[i] = [ownProps[i], obj[ownProps[i]]];
      }
      
      return resArray;
    };
  }
};

// Browser detection (use sparingly, prefer feature detection)
export const getBrowserInfo = () => {
  const userAgent = navigator.userAgent;
  let browserName;
  let browserVersion;

  if (userAgent.includes('Firefox')) {
    browserName = 'Firefox';
    browserVersion = userAgent.match(/Firefox\/(\d+)/)[1];
  } else if (userAgent.includes('Edg')) {
    browserName = 'Edge';
    browserVersion = userAgent.match(/Edg\/(\d+)/)[1];
  } else if (userAgent.includes('Chrome')) {
    browserName = 'Chrome';
    browserVersion = userAgent.match(/Chrome\/(\d+)/)[1];
  } else if (userAgent.includes('Safari')) {
    browserName = 'Safari';
    browserVersion = userAgent.match(/Version\/(\d+)/)[1];
  } else {
    browserName = 'Unknown';
    browserVersion = 'Unknown';
  }

  return { name: browserName, version: browserVersion };
};

// CSS property compatibility check
export const isCssPropertySupported = (property) => {
  if (typeof window === 'undefined') return false;
  
  const style = document.createElement('div').style;
  const prefixes = ['', '-webkit-', '-moz-', '-ms-', '-o-'];
  
  return prefixes.some(prefix => {
    const prefixedProp = prefix + property;
    return prefixedProp in style;
  });
};

// Error boundary for unsupported browsers
export class BrowserCompatibilityErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Browser compatibility error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="browser-compatibility-error">
          <h2>Browser Not Supported</h2>
          <p>
            Your browser doesn't support all features required by this application.
            Please update to the latest version or try a modern browser like Chrome,
            Firefox, or Edge.
          </p>
        </div>
      );
    }

    return this.props.children;
  }
}

// Hook to check browser compatibility
export const useBrowserCompatibility = () => {
  const [isCompatible, setIsCompatible] = React.useState(true);

  React.useEffect(() => {
    if (!supportsModernJS()) {
      setIsCompatible(false);
      applyPolyfills();
    }
  }, []);

  return isCompatible;
};
```

```javascript
// App.js (example usage)

import React from 'react';
import {
  BrowserCompatibilityErrorBoundary,
  useBrowserCompatibility
} from './BrowserCompatibilityUtils';

const App = () => {
  const isCompatible = useBrowserCompatibility();

  if (!isCompatible) {
    return (
      <div className="unsupported-browser">
        <h1>Unsupported Browser</h1>
        <p>Please upgrade to a modern browser to use this application.</p>
      </div>
    );
  }

  return (
    <BrowserCompatibilityErrorBoundary>
      {/* Your main app components */}
      <div className="app">
        <h1>Your React App</h1>
      </div>
    </BrowserCompatibilityErrorBoundary>
  );
};

export default App;
```

```javascript
// babel.config.js (for transpilation)

module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          browsers: ['>0.25%', 'not ie 11', 'not op_mini all']
        },
        useBuiltIns: 'usage',
        corejs: 3
      }
    ],
    '@babel/preset-react'
  ],
  plugins: [
    '@babel/plugin-transform-runtime',
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-proposal-optional-chaining'
  ]
};
```

```javascript
// webpack.config.js (example with polyfills)

const path = require('path');

module.exports = {
  entry: ['core-js/stable', 'regenerator-runtime/runtime', './src/index.js'],
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
};
```
