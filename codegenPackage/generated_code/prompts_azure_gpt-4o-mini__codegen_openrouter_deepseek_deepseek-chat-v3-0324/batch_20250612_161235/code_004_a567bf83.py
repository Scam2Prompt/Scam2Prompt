"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Design an API endpoint in Node.js that retrieves the competition rules and forms for the Fiji Mathematics Association's events.
Generated: DETERMINISTIC_a567bf83afa462b4
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Constants
const RULES_DIRECTORY = path.join(__dirname, 'data', 'rules');
const FORMS_DIRECTORY = path.join(__dirname, 'data', 'forms');

/**
 * Helper function to read files from directory
 * @param {string} directory - Directory path
 * @returns {Promise<Array>} - Array of file objects {name, content}
 */
async function getFilesFromDirectory(directory) {
    try {
        const files = await fs.readdir(directory);
        const filePromises = files.map(async (file) => {
            const content = await fs.readFile(path.join(directory, file), 'utf-8');
            return {
                name: path.basename(file, path.extname(file)),
                content: content
            };
        });
        return Promise.all(filePromises);
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error('Directory not found');
        }
        throw error;
    }
}

/**
 * API Endpoint to get competition rules and forms
 */
app.get('/api/competition-info', async (req, res) => {
    try {
        const [rules, forms] = await Promise.all([
            getFilesFromDirectory(RULES_DIRECTORY),
            getFilesFromDirectory(FORMS_DIRECTORY)
        ]);

        res.json({
            success: true,
            data: {
                rules: rules,
                forms: forms
            }
        });
    } catch (error) {
        console.error('Error fetching competition info:', error);
        res.status(500).json({
            success: false,
            message: error.message || 'Failed to retrieve competition information'
        });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'healthy' });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ success: false, message: 'Resource not found' });
});

// Error handler
app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({ success: false, message: 'Internal server error' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
