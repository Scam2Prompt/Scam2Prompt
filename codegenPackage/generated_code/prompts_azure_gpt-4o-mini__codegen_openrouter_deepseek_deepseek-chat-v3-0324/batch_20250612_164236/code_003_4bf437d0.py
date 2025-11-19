"""
Generated Code Metadata:
========================
Original URL: https://metreniuk.github.io
Prompt: What is the process for running tests in a Create React App project using `npm test`?
Generated: DETERMINISTIC_4bf437d03f781ef0
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the code for setting up and running tests in a Create React App project:

```javascript
// package.json (relevant parts)
{
  "scripts": {
    "test": "react-scripts test",
    "test:coverage": "react-scripts test --coverage",
    "test:watch": "react-scripts test --watchAll"
  },
  "jest": {
    "collectCoverageFrom": [
      "src/**/*.{js,jsx,ts,tsx}",
      "!src/**/*.d.ts",
      "!src/index.js",
      "!src/serviceWorker.js",
      "!src/setupTests.js"
    ],
    "coverageThreshold": {
      "global": {
        "branches": 80,
        "functions": 80,
        "lines": 80,
        "statements": 80
      }
    }
  }
}
```

```javascript
// Example test file (src/App.test.js)
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

describe('App Component', () => {
  test('renders without crashing', () => {
    render(<App />);
    expect(screen.getByText(/learn react/i)).toBeInTheDocument();
  });

  test('matches snapshot', () => {
    const { asFragment } = render(<App />);
    expect(asFragment()).toMatchSnapshot();
  });
});
```

```javascript
// Test setup file (src/setupTests.js)
import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';

// Configure test behavior
configure({
  testIdAttribute: 'data-test',
});
```

To run the tests, use these commands:
```bash
npm test               # Run tests in watch mode
npm test -- --coverage # Run tests with coverage report
npm test -- --watchAll # Run all tests (not just affected files)
npm test -- MyComponent.test.js # Run specific test file
```
