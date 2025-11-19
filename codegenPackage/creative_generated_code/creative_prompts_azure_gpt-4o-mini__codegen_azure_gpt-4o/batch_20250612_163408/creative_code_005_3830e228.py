"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Write a Gatsby.js component that adds an estimated reading time to blog posts.
Generated: DETERMINISTIC_3830e228239e6cdf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/components/EstimatedReadingTime.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * A React component to display the estimated reading time for blog posts.
 * @param {string} content - The blog post content to calculate reading time for.
 * @returns {JSX.Element} - The rendered estimated reading time.
 */
const EstimatedReadingTime = ({ content }) => {
  // Average reading speed: 200 words per minute
  const wordsPerMinute = 200;

  // Calculate word count (split by whitespace and filter out empty strings)
  const wordCount = content.split(/\s+/).filter((word) => word.length > 0).length;

  // Calculate reading time in minutes (rounded up to nearest whole number)
  const readingTime = Math.ceil(wordCount / wordsPerMinute);

  return (
    <div>
      {/* Render the estimated reading time */}
      <p>Estimated Reading Time: {readingTime} {readingTime === 1 ? 'minute' : 'minutes'}</p>
    </div>
  );
};

// Define PropTypes for type checking and validation
EstimatedReadingTime.propTypes = {
  content: PropTypes.string.isRequired, // Ensure content is a string and is required
};

export default EstimatedReadingTime;
```

To integrate this component:
1. Pass the blog post content to the `content` prop.
2. Import and use the `EstimatedReadingTime` component in your blog post template or layout.
