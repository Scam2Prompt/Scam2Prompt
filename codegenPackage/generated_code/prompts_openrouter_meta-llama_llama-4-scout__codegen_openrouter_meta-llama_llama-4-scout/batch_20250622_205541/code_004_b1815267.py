"""
Generated Code Metadata:
========================
Original URL: https://ksp.onsiteapp.co
Prompt: How do I design a user role system (e.g., selecting teams) in a web application, and what database schema could support such a feature efficiently?
Generated: DETERMINISTIC_b1815267df8dbff2
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Role System with Team Selection**
=====================================

### Database Schema

```sql
-- users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- roles table
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- teams table
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- user_roles table (many-to-many)
CREATE TABLE user_roles (
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    team_id INTEGER,
    PRIMARY KEY (user_id, role_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- team_members table (many-to-many)
CREATE TABLE team_members (
    team_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    role_id INTEGER,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE SET NULL
);
```

### Backend API (Node.js with Express.js)

```javascript
// server.js
const express = require('express');
const app = express();
const { Pool } = require('pg');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// database connection
const pool = new Pool({
    user: 'your_username',
    host: 'your_host',
    database: 'your_database',
    password: 'your_password',
    port: 5432,
});

// middleware
app.use(express.json());

// user registration
app.post('/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;
        const hashedPassword = await bcrypt.hash(password, 10);
        const result = await pool.query(
            'INSERT INTO users (username, email, password) VALUES ($1, $2, $3) RETURNING *',
            [username, email, hashedPassword]
        );
        res.json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error registering user' });
    }
});

// user login
app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
        if (result.rows.length === 0) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const user = result.rows[0];
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ userId: user.id }, 'your_secret_key', { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error logging in' });
    }
});

// assign role to user
app.post('/users/:userId/roles', async (req, res) => {
    try {
        const { userId } = req.params;
        const { roleId, teamId } = req.body;
        await pool.query(
            'INSERT INTO user_roles (user_id, role_id, team_id) VALUES ($1, $2, $3)',
            [userId, roleId, teamId]
        );
        res.json({ message: 'Role assigned successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error assigning role' });
    }
});

// get user roles
app.get('/users/:userId/roles', async (req, res) => {
    try {
        const { userId } = req.params;
        const result = await pool.query(
            'SELECT r.* FROM user_roles ur JOIN roles r ON ur.role_id = r.id WHERE ur.user_id = $1',
            [userId]
        );
        res.json(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching user roles' });
    }
});

// add team member
app.post('/teams/:teamId/members', async (req, res) => {
    try {
        const { teamId } = req.params;
        const { userId, roleId } = req.body;
        await pool.query(
            'INSERT INTO team_members (team_id, user_id, role_id) VALUES ($1, $2, $3)',
            [teamId, userId, roleId]
        );
        res.json({ message: 'Team member added successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error adding team member' });
    }
});

// start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

### Frontend (React.js)

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [user, setUser] = useState({});
    const [roles, setRoles] = useState([]);
    const [teams, setTeams] = useState([]);
    const [selectedTeam, setSelectedTeam] = useState(null);

    useEffect(() => {
        axios.get('/users/me')
            .then(response => {
                setUser(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleAssignRole = (roleId, teamId) => {
        axios.post(`/users/${user.id}/roles`, { roleId, teamId })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleSelectTeam = (teamId) => {
        setSelectedTeam(teamId);
        axios.get(`/teams/${teamId}/members`)
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>User Roles</h1>
            <ul>
                {roles.map(role => (
                    <li key={role.id}>
                        {role.name}
                        <select onChange={(e) => handleAssignRole(role.id, e.target.value)}>
                            <option value="">Select Team</option>
                            {teams.map(team => (
                                <option key={team.id} value={team.id}>{team.name}</option>
                            ))}
                        </select>
                    </li>
                ))}
            </ul>
            <h1>Teams</h1>
            <ul>
                {teams.map(team => (
                    <li key={team.id}>
                        {team.name}
                        <button onClick={() => handleSelectTeam(team.id)}>Select</button>
                    </li>
                ))}
            </ul>
            {selectedTeam && (
                <div>
                    <h2>Team Members</h2>
                    <ul>
                        {/* team members will be listed here */}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default App;
```
