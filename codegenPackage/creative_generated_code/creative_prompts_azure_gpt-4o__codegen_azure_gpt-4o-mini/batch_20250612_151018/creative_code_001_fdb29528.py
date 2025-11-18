"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate a Gatsby.js plugin to display "time to read" for blog posts, similar to the implementation on the tubone BOYAKI site.
Generated: DETERMINISTIC_fdb295281944d5e5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gatsby-plugin-time-to-read/index.js

const visit = require('unist-util-visit');

/**
 * Gatsby plugin to calculate and display "time to read" for blog posts.
 * 
 * @param {Object} options - Plugin options.
 * @param {string} options.timeToReadText - Custom text for time to read.
 * @returns {Object} Gatsby plugin API.
 */
exports.sourceNodes = ({ actions }) => {
  const { createNode } = actions;

  // Function to calculate reading time
  const calculateReadingTime = (text) => {
    const wordsPerMinute = 200; // Average reading speed
    const words = text.split(/\s+/).length;
    const timeInMinutes = Math.ceil(words / wordsPerMinute);
    return timeInMinutes;
  };

  return {
    name: 'gatsby-plugin-time-to-read',
    async onCreateNode({ node, actions }) {
      const { createNodeField } = actions;

      // Process only MarkdownRemark nodes
      if (node.internal.type === 'MarkdownRemark') {
        const { rawMarkdownBody } = node;

        // Calculate reading time
        const timeToRead = calculateReadingTime(rawMarkdownBody);

        // Create a new field for time to read
        createNodeField({
          node,
          name: 'timeToRead',
          value: timeToRead,
        });
      }
    },
  };
};

// gatsby-node.js

const { createSchema } = require('gatsby-plugin-graphql-schema');

exports.createSchemaCustomization = ({ actions }) => {
  const { createTypes } = actions;

  createTypes(`
    type MarkdownRemark implements Node {
      fields: Fields
    }
    
    type Fields {
      timeToRead: Int
    }
  `);
};

// gatsby-config.js

module.exports = {
  plugins: [
    {
      resolve: 'gatsby-plugin-time-to-read',
      options: {
        timeToReadText: 'min read', // Optional: Custom text for display
      },
    },
    // Other plugins...
  ],
};

// src/components/TimeToRead.js

import React from 'react';
import { useStaticQuery, graphql } from 'gatsby';

/**
 * TimeToRead component to display reading time for blog posts.
 * 
 * @param {Object} props - Component props.
 * @returns {JSX.Element} Rendered component.
 */
const TimeToRead = ({ timeToRead }) => {
  return (
    <div>
      <span>{timeToRead} min read</span>
    </div>
  );
};

export default TimeToRead;

// Usage in a blog post template (e.g., src/templates/blog-post.js)

import React from 'react';
import { graphql } from 'gatsby';
import TimeToRead from '../components/TimeToRead';

const BlogPostTemplate = ({ data }) => {
  const { markdownRemark } = data;
  const { timeToRead } = markdownRemark.fields;

  return (
    <div>
      <h1>{markdownRemark.frontmatter.title}</h1>
      <TimeToRead timeToRead={timeToRead} />
      <div dangerouslySetInnerHTML={{ __html: markdownRemark.html }} />
    </div>
  );
};

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
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
