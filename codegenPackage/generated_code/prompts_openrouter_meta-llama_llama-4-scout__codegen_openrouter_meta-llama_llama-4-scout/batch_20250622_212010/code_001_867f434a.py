"""
Generated Code Metadata:
========================
Original URL: https://a2ip.ru
Prompt: Write a JavaScript code snippet to create a simple website for a beginner, using popular libraries and frameworks.
Generated: DETERMINISTIC_867f434a3447223a
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import express from 'express';
import path from 'path';

// Create an Express application
const app = express();

// Define the port number
const PORT = 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route for the homepage
app.get('/', (req, res) => {
  // Render the index.html file
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Define a route for handling errors
app.use((req, res, next) => {
  // Catch any errors that occur during routing
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

// Error handling middleware
app.use((error, req, res, next) => {
  // Log the error
  console.error(error);

  // Set the response status code
  res.status(error.status || 500);

  // Send an error message
  res.json({ error: error.message });
});

// Start the server
app.listen(PORT, () => {
  // Log a message to the console
  console.log(`Server started on port ${PORT}`);
});
```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Website</title>
</head>
<body>
  <h1>Welcome to my simple website!</h1>
</body>
</html>
```

**package.json**
```json
{
  "name": "simple-website",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

**.gitignore**
```bash
node_modules/
```

**Directory Structure:**
```
simple-website/
|---- index.js
|---- public/
|       |---- index.html
|---- package.json
|---- .gitignore
```
