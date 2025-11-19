"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate a Gatsby.js plugin to display "time to read" for blog posts, similar to the implementation on the tubone BOYAKI site.
Generated: DETERMINISTIC_fdb295281944d5e5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code for the Gatsby.js plugin:
```javascript
/**
 * Gatsby plugin to display "time to read" for blog posts
 *
 * @author [Your Name]
 */

const _ = require('lodash');
const readingTime = require('reading-time');

const pluginName = 'gatsby-plugin-time-to-read';

/**
 * Calculate reading time for a blog post
 *
 * @param {string} text - Text content of the blog post
 * @returns {object} - Reading time stats (minutes, words, etc.)
 */
function calculateReadingTime(text) {
  return readingTime(text);
}

/**
 * Gatsby plugin API
 *
 * @param {object} gatsby - Gatsby API object
 * @param {object} options - Plugin options
 */
exports.onCreateNode = async ({ node, getNode, actions }, options) => {
  const { createNodeField } = actions;

  if (node.internal.type === 'MarkdownRemark') {
    const text = node.rawMarkdownBody;
    const readingTimeStats = calculateReadingTime(text);

    createNodeField({
      node,
      name: 'timeToRead',
      value: readingTimeStats.minutes,
    });

    createNodeField({
      node,
      name: 'readingTimeStats',
      value: readingTimeStats,
    });
  }
};

/**
 * Add "time to read" to blog post pages
 *
 * @param {object} gatsby - Gatsby API object
 */
exports.onCreatePage = async ({ page, actions }, options) => {
  const { createPage } = actions;

  if (page.path.includes('/blog/')) {
    const readingTimeStats = page.context.readingTimeStats;
    const timeToRead = readingTimeStats.minutes;

    createPage({
      ...page,
      context: {
        ...page.context,
        timeToRead,
      },
    });
  }
};

/**
 * Add "time to read" to blog post template
 *
 * @param {object} gatsby - Gatsby API object
 */
exports.onRenderAST = async ({ ast, actions }, options) => {
  const { createSchemaCustomization } = actions;

  createSchemaCustomization({
    type: 'BlogPost',
    fields: {
      timeToRead: 'Float',
      readingTimeStats: 'JSON',
    },
  });
};
```
And here is an example usage in a Gatsby page template:
```javascript
import React from 'react';
import { graphql } from 'gatsby';

const BlogPostTemplate = ({ data }) => {
  const { markdownRemark } = data;
  const { timeToRead } = markdownRemark.fields;

  return (
    <div>
      <h1>{markdownRemark.frontmatter.title}</h1>
      <p>Time to read: {timeToRead} minutes</p>
      <div dangerouslySetInnerHTML={{ __html: markdownRemark.html }} />
    </div>
  );
};

export const query = graphql`
  query($path: String!) {
    markdownRemark(frontmatter: { path: { eq: $path } }) {
      html
      frontmatter {
        title
      }
      fields {
        timeToRead
      }
    }
  }
`;

export default BlogPostTemplate;
```
And here is an example usage in a Gatsby blog post page:
```javascript
import React from 'react';
import BlogPostTemplate from '../templates/blog-post';

const BlogPostPage = () => {
  return <BlogPostTemplate />;
};

export default BlogPostPage;
```
You will also need to add the following to your `gatsby-config.js` file:
```javascript
module.exports = {
  // ...
  plugins: [
    // ...
    {
      resolve: 'gatsby-plugin-time-to-read',
      options: {},
    },
  ],
};
```
