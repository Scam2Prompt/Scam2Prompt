"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Generate code for adding a "time to read" feature to a Gatsby.js blog, similar to the implementation discussed on the "tubone BOYAKI" site.
Generated: DETERMINISTIC_ad9743b20c1427f9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gatsby-node.js

const path = require('path');
const fs = require('fs');

/**
 * Function to calculate the estimated reading time based on word count.
 * @param {string} content - The content of the blog post.
 * @returns {number} - Estimated reading time in minutes.
 */
const calculateReadingTime = (content) => {
  const wordsPerMinute = 200; // Average reading speed
  const words = content.split(/\s+/).filter(Boolean).length; // Split content into words and count
  return Math.ceil(words / wordsPerMinute); // Return rounded up reading time
};

/**
 * Create pages for each markdown file.
 * @param {object} actions - Gatsby actions object for creating pages.
 * @param {object} graphql - Gatsby's GraphQL query function.
 */
exports.createPages = async ({ actions, graphql }) => {
  const { createPage } = actions;

  // GraphQL query to get all markdown files
  const result = await graphql(`
    {
      allMarkdownRemark {
        edges {
          node {
            frontmatter {
              path
              content
            }
          }
        }
      }
    }
  `);

  // Handle errors in GraphQL query
  if (result.errors) {
    console.error('Error fetching markdown data:', result.errors);
    throw new Error('Failed to fetch markdown data');
  }

  // Create a page for each markdown file
  result.data.allMarkdownRemark.edges.forEach(({ node }) => {
    const readingTime = calculateReadingTime(node.frontmatter.content || "");

    createPage({
      path: node.frontmatter.path,
      component: path.resolve(`./src/templates/blog-post.js`),
      context: {
        readingTime, // Pass reading time to the page context
      },
    });
  });
};

// src/templates/blog-post.js

import React from 'react';
import { graphql } from 'gatsby';

/**
 * BlogPost component to render the individual blog post.
 * @param {object} props - Component properties containing data and context.
 */
const BlogPost = ({ data, pageContext }) => {
  const { markdownRemark } = data;
  const { frontmatter, html } = markdownRemark;
  const { readingTime } = pageContext; // Destructure reading time from context

  return (
    <div>
      <h1>{frontmatter.title}</h1>
      <div>
        <p>Estimated reading time: {readingTime} minute(s)</p>
      </div>
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </div>
  );
};

/**
 * GraphQL query to fetch markdown data for the blog post.
 * @param {object} graphql - Gatsby's GraphQL query function.
 * @returns {object} - The GraphQL query result.
 */
export const query = graphql`
  query($path: String!) {
    markdownRemark(frontmatter: { path: { eq: $path } }) {
      html
      frontmatter {
        title
        content
      }
    }
  }
`;

export default BlogPost;
```

This code includes two main parts: the first part contains the `gatsby-node.js`, which handles creating pages and calculating reading time, while the second part is the `blog-post.js` template that displays each individual blog post along with its estimated reading time. Proper error handling is implemented for the GraphQL query, and the code follows best practices for clean and efficient programming.
