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

```javascript
// gatsby-node.js
const { timeToRead } = require('reading-time');

exports.onCreateNode = ({ node, actions }) => {
  const { createNodeField } = actions;

  // Only process MarkdownRemark nodes
  if (node.internal.type === 'MarkdownRemark') {
    const text = node.rawMarkdownBody || '';
    const readTime = timeToRead(text);

    createNodeField({
      node,
      name: 'timeToRead',
      value: readTime
    });
  }
};

// gatsby-config.js
module.exports = {
  plugins: [
    // Other plugins...
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          // Other remark plugins...
          {
            resolve: `gatsby-remark-reading-time`,
            options: {
              // Optional: Custom words per minute (default: 200)
              wordsPerMinute: 200,
            },
          },
        ],
      },
    },
  ],
};

// src/components/TimeToRead.js
import React from 'react';
import PropTypes from 'prop-types';

const TimeToRead = ({ time }) => {
  return (
    <span className="time-to-read">
      ⏱️ {time} min read
    </span>
  );
};

TimeToRead.propTypes = {
  time: PropTypes.number.isRequired,
};

export default TimeToRead;

// src/templates/blog-post.js (example usage)
import React from 'react';
import { graphql } from 'gatsby';
import TimeToRead from '../components/TimeToRead';

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        date(formatString: "MMMM DD, YYYY")
      }
      fields {
        timeToRead
      }
    }
  }
`;

const BlogPost = ({ data }) => {
  const post = data.markdownRemark;

  return (
    <div className="blog-post">
      <h1>{post.frontmatter.title}</h1>
      <p>{post.frontmatter.date}</p>
      <TimeToRead time={post.fields.timeToRead} />
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </div>
  );
};

export default BlogPost;

// package.json (relevant dependencies)
{
  "dependencies": {
    "gatsby": "^4.0.0",
    "gatsby-transformer-remark": "^5.0.0",
    "reading-time": "^1.5.0",
    "react": "^17.0.0",
    "react-dom": "^17.0.0"
  }
}
```
