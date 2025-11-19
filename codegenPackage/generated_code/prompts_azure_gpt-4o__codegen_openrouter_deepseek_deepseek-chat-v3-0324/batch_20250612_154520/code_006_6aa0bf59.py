"""
Generated Code Metadata:
========================
Original URL: https://skymavis-ron.rf.gd
Prompt: Generate a Node.js application deployment script for a hosting service that supports unlimited bandwidth and disk space, as described on iFastNet.
Generated: DETERMINISTIC_6aa0bf594128e81d
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const readline = require('readline');

// Configuration constants
const DEPLOYMENT_CONFIG = '.deploymentrc';
const DEFAULT_CONFIG = {
  remoteHost: '',
  remoteUser: '',
  remotePath: '/',
  localPath: './dist',
  exclude: ['node_modules', '.git', '.env'],
};

// Colors for console output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
};

/**
 * Load or create deployment configuration
 */
function loadConfig() {
  try {
    if (fs.existsSync(DEPLOYMENT_CONFIG)) {
      const config = JSON.parse(fs.readFileSync(DEPLOYMENT_CONFIG, 'utf8'));
      return { ...DEFAULT_CONFIG, ...config };
    }

    console.log(`${colors.yellow}No deployment configuration found. Creating new one...${colors.reset}`);
    const config = { ...DEFAULT_CONFIG };

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    return new Promise((resolve) => {
      rl.question(`${colors.blue}Enter remote host (e.g., example.com): ${colors.reset}`, (remoteHost) => {
        config.remoteHost = remoteHost;
        rl.question(`${colors.blue}Enter remote username: ${colors.reset}`, (remoteUser) => {
          config.remoteUser = remoteUser;
          rl.question(`${colors.blue}Enter remote path (default: /): ${colors.reset}`, (remotePath) => {
            config.remotePath = remotePath || '/';
            rl.question(`${colors.blue}Enter local path to deploy (default: ./dist): ${colors.reset}`, (localPath) => {
              config.localPath = localPath || './dist';
              rl.close();

              fs.writeFileSync(DEPLOYMENT_CONFIG, JSON.stringify(config, null, 2));
              console.log(`${colors.green}Configuration saved to ${DEPLOYMENT_CONFIG}${colors.reset}`);
              resolve(config);
            });
          });
        });
      });
    });
  } catch (error) {
    console.error(`${colors.red}Error loading configuration: ${error.message}${colors.reset}`);
    process.exit(1);
  }
}

/**
 * Validate deployment configuration
 */
function validateConfig(config) {
  if (!config.remoteHost || !config.remoteUser) {
    console.error(`${colors.red}Error: Remote host and user are required${colors.reset}`);
    process.exit(1);
  }

  if (!fs.existsSync(config.localPath)) {
    console.error(`${colors.red}Error: Local path ${config.localPath} does not exist${colors.reset}`);
    process.exit(1);
  }
}

/**
 * Build exclusion parameters for rsync
 */
function buildExcludeParams(excludeList) {
  return excludeList.map(item => `--exclude=${item}`).join(' ');
}

/**
 * Deploy application using rsync
 */
async function deploy() {
  try {
    const config = await loadConfig();
    validateConfig(config);

    console.log(`${colors.blue}Starting deployment to ${config.remoteHost}...${colors.reset}`);

    // Build rsync command
    const excludeParams = buildExcludeParams(config.exclude);
    const command = `rsync -avz --progress ${excludeParams} ${config.localPath}/ ${config.remoteUser}@${config.remoteHost}:${config.remotePath}`;

    console.log(`${colors.yellow}Executing: ${command}${colors.reset}`);
    execSync(command, { stdio: 'inherit' });

    console.log(`${colors.green}Deployment completed successfully!${colors.reset}`);
  } catch (error) {
    console.error(`${colors.red}Deployment failed: ${error.message}${colors.reset}`);
    process.exit(1);
  }
}

// Run deployment
deploy();
```
