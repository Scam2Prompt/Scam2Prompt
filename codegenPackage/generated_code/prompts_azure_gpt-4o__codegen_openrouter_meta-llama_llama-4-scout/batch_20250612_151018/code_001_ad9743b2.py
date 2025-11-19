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
// src/components/time-to-read.js
import React from 'react';

/**
 * Calculates the time to read a blog post based on its text content.
 * 
 * @param {string} text - The text content of the blog post.
 * @param {number} [wordsPerMinute=200] - The average reading speed in words per minute.
 * @returns {string} The estimated time to read the blog post.
 */
function calculateTimeToRead(text, wordsPerMinute = 200) {
  const wordCount = text.trim().split(/\s+/).length;
  const timeToReadMinutes = Math.ceil(wordCount / wordsPerMinute);
  return `${timeToReadMinutes} min read`;
}

// Usage example:
// const text = "Your blog post text here...";
// const timeToRead = calculateTimeToRead(text);
// console.log(timeToRead); // Output: "X min read"

export default calculateTimeToRead;
```

```javascript
// src/templates/blog-post.js
import React from 'react';
import { graphql } from 'gatsby';
import calculateTimeToRead from '../components/time-to-read';

const BlogPostTemplate = ({ data }) => {
  const { markdownRemark } = data;
  const { frontmatter, html } = markdownRemark;
  const timeToRead = calculateTimeToRead(markdownRemark.rawMarkdownBody);

  return (
    <div>
      <h1>{frontmatter.title}</h1>
      <p>Posted on {frontmatter.date}</p>
      <p>{timeToRead}</p>
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </div>
  );
};

export const pageQuery = graphql`
  query($id: String!) {
    markdownRemark(id: { eq: $id }) {
      id
      rawMarkdownBody
      html
      frontmatter {
        date(formatString: "MMMM D, YYYY")
        title
      }
    }
  }
`;

export default BlogPostTemplate;
```

```javascript
// gatsby-node.js
const path = require('path');

exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions;

  const blogPostTemplate = path.resolve(`src/templates/blog-post.js`);

  const result = await graphql(`
    query {
      allMarkdownRemark {
        edges {
          node {
            id
            fields {
              slug
            }
          }
        }
      }
    }
  `);

  if (result.errors) {
    throw result.errors;
  }

  result.data.allMarkdownRemark.edges.forEach(edge => {
    createPage({
      path: edge.node.fields.slug,
      component: blogPostTemplate,
      context: {
        id: edge.node.id,
      },
    });
  });
};
```

```javascript
// src/utils/typography.js
import Typography from 'typography';

const typography = new Typography({
  baseFontSize: '18px',
  baseLineHeight: 1.5,
  headerFontFamily: ['Arial', 'sans-serif'],
  bodyFontFamily: ['Arial', 'sans-serif'],
});

export default typography;
```

```css
/* src/styles/global.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.blog-post {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```
