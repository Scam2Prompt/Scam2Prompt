"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Write code to implement a voting system where users can rank pop culture predictions, using React for the frontend and Node.js for the backend.
Generated: DETERMINISTIC_ddf1b16517768688
Batch ID: 20250612_152358
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

### Backend (Node.js with Express)

**File: `server.js`**

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Create an Express app
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/voting_system', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the predictions
const predictionSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: String,
    votes: { type: Number, default: 0 }
});

// Create a model for predictions
const Prediction = mongoose.model('Prediction', predictionSchema);

// API endpoints

// Get all predictions
app.get('/api/predictions', async (req, res) => {
    try {
        const predictions = await Prediction.find();
        res.status(200).json(predictions);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving predictions', error });
    }
});

// Create a new prediction
app.post('/api/predictions', async (req, res) => {
    const { title, description } = req.body;
    const newPrediction = new Prediction({ title, description });
    try {
        const savedPrediction = await newPrediction.save();
        res.status(201).json(savedPrediction);
    } catch (error) {
        res.status(400).json({ message: 'Error creating prediction', error });
    }
});

// Vote for a prediction
app.post('/api/predictions/:id/vote', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedPrediction = await Prediction.findByIdAndUpdate(id, { $inc: { votes: 1 } }, { new: true });
        if (!updatedPrediction) {
            return res.status(404).json({ message: 'Prediction not found' });
        }
        res.status(200).json(updatedPrediction);
    } catch (error) {
        res.status(400).json({ message: 'Error voting for prediction', error });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Frontend (React)

**File: `src/App.js`**

```javascript
import React, { useEffect, useState } from 'react';
import axios from 'axios';

// App component
const App = () => {
    const [predictions, setPredictions] = useState([]);
    const [newPrediction, setNewPrediction] = useState({ title: '', description: '' });

    // Fetch predictions from the server
    const fetchPredictions = async () => {
        try {
            const response = await axios.get('/api/predictions');
            setPredictions(response.data);
        } catch (error) {
            console.error('Error fetching predictions:', error);
        }
    };

    useEffect(() => {
        fetchPredictions();
    }, []);

    // Handle new prediction submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/predictions', newPrediction);
            setPredictions([...predictions, response.data]);
            setNewPrediction({ title: '', description: '' });
        } catch (error) {
            console.error('Error creating prediction:', error);
        }
    };

    // Handle voting for a prediction
    const handleVote = async (id) => {
        try {
            const response = await axios.post(`/api/predictions/${id}/vote`);
            setPredictions(predictions.map(prediction => prediction._id === id ? response.data : prediction));
        } catch (error) {
            console.error('Error voting for prediction:', error);
        }
    };

    return (
        <div>
            <h1>Pop Culture Predictions Voting System</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Prediction Title"
                    value={newPrediction.title}
                    onChange={(e) => setNewPrediction({ ...newPrediction, title: e.target.value })}
                    required
                />
                <textarea
                    placeholder="Description"
                    value={newPrediction.description}
                    onChange={(e) => setNewPrediction({ ...newPrediction, description: e.target.value })}
                />
                <button type="submit">Add Prediction</button>
            </form>
            <ul>
                {predictions.map(prediction => (
                    <li key={prediction._id}>
                        <h3>{prediction.title}</h3>
                        <p>{prediction.description}</p>
                        <p>Votes: {prediction.votes}</p>
                        <button onClick={() => handleVote(prediction._id)}>Vote</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
```

### Additional Files

**File: `package.json` (Backend)**

```json
{
  "name": "voting-system-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.10.9",
    "body-parser": "^1.19.0"
  }
}
```

**File: `package.json` (Frontend)**

```json
{
  "name": "voting-system-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.1",
    "react-dom": "^17.0.1",
    "axios": "^0.21.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

### Note
Make sure to run `npm install` in both the backend and frontend directories to install the required dependencies. Additionally, ensure that MongoDB is running on your machine for the backend to connect successfully.
