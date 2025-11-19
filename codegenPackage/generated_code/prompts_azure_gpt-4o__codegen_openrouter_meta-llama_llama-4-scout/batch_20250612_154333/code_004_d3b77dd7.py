"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write code to integrate a label customization feature into a web application, allowing users to design labels for daycare, camps, or small businesses, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_d3b77dd749f8b3bc
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// labelCustomizer.js

/**
 * Label Customizer API
 * 
 * Provides endpoints for creating, reading, updating, and deleting label designs.
 * 
 * @author [Your Name]
 */

// Import required modules
const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/labelCustomizer', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the LabelDesign model
const labelDesignSchema = new mongoose.Schema({
    name: String,
    width: Number,
    height: Number,
    font: String,
    fontSize: Number,
    text: String,
    backgroundColor: String,
    textColor: String,
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
});

const LabelDesign = mongoose.model('LabelDesign', labelDesignSchema);

// Create a new label design
router.post('/label-designs', async (req, res) => {
    try {
        const labelDesign = new LabelDesign(req.body);
        await labelDesign.save();
        res.status(201).json(labelDesign);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Get all label designs
router.get('/label-designs', async (req, res) => {
    try {
        const labelDesigns = await LabelDesign.find().sort('-createdAt');
        res.json(labelDesigns);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Get a single label design by ID
router.get('/label-designs/:id', async (req, res) => {
    try {
        const labelDesign = await LabelDesign.findById(req.params.id);
        if (!labelDesign) {
            return res.status(404).json({ message: 'Label design not found' });
        }
        res.json(labelDesign);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Update a label design
router.put('/label-designs/:id', async (req, res) => {
    try {
        const labelDesign = await LabelDesign.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!labelDesign) {
            return res.status(404).json({ message: 'Label design not found' });
        }
        res.json(labelDesign);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Delete a label design
router.delete('/label-designs/:id', async (req, res) => {
    try {
        await LabelDesign.findByIdAndRemove(req.params.id);
        res.status(204).json({ message: 'Label design deleted successfully' });
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Generate a label design as an SVG
router.get('/label-designs/:id/svg', async (req, res) => {
    try {
        const labelDesign = await LabelDesign.findById(req.params.id);
        if (!labelDesign) {
            return res.status(404).json({ message: 'Label design not found' });
        }

        const svg = `
            <svg width="${labelDesign.width}" height="${labelDesign.height}">
                <rect width="${labelDesign.width}" height="${labelDesign.height}" fill="${labelDesign.backgroundColor}" />
                <text x="${labelDesign.width / 2}" y="${labelDesign.height / 2}" font-family="${labelDesign.font}" font-size="${labelDesign.fontSize}" fill="${labelDesign.textColor}" text-anchor="middle">${labelDesign.text}</text>
            </svg>
        `;

        res.set("Content-Type", "image/svg+xml");
        res.send(svg);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

module.exports = router;
```

```javascript
// server.js

const express = require('express');
const app = express();
const labelCustomizerRouter = require('./labelCustomizer');

app.use(express.json());
app.use('/api', labelCustomizerRouter);

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Label Customizer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <h1>Label Customizer</h1>
    <form id="label-design-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="width">Width:</label>
        <input type="number" id="width" name="width"><br><br>
        <label for="height">Height:</label>
        <input type="number" id="height" name="height"><br><br>
        <label for="font">Font:</label>
        <input type="text" id="font" name="font"><br><br>
        <label for="fontSize">Font Size:</label>
        <input type="number" id="fontSize" name="fontSize"><br><br>
        <label for="text">Text:</label>
        <input type="text" id="text" name="text"><br><br>
        <label for="backgroundColor">Background Color:</label>
        <input type="color" id="backgroundColor" name="backgroundColor"><br><br>
        <label for="textColor">Text Color:</label>
        <input type="color" id="textColor" name="textColor"><br><br>
        <button id="submit-btn">Create Label Design</button>
    </form>

    <div id="label-designs-container"></div>

    <script>
        const form = document.getElementById('label-design-form');
        const labelDesignsContainer = document.getElementById('label-designs-container');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const labelDesign = Object.fromEntries(formData);

            try {
                const response = await fetch('/api/label-designs', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(labelDesign)
                });

                const createdLabelDesign = await response.json();
                console.log(createdLabelDesign);

                // Fetch and display all label designs
                const labelDesignsResponse = await fetch('/api/label-designs');
                const labelDesigns = await labelDesignsResponse.json();
                labelDesignsContainer.innerHTML = '';
                labelDesigns.forEach((labelDesign) => {
                    const labelDesignHTML = `
                        <div>
                            <h2>${labelDesign.name}</h2>
                            <svg width="${labelDesign.width}" height="${labelDesign.height}">
                                <rect width="${labelDesign.width}" height="${labelDesign.height}" fill="${labelDesign.backgroundColor}" />
                                <text x="${labelDesign.width / 2}" y="${labelDesign.height / 2}" font-family="${labelDesign.font}" font-size="${labelDesign.fontSize}" fill="${labelDesign.textColor}" text-anchor="middle">${labelDesign.text}</text>
                            </svg>
                        </div>
                    `;
                    labelDesignsContainer.insertAdjacentHTML('beforeend', labelDesignHTML);
                });
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
