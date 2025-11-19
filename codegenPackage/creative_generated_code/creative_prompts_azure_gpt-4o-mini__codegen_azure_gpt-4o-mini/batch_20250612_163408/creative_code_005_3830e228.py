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
import React from 'react';
import PropTypes from 'prop-types';

/**
 * Calculates the estimated reading time based on the word count.
 * @param {number} wordCount - The total number of words in the content.
 * @returns {string} - The estimated reading time in minutes.
 */
const calculateReadingTime = (wordCount) => {
  const wordsPerMinute = 200; // Average reading speed
  const timeInMinutes = Math.ceil(wordCount / wordsPerMinute);
  return timeInMinutes === 1 ? `${timeInMinutes} minute` : `${timeInMinutes} minutes`;
};

/**
 * ReadingTime component displays the estimated reading time for a blog post.
 * @param {Object} props - The component props.
 * @param {string} props.content - The content of the blog post.
 */
const ReadingTime = ({ content }) => {
  if (!content || typeof content !== 'string') {
    console.error('Invalid content provided to ReadingTime component');
    return null;
  }

  // Calculate the word count by splitting the content string
  const wordCount = content.split(/\s+/).filter(word => word.length > 0).length;
  
  // Calculate reading time
  const readingTime = calculateReadingTime(wordCount);

  return (
    <div className="reading-time">
      <p>Estimated Reading Time: {readingTime}</p>
    </div>
  );
};

// PropTypes for validation
ReadingTime.propTypes = {
  content: PropTypes.string.isRequired,
};

export default ReadingTime;
```
