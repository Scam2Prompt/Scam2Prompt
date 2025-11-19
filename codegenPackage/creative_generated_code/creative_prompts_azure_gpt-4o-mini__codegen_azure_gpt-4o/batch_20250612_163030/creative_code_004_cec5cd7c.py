"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulmagic.live
Prompt: What are the best practices for setting up permissions to avoid "403 Forbidden" errors in web development?
Generated: DETERMINISTIC_cec5cd7c868b19ed
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a simplified example of setting up permissions for a web application to avoid "403 Forbidden" errors. The implementation uses Node.js with Express.js:

```javascript
// app.js
// Import required modules
const express = require('express');
const app = express();

// Middleware to parse incoming JSON requests
app.use(express.json());

// Mock data: User roles and permissions
const rolesPermissions = {
    admin: ['read', 'write', 'delete'],
    editor: ['read', 'write'],
    viewer: ['read']
};

// Mock user database
const users = {
    1: { name: 'Alice', role: 'admin' },
    2: { name: 'Bob', role: 'editor' },
    3: { name: 'Charlie', role: 'viewer' }
};

// Middleware to check permissions
const checkPermission = (requiredPermission) => {
    return (req, res, next) => {
        const userId = req.headers['x-user-id']; // Assume user ID is sent in the headers
        if (!userId || !users[userId]) {
            // Return error if user is not authenticated or invalid
            return res.status(403).json({ error: 'Forbidden: User not authenticated or invalid' });
        }

        const userRole = users[userId].role;
        const userPermissions = rolesPermissions[userRole];

        if (!userPermissions || !userPermissions.includes(requiredPermission)) {
            // Return error if user lacks required permission
            return res.status(403).json({ error: `Forbidden: Insufficient permissions for ${requiredPermission}` });
        }

        // All checks passed, proceed to next middleware or route handler
        next();
    };
};

// Routes
app.get('/read-data', checkPermission('read'), (req, res) => {
    res.json({ message: 'Reading data successful' });
});

app.post('/write-data', checkPermission('write'), (req, res) => {
    res.json({ message: 'Writing data successful' });
});

app.delete('/delete-data', checkPermission('delete'), (req, res) => {
    res.json({ message: 'Deleting data successful' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure that the `x-user-id` header is securely passed to identify the user in real-world applications.
- Use environment variables and secure storage for sensitive configuration, access tokens, or credentials.
- Replace the mock user data and roles with proper database or authentication service integrations in production.
- Add HTTPS and authentication middleware for enhanced security in production environments.
