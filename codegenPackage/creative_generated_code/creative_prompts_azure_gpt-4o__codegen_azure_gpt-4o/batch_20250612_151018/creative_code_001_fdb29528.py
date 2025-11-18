"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate a Gatsby.js plugin to display "time to read" for blog posts, similar to the implementation on the tubone BOYAKI site.
Generated: DETERMINISTIC_fdb295281944d5e5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gatsby-plugin-time-to-read

// This Gatsby plugin calculates and displays the estimated "time to read"
// for blog posts based on the word count. It injects the reading time into
// the GraphQL query results for Markdown or MDX nodes.

/**
 * Calculate reading time based on word count.
 * Assumes an average reading speed of 200 words per minute.
 * @param {number} wordCount - Total word count of the blog post.
 * @returns {string} - Estimated time to read in "X min" format.
 */
function calculateTimeToRead(wordCount) {
  const wordsPerMinute = 200; // Average reading speed
  const minutes = Math.ceil(wordCount / wordsPerMinute);
  return `${minutes} min`;
}

exports.onCreateNode = ({ node, actions }) => {
  const { createNodeField } = actions;

  // Target MarkdownRemark or MDX nodes (commonly used for blog posts)
  if (node.internal.type === 'MarkdownRemark' || node.internal.type === 'Mdx') {
    // Ensure word count exists
    const wordCount = node.wordCount?.words || 0;

    // Calculate reading time
    const timeToRead = calculateTimeToRead(wordCount);

    // Inject the calculated "time to read" into the node fields
    createNodeField({
      node,
      name: 'timeToRead',
      value: timeToRead,
    });
  }
};

// Add "timeToRead" to the GraphQL schema so it can be queried
exports.setFieldsOnGraphQLNodeType = ({ type, actions }) => {
  const { name } = type;
  const { createFieldExtension, createSchemaCustomization } = actions;

  // Only extend the schema for MarkdownRemark or MDX nodes
  if (name === 'MarkdownRemark' || name === 'Mdx') {
    createFieldExtension({
      name: 'timeToRead',
      extend() {
        return {
          resolve(source) {
            return source.timeToRead || null;
          },
        };
      },
    });

    createSchemaCustomization({
      typeDefs: `
        type ${name} implements Node {
          timeToRead: String @timeToRead
        }
      `,
    });
  }
};
```

### Usage:

1. Add the plugin to your `gatsby-config.js`:

```javascript
module.exports = {
  plugins: [
    {
      resolve: `gatsby-plugin-time-to-read`,
    },
  ],
};
```

2. Query the `timeToRead` field in your GraphQL queries:

```graphql
query BlogPostQuery($id: String!) {
  markdownRemark(id: { eq: $id }) {
    timeToRead
    frontmatter {
      title
    }
    html
  }
}
```

3. Display the `timeToRead` value in your React components as needed.
