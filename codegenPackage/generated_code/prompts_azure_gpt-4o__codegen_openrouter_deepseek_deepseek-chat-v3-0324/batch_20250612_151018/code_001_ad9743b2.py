"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Generate code for adding a "time to read" feature to a Gatsby.js blog, similar to the implementation discussed on the "tubone BOYAKI" site.
Generated: DETERMINISTIC_ad9743b20c1427f9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/utils/calculateReadingTime.js
/**
 * Calculates the estimated reading time for a given text.
 * @param {string} text - The text content to analyze.
 * @param {number} [wordsPerMinute=200] - Average reading speed (words per minute).
 * @returns {Object} An object containing minutes and text representation.
 */
export const calculateReadingTime = (text, wordsPerMinute = 200) => {
  if (!text || typeof text !== 'string') {
    return {
      minutes: 0,
      text: '0 min read'
    };
  }

  // Remove HTML tags if present
  const cleanText = text.replace(/<[^>]*>/g, '');
  const wordCount = cleanText.trim().split(/\s+/).length;
  const minutes = Math.ceil(wordCount / wordsPerMinute);

  return {
    minutes,
    text: `${minutes} min read`
  };
};
```

```javascript
// src/templates/blog-post.js
import React from 'react';
import { graphql } from 'gatsby';
import { calculateReadingTime } from '../utils/calculateReadingTime';

const BlogPostTemplate = ({ data }) => {
  const post = data.markdownRemark;
  const { minutes, text } = calculateReadingTime(post.html);

  return (
    <article>
      <header>
        <h1>{post.frontmatter.title}</h1>
        <p>{post.frontmatter.date}</p>
        <p>{text}</p>
      </header>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </article>
  );
};

export default BlogPostTemplate;

export const pageQuery = graphql`
  query BlogPostBySlug($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        date(formatString: "MMMM DD, YYYY")
      }
    }
  }
`;
```

```javascript
// gatsby-node.js
const { calculateReadingTime } = require('./src/utils/calculateReadingTime');

exports.onCreateNode = ({ node, actions }) => {
  const { createNodeField } = actions;

  if (node.internal.type === 'MarkdownRemark') {
    const readingTime = calculateReadingTime(node.html);
    createNodeField({
      node,
      name: 'readingTime',
      value: readingTime.text
    });
  }
};
```

```javascript
// src/components/PostMeta.js
import React from 'react';
import PropTypes from 'prop-types';

const PostMeta = ({ date, readingTime }) => (
  <div className="post-meta">
    <span>{date}</span>
    <span> · </span>
    <span>{readingTime}</span>
  </div>
);

PostMeta.propTypes = {
  date: PropTypes.string.isRequired,
  readingTime: PropTypes.string.isRequired
};

export default PostMeta;
```

```javascript
// src/templates/blog-post.js (updated with PostMeta component)
import React from 'react';
import { graphql } from 'gatsby';
import PostMeta from '../components/PostMeta';

const BlogPostTemplate = ({ data }) => {
  const post = data.markdownRemark;

  return (
    <article>
      <header>
        <h1>{post.frontmatter.title}</h1>
        <PostMeta 
          date={post.frontmatter.date} 
          readingTime={post.fields.readingTime} 
        />
      </header>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </article>
  );
};

export default BlogPostTemplate;

export const pageQuery = graphql`
  query BlogPostBySlug($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        date(formatString: "MMMM DD, YYYY")
      }
      fields {
        readingTime
      }
    }
  }
`;
```
