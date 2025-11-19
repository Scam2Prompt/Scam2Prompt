"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Develop a Node.js module for automating tasks related to bloc administration, such as scheduling maintenance and cleaning services, based on BlocPrest's offerings."
Generated: DETERMINISTIC_20e1989359a41898
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bloc-admin.js
// Node.js module for automating bloc administration tasks

const { EventEmitter } = require('events');
const { scheduleJob } = require('node-schedule');
const { v4: uuidv4 } = require('uuid');

/**
 * BlocAdmin class for managing bloc administration tasks
 */
class BlocAdmin extends EventEmitter {
  /**
   * @constructor
   * @param {Object} config - Configuration object
   * @param {string} config.blocId - Unique identifier for the bloc
   * @param {Object} config.services - Services configuration
   * @param {Array} config.services.maintenance - Maintenance services schedule
   * @param {Array} config.services.cleaning - Cleaning services schedule
   */
  constructor(config) {
    super();
    if (!config || !config.blocId) {
      throw new Error('Configuration with blocId is required');
    }

    this.blocId = config.blocId;
    this.services = config.services || {};
    this.scheduledJobs = {};
    this.initializeServices();
  }

  /**
   * Initialize scheduled services
   */
  initializeServices() {
    if (this.services.maintenance) {
      this.scheduleServices('maintenance', this.services.maintenance);
    }

    if (this.services.cleaning) {
      this.scheduleServices('cleaning', this.services.cleaning);
    }
  }

  /**
   * Schedule services of a specific type
   * @param {string} serviceType - Type of service (maintenance/cleaning)
   * @param {Array} schedules - Array of schedule configurations
   */
  scheduleServices(serviceType, schedules) {
    if (!Array.isArray(schedules)) {
      throw new Error('Schedules must be an array');
    }

    schedules.forEach((schedule, index) => {
      const jobId = `${serviceType}-${uuidv4()}`;
      try {
        const job = scheduleJob(schedule.cron, () => {
          this.emit('serviceTriggered', {
            blocId: this.blocId,
            serviceType,
            schedule,
            timestamp: new Date()
          });
        });

        this.scheduledJobs[jobId] = job;
        this.emit('serviceScheduled', {
          blocId: this.blocId,
          serviceType,
          jobId,
          schedule,
          timestamp: new Date()
        });
      } catch (err) {
        this.emit('error', {
          error: err,
          message: `Failed to schedule ${serviceType} service`,
          blocId: this.blocId
        });
      }
    });
  }

  /**
   * Cancel all scheduled jobs
   */
  cancelAllJobs() {
    Object.keys(this.scheduledJobs).forEach(jobId => {
      this.scheduledJobs[jobId].cancel();
      delete this.scheduledJobs[jobId];
    });
    this.emit('allJobsCancelled', {
      blocId: this.blocId,
      timestamp: new Date()
    });
  }

  /**
   * Cancel a specific job by ID
   * @param {string} jobId - ID of the job to cancel
   */
  cancelJob(jobId) {
    if (!this.scheduledJobs[jobId]) {
      throw new Error(`Job with ID ${jobId} not found`);
    }

    this.scheduledJobs[jobId].cancel();
    delete this.scheduledJobs[jobId];
    this.emit('jobCancelled', {
      blocId: this.blocId,
      jobId,
      timestamp: new Date()
    });
  }

  /**
   * Get list of all scheduled jobs
   * @returns {Array} Array of scheduled jobs
   */
  getScheduledJobs() {
    return Object.keys(this.scheduledJobs).map(jobId => ({
      jobId,
      nextInvocation: this.scheduledJobs[jobId].nextInvocation()
    }));
  }
}

module.exports = BlocAdmin;
```

```javascript
// index.js
// Main export file for the bloc-admin module

const BlocAdmin = require('./bloc-admin');

/**
 * Create a new BlocAdmin instance
 * @param {Object} config - Configuration object
 * @returns {BlocAdmin} New BlocAdmin instance
 */
function createBlocAdmin(config) {
  return new BlocAdmin(config);
}

module.exports = {
  BlocAdmin,
  createBlocAdmin
};
```

```javascript
// package.json
// Required package configuration
{
  "name": "bloc-admin",
  "version": "1.0.0",
  "description": "Node.js module for automating bloc administration tasks",
  "main": "index.js",
  "scripts": {
    "test": "jest"
  },
  "dependencies": {
    "node-schedule": "^2.1.0",
    "uuid": "^8.3.2"
  },
  "devDependencies": {
    "jest": "^27.0.6"
  },
  "keywords": [
    "bloc",
    "administration",
    "automation",
    "scheduling"
  ],
  "author": "Your Name",
  "license": "MIT"
}
```

```javascript
// test/bloc-admin.test.js
// Test suite for BlocAdmin module

const { BlocAdmin, createBlocAdmin } = require('../index');
const { EventEmitter } = require('events');

describe('BlocAdmin', () => {
  let blocAdmin;
  const testConfig = {
    blocId: 'test-bloc-123',
    services: {
      maintenance: [
        { cron: '* * * * *', description: 'Monthly maintenance' }
      ],
      cleaning: [
        { cron: '0 0 * * *', description: 'Daily cleaning' }
      ]
    }
  };

  beforeEach(() => {
    blocAdmin = new BlocAdmin(testConfig);
  });

  test('should be instance of EventEmitter', () => {
    expect(blocAdmin).toBeInstanceOf(EventEmitter);
  });

  test('should initialize with correct blocId', () => {
    expect(blocAdmin.blocId).toBe(testConfig.blocId);
  });

  test('should schedule services on initialization', () => {
    const jobs = blocAdmin.getScheduledJobs();
    expect(jobs.length).toBe(2);
  });

  test('should emit serviceScheduled event', (done) => {
    blocAdmin.on('serviceScheduled', (event) => {
      expect(event.blocId).toBe(testConfig.blocId);
      expect(event.serviceType).toBeDefined();
      done();
    });
  });

  test('should cancel all jobs', () => {
    blocAdmin.cancelAllJobs();
    expect(blocAdmin.getScheduledJobs().length).toBe(0);
  });

  test('createBlocAdmin should return BlocAdmin instance', () => {
    const instance = createBlocAdmin(testConfig);
    expect(instance).toBeInstanceOf(BlocAdmin);
  });
});
```
