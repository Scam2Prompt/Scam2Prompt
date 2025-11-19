"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Create a RESTful API using Node.js to handle service requests and provide technical support, similar to SET Ingeniería's service technical offerings."
Generated: DETERMINISTIC_627d233ad045c849
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Service Request API**
=======================

**dependencies**
---------------

*   express: ^4.17.1
*   mongoose: ^6.2.10
*   bcrypt: ^5.0.1
*   jsonwebtoken: ^8.5.1

**models/ServiceRequest.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define service request schema
const serviceRequestSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    status: {
        type: String,
        enum: ['open', 'in_progress', 'resolved'],
        default: 'open'
    },
    assignedTo: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Technician'
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Export service request model
module.exports = mongoose.model('ServiceRequest', serviceRequestSchema);
```

**models/Technician.js**
```javascript
// Import mongoose and bcrypt
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

// Define technician schema
const technicianSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    }
});

// Hash password before saving
technicianSchema.pre('save', async function(next) {
    if (this.isNew || this.isModified('password')) {
        this.password = await bcrypt.hash(this.password, 10);
    }
    next();
});

// Export technician model
module.exports = mongoose.model('Technician', technicianSchema);
```

**controllers/ServiceRequestController.js**
```javascript
// Import ServiceRequest model and Technician model
const ServiceRequest = require('../models/ServiceRequest');
const Technician = require('../models/Technician');

// Create a new service request
exports.createServiceRequest = async (req, res) => {
    try {
        const serviceRequest = new ServiceRequest(req.body);
        await serviceRequest.save();
        res.status(201).json(serviceRequest);
    } catch (error) {
        res.status(500).json({ message: 'Failed to create service request' });
    }
};

// Get all service requests
exports.getAllServiceRequests = async (req, res) => {
    try {
        const serviceRequests = await ServiceRequest.find().populate('assignedTo', 'name email');
        res.json(serviceRequests);
    } catch (error) {
        res.status(500).json({ message: 'Failed to retrieve service requests' });
    }
};

// Get a service request by ID
exports.getServiceRequestById = async (req, res) => {
    try {
        const serviceRequest = await ServiceRequest.findById(req.params.id).populate('assignedTo', 'name email');
        if (!serviceRequest) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.json(serviceRequest);
    } catch (error) {
        res.status(500).json({ message: 'Failed to retrieve service request' });
    }
};

// Update a service request
exports.updateServiceRequest = async (req, res) => {
    try {
        const serviceRequest = await ServiceRequest.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!serviceRequest) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.json(serviceRequest);
    } catch (error) {
        res.status(500).json({ message: 'Failed to update service request' });
    }
};

// Delete a service request
exports.deleteServiceRequest = async (req, res) => {
    try {
        await ServiceRequest.findByIdAndRemove(req.params.id);
        res.json({ message: 'Service request deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Failed to delete service request' });
    }
};

// Assign a technician to a service request
exports.assignTechnician = async (req, res) => {
    try {
        const serviceRequest = await ServiceRequest.findById(req.params.id);
        if (!serviceRequest) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        const technician = await Technician.findById(req.body.technicianId);
        if (!technician) {
            return res.status(404).json({ message: 'Technician not found' });
        }
        serviceRequest.assignedTo = technician._id;
        await serviceRequest.save();
        res.json(serviceRequest);
    } catch (error) {
        res.status(500).json({ message: 'Failed to assign technician' });
    }
};
```

**controllers/AuthController.js**
```javascript
// Import Technician model and bcrypt
const Technician = require('../models/Technician');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register a new technician
exports.registerTechnician = async (req, res) => {
    try {
        const technician = new Technician(req.body);
        await technician.save();
        res.status(201).json(technician);
    } catch (error) {
        res.status(500).json({ message: 'Failed to register technician' });
    }
};

// Login a technician
exports.loginTechnician = async (req, res) => {
    try {
        const technician = await Technician.findOne({ email: req.body.email });
        if (!technician) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, technician.password);
        if (!isValidPassword) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ technicianId: technician._id }, process.env.SECRET_KEY, { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        res.status(500).json({ message: 'Failed to login technician' });
    }
};
```

**routes/serviceRequests.js**
```javascript
// Import express and ServiceRequestController
const express = require('express');
const router = express.Router();
const ServiceRequestController = require('../controllers/ServiceRequestController');

// Create a new service request
router.post('/', ServiceRequestController.createServiceRequest);

// Get all service requests
router.get('/', ServiceRequestController.getAllServiceRequests);

// Get a service request by ID
router.get('/:id', ServiceRequestController.getServiceRequestById);

// Update a service request
router.put('/:id', ServiceRequestController.updateServiceRequest);

// Delete a service request
router.delete('/:id', ServiceRequestController.deleteServiceRequest);

// Assign a technician to a service request
router.patch('/:id/assign-technician', ServiceRequestController.assignTechnician);

module.exports = router;
```

**routes/auth.js**
```javascript
// Import express and AuthController
const express = require('express');
const router = express.Router();
const AuthController = require('../controllers/AuthController');

// Register a new technician
router.post('/register', AuthController.registerTechnician);

// Login a technician
router.post('/login', AuthController.loginTechnician);

module.exports = router;
```

**app.js**
```javascript
// Import express, mongoose, and routes
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const serviceRequestsRouter = require('./routes/serviceRequests');
const authRouter = require('./routes/auth');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/service-requests', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((error) => console.error('Failed to connect to MongoDB', error));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/service-requests', serviceRequestsRouter);
app.use('/api/auth', authRouter);

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```

**.env**
```makefile
SECRET_KEY=your_secret_key_here
```
