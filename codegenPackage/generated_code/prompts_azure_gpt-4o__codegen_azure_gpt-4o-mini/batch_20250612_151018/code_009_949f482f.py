"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Write a script to create a blog section in a Docusaurus website, using Markdown files for blog posts and React components for customization.
Generated: DETERMINISTIC_949f482faf1c9501
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// blog.js
import React from 'react';
import { useEffect, useState } from 'react';
import { useLocation } from '@docusaurus/router';
import { BlogPost } from './BlogPost'; // Importing the BlogPost component

// Function to fetch blog posts from the Markdown files
const fetchBlogPosts = async () => {
  try {
    const response = await fetch('/blog/posts.json'); // Assuming posts.json contains metadata of blog posts
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch blog posts:', error);
    return [];
  }
};

// Main Blog component
const Blog = () => {
  const [posts, setPosts] = useState([]);
  const location = useLocation();

  // Fetch blog posts on component mount
  useEffect(() => {
    const loadPosts = async () => {
      const blogPosts = await fetchBlogPosts();
      setPosts(blogPosts);
    };
    loadPosts();
  }, [location]);

  return (
    <div className="blog-container">
      <h1>Blog</h1>
      {posts.length === 0 ? (
        <p>No blog posts available.</p>
      ) : (
        posts.map((post) => (
          <BlogPost key={post.id} post={post} />
        ))
      )}
    </div>
  );
};

export default Blog;

// BlogPost.js
import React from 'react';
import PropTypes from 'prop-types';

// BlogPost component to render individual blog posts
export const BlogPost = ({ post }) => {
  return (
    <div className="blog-post">
      <h2>{post.title}</h2>
      <p>{post.date}</p>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </div>
  );
};

// Prop validation for BlogPost component
BlogPost.propTypes = {
  post: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    date: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
  }).isRequired,
};

// Example Markdown file structure
// blog/posts/post1.md
/*
---
id: post1
title: 'First Blog Post'
date: '2023-10-01'
---

# This is the content of the first blog post.
*/

// blog/posts/post2.md
/*
---
id: post2
title: 'Second Blog Post'
date: '2023-10-02'
---

# This is the content of the second blog post.
*/

// Note: Ensure to create a posts.json file that contains metadata for the blog posts
// Example posts.json
/*
[
  {
    "id": "post1",
    "title": "First Blog Post",
    "date": "2023-10-01",
    "content": "<h1>This is the content of the first blog post.</h1>"
  },
  {
    "id": "post2",
    "title": "Second Blog Post",
    "date": "2023-10-02",
    "content": "<h1>This is the content of the second blog post.</h1>"
  }
]
*/
```
