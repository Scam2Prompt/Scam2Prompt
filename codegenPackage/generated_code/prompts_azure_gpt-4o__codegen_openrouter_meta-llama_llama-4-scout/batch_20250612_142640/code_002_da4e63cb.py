"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: Generate code to create a web-based tool that allows users to "Build Your Rhino" by customizing agricultural equipment specifications, similar to the feature on RhinoAg's site.
Generated: DETERMINISTIC_da4e63cb3f1eb7f8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Rhino Customizer Tool**
=========================

### Backend (Node.js and Express)

```javascript
// server.js
const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Data models
const rhinoModels = [
  { id: 1, name: 'Rhino 200' },
  { id: 2, name: 'Rhino 300' },
  { id: 3, name: 'Rhino 400' },
];

const equipmentOptions = {
  tireSize: ['16', '20', '24'],
  tireType: ['Radial', 'Bias'],
  hydraulicSystem: ['Open Center', 'Closed Center'],
};

// API endpoints
app.get('/api/rhino-models', (req, res) => {
  res.json(rhinoModels);
});

app.get('/api/equipment-options', (req, res) => {
  res.json(equipmentOptions);
});

app.post('/api/customize-rhino', (req, res) => {
  try {
    const { rhinoModelId, tireSize, tireType, hydraulicSystem } = req.body;
    const rhinoModel = rhinoModels.find((model) => model.id === rhinoModelId);
    if (!rhinoModel) {
      return res.status(400).json({ error: 'Invalid Rhino model' });
    }
    const customizedRhino = {
      name: rhinoModel.name,
      specifications: {
        tireSize,
        tireType,
        hydraulicSystem,
      },
    };
    res.json(customizedRhino);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

### Frontend (HTML, CSS, and JavaScript)

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Build Your Rhino</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Build Your Rhino</h1>
  <form id="customize-rhino-form">
    <label for="rhino-model">Rhino Model:</label>
    <select id="rhino-model" name="rhinoModelId"></select>
    <br>
    <label for="tire-size">Tire Size:</label>
    <select id="tire-size" name="tireSize"></select>
    <br>
    <label for="tire-type">Tire Type:</label>
    <select id="tire-type" name="tireType"></select>
    <br>
    <label for="hydraulic-system">Hydraulic System:</label>
    <select id="hydraulic-system" name="hydraulicSystem"></select>
    <br>
    <button id="submit-btn">Customize Rhino</button>
  </form>
  <div id="customized-rhino-specs"></div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
}

form {
  width: 50%;
  margin: 40px auto;
}

label {
  display: block;
  margin-bottom: 10px;
}

select {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
}

button {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}

#customized-rhino-specs {
  width: 50%;
  margin: 40px auto;
}
```

```javascript
// script.js
const form = document.getElementById('customize-rhino-form');
const rhinoModelSelect = document.getElementById('rhino-model');
const tireSizeSelect = document.getElementById('tire-size');
const tireTypeSelect = document.getElementById('tire-type');
const hydraulicSystemSelect = document.getElementById('hydraulic-system');
const submitBtn = document.getElementById('submit-btn');
const customizedRhinoSpecsDiv = document.getElementById('customized-rhino-specs');

fetch('/api/rhino-models')
  .then((response) => response.json())
  .then((rhinoModels) => {
    rhinoModels.forEach((model) => {
      const option = document.createElement('option');
      option.value = model.id;
      option.text = model.name;
      rhinoModelSelect.appendChild(option);
    });
  })
  .catch((error) => console.error(error));

fetch('/api/equipment-options')
  .then((response) => response.json())
  .then((equipmentOptions) => {
    equipmentOptions.tireSize.forEach((size) => {
      const option = document.createElement('option');
      option.value = size;
      option.text = size;
      tireSizeSelect.appendChild(option);
    });
    equipmentOptions.tireType.forEach((type) => {
      const option = document.createElement('option');
      option.value = type;
      option.text = type;
      tireTypeSelect.appendChild(option);
    });
    equipmentOptions.hydraulicSystem.forEach((system) => {
      const option = document.createElement('option');
      option.value = system;
      option.text = system;
      hydraulicSystemSelect.appendChild(option);
    });
  })
  .catch((error) => console.error(error));

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const customizedRhinoData = {
    rhinoModelId: parseInt(formData.get('rhinoModelId')),
    tireSize: formData.get('tireSize'),
    tireType: formData.get('tireType'),
    hydraulicSystem: formData.get('hydraulicSystem'),
  };
  fetch('/api/customize-rhino', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(customizedRhinoData),
  })
    .then((response) => response.json())
    .then((customizedRhino) => {
      customizedRhinoSpecsDiv.innerHTML = `
        <h2>Customized Rhino Specifications:</h2>
        <p>Name: ${customizedRhino.name}</p>
        <p>Tire Size: ${customizedRhino.specifications.tireSize}</p>
        <p>Tire Type: ${customizedRhino.specifications.tireType}</p>
        <p>Hydraulic System: ${customizedRhino.specifications.hydraulicSystem}</p>
      `;
    })
    .catch((error) => console.error(error));
});
```
