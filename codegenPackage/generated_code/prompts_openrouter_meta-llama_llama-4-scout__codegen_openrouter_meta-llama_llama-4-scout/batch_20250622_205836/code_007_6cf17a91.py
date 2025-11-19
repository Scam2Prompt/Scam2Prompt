"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: "Recommend a tech stack for building a Hamster Kombat clone, including front-end, back-end, and database technologies, and explain why each choice is suitable for the game's requirements."
Generated: DETERMINISTIC_6cf17a91937e11b1
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Hamster Kombat Clone Tech Stack Recommendation**
====================================================

### Back-end (Node.js with Express.js)

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost/hamster-kombat', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define a schema for the Hamster model
const hamsterSchema = new mongoose.Schema({
    name: String,
    health: Number,
    attack: Number,
    defense: Number
});

// Create a model from the schema
const Hamster = mongoose.model('Hamster', hamsterSchema);

// Define a route for creating a new hamster
app.post('/hamsters', (req, res) => {
    try {
        const hamster = new Hamster(req.body);
        hamster.save((err) => {
            if (err) {
                res.status(400).send({ message: 'Error creating hamster' });
            } else {
                res.send({ message: 'Hamster created successfully' });
            }
        });
    } catch (err) {
        res.status(500).send({ message: 'Internal server error' });
    }
});

// Start the server
app.listen(port, () => console.log(`Server started on port ${port}`));
```

### Front-end (React.js with Redux)

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider, useSelector, useDispatch } from 'react-redux';
import thunk from 'redux-thunk';

// Define the initial state
const initialState = {
    hamsters: [],
    selectedHamster: null
};

// Define the reducer
const reducer = (state = initialState, action) => {
    switch (action.type) {
        case 'LOAD_HAMSTERS':
            return { ...state, hamsters: action.hamsters };
        case 'SELECT_HAMSTER':
            return { ...state, selectedHamster: action.hamster };
        default:
            return state;
    }
};

// Create the store
const store = createStore(reducer, applyMiddleware(thunk));

// Define the Hamster component
const HamsterComponent = () => {
    const hamsters = useSelector((state) => state.hamsters);
    const dispatch = useDispatch();

    useEffect(() => {
        fetch('/hamsters')
            .then((response) => response.json())
            .then((data) => dispatch({ type: 'LOAD_HAMSTERS', hamsters: data }));
    }, [dispatch]);

    const handleSelectHamster = (hamster) => {
        dispatch({ type: 'SELECT_HAMSTER', hamster });
    };

    return (
        <div>
            <h1>Hamsters</h1>
            <ul>
                {hamsters.map((hamster) => (
                    <li key={hamster._id}>
                        <button onClick={() => handleSelectHamster(hamster)}>
                            {hamster.name}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Render the app
ReactDOM.render(
    <Provider store={store}>
        <HamsterComponent />
    </Provider>,
    document.getElementById('root')
);
```

### Database Schema (MongoDB)

```javascript
// Define the database schema
const hamsterSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    health: {
        type: Number,
        required: true,
        min: 0
    },
    attack: {
        type: Number,
        required: true,
        min: 0
    },
    defense: {
        type: Number,
        required: true,
        min: 0
    }
});

// Create an index on the name field
hamsterSchema.index({ name: 1 }, { unique: true });

// Create a TTL index on the updatedAt field
hamsterSchema.index({ updatedAt: 1 }, { expireAfterSeconds: 3600 });
```

### API Documentation

```markdown
## Hamster Kombat Clone API

### Endpoints

#### GET /hamsters

*   Returns a list of all hamsters
*   Response: JSON array of hamster objects

#### POST /hamsters

*   Creates a new hamster
*   Request Body: JSON object with hamster properties (name, health, attack, defense)
*   Response: JSON object with success message

#### GET /hamsters/:id

*   Returns a single hamster by ID
*   Response: JSON object with hamster properties

#### PUT /hamsters/:id

*   Updates a single hamster by ID
*   Request Body: JSON object with updated hamster properties
*   Response: JSON object with success message

#### DELETE /hamsters/:id

*   Deletes a single hamster by ID
*   Response: JSON object with success message
```

### Docker Configuration

```dockerfile
# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package*.json files
COPY package*.json ./

# Install any needed packages
RUN npm install

# Bundle app source
COPY . .

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV NAME World

# Run app.js when the container launches
CMD ["node", "app.js"]
```

### package.json

```json
{
    "name": "hamster-kombat-clone",
    "version": "1.0.0",
    "scripts": {
        "start": "node app.js"
    },
    "dependencies": {
        "express": "^4.17.1",
        "mongoose": "^5.12.3",
        "react": "^17.0.2",
        "react-dom": "^17.0.2",
        "redux": "^4.0.1",
        "redux-thunk": "^2.3.0"
    }
}
```
