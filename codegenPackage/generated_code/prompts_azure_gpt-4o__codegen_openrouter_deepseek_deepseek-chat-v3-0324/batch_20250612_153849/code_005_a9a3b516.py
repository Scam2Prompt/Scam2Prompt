"""
Generated Code Metadata:
========================
Original URL: https://zeebu-governance.azurewebsites.net
Prompt: Create a JavaScript-based implementation to handle user authentication and permissions within the Zeebu Protocol governance framework.
Generated: DETERMINISTIC_a9a3b5160601b1b4
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// auth.js - Zeebu Protocol Governance Authentication Module

const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const { v4: uuidv4 } = require('uuid');
const { PermissionError, AuthError } = require('./errors');

// Configuration
const {
  JWT_SECRET = 'zeebu_protocol_secret_key',
  JWT_EXPIRES_IN = '1h',
  SALT_ROUNDS = 10
} = process.env;

// Mock database (in production, replace with actual database connection)
const users = [];
const roles = {
  ADMIN: ['create', 'read', 'update', 'delete', 'manage_users'],
  MEMBER: ['create', 'read', 'update'],
  GUEST: ['read']
};

/**
 * User model
 */
class User {
  constructor({ username, email, password, role = 'MEMBER' }) {
    this.id = uuidv4();
    this.username = username;
    this.email = email;
    this.password = this._hashPassword(password);
    this.role = role;
    this.createdAt = new Date();
    this.updatedAt = new Date();
    this.isActive = true;
  }

  _hashPassword(password) {
    return bcrypt.hashSync(password, parseInt(SALT_ROUNDS));
  }

  verifyPassword(password) {
    return bcrypt.compareSync(password, this.password);
  }
}

/**
 * Auth Service
 */
class AuthService {
  static async register(userData) {
    try {
      // Validate input
      if (!userData.username || !userData.email || !userData.password) {
        throw new AuthError('Missing required fields');
      }

      // Check if user exists
      const existingUser = users.find(u => u.email === userData.email);
      if (existingUser) {
        throw new AuthError('User already exists');
      }

      // Create new user
      const user = new User(userData);
      users.push(user);
      
      // Generate token
      const token = this.generateToken(user);
      return { user, token };
    } catch (error) {
      throw new AuthError(`Registration failed: ${error.message}`);
    }
  }

  static async login(email, password) {
    try {
      // Find user
      const user = users.find(u => u.email === email && u.isActive);
      if (!user) {
        throw new AuthError('Invalid credentials');
      }

      // Verify password
      if (!user.verifyPassword(password)) {
        throw new AuthError('Invalid credentials');
      }

      // Generate token
      const token = this.generateToken(user);
      return { user, token };
    } catch (error) {
      throw new AuthError(`Login failed: ${error.message}`);
    }
  }

  static generateToken(user) {
    const payload = {
      sub: user.id,
      username: user.username,
      role: user.role,
      iat: Math.floor(Date.now() / 1000)
    };

    return jwt.sign(payload, JWT_SECRET, { expiresIn: JWT_EXPIRES_IN });
  }

  static verifyToken(token) {
    try {
      return jwt.verify(token, JWT_SECRET);
    } catch (error) {
      throw new AuthError('Invalid or expired token');
    }
  }

  static async changePassword(userId, oldPassword, newPassword) {
    try {
      const user = users.find(u => u.id === userId);
      if (!user) {
        throw new AuthError('User not found');
      }

      if (!user.verifyPassword(oldPassword)) {
        throw new AuthError('Invalid current password');
      }

      user.password = bcrypt.hashSync(newPassword, parseInt(SALT_ROUNDS));
      user.updatedAt = new Date();
      return { success: true };
    } catch (error) {
      throw new AuthError(`Password change failed: ${error.message}`);
    }
  }
}

/**
 * Permission Middleware
 */
class PermissionMiddleware {
  static hasPermission(requiredPermission) {
    return (req, res, next) => {
      try {
        // Extract token from header
        const token = req.headers.authorization?.split(' ')[1];
        if (!token) {
          throw new AuthError('No token provided');
        }

        // Verify token
        const decoded = AuthService.verifyToken(token);

        // Check permissions
        const userRole = decoded.role;
        const userPermissions = roles[userRole] || [];

        if (!userPermissions.includes(requiredPermission)) {
          throw new PermissionError('Insufficient permissions');
        }

        // Attach user to request
        req.user = decoded;
        next();
      } catch (error) {
        next(error);
      }
    };
  }

  static isAdmin(req, res, next) {
    try {
      const token = req.headers.authorization?.split(' ')[1];
      if (!token) {
        throw new AuthError('No token provided');
      }

      const decoded = AuthService.verifyToken(token);
      if (decoded.role !== 'ADMIN') {
        throw new PermissionError('Admin access required');
      }

      req.user = decoded;
      next();
    } catch (error) {
      next(error);
    }
  }
}

module.exports = {
  AuthService,
  PermissionMiddleware,
  User
};
```

```javascript
// errors.js - Custom Error Classes
class AuthError extends Error {
  constructor(message) {
    super(message);
    this.name = 'AuthError';
    this.statusCode = 401;
  }
}

class PermissionError extends Error {
  constructor(message) {
    super(message);
    this.name = 'PermissionError';
    this.statusCode = 403;
  }
}

module.exports = {
  AuthError,
  PermissionError
};
```

```javascript
// index.js - Example Usage
const express = require('express');
const { AuthService, PermissionMiddleware } = require('./auth');
const { AuthError, PermissionError } = require('./errors');

const app = express();
app.use(express.json());

// Example routes
app.post('/register', async (req, res, next) => {
  try {
    const { user, token } = await AuthService.register(req.body);
    res.status(201).json({ user, token });
  } catch (error) {
    next(error);
  }
});

app.post('/login', async (req, res, next) => {
  try {
    const { email, password } = req.body;
    const { user, token } = await AuthService.login(email, password);
    res.json({ user, token });
  } catch (error) {
    next(error);
  }
});

app.get('/protected', 
  PermissionMiddleware.hasPermission('read'), 
  (req, res) => {
    res.json({ message: 'Access granted to protected route' });
  }
);

app.post('/admin-only', 
  PermissionMiddleware.isAdmin, 
  (req, res) => {
    res.json({ message: 'Admin access granted' });
  }
);

// Error handling middleware
app.use((err, req, res, next) => {
  if (err instanceof AuthError || err instanceof PermissionError) {
    return res.status(err.statusCode).json({ error: err.message });
  }
  res.status(500).json({ error: 'Internal server error' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
