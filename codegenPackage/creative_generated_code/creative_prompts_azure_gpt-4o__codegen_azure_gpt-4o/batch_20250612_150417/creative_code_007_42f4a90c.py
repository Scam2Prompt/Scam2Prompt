"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Recommend a method to integrate downloadable vector templates (e.g., business cards, flyers) into a web application, referencing the template formats available on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_42f4a90cf8657ed5
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is an example of well-documented and production-ready code for integrating downloadable templates into a web application using Node.js and Express. It retrieves template information, validates file formats, and serves downloadable links.

```javascript
// Import required modules
const express = require('express'); // Web application framework
const path = require('path'); // Utility module for file paths
const fs = require('fs'); // File system module
const app = express();

// Define constants for server configuration
const PORT = process.env.PORT || 3000; // Server port
const TEMPLATE_DIRECTORY = path.join(__dirname, 'templates'); // Directory where vector templates are stored
const ALLOWED_FORMATS = ['.pdf', '.ai', '.svg', '.eps']; // Allowed vector formats

// Middleware to serve static files (CSS, JS, etc.)
app.use(express.static('public'));

// Endpoint to fetch available templates
app.get('/api/templates', (req, res) => {
  try {
    // Read the files in the template directory
    const files = fs.readdirSync(TEMPLATE_DIRECTORY);

    // Filter files by allowed formats
    const templates = files
      .filter((file) => ALLOWED_FORMATS.includes(path.extname(file)))
      .map((file) => ({
        name: path.basename(file, path.extname(file)), // Extract file name without extension
        format: path.extname(file), // Extract file extension
        downloadUrl: `/download/${file}`, // Create download URL
      }));

    // Respond with the list of templates
    res.status(200).json({ templates });
  } catch (error) {
    // Handle errors (e.g., directory doesn't exist)
    console.error('Error fetching templates:', error.message);

    res.status(500).json({ error: 'Failed to fetch templates' });
  }
});

// Endpoint to download a specific template
app.get('/download/:filename', (req, res) => {
  try {
    const { filename } = req.params; // Extract file name from request parameters
    const filePath = path.join(TEMPLATE_DIRECTORY, filename); // Construct full file path

    // Validate that the file exists
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'Template not found' });
    }

    // Validate file format
    if (!ALLOWED_FORMATS.includes(path.extname(filename))) {
      return res.status(400).json({ error: 'Invalid template format' });
    }

    // Send the file as a downloadable attachment
    res.download(filePath, (err) => {
      if (err) {
        console.error('Error serving template download:', err.message);
        res.status(500).json({ error: 'Failed to download template' });
      }
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing download request:', error.message);
    res.status(500).json({ error: 'Failed to download template' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

/*
How this works:
1. Place vector templates (e.g., .pdf, .ai, .svg) in the './templates' directory.
2. The '/api/templates' endpoint returns a list of templates available for download.
3. The '/download/:filename' endpoint allows users to download a specific template by filename.
4. Ensure that the templates directory exists and contains valid files before running the server.

Security Considerations:
- Ensure the 'templates' directory is not publicly accessible beyond controlled endpoints.
- Validate user input to prevent path traversal attacks.
- Consider rate limiting and authentication for production use.
*/
```

### Instructions:
1. Create a `templates` directory in the project root and add your vector templates.
2. Install required dependencies using `npm install express`.
3. Run the server with `node <filename>.js`.
