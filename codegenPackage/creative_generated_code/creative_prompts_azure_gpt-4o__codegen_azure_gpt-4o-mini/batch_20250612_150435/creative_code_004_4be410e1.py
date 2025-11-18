"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooledether.io
Prompt: Create a code snippet in Node.js to programmatically update the title and content of an existing blog post on Blogger using the Blogger API.
Generated: DETERMINISTIC_4be410e1abfc51c8
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const { google } = require('googleapis');
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// Configuration for OAuth2 client
const oauth2Client = new google.auth.OAuth2(
    'YOUR_CLIENT_ID', // Replace with your client ID
    'YOUR_CLIENT_SECRET', // Replace with your client secret
    'YOUR_REDIRECT_URI' // Replace with your redirect URI
);

// Set the credentials for OAuth2 client
oauth2Client.setCredentials({
    refresh_token: 'YOUR_REFRESH_TOKEN' // Replace with your refresh token
});

// Blogger API instance
const blogger = google.blogger({
    version: 'v3',
    auth: oauth2Client
});

// Endpoint to update a blog post
app.put('/update-post/:blogId/:postId', async (req, res) => {
    const { blogId, postId } = req.params;
    const { title, content } = req.body;

    // Validate input
    if (!title || !content) {
        return res.status(400).json({ error: 'Title and content are required.' });
    }

    try {
        // Prepare the update request
        const response = await blogger.posts.update({
            blogId: blogId,
            postId: postId,
            resource: {
                title: title,
                content: content
            }
        });

        // Respond with the updated post
        res.status(200).json(response.data);
    } catch (error) {
        // Handle errors appropriately
        console.error('Error updating post:', error);
        res.status(500).json({ error: 'An error occurred while updating the post.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Ensure to replace placeholders like `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_REDIRECT_URI`, and `YOUR_REFRESH_TOKEN` with actual values from your Google Developer Console. Additionally, make sure to handle the OAuth2 authentication properly before using this snippet.
