"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Develop a web application for tracking time and billing for lawyers, incorporating features like those described on BillYourTime.com.
Generated: DETERMINISTIC_310311373ebb1007
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Time Tracking and Billing Application for Lawyers**
=====================================================

**Backend (Node.js, Express.js, MongoDB)**
-----------------------------------------

### Dependencies

*   `express`: ^4.17.1
*   `mongodb`: ^3.6.4
*   `mongoose`: ^5.10.15
*   `bcrypt`: ^5.0.1
*   `jsonwebtoken`: ^8.5.1

### Models

```javascript
// models/User.js
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    role: { type: String, enum: ['lawyer', 'admin'], default: 'lawyer' },
});

userSchema.pre('save', async function(next) {
    if (this.isNew || this.isModified('password')) {
        this.password = await bcrypt.hash(this.password, 10);
    }
    next();
});

const User = mongoose.model('User', userSchema);

module.exports = User;
```

```javascript
// models/Client.js
const mongoose = require('mongoose');

const clientSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    projects: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Project' }],
});

const Client = mongoose.model('Client', clientSchema);

module.exports = Client;
```

```javascript
// models/Project.js
const mongoose = require('mongoose');

const projectSchema = new mongoose.Schema({
    name: { type: String, required: true },
    client: { type: mongoose.Schema.Types.ObjectId, ref: 'Client' },
    tasks: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Task' }],
});

const Project = mongoose.model('Project', projectSchema);

module.exports = Project;
```

```javascript
// models/Task.js
const mongoose = require('mongoose');

const taskSchema = new mongoose.Schema({
    name: { type: String, required: true },
    project: { type: mongoose.Schema.Types.ObjectId, ref: 'Project' },
    timeEntries: [{ type: mongoose.Schema.Types.ObjectId, ref: 'TimeEntry' }],
});

const Task = mongoose.model('Task', taskSchema);

module.exports = Task;
```

```javascript
// models/TimeEntry.js
const mongoose = require('mongoose');

const timeEntrySchema = new mongoose.Schema({
    task: { type: mongoose.Schema.Types.ObjectId, ref: 'Task' },
    date: { type: Date, required: true },
    hours: { type: Number, required: true },
    description: { type: String },
});

const TimeEntry = mongoose.model('TimeEntry', timeEntrySchema);

module.exports = TimeEntry;
```

### Controllers

```javascript
// controllers/AuthController.js
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

router.post('/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        const user = new User({ name, email, password });
        await user.save();
        res.status(201).send({ message: 'User created successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error creating user' });
    }
});

router.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).send({ message: 'Invalid credentials' });
        }
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, {
            expiresIn: '1h',
        });
        res.send({ token });
    } catch (error) {
        res.status(400).send({ message: 'Error logging in' });
    }
});

module.exports = router;
```

```javascript
// controllers/ClientController.js
const express = require('express');
const router = express.Router();
const Client = require('../models/Client');

router.get('/', async (req, res) => {
    try {
        const clients = await Client.find().populate('projects');
        res.send(clients);
    } catch (error) {
        res.status(400).send({ message: 'Error fetching clients' });
    }
});

router.post('/', async (req, res) => {
    try {
        const { name, email } = req.body;
        const client = new Client({ name, email });
        await client.save();
        res.status(201).send(client);
    } catch (error) {
        res.status(400).send({ message: 'Error creating client' });
    }
});

module.exports = router;
```

```javascript
// controllers/ProjectController.js
const express = require('express');
const router = express.Router();
const Project = require('../models/Project');
const Client = require('../models/Client');

router.get('/', async (req, res) => {
    try {
        const projects = await Project.find().populate('client').populate('tasks');
        res.send(projects);
    } catch (error) {
        res.status(400).send({ message: 'Error fetching projects' });
    }
});

router.post('/', async (req, res) => {
    try {
        const { name, clientId } = req.body;
        const client = await Client.findById(clientId);
        if (!client) {
            return res.status(404).send({ message: 'Client not found' });
        }
        const project = new Project({ name, client: client._id });
        await project.save();
        client.projects.push(project._id);
        await client.save();
        res.status(201).send(project);
    } catch (error) {
        res.status(400).send({ message: 'Error creating project' });
    }
});

module.exports = router;
```

```javascript
// controllers/TaskController.js
const express = require('express');
const router = express.Router();
const Task = require('../models/Task');
const Project = require('../models/Project');

router.get('/', async (req, res) => {
    try {
        const tasks = await Task.find().populate('project').populate('timeEntries');
        res.send(tasks);
    } catch (error) {
        res.status(400).send({ message: 'Error fetching tasks' });
    }
});

router.post('/', async (req, res) => {
    try {
        const { name, projectId } = req.body;
        const project = await Project.findById(projectId);
        if (!project) {
            return res.status(404).send({ message: 'Project not found' });
        }
        const task = new Task({ name, project: project._id });
        await task.save();
        project.tasks.push(task._id);
        await project.save();
        res.status(201).send(task);
    } catch (error) {
        res.status(400).send({ message: 'Error creating task' });
    }
});

module.exports = router;
```

```javascript
// controllers/TimeEntryController.js
const express = require('express');
const router = express.Router();
const TimeEntry = require('../models/TimeEntry');
const Task = require('../models/Task');

router.get('/', async (req, res) => {
    try {
        const timeEntries = await TimeEntry.find().populate('task');
        res.send(timeEntries);
    } catch (error) {
        res.status(400).send({ message: 'Error fetching time entries' });
    }
});

router.post('/', async (req, res) => {
    try {
        const { taskId, date, hours, description } = req.body;
        const task = await Task.findById(taskId);
        if (!task) {
            return res.status(404).send({ message: 'Task not found' });
        }
        const timeEntry = new TimeEntry({ task: task._id, date, hours, description });
        await timeEntry.save();
        task.timeEntries.push(timeEntry._id);
        await task.save();
        res.status(201).send(timeEntry);
    } catch (error) {
        res.status(400).send({ message: 'Error creating time entry' });
    }
});

module.exports = router;
```

### Routes

```javascript
// routes/index.js
const express = require('express');
const router = express.Router();
const authController = require('../controllers/AuthController');
const clientController = require('../controllers/ClientController');
const projectController = require('../controllers/ProjectController');
const taskController = require('../controllers/TaskController');
const timeEntryController = require('../controllers/TimeEntryController');

router.use('/api/auth', authController);
router.use('/api/clients', clientController);
router.use('/api/projects', projectController);
router.use('/api/tasks', taskController);
router.use('/api/time-entries', timeEntryController);

module.exports = router;
```

### Server

```javascript
// server.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const routes = require('./routes/index');

mongoose.connect('mongodb://localhost/time-tracking
