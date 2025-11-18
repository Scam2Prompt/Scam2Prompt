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
// src/utils/calculateReadingTime.js

/**
 * Utility function to calculate the estimated reading time for a given text.
 * @param {string} content - The content of the blog post.
 * @param {number} wordsPerMinute - Average reading speed (default: 200 words per minute).
 * @returns {string} Estimated reading time in minutes.
 */
export const calculateReadingTime = (content, wordsPerMinute = 200) => {
  try {
    const wordCount = content.split(/\s+/).length; // Count words by splitting on whitespace
    const readingTime = Math.ceil(wordCount / wordsPerMinute); // Calculate reading time in minutes
    return `${readingTime} min read`;
  } catch (error) {
    console.error("Error calculating reading time:", error);
    return "N/A"; // Return a fallback value in case of error
  }
};
```

```javascript
// src/components/ReadingTime.js

import React from "react";
import PropTypes from "prop-types";
import { calculateReadingTime } from "../utils/calculateReadingTime";

/**
 * Component to display the estimated reading time of a blog post.
 * @param {Object} props - React props.
 * @param {string} props.content - Content of the blog post to calculate reading time.
 * @returns {JSX.Element} Component to display reading time.
 */
const ReadingTime = ({ content }) => {
  if (!content) {
    console.error("Content is required to calculate reading time.");
    return null; // Return nothing if content is missing
  }

  const readingTime = calculateReadingTime(content);

  return <p>{readingTime}</p>;
};

ReadingTime.propTypes = {
  content: PropTypes.string.isRequired, // Ensure content prop is passed and is a string
};

export default ReadingTime;
```

```javascript
// src/templates/blog-post.js

import React from "react";
import { graphql } from "gatsby";
import ReadingTime from "../components/ReadingTime";

const BlogPostTemplate = ({ data }) => {
  const post = data.markdownRemark;

  return (
    <article>
      <h1>{post.frontmatter.title}</h1>
      <p>
        {post.frontmatter.date} • <ReadingTime content={post.rawMarkdownBody} />
      </p>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </article>
  );
};

export const query = graphql`
  query BlogPostBySlug($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      frontmatter {
        title
        date(formatString: "MMMM DD, YYYY")
      }
      rawMarkdownBody
      html
    }
  }
`;

export default BlogPostTemplate;
```

```json
// gatsby-config.js (Ensure `gatsby-transformer-remark` is included)
// Add the necessary plugin for markdown processing.

module.exports = {
  plugins: [
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        // Options for markdown processing
      },
    },
    // Other plugins...
  ],
};
```

```bash
# Install required dependencies
npm install prop-types
```

This code calculates the estimated reading time for a blog post and displays it alongside the post's metadata. It is well-documented and adheres to best practices for production-ready code.
