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
// Import required modules
const express = require('express');
const app = express();
const i18n = require('i18n');

// Initialize i18n
i18n.configure({
  locales: ['en', 'it', 'es'],
  defaultLocale: 'en',
  directory: './locales',
  objectNotation: true,
  fallbacks: {
    'en': ['en'],
    'it': ['it'],
    'es': ['es']
  }
});

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to get service maintenance status
app.get('/api/maintenance-status', (req, res) => {
  try {
    // Get the locale from the request query or use the default locale
    const locale = req.query.locale || i18n.defaultLocale;
    i18n.setLocale(locale);

    // Maintenance status message in multiple languages
    const maintenanceStatus = {
      message: i18n.__('maintenance.status.message'),
      status: i18n.__('maintenance.status.status')
    };

    // Return the maintenance status in JSON format
    res.json(maintenanceStatus);
  } catch (error) {
    // Handle any errors that occur during processing
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Error handler for unsupported locales
app.use((req, res, next) => {
  if (req.url.includes('/api/') && req.query.locale) {
    const supportedLocales = i18n.locales;
    if (!supportedLocales.includes(req.query.locale)) {
      res.status(400).json({ error: `Unsupported locale: ${req.query.locale}` });
    } else {
      next();
    }
  } else {
    next();
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// locales/en/maintenance.json
{
  "maintenance": {
    "status": {
      "message": "Service is currently under maintenance.",
      "status": "Down"
    }
  }
}
```

```javascript
// locales/it/maintenance.json
{
  "maintenance": {
    "status": {
      "message": "Il servizio è attualmente in manutenzione.",
      "status": "Indisponibile"
    }
  }
}
```

```javascript
// locales/es/maintenance.json
{
  "maintenance": {
    "status": {
      "message": "El servicio está actualmente en mantenimiento.",
      "status": "No disponible"
    }
  }
}
```
