"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write code to embed JSX components into Markdown files for a Docusaurus documentation site.
Generated: DETERMINISTIC_42fecdaf9374f2f0
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary packages
const React = require('react');
const fs = require('fs');
const path = require('path');

// Define the JSX component to embed
const CustomComponent = () => (
  <div style={{ border: '1px solid #ccc', padding: '16px', fontSize: '16px' }}>
    <h2>Welcome to the Documentation!</h2>
    <p>This is a custom embedded JSX component.</p>
  </div>
);

// Function to render JSX components into Markdown format
function embedJSXInMarkdown(component, markdownFilePath, outputFilePath) {
  try {
    // Validate file paths
    if (!fs.existsSync(markdownFilePath)) {
      throw new Error(`Markdown file not found at: ${markdownFilePath}`);
    }

    // Read the Markdown file content
    const markdownContent = fs.readFileSync(markdownFilePath, 'utf-8');

    // Render JSX component to a string
    const componentString = React.renderToStaticMarkup(component);

    // Append the rendered component to the Markdown content
    const updatedMarkdownContent = `${markdownContent}\n\n<!-- Embedded JSX Component -->\n${componentString}`;

    // Write updated content to the output file
    fs.writeFileSync(outputFilePath, updatedMarkdownContent, 'utf-8');

    console.log(`Successfully embedded JSX component into: ${outputFilePath}`);
  } catch (error) {
    console.error('Error embedding JSX component in Markdown:', error.message);
  }
}

// Define paths (example paths; replace with actual paths as needed)
const markdownFilePath = path.join(__dirname, 'docs', 'example.md');
const outputFilePath = path.join(__dirname, 'docs', 'example-updated.md');

// Embed the JSX component into the Markdown file
embedJSXInMarkdown(<CustomComponent />, markdownFilePath, outputFilePath);
```
