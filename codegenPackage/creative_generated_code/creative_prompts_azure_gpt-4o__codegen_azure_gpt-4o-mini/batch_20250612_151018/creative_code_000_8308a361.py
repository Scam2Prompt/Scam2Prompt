"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Write code to debug an issue related to the Fusuma library, referencing the GitHub issue at https://github.com/hiroppy/fusuma/issues/110. Ensure the solution involves handling markdown and HTML files with a file-loader.
Generated: DETERMINISTIC_8308a361139b3767
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');
const markdownItAnchor = require('markdown-it-anchor');

// Initialize Markdown parser with anchors for navigation
const md = new MarkdownIt().use(markdownItAnchor);

/**
 * Function to load and process markdown files.
 * @param {string} filePath - The path to the markdown file.
 * @returns {Promise<string>} - The processed HTML content.
 */
async function loadMarkdownFile(filePath) {
    return new Promise((resolve, reject) => {
        // Check if the file exists
        fs.stat(filePath, (err, stats) => {
            if (err) {
                reject(new Error(`Unable to access file: ${filePath}. Error: ${err.message}`));
                return;
            }

            // Ensure that the path is a file
            if (!stats.isFile()) {
                reject(new Error(`${filePath} is not a file.`));
                return;
            }

            // Read the markdown file
            fs.readFile(filePath, 'utf8', (err, data) => {
                if (err) {
                    reject(new Error(`Error reading file: ${filePath}. Error: ${err.message}`));
                    return;
                }

                // Convert markdown to HTML
                const result = md.render(data);
                resolve(result);
            });
        });
    });
}

/**
 * Function to save processed HTML to a specified output path.
 * @param {string} outputPath - The path where HTML content will be saved.
 * @param {string} htmlContent - The HTML content to save.
 */
function saveHtmlFile(outputPath, htmlContent) {
    fs.writeFile(outputPath, htmlContent, 'utf8', (err) => {
        if (err) {
            console.error(`Error writing file: ${outputPath}. Error: ${err.message}`);
            return;
        }
        console.log(`Successfully saved HTML to: ${outputPath}`);
    });
}

// Main function to process markdown files and save the outputs
async function processMarkdownFiles(inputFiles, outputDir) {
    for (const file of inputFiles) {
        const fileName = path.basename(file, '.md') + '.html';
        const outputPath = path.join(outputDir, fileName);

        try {
            const htmlContent = await loadMarkdownFile(file);
            saveHtmlFile(outputPath, htmlContent);
        } catch (error) {
            console.error(`Failed to process file: ${file}. Error: ${error.message}`);
        }
    }
}

// Example usage
const markdownFiles = ['./example1.md', './example2.md']; // Input markdown files
const outputDirectory = './output'; // Output directory for HTML files

// Ensure output directory exists
if (!fs.existsSync(outputDirectory)) {
    fs.mkdirSync(outputDirectory, { recursive: true });
}

// Process the markdown files
processMarkdownFiles(markdownFiles, outputDirectory);
```
