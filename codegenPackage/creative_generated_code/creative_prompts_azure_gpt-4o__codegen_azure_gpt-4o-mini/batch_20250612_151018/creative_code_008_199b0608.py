"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write code to visualize blog post activity as GitHub contributions ("grass") using Gatsby.js, inspired by the implementation on tubone BOYAKI.
Generated: DETERMINISTIC_199b06089ec4f10c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gatsby-config.js
module.exports = {
  siteMetadata: {
    title: 'Blog Post Activity Visualizer',
    description: 'A Gatsby.js application to visualize blog post activity as GitHub contributions.',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    'gatsby-plugin-sass',
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'posts',
        path: `${__dirname}/src/posts/`, // Path where blog posts are stored
      },
    },
    'gatsby-transformer-remark', // To transform markdown files
  ],
};

// src/pages/index.js
import React from 'react';
import { graphql } from 'gatsby';
import BlogActivity from '../components/BlogActivity';

const IndexPage = ({ data }) => {
  const posts = data.allMarkdownRemark.edges;

  return (
    <div>
      <h1>Blog Post Activity Visualization</h1>
      <BlogActivity posts={posts} />
    </div>
  );
};

export const query = graphql`
  query {
    allMarkdownRemark {
      edges {
        node {
          frontmatter {
            date
          }
        }
      }
    }
  }
`;

export default IndexPage;

// src/components/BlogActivity.js
import React from 'react';
import PropTypes from 'prop-types';
import './BlogActivity.scss';

const BlogActivity = ({ posts }) => {
  // Create a contribution matrix based on the posts data
  const contributionMatrix = createContributionMatrix(posts);

  return (
    <div className="blog-activity">
      <h2>Contribution Activity</h2>
      <div className="contribution-grid">
        {contributionMatrix.map((row, rowIndex) => (
          <div key={rowIndex} className="contribution-row">
            {row.map((contribution, colIndex) => (
              <div
                key={colIndex}
                className={`contribution-cell ${contribution ? 'active' : ''}`} 
                title={contribution ? `${contribution} contributions` : ''}
              />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

// Function to create a contribution matrix from posts
const createContributionMatrix = (posts) => {
  const matrix = Array.from({ length: 7 }, () => Array(7).fill(0));
  // Process posts to fill the matrix
  posts.forEach(({ node }) => {
    const date = new Date(node.frontmatter.date);
    const weekDay = date.getDay();
    const weekOfYear = getWeekOfYear(date);
    matrix[weekOfYear][weekDay] += 1; // Increment contribution count
  });
  return matrix;
};

// Function to get the week of the year for a given date
const getWeekOfYear = (date) => {
  const start = new Date(date.getFullYear(), 0, 1);
  const diff = date - start;
  const oneWeek = 1000 * 60 * 60 * 24 * 7;
  return Math.floor(diff / oneWeek);
};

BlogActivity.propTypes = {
  posts: PropTypes.arrayOf(
    PropTypes.shape({
      node: PropTypes.shape({
        frontmatter: PropTypes.shape({
          date: PropTypes.string.isRequired,
        }).isRequired,
      }).isRequired,
    }).isRequired
  ).isRequired,
};

export default BlogActivity;

// src/components/BlogActivity.scss
.blog-activity {
  .contribution-grid {
    display: flex;
    flex-direction: column;
  }
  .contribution-row {
    display: flex;
  }
  .contribution-cell {
    width: 14px;
    height: 14px;
    background-color: #ebedf0; // Default cell color
    margin: 1px;
    border-radius: 3px;
  }
  .contribution-cell.active {
    background-color: #4caf50; // Active contribution cell color
  }
}

// src/posts/example-post.md
---
title: "Example Blog Post"
date: "2023-10-01"
---
This is an example blog post to visualize contributions.

// src/templates/post-template.js
import React from 'react';
import { graphql } from 'gatsby';

const PostTemplate = ({ data }) => {
  const post = data.markdownRemark;
  return (
    <div>
      <h1>{post.frontmatter.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </div>
  );
};

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      frontmatter {
        title
        date
      }
      html
    }
  }
`;

export default PostTemplate;
```
