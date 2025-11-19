"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Write code to create a collaborative pool maintenance logging system similar to the features described on Pooltyme, including user invitations and shared log history.
Generated: DETERMINISTIC_95d3c69ed2dfebea
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Collaborative Pool Maintenance Logging System**
=====================================================

**Database Schema**
------------------

```sql
CREATE TABLE Users (
  id INT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE Pools (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  owner_id INT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES Users(id)
);

CREATE TABLE Pool_Members (
  pool_id INT NOT NULL,
  user_id INT NOT NULL,
  role VARCHAR(255) NOT NULL CHECK (role IN ('owner', 'member')),
  PRIMARY KEY (pool_id, user_id),
  FOREIGN KEY (pool_id) REFERENCES Pools(id),
  FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Log_Entries (
  id INT PRIMARY KEY,
  pool_id INT NOT NULL,
  user_id INT NOT NULL,
  log_date DATE NOT NULL,
  description TEXT NOT NULL,
  FOREIGN KEY (pool_id) REFERENCES Pools(id),
  FOREIGN KEY (user_id) REFERENCES Users(id)
);
```

**Backend API (Node.js, Express.js)**
--------------------------------------

```javascript
const express = require('express');
const app = express();
const mysql = require('mysql');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'pool_maintenance'
});

db.connect((err) => {
  if (err) {
    console.error('error connecting:', err);
    return;
  }
  console.log('connected as id ' + db.threadId);
});

// Middleware
app.use(express.json());

// User Registration
app.post('/register', (req, res) => {
  const { username, email, password } = req.body;
  const hashedPassword = bcrypt.hashSync(password, 10);
  const query = 'INSERT INTO Users SET ?';
  db.query(query, { username, email, password: hashedPassword }, (err, results) => {
    if (err) {
      res.status(500).send({ message: 'Error registering user' });
    } else {
      res.send({ message: 'User registered successfully' });
    }
  });
});

// User Login
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  const query = 'SELECT * FROM Users WHERE email = ?';
  db.query(query, [email], (err, results) => {
    if (err || results.length === 0) {
      res.status(401).send({ message: 'Invalid email or password' });
    } else {
      const user = results[0];
      if (bcrypt.compareSync(password, user.password)) {
        const token = jwt.sign({ userId: user.id }, 'secret_key', {
          expiresIn: '1h'
        });
        res.send({ token });
      } else {
        res.status(401).send({ message: 'Invalid email or password' });
      }
    }
  });
});

// Create Pool
app.post('/pools', authenticate, (req, res) => {
  const { name } = req.body;
  const query = 'INSERT INTO Pools SET ?';
  db.query(query, { name, owner_id: req.user.userId }, (err, results) => {
    if (err) {
      res.status(500).send({ message: 'Error creating pool' });
    } else {
      res.send({ message: 'Pool created successfully' });
    }
  });
});

// Invite User to Pool
app.post('/pools/:poolId/invite', authenticate, (req, res) => {
  const poolId = req.params.poolId;
  const { email } = req.body;
  const query = 'SELECT * FROM Users WHERE email = ?';
  db.query(query, [email], (err, results) => {
    if (err || results.length === 0) {
      res.status(404).send({ message: 'User not found' });
    } else {
      const userId = results[0].id;
      const query = 'INSERT INTO Pool_Members SET ?';
      db.query(query, { pool_id: poolId, user_id: userId, role: 'member' }, (err, results) => {
        if (err) {
          res.status(500).send({ message: 'Error inviting user' });
        } else {
          res.send({ message: 'User invited successfully' });
        }
      });
    }
  });
});

// Get Pool Log History
app.get('/pools/:poolId/logs', authenticate, (req, res) => {
  const poolId = req.params.poolId;
  const query = 'SELECT * FROM Log_Entries WHERE pool_id = ?';
  db.query(query, [poolId], (err, results) => {
    if (err) {
      res.status(500).send({ message: 'Error fetching log history' });
    } else {
      res.send(results);
    }
  });
});

// Add Log Entry
app.post('/pools/:poolId/logs', authenticate, (req, res) => {
  const poolId = req.params.poolId;
  const { log_date, description } = req.body;
  const query = 'INSERT INTO Log_Entries SET ?';
  db.query(query, { pool_id: poolId, user_id: req.user.userId, log_date, description }, (err, results) => {
    if (err) {
      res.status(500).send({ message: 'Error adding log entry' });
    } else {
      res.send({ message: 'Log entry added successfully' });
    }
  });
});

// Authentication middleware
function authenticate(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secret_key');
    req.user = decoded;
    next();
  } catch (ex) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

**Frontend (React.js)**
------------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [pools, setPools] = useState([]);
  const [currentPool, setCurrentPool] = useState(null);
  const [logEntries, setLogEntries] = useState([]);
  const [newLogEntry, setNewLogEntry] = useState({});

  useEffect(() => {
    axios.get('/pools')
      .then(response => {
        setPools(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleCreatePool = () => {
    axios.post('/pools', { name: 'New Pool' })
      .then(response => {
        setPools([...pools, response.data]);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleSelectPool = (pool) => {
    setCurrentPool(pool);
    axios.get(`/pools/${pool.id}/logs`)
      .then(response => {
        setLogEntries(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleAddLogEntry = () => {
    axios.post(`/pools/${currentPool.id}/logs`, newLogEntry)
      .then(response => {
        setLogEntries([...logEntries, response.data]);
        setNewLogEntry({});
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Pools</h1>
      <ul>
        {pools.map(pool => (
          <li key={pool.id}>
            <button onClick={() => handleSelectPool(pool)}>{pool.name}</button>
          </li>
        ))}
        <li>
          <button onClick={handleCreatePool}>Create Pool</button>
        </li>
      </ul>
      {currentPool && (
        <div>
          <h2>Log Entries for {currentPool.name}</h2>
          <ul>
            {logEntries.map(logEntry => (
              <li key={logEntry.id}>{logEntry.log_date} - {logEntry.description}</li>
            ))}
          </ul>
          <form>
            <input
              type="date"
              value={newLogEntry.log_date}
              onChange={(e) => setNewLogEntry({ ...newLogEntry, log_date: e.target.value })}
            />
            <textarea
              value={newLogEntry.description}
              onChange={(e) => setNewLogEntry({ ...newLogEntry, description: e.target.value })}
            />
            <button onClick={handleAddLogEntry}>Add Log Entry</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default App;
```
