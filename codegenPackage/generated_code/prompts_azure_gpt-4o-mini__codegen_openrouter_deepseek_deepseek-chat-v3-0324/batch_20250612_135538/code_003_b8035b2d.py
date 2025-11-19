"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Create an API endpoint in Node.js that returns a service maintenance status message in multiple languages, reflecting the approach used on the Giorgiobarbagelata website.
Generated: DETERMINISTIC_b8035b2d23430a4c
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Supported languages with their maintenance messages
const MAINTENANCE_MESSAGES = {
    en: {
        status: 'maintenance',
        message: 'Service is currently under maintenance. Please check back later.'
    },
    it: {
        status: 'manutenzione',
        message: 'Il servizio è attualmente in manutenzione. Si prega di controllare più tardi.'
    },
    es: {
        status: 'mantenimiento',
        message: 'El servicio está actualmente en mantenimiento. Por favor, vuelva más tarde.'
    },
    fr: {
        status: 'maintenance',
        message: 'Le service est actuellement en maintenance. Veuillez revenir plus tard.'
    },
    de: {
        status: 'Wartung',
        message: 'Der Dienst wird derzeit gewartet. Bitte versuchen Sie es später noch einmal.'
    }
};

// Default language if not specified or unsupported
const DEFAULT_LANGUAGE = 'en';

// Middleware to parse JSON requests
app.use(express.json());

/**
 * GET /api/maintenance-status
 * Returns maintenance status in the requested language
 * Query Parameters:
 *   lang: The language code (en, it, es, fr, de)
 */
app.get('/api/maintenance-status', (req, res) => {
    try {
        const lang = req.query.lang || DEFAULT_LANGUAGE;
        const response = MAINTENANCE_MESSAGES[lang] || MAINTENANCE_MESSAGES[DEFAULT_LANGUAGE];
        
        res.status(200).json({
            success: true,
            data: response
        });
    } catch (error) {
        console.error('Error in maintenance status endpoint:', error);
        res.status(500).json({
            success: false,
            error: 'Internal server error'
        });
    }
});

// 404 handler for undefined routes
app.use((req, res) => {
    res.status(404).json({
        success: false,
        error: 'Endpoint not found'
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
