"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write a code snippet to create a blog post using Markdown and MDX in Docusaurus.
Generated: DETERMINISTIC_3eca3030b4313ec6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const fs = require('fs');
const path = require('path');

// Configuration: Define default settings for the blog post
const blogDirectory = path.join(__dirname, 'blog'); // Path to the blog folder
const defaultAuthor = 'John Doe'; // Default author name
const dateFormat = 'YYYY-MM-DD'; // Date format for the post filename

// Function to get today's date in the specified format
function getTodaysDate() {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const day = String(today.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// Function to generate a new blog post in Markdown/MDX format
function createBlogPost(title, author = defaultAuthor, tags = []) {
  try {
    // Validate input
    if (!title || typeof title !== 'string') {
      throw new Error('Title must be a non-empty string.');
    }

    // Generate filename based on today's date and title
    const formattedDate = getTodaysDate();
    const slug = title.trim().toLowerCase().replace(/\s+/g, '-');
    const fileName = `${formattedDate}-${slug}.mdx`;

    // Define the content of the blog post
    const content = `---
title: ${title}
author: ${author}
tags: ${JSON.stringify(tags)}
date: ${formattedDate}
---

## ${title}

Welcome to your new blog post! Write your content here.

### Example Section

You can use **Markdown** or **MDX** to create rich content.
`;

    // Ensure the blog directory exists
    if (!fs.existsSync(blogDirectory)) {
      fs.mkdirSync(blogDirectory, { recursive: true });
    }

    // Write the blog post to a file
    const filePath = path.join(blogDirectory, fileName);
    fs.writeFileSync(filePath, content, 'utf8');

    console.log(`Blog post created successfully: ${filePath}`);
  } catch (error) {
    console.error(`Error creating blog post: ${error.message}`);
  }
}

// Example usage: Pass the title and optional author/tags
createBlogPost(
  'My First Blog Post', 
  'Jane Smith', 
  ['javascript', 'web development', 'docusaurus']
);
```
