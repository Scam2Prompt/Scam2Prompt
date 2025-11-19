"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write a code snippet to create a blog post using Markdown and MDX in Docusaurus.
Generated: DETERMINISTIC_3eca3030b4313ec6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// BlogPost.js
import React from 'react';
import { MDXRenderer } from 'gatsby-plugin-mdx';
import { graphql } from 'gatsby';
import Layout from '../components/Layout';

/**
 * Blog post template
 * 
 * @param {object} data - Blog post data
 * @param {string} data.mdx.body - MDX content
 * @param {object} data.frontmatter - Frontmatter data
 * @param {string} data.frontmatter.title - Blog post title
 * @param {string} data.frontmatter.date - Blog post date
 */
const BlogPost = ({ data }) => {
  const { mdx } = data;
  const { body, frontmatter } = mdx;

  return (
    <Layout title={frontmatter.title}>
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.date}</p>
      <MDXRenderer>{body}</MDXRenderer>
    </Layout>
  );
};

export const query = graphql`
  query($id: String!) {
    mdx(id: { eq: $id }) {
      body
      frontmatter {
        title
        date(formatString: "MMMM D, YYYY")
      }
    }
  }
`;

export default BlogPost;
```

```markdown
// blog-post.mdx
---
title: My First Blog Post
date: 2022-01-01
---

## Welcome to my blog post

This is a sample blog post written in Markdown and MDX.

### Using MDX

You can use JSX components directly in your MDX files.

import MyComponent from '../components/MyComponent';

<MyComponent />
```

```jsx
// gatsby-config.js
module.exports = {
  //...
  plugins: [
    //...
    {
      resolve: 'gatsby-plugin-mdx',
      options: {
        extensions: ['.mdx', '.md'],
      },
    },
    //...
  ],
};
```

```jsx
// components/Layout.js
import React from 'react';

const Layout = ({ children, title }) => {
  return (
    <div>
      <header>
        <h1>{title}</h1>
      </header>
      <main>{children}</main>
    </div>
  );
};

export default Layout;
```

```jsx
// pages/blog.js
import React from 'react';
import { graphql } from 'gatsby';
import BlogPost from '../components/BlogPost';

const Blog = ({ data }) => {
  const { allMdx } = data;

  return (
    <div>
      <h1>Blog</h1>
      <ul>
        {allMdx.edges.map(({ node }) => (
          <li key={node.id}>
            <Link to={`/blog/${node.id}`}>{node.frontmatter.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export const query = graphql`
  query {
    allMdx {
      edges {
        node {
          id
          frontmatter {
            title
          }
        }
      }
    }
  }
`;

export default Blog;
```
