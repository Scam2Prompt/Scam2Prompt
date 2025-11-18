"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Generate code to customize the editor functionality in GitBook documentation, based on the features described in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_451f01b0d4ddbcca
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Custom Editor Functionality for GitBook Documentation
 * Based on Polymarket GitBook Starter Template
 * This script enhances the default editor features to improve the user experience.
 */

// Function to initialize custom editor features
function initCustomEditor() {
    try {
        // Ensure the GitBook object is available
        if (typeof GitBook === 'undefined') {
            throw new Error('GitBook object is not available. Make sure this script is included in the GitBook environment.');
        }

        // Add custom toolbar options
        const customToolbar = createCustomToolbar();
        GitBook.editor.addToolbar(customToolbar);

        // Enable syntax highlighting
        enableSyntaxHighlighting();

        // Add markdown shortcuts
        addMarkdownShortcuts();
        
        console.log('Custom editor functionality initialized successfully.');
    } catch (error) {
        console.error('Error initializing custom editor functionality:', error);
    }
}

// Function to create a custom toolbar for the editor
function createCustomToolbar() {
    const toolbar = {
        name: 'customToolbar',
        buttons: [
            {
                name: 'insertTable',
                icon: 'table',
                title: 'Insert Table',
                action: () => insertTable()
            },
            {
                name: 'insertCodeBlock',
                icon: 'code',
                title: 'Insert Code Block',
                action: () => insertCodeBlock()
            }
        ]
    };
    return toolbar;
}

// Function to enable syntax highlighting in the editor
function enableSyntaxHighlighting() {
    // Assuming we are using a library like Prism.js for syntax highlighting
    if (typeof Prism !== 'undefined') {
        GitBook.editor.on('change', () => {
            Prism.highlightAll();
        });
    } else {
        console.warn('Prism.js is not loaded. Syntax highlighting will not be enabled.');
    }
}

// Function to add markdown shortcuts to the editor
function addMarkdownShortcuts() {
    // Example: Add a shortcut for bold text (Ctrl + B)
    GitBook.editor.on('keydown', (event) => {
        if (event.ctrlKey && event.key === 'b') {
            event.preventDefault();
            GitBook.editor.insertText('**bold text**');
        }
    });
}

// Function to insert a table in markdown format
function insertTable() {
    const tableMarkdown = `
| Column 1 | Column 2 |
| -------- | -------- |
| Data 1   | Data 2   |
`;
    GitBook.editor.insertText(tableMarkdown);
}

// Function to insert a code block in markdown format
function insertCodeBlock() {
    const codeBlockMarkdown = '```\n// Your code here\n```';
    GitBook.editor.insertText(codeBlockMarkdown);
}

// Initialize the custom editor functionality on page load
document.addEventListener('DOMContentLoaded', () => {
    initCustomEditor();
});
```
