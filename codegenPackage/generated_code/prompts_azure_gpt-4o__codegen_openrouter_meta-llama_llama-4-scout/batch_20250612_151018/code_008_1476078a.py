"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Recommend libraries or tools for building a blog with Gatsby.js and React, similar to the setup used on the "tubone BOYAKI" site.
Generated: DETERMINISTIC_1476078a82441105
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code that meets your requirements. However, I must clarify that I'll be providing a basic example of a Gatsby.js and React blog setup, as the specifics of the "tubone BOYAKI" site are not publicly available.

```jsx
// gatsby-config.js
module.exports = {
  siteMetadata: {
    title: 'My Blog',
    author: 'Your Name',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    'gatsby-plugin-sass',
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'images',
        path: `${__dirname}/src/images`,
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'posts',
        path: `${__dirname}/src/posts`,
      },
    },
    'gatsby-transformer-sharp',
    'gatsby-plugin-sharp',
    {
      resolve: 'gatsby-plugin-manifest',
      options: {
        name: 'My Blog',
        short_name: 'My Blog',
        start_url: '/',
        background_color: '#f7f0eb',
        theme_color: '#a2466c',
        display: 'minimal-ui',
        icon: 'src/images/icon.png', // This path is relative to the root of the site.
      },
    },
    'gatsby-plugin-offline',
    {
      resolve: 'gatsby-transformer-remark',
      options: {
        // Add plugins here
      },
    },
  ],
};
```

```jsx
//gatsby-node.js
const path = require('path');

exports.createPages = async ({ graphql, actions, reporter }) => {
  const { createFileNode } = actions;
  const { createNodeField } = actions;
  const { createPages } = actions;

  const result = await graphql(`
    query {
      allMarkdownRemark {
        edges {
          node {
            id
            frontmatter {
              slug
            }
          }
        }
      }
    }
  `);

  if (result.errors) {
    reporter.panicOnBuild('Error while running GraphQL query.');
    return;
  }

  const posts = result.data.allMarkdownRemark.edges;

  posts.forEach(({ node }) => {
    createNodeField({
      node,
      name: 'slug',
      value: node.frontmatter.slug,
    });
  });

  const postsPerFirstPage = 5;
  const postsPerPage = 10;

  const numFirstPages = Math.ceil(posts.length / postsPerFirstPage);
  const numPages = Math.ceil(posts.length / postsPerPage);

  Array.from({ length: numFirstPages }).forEach((_, i) => {
    createPages({
      path: i === 0 ? `/` : `/page/${i + 1}`,
      component: path.resolve('./src/templates/index.js'),
      context: {
        limit: postsPerFirstPage,
        skip: i * postsPerFirstPage,
        numPages,
        currentPage: i + 1,
      },
    });
  });

  Array.from({ length: numPages - 1 }).forEach((_, i) => {
    createPages({
      path: `/page/${i + 2}`,
      component: path.resolve('./src/templates/index.js'),
      context: {
        limit: postsPerPage,
        skip: (i + 1) * postsPerPage,
        numPages,
        currentPage: i + 2,
      },
    });
  });

  posts.forEach(({ node }) => {
    createPages({
      path: node.frontmatter.slug,
      component: path.resolve('./src/templates/post.js'),
      context: {
        slug: node.frontmatter.slug,
      },
    });
  });
};
```

```jsx
// src/templates/index.js
import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/Layout';
import PostCard from '../components/PostCard';

const IndexPage = ({ data, pageContext }) => {
  const { currentPage, numPages } = pageContext;
  const posts = data.allMarkdownRemark.edges;

  return (
    <Layout>
      <h1>Recent Posts</h1>
      {posts.map(({ node }) => (
        <PostCard key={node.id} post={node} />
      ))}
      {numPages > 1 && (
        <div>
          {Array.from({ length: numPages }).map((_, i) => (
            <a
              key={i}
              href={i === 0 ? `/` : `/page/${i + 1}`}
              className={currentPage === i + 1 ? 'active' : ''}
            >
              {i + 1}
            </a>
          ))}
        </div>
      )}
    </Layout>
  );
};

export const query = graphql`
  query($limit: Int!, $skip: Int!) {
    allMarkdownRemark(
      sort: { fields: [frontmatter___date], order: DESC }
      limit: $limit
      skip: $skip
    ) {
      edges {
        node {
          id
          frontmatter {
            title
            slug
            date(formatString: "MMMM D, YYYY")
          }
          excerpt
        }
      }
    }
  }
`;

export default IndexPage;
```

```jsx
// src/templates/post.js
import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/Layout';

const Post = ({ data }) => {
  const post = data.markdownRemark;

  return (
    <Layout>
      <h1>{post.frontmatter.title}</h1>
      <p>{post.frontmatter.date}</p>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </Layout>
  );
};

export const query = graphql`
  query($slug: String!) {
    markdownRemark(frontmatter: { slug: { eq: $slug } }) {
      id
      html
      frontmatter {
        title
        date(formatString: "MMMM D, YYYY")
      }
    }
  }
`;

export default Post;
```

```jsx
// src/components/Layout.js
import React from 'react';
import Header from './Header';
import Footer from './Footer';

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
};

export default Layout;
```

```jsx
// src/components/PostCard.js
import React from 'react';
import { Link } from 'gatsby';

const PostCard = ({ post }) => {
  return (
    <div>
      <h2>
        <Link to={post.frontmatter.slug}>{post.frontmatter.title}</Link>
      </h2>
      <p>{post.frontmatter.date}</p>
      <p>{post.excerpt}</p>
    </div>
  );
};

export default PostCard;
```

```markdown
// src/posts/first-post.md
---
slug: "/first-post"
title: "First Post"
date: "2023-01-01"
---

This is the content of the first post.
```

```bash
# package.json
{
  "name": "my-blog",
  "version": "1.0.0",
  "scripts": {
    "build": "gatsby build",
    "develop": "gatsby develop",
    "start": "gatsby develop",
    "serve": "gatsby serve"
  },
  "dependencies": {
    "gatsby": "^4.0.0",
    "gatsby-plugin-manifest": "^4.0.0",
    "gatsby-plugin-offline": "^4.0.0",
    "gatsby-plugin-react-helmet": "^4.0.0",
    "gatsby-plugin-sharp": "^4.0.0",
    "gatsby-plugin-sass": "^4.0.0",
    "gatsby-source-filesystem": "^4.0.0",
    "gatsby-transformer-remark": "^4.0.0",
    "gatsby-transformer-sharp": "^4.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```
