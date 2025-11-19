"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Design a system to notify users of new missions and multipliers on MANTRA Zone using a library like Node.js and Express.js.
Generated: DETERMINISTIC_54dbc0e6ba916d09
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mission Notification System**
==========================

**dependencies:**
* Node.js
* Express.js
* MongoDB
* Nodemailer

**mission-notification-system.js**
```javascript
// Import required libraries
const express = require('express');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/mantra-zone', { useNewUrlParser: true, useUnifiedTopology: true });

// Define mission schema
const missionSchema = new mongoose.Schema({
  id: String,
  name: String,
  description: String,
  reward: Number,
  createdAt: Date
});

// Define user schema
const userSchema = new mongoose.Schema({
  id: String,
  email: String,
  missions: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Mission' }]
});

// Compile schemas into models
const Mission = mongoose.model('Mission', missionSchema);
const User = mongoose.model('User', userSchema);

// Create Express app
const app = express();
app.use(express.json());

// Define notification service
class NotificationService {
  async sendNotification(userEmail, mission) {
    try {
      // Create transporter for nodemailer
      const transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 587,
        secure: false, // or 'STARTTLS'
        auth: {
          user: 'your-email@gmail.com',
          pass: 'your-password'
        }
      });

      // Define email content
      const mailOptions = {
        from: 'MANTRA Zone <your-email@gmail.com>',
        to: userEmail,
        subject: `New Mission Alert: ${mission.name}`,
        text: `A new mission has been added: ${mission.name} - ${mission.description}`
      };

      // Send email
      await transporter.sendMail(mailOptions);
      console.log(`Notification sent to ${userEmail}`);
    } catch (error) {
      console.error(`Error sending notification: ${error.message}`);
    }
  }
}

// Initialize notification service
const notificationService = new NotificationService();

// API endpoint to create new mission
app.post('/missions', async (req, res) => {
  try {
    const mission = new Mission(req.body);
    await mission.save();

    // Find users interested in mission notifications
    const users = await User.find({});

    // Send notifications to users
    users.forEach(async (user) => {
      await notificationService.sendNotification(user.email, mission);
    });

    res.status(201).json({ message: 'Mission created successfully' });
  } catch (error) {
    console.error(`Error creating mission: ${error.message}`);
    res.status(500).json({ message: 'Error creating mission' });
  }
});

// API endpoint to create new user
app.post('/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.status(201).json({ message: 'User created successfully' });
  } catch (error) {
    console.error(`Error creating user: ${error.message}`);
    res.status(500).json({ message: 'Error creating user' });
  }
});

// API endpoint to get all missions
app.get('/missions', async (req, res) => {
  try {
    const missions = await Mission.find({});
    res.json(missions);
  } catch (error) {
    console.error(`Error fetching missions: ${error.message}`);
    res.status(500).json({ message: 'Error fetching missions' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**multiplier-notification-system.js**
```javascript
// Import required libraries
const express = require('express');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/mantra-zone', { useNewUrlParser: true, useUnifiedTopology: true });

// Define multiplier schema
const multiplierSchema = new mongoose.Schema({
  id: String,
  name: String,
  description: String,
  reward: Number,
  createdAt: Date
});

// Define user schema
const userSchema = new mongoose.Schema({
  id: String,
  email: String,
  multipliers: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Multiplier' }]
});

// Compile schemas into models
const Multiplier = mongoose.model('Multiplier', multiplierSchema);
const User = mongoose.model('User', userSchema);

// Create Express app
const app = express();
app.use(express.json());

// Define notification service
class NotificationService {
  async sendNotification(userEmail, multiplier) {
    try {
      // Create transporter for nodemailer
      const transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 587,
        secure: false, // or 'STARTTLS'
        auth: {
          user: 'your-email@gmail.com',
          pass: 'your-password'
        }
      });

      // Define email content
      const mailOptions = {
        from: 'MANTRA Zone <your-email@gmail.com>',
        to: userEmail,
        subject: `New Multiplier Alert: ${multiplier.name}`,
        text: `A new multiplier has been added: ${multiplier.name} - ${multiplier.description}`
      };

      // Send email
      await transporter.sendMail(mailOptions);
      console.log(`Notification sent to ${userEmail}`);
    } catch (error) {
      console.error(`Error sending notification: ${error.message}`);
    }
  }
}

// Initialize notification service
const notificationService = new NotificationService();

// API endpoint to create new multiplier
app.post('/multipliers', async (req, res) => {
  try {
    const multiplier = new Multiplier(req.body);
    await multiplier.save();

    // Find users interested in multiplier notifications
    const users = await User.find({});

    // Send notifications to users
    users.forEach(async (user) => {
      await notificationService.sendNotification(user.email, multiplier);
    });

    res.status(201).json({ message: 'Multiplier created successfully' });
  } catch (error) {
    console.error(`Error creating multiplier: ${error.message}`);
    res.status(500).json({ message: 'Error creating multiplier' });
  }
});

// Start server
const port = 3001;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Dockerfile**
```dockerfile
FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000
EXPOSE 3001

CMD ["node", "mission-notification-system.js"]
CMD ["node", "multiplier-notification-system.js"]
```

**docker-compose.yml**
```yml
version: '3'

services:
  mission-notification-system:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - mongo
    environment:
      - DATABASE_URL=mongodb://mongo:27017/mantra-zone

  multiplier-notification-system:
    build: .
    ports:
      - "3001:3001"
    depends_on:
      - mongo
    environment:
      - DATABASE_URL=mongodb://mongo:27017/mantra-zone

  mongo:
    image: mongo:4.4
    volumes:
      - mongo-data:/data/db
    ports:
      - "27017:27017"

volumes:
  mongo-data:
```

**package.json**
```json
{
  "name": "mission-notification-system",
  "version": "1.0.0",
  "scripts": {
    "start": "node mission-notification-system.js",
    "start:multiplier": "node multiplier-notification-system.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.10.15",
    "nodemailer": "^6.4.11"
  }
}
```
