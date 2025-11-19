"""
Generated Code Metadata:
========================
Original URL: https://genopets.eu
Prompt: "Create a simple front-end form using React or Vue.js to input new pet attributes in a Genopets-style application, including validation and submission handling."
Generated: DETERMINISTIC_55334bd5d8b1aee4
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PetForm.js
import React, { useState } from 'react';

// A functional component for the pet input form
const PetForm = () => {
    // State to hold pet attributes
    const [petName, setPetName] = useState('');
    const [petType, setPetType] = useState('');
    const [petAge, setPetAge] = useState('');
    const [error, setError] = useState('');

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        // Validate inputs
        if (!petName || !petType || !petAge) {
            setError('All fields are required.');
            return;
        }
        if (isNaN(petAge) || petAge <= 0) {
            setError('Age must be a positive number.');
            return;
        }
        // Clear error and proceed with submission
        setError('');
        const petData = {
            name: petName,
            type: petType,
            age: parseInt(petAge, 10),
        };
        console.log('Pet Data Submitted:', petData);
        // Here you would typically send petData to your API
        // reset form fields
        resetForm();
    };

    // Reset form fields
    const resetForm = () => {
        setPetName('');
        setPetType('');
        setPetAge('');
    };

    return (
        <div>
            <h2>Add a New Pet</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="petName">Pet Name:</label>
                    <input
                        type="text"
                        id="petName"
                        value={petName}
                        onChange={(e) => setPetName(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="petType">Pet Type:</label>
                    <input
                        type="text"
                        id="petType"
                        value={petType}
                        onChange={(e) => setPetType(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="petAge">Pet Age:</label>
                    <input
                        type="number"
                        id="petAge"
                        value={petAge}
                        onChange={(e) => setPetAge(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Add Pet</button>
            </form>
        </div>
    );
};

export default PetForm;
```

```javascript
// App.js
import React from 'react';
import PetForm from './PetForm';

// Main application component
const App = () => {
    return (
        <div>
            <h1>Genopets Application</h1>
            <PetForm />
        </div>
    );
};

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the main application
ReactDOM.render(<App />, document.getElementById('root'));
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Genopets Application</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js" type="text/javascript"></script>
</body>
</html>
```

```bash
# package.json
{
  "name": "genopets-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
