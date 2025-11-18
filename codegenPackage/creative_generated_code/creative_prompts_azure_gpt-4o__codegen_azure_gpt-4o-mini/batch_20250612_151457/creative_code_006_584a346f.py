"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Generate code for creating a multilingual NFT sales website that supports both domestic and international audiences, as described on the VIP Management website.
Generated: DETERMINISTIC_584a346f8ba99597
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const { i18n, init } = require('i18n');

// Initialize the app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Internationalization setup
i18n.configure({
    locales: ['en', 'fr', 'de', 'es'], // Supported languages
    directory: __dirname + '/locales',
    defaultLocale: 'en',
    autoReload: true,
    queryParameter: 'lang',
});

app.use(i18n.init);

// MongoDB connection setup
mongoose.connect('mongodb://localhost:27017/nftSales', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected!'))
    .catch(err => console.error('MongoDB connection error:', err));

// NFT Schema
const nftSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    imageUrl: { type: String, required: true },
    language: { type: String, required: true },
}, { timestamps: true });

const NFT = mongoose.model('NFT', nftSchema);

// Routes

// Get all NFTs
app.get('/api/nfts', async (req, res) => {
    try {
        const nfts = await NFT.find({});
        res.status(200).json(nfts);
    } catch (error) {
        console.error('Error fetching NFTs:', error);
        res.status(500).json({ error: i18n.__('server.error') });
    }
});

// Create a new NFT
app.post('/api/nfts', async (req, res) => {
    const { title, description, price, imageUrl, language } = req.body;

    if (!title || !description || !price || !imageUrl || !language) {
        return res.status(400).json({ error: i18n.__('validation.requiredFields') });
    }

    try {
        const newNFT = new NFT({ title, description, price, imageUrl, language });
        await newNFT.save();
        res.status(201).json(newNFT);
    } catch (error) {
        console.error('Error creating NFT:', error);
        res.status(500).json({ error: i18n.__('server.error') });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({ error: i18n.__('server.error') });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### locales/en.json
```json
{
    "server": {
        "error": "Internal Server Error"
    },
    "validation": {
        "requiredFields": "All fields are required."
    }
}
```

### locales/fr.json
```json
{
    "server": {
        "error": "Erreur interne du serveur"
    },
    "validation": {
        "requiredFields": "Tous les champs sont requis."
    }
}
```

### locales/de.json
```json
{
    "server": {
        "error": "Interner Serverfehler"
    },
    "validation": {
        "requiredFields": "Alle Felder sind erforderlich."
    }
}
```

### locales/es.json
```json
{
    "server": {
        "error": "Error interno del servidor"
    },
    "validation": {
        "requiredFields": "Todos los campos son obligatorios."
    }
}
```

Make sure to create the `locales` directory with the corresponding JSON files for the languages you wish to support.
