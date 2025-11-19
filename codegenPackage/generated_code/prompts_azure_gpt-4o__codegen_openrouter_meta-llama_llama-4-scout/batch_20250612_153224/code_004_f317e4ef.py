"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: Create a web application using MASIT Solutions' recommended technologies for app development and managed IT services.
Generated: DETERMINISTIC_f317e4ef1aa456be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**MASIT Solutions Web Application**
=====================================

**Technology Stack:**
* Frontend: React.js
* Backend: Node.js with Express.js
* Database: MongoDB

**Project Structure:**
```markdown
masit-solutions-app/
|---- backend/
|       |---- app.js
|       |---- models/
|       |       |---- user.js
|       |---- controllers/
|       |       |---- userController.js
|       |---- routes/
|       |       |---- userRoutes.js
|       |---- utils/
|       |       |---- database.js
|---- frontend/
|       |---- public/
|       |---- src/
|       |       |---- components/
|       |       |       |---- UserForm.js
|       |       |---- App.js
|       |       |---- index.js
|---- package.json
```

**Backend Code:**
```javascript
// backend/app.js
const express = require('express');
const mongoose = require('mongoose');
const userRoutes = require('./routes/userRoutes');

const app = express();
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/masit-solutions-app', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

app.use('/api/users', userRoutes);

const port = 3001;
app.listen(port, () => console.log(`Server listening on port ${port}`));
```

```javascript
// backend/models/user.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
});

module.exports = mongoose.model('User', userSchema);
```

```javascript
// backend/controllers/userController.js
const User = require('../models/user');

exports.getUsers = async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching users' });
    }
};

exports.createUser = async (req, res) => {
    try {
        const user = new User(req.body);
        await user.save();
        res.json(user);
    } catch (err) {
        res.status(400).json({ message: 'Error creating user' });
    }
};
```

```javascript
// backend/routes/userRoutes.js
const express = require('express');
const userController = require('../controllers/userController');

const router = express.Router();

router.get('/', userController.getUsers);
router.post('/', userController.createUser);

module.exports = router;
```

**Frontend Code:**
```javascript
// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import UserForm from './components/UserForm';

function App() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/api/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    return (
        <div>
            <h1>Users</h1>
            <ul>
                {users.map(user => (
                    <li key={user._id}>{user.name} ({user.email})</li>
                ))}
            </ul>
            <UserForm />
        </div>
    );
}

export default App;
```

```javascript
// frontend/src/components/UserForm.js
import React, { useState } from 'react';

function UserForm() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('/api/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email }),
        })
            .then(response => response.json())
            .then(data => console.log(data));
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
            </label>
            <br />
            <label>
                Email:
                <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
            </label>
            <br />
            <button type="submit">Create User</button>
        </form>
    );
}

export default UserForm;
```

**package.json:**
```json
{
    "name": "masit-solutions-app",
    "version": "1.0.0",
    "scripts": {
        "start": "node backend/app.js & react-scripts start",
        "build": "react-scripts build"
    },
    "dependencies": {
        "express": "^4.17.1",
        "mongoose": "^5.10.15",
        "react": "^17.0.2",
        "react-dom": "^17.0.2",
        "react-scripts": "4.0.3"
    }
}
```
