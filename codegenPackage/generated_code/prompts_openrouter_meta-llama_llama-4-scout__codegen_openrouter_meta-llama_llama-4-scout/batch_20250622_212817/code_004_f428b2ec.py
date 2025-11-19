"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Create a RESTful API in Node.js to manage projects and services for a digital agency like Phosphor.
Generated: DETERMINISTIC_f428b2ec2bb34849
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Project Management API**
==========================

**dependencies**
---------------

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `mongoose`: ^5.10.15
* `joi`: ^17.6.0

**project.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define project schema
const projectSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    trim: true
  },
  services: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Service'
    }
  ],
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Export project model
module.exports = mongoose.model('Project', projectSchema);
```

**service.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define service schema
const serviceSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    trim: true
  },
  projects: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Project'
    }
  ],
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Export service model
module.exports = mongoose.model('Service', serviceSchema);
```

**project.controller.js**
```javascript
// Import project model
const Project = require('./project.model');

// Import service model
const Service = require('./service.model');

// Joi validation
const Joi = require('joi');

// Define validation schema
const projectValidationSchema = Joi.object({
  name: Joi.string().required(),
  description: Joi.string().optional()
});

// Create a new project
exports.createProject = async (req, res) => {
  try {
    const { error } = projectValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const project = new Project(req.body);
    await project.save();
    res.status(201).send(project);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Get all projects
exports.getProjects = async (req, res) => {
  try {
    const projects = await Project.find().populate('services');
    res.status(200).send(projects);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Get a project by id
exports.getProject = async (req, res) => {
  try {
    const project = await Project.findById(req.params.projectId).populate('services');
    if (!project) {
      return res.status(404).send({ message: 'Project not found' });
    }
    res.status(200).send(project);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Update a project
exports.updateProject = async (req, res) => {
  try {
    const { error } = projectValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const project = await Project.findByIdAndUpdate(req.params.projectId, req.body, { new: true });
    if (!project) {
      return res.status(404).send({ message: 'Project not found' });
    }
    res.status(200).send(project);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Delete a project
exports.deleteProject = async (req, res) => {
  try {
    const project = await Project.findByIdAndRemove(req.params.projectId);
    if (!project) {
      return res.status(404).send({ message: 'Project not found' });
    }
    res.status(204).send();
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};
```

**service.controller.js**
```javascript
// Import service model
const Service = require('./service.model');

// Import project model
const Project = require('./project.model');

// Joi validation
const Joi = require('joi');

// Define validation schema
const serviceValidationSchema = Joi.object({
  name: Joi.string().required(),
  description: Joi.string().optional()
});

// Create a new service
exports.createService = async (req, res) => {
  try {
    const { error } = serviceValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const service = new Service(req.body);
    await service.save();
    res.status(201).send(service);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Get all services
exports.getServices = async (req, res) => {
  try {
    const services = await Service.find().populate('projects');
    res.status(200).send(services);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Get a service by id
exports.getService = async (req, res) => {
  try {
    const service = await Service.findById(req.params.serviceId).populate('projects');
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.status(200).send(service);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Update a service
exports.updateService = async (req, res) => {
  try {
    const { error } = serviceValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const service = await Service.findByIdAndUpdate(req.params.serviceId, req.body, { new: true });
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.status(200).send(service);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Delete a service
exports.deleteService = async (req, res) => {
  try {
    const service = await Service.findByIdAndRemove(req.params.serviceId);
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.status(204).send();
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};

// Associate a service with a project
exports.associateServiceWithProject = async (req, res) => {
  try {
    const project = await Project.findById(req.body.projectId);
    if (!project) {
      return res.status(404).send({ message: 'Project not found' });
    }

    const service = await Service.findById(req.params.serviceId);
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }

    project.services.push(service._id);
    await project.save();

    service.projects.push(project._id);
    await service.save();

    res.status(200).send({ message: 'Service associated with project successfully' });
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
};
```

**routes.js**
```javascript
// Import express
const express = require('express');

// Import project controller
const projectController = require('./project.controller');

// Import service controller
const serviceController = require('./service.controller');

// Create a router
const router = express.Router();

// Project routes
router.post('/projects', projectController.createProject);
router.get('/projects', projectController.getProjects);
router.get('/projects/:projectId', projectController.getProject);
router.put('/projects/:projectId', projectController.updateProject);
router.delete('/projects/:projectId', projectController.deleteProject);

// Service routes
router.post('/services', serviceController.createService);
router.get('/services', serviceController.getServices);
router.get('/services/:serviceId', serviceController.getService);
router.put('/services/:serviceId', serviceController.updateService);
router.delete('/services/:serviceId', serviceController.deleteService);

// Associate a service with a project
router.patch('/services/:serviceId/projects', serviceController.associateServiceWithProject);

// Export router
module.exports = router;
```

**app.js**
```javascript
// Import express
const express = require('express');

// Import mongoose
const mongoose = require('mongoose');

// Import routes
const routes = require('./routes');

// Create an express app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/phosphor', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error
