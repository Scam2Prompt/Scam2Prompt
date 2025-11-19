"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Write a Gatsby.js component that adds an estimated reading time to blog posts.
Generated: DETERMINISTIC_3830e228239e6cdf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
/**
 * Estimated Reading Time component for Gatsby.js blog posts.
 *
 * @param {object} props
 * @param {string} props.text - The text content of the blog post.
 * @param {number} [props.wordsPerMinute=200] - The average reading speed in words per minute.
 * @returns {JSX.Element} The estimated reading time component.
 */
import React from 'react';

const EstimatedReadingTime = ({ text, wordsPerMinute = 200 }) => {
  // Calculate the number of words in the text
  const wordCount = text.split(' ').length;

  // Calculate the estimated reading time in minutes
  const readingTime = wordCount / wordsPerMinute;

  // Format the reading time to a human-readable string
  const formattedReadingTime = Math.round(readingTime * 10) / 10;

  return (
    <span>
      Estimated reading time: {formattedReadingTime}{' '}
      {formattedReadingTime === 1 ? 'minute' : 'minutes'}
    </span>
  );
};

export default EstimatedReadingTime;
```

```jsx
/**
 * Example usage in a Gatsby.js blog post template.
 *
 * @param {object} data
 * @param {string} data.markdownRemark.html - The HTML content of the blog post.
 * @param {string} data.markdownRemark.rawMarkdownBody - The raw Markdown content of the blog post.
 */
import React from 'react';
import EstimatedReadingTime from './EstimatedReadingTime';

const BlogPostTemplate = ({ data }) => {
  const { markdownRemark } = data;
  const { html, rawMarkdownBody } = markdownRemark;

  return (
    <div>
      <h1>{markdownRemark.frontmatter.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: html }} />
      <p>
        <EstimatedReadingTime text={rawMarkdownBody} />
      </p>
    </div>
  );
};

export const query = graphql`
  query($id: String!) {
    markdownRemark(id: { eq: $id }) {
      html
      rawMarkdownBody
      frontmatter {
        title
      }
    }
  }
`;

export default BlogPostTemplate;
```
