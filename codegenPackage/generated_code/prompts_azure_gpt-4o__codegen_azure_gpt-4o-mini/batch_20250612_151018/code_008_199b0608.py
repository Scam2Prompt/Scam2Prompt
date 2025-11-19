"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write code to visualize blog post activity as GitHub contributions ("grass") using Gatsby.js, inspired by the implementation on tubone BOYAKI.
Generated: DETERMINISTIC_199b06089ec4f10c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// gatsby-config.js

module.exports = {
  siteMetadata: {
    title: 'Blog Post Activity Visualizer',
    description: 'Visualize blog post activity as GitHub contributions using Gatsby.js',
    author: 'Your Name',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'posts',
        path: `${__dirname}/src/posts/`, // Path to your blog posts
      },
    },
    'gatsby-transformer-remark', // For processing markdown files
    'gatsby-plugin-sass', // For styling
  ],
};

// src/pages/index.js

import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/layout';
import ContributionGraph from '../components/ContributionGraph';

const IndexPage = ({ data }) => {
  const posts = data.allMarkdownRemark.nodes;

  return (
    <Layout>
      <h1>Blog Post Activity</h1>
      <ContributionGraph posts={posts} />
    </Layout>
  );
};

export const query = graphql`
  query {
    allMarkdownRemark {
      nodes {
        frontmatter {
          date
        }
      }
    }
  }
`;

export default IndexPage;

// src/components/ContributionGraph.js

import React from 'react';
import PropTypes from 'prop-types';
import { GitHubCalendar } from 'react-github-calendar'; // A library to visualize contributions

const ContributionGraph = ({ posts }) => {
  // Function to format posts into a contributions object
  const formatContributions = (posts) => {
    const contributions = {};
    posts.forEach(post => {
      const date = new Date(post.frontmatter.date);
      const dateString = date.toISOString().split('T')[0]; // Format date as YYYY-MM-DD
      contributions[dateString] = (contributions[dateString] || 0) + 1; // Count posts per day
    });
    return contributions;
  };

  const contributions = formatContributions(posts);

  return (
    <div>
      <h2>Contribution Graph</h2>
      <GitHubCalendar
        username="your-github-username" // Replace with your GitHub username
        contributions={contributions}
        blockSize={15}
        blockMargin={5}
        color="#c6e48b"
        colors={[
          '#ebedf0',
          '#c6e48b',
          '#7bc96f',
          '#239a3b',
          '#196127',
        ]}
      />
    </div>
  );
};

ContributionGraph.propTypes = {
  posts: PropTypes.array.isRequired,
};

export default ContributionGraph;

// src/components/layout.js

import React from 'react';
import PropTypes from 'prop-types';
import './layout.scss'; // Import your styles

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header>
        <h1>Blog Post Activity Visualizer</h1>
      </header>
      <main>{children}</main>
      <footer>
        <p>© {new Date().getFullYear()} Your Name</p>
      </footer>
    </div>
  );
};

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;

// src/styles/layout.scss

.layout {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  background-color: #f9f9f9;
}

header {
  background: #4a90e2;
  color: white;
  padding: 10px;
  text-align: center;
}

footer {
  text-align: center;
  margin-top: 20px;
}

// src/posts/sample-post.md

---
title: "Sample Blog Post"
date: "2023-10-01"
---

This is a sample blog post to visualize activity.

```

Make sure to install the necessary dependencies by running:

```bash
npm install gatsby gatsby-plugin-react-helmet gatsby-source-filesystem gatsby-transformer-remark gatsby-plugin-sass react-github-calendar
```

Replace `your-github-username` with your actual GitHub username in the `ContributionGraph` component. Adjust the paths and styles as needed for your project structure.
