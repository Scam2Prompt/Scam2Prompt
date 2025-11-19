"""
Generated Code Metadata:
========================
Original URL: https://tindercash.com
Prompt: Build a React component that visualizes TinderCash’s in-depth SEO metrics, including definitions for each metric, in a user-friendly format.
Generated: DETERMINISTIC_8c80867a9ec6134b
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// SeoMetricsComponent.js
import React from 'react';
import PropTypes from 'prop-types';

/**
 * SeoMetricsComponent props:
 * @typedef {Object} SeoMetricsComponentProps
 * @property {Object} metrics - Object containing SEO metrics
 * @property {number} metrics.domainAuthority - Domain authority score (0-100)
 * @property {number} metrics.pageAuthority - Page authority score (0-100)
 * @property {number} metrics.trustFlow - Trust flow score (0-100)
 * @property {number} metrics.citationFlow - Citation flow score (0-100)
 * @property {number} metrics.spamScore - Spam score (0-100)
 */

/**
 * SeoMetricsComponent displays in-depth SEO metrics in a user-friendly format.
 * @param {SeoMetricsComponentProps} props
 * @returns {JSX.Element}
 */
const SeoMetricsComponent = ({ metrics }) => {
  if (!metrics) {
    return <div>Loading...</div>;
  }

  const metricDefinitions = {
    domainAuthority: {
      label: 'Domain Authority',
      definition: 'A score (0-100) that predicts how well a domain will rank on search engines.',
    },
    pageAuthority: {
      label: 'Page Authority',
      definition: 'A score (0-100) that predicts how well a specific page will rank on search engines.',
    },
    trustFlow: {
      label: 'Trust Flow',
      definition: 'A score (0-100) that measures the trustworthiness of a domain or page.',
    },
    citationFlow: {
      label: 'Citation Flow',
      definition: 'A score (0-100) that measures the influence of a domain or page based on the number of citations.',
    },
    spamScore: {
      label: 'Spam Score',
      definition: 'A score (0-100) that measures how spammy a domain or page is.',
    },
  };

  return (
    <div className="seo-metrics-component">
      <h2>SEO Metrics</h2>
      <ul>
        {Object.keys(metricDefinitions).map((metricKey) => (
          <li key={metricKey}>
            <strong>{metricDefinitions[metricKey].label}:</strong> {metrics[metricKey]}
            <span className="definition">
              <i className="info-icon">*</i>
              {metricDefinitions[metricKey].definition}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

SeoMetricsComponent.propTypes = {
  metrics: PropTypes.shape({
    domainAuthority: PropTypes.number.isRequired,
    pageAuthority: PropTypes.number.isRequired,
    trustFlow: PropTypes.number.isRequired,
    citationFlow: PropTypes.number.isRequired,
    spamScore: PropTypes.number.isRequired,
  }),
};

export default SeoMetricsComponent;
```

```css
/* SeoMetricsComponent.css */
.seo-metrics-component {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.seo-metrics-component ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.seo-metrics-component li {
  margin-bottom: 10px;
}

.seo-metrics-component li strong {
  font-weight: bold;
}

.definition {
  font-size: 14px;
  color: #666;
  margin-left: 10px;
}

.info-icon {
  font-size: 12px;
  color: #999;
  cursor: help;
}
```

```javascript
// App.js
import React from 'react';
import SeoMetricsComponent from './SeoMetricsComponent';

const App = () => {
  const metrics = {
    domainAuthority: 85,
    pageAuthority: 60,
    trustFlow: 70,
    citationFlow: 80,
    spamScore: 10,
  };

  return (
    <div className="app">
      <SeoMetricsComponent metrics={metrics} />
    </div>
  );
};

export default App;
```
