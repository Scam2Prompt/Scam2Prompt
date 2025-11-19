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
// src/components/TimeToRead.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * TimeToRead component calculates and displays the estimated reading time
 * for a given text based on an average reading speed.
 *
 * @param {Object} props - Component properties
 * @param {string} props.text - The text content for which to calculate reading time
 * @returns {JSX.Element} The rendered component
 */
const TimeToRead = ({ text }) => {
  // Average reading speed in words per minute
  const wordsPerMinute = 200;

  // Function to calculate reading time
  const calculateReadingTime = (text) => {
    if (!text) return 0; // Return 0 if text is empty
    const words = text.split(/\s+/).filter(Boolean).length; // Split text into words
    return Math.ceil(words / wordsPerMinute); // Calculate and round up reading time
  };

  // Calculate the reading time
  const readingTime = calculateReadingTime(text);

  return (
    <div className="time-to-read">
      {readingTime > 0 ? `${readingTime} min read` : 'Reading time not available'}
    </div>
  );
};

// Prop validation
TimeToRead.propTypes = {
  text: PropTypes.string.isRequired,
};

export default TimeToRead;
```

```javascript
// src/templates/blog-post.js

import React from 'react';
import { graphql } from 'gatsby';
import TimeToRead from '../components/TimeToRead';

/**
 * BlogPost template component
 *
 * @param {Object} props - Component properties
 * @param {Object} props.data - GraphQL data for the blog post
 * @returns {JSX.Element} The rendered blog post
 */
const BlogPost = ({ data }) => {
  const post = data.markdownRemark;

  return (
    <div className="blog-post">
      <h1>{post.frontmatter.title}</h1>
      <TimeToRead text={post.rawMarkdownBody} />
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </div>
  );
};

// GraphQL query to fetch blog post data
export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      frontmatter {
        title
      }
      rawMarkdownBody
      html
    }
  }
`;

export default BlogPost;
```

```css
/* src/styles/global.css */

/* Styles for the TimeToRead component */
.time-to-read {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 1em;
}
```

```javascript
// gatsby-config.js

module.exports = {
  siteMetadata: {
    title: 'Your Blog Title',
    description: 'Your Blog Description',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'posts',
        path: `${__dirname}/src/posts/`,
      },
    },
    'gatsby-transformer-remark',
    // Add other plugins as needed
  ],
};
```

```javascript
// src/pages/index.js

import React from 'react';
import { graphql } from 'gatsby';

/**
 * Index page component that lists all blog posts
 *
 * @param {Object} props - Component properties
 * @param {Object} props.data - GraphQL data for the blog posts
 * @returns {JSX.Element} The rendered index page
 */
const IndexPage = ({ data }) => {
  const posts = data.allMarkdownRemark.nodes;

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.fields.slug}>
            <h2>
              <a href={post.fields.slug}>{post.frontmatter.title}</a>
            </h2>
          </li>
        ))}
      </ul>
    </div>
  );
};

// GraphQL query to fetch all blog posts
export const query = graphql`
  query {
    allMarkdownRemark {
      nodes {
        frontmatter {
          title
        }
        fields {
          slug
        }
      }
    }
  }
`;

export default IndexPage;
```

This code provides a complete implementation of a "time to read" feature for a Gatsby.js blog, including components, styles, and GraphQL queries.
