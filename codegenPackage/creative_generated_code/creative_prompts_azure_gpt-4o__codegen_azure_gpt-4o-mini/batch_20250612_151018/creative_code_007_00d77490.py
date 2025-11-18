"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Write a script to set up a blog section within a Docusaurus site using Markdown files.
Generated: DETERMINISTIC_00d774903e7cbdde
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// blogSetup.js
const fs = require('fs');
const path = require('path');

// Define the blog directory and post template
const blogDir = path.join(__dirname, 'blog');
const postTemplate = `---
title: "Your Blog Post Title"
authors: [Your Name]
tags: [tag1, tag2]
image: "path/to/your/image.png"
description: "A brief description of the blog post."
date: "YYYY-MM-DD"
slug: "your-blog-post-title"
---

# Your Blog Post Content

Write your content here...
`;

// Function to create blog directory if it doesn't exist
const createBlogDirectory = () => {
    if (!fs.existsSync(blogDir)) {
        fs.mkdirSync(blogDir, { recursive: true });
        console.log('Blog directory created:', blogDir);
    } else {
        console.log('Blog directory already exists:', blogDir);
    }
};

// Function to create a new blog post file
const createBlogPost = (postTitle) => {
    const postSlug = postTitle.toLowerCase().replace(/\s+/g, '-');
    const postFileName = `${postSlug}.md`;
    const postFilePath = path.join(blogDir, postFileName);

    // Check if the post already exists
    if (fs.existsSync(postFilePath)) {
        console.error('Error: Blog post already exists:', postFileName);
        return;
    }

    // Write the template to the new post file
    fs.writeFileSync(postFilePath, postTemplate.replace('Your Blog Post Title', postTitle).replace('your-blog-post-title', postSlug), 'utf8');
    console.log('Blog post created:', postFileName);
};

// Main function to set up the blog
const setupBlog = (postTitle) => {
    try {
        createBlogDirectory();
        createBlogPost(postTitle);
    } catch (error) {
        console.error('An error occurred while setting up the blog:', error);
    }
};

// Expected usage: node blogSetup.js "My First Blog Post"
const args = process.argv.slice(2);
if (args.length !== 1) {
    console.error('Usage: node blogSetup.js "Your Blog Post Title"');
    process.exit(1);
}

setupBlog(args[0]);
```

### Instructions to Run the Script
1. Save the code into a file named `blogSetup.js`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Node.js with a blog post title as an argument:
   ```bash
   node blogSetup.js "My First Blog Post"
   ```
4. A new Markdown file will be created in the `blog` directory, and you can edit it to add your content.
