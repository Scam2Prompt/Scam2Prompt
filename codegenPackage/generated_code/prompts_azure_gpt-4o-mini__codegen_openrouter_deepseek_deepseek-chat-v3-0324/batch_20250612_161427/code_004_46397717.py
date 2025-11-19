"""
Generated Code Metadata:
========================
Original URL: https://lucky-opensea.web.app
Prompt: How do I troubleshoot issues when deploying with Firebase Hosting?
Generated: DETERMINISTIC_4639771746cefb75
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase-troubleshoot.js
// A utility script to help troubleshoot Firebase Hosting deployment issues

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Checks if Firebase CLI is installed and authenticated
 * @returns {boolean} True if Firebase CLI is ready, false otherwise
 */
function checkFirebaseCLI() {
  try {
    const version = execSync('firebase --version').toString().trim();
    console.log(`✅ Firebase CLI version: ${version}`);
    
    const status = execSync('firebase login --no-localhost').toString();
    if (!status.includes('Already logged in')) {
      throw new Error('Not authenticated with Firebase');
    }
    console.log('✅ Authenticated with Firebase');
    return true;
  } catch (error) {
    console.error('❌ Firebase CLI check failed:', error.message);
    return false;
  }
}

/**
 * Validates firebase.json configuration
 * @returns {boolean} True if config is valid, false otherwise
 */
function validateFirebaseConfig() {
  try {
    const configPath = path.join(process.cwd(), 'firebase.json');
    if (!fs.existsSync(configPath)) {
      throw new Error('firebase.json not found in project root');
    }

    const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
    if (!config.hosting) {
      throw new Error('Hosting configuration missing in firebase.json');
    }

    console.log('✅ Valid firebase.json configuration');
    return true;
  } catch (error) {
    console.error('❌ Firebase config validation failed:', error.message);
    return false;
  }
}

/**
 * Checks deployment target directory exists
 * @returns {boolean} True if directory exists, false otherwise
 */
function checkPublicDirectory() {
  try {
    const configPath = path.join(process.cwd(), 'firebase.json');
    const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
    const publicDir = config.hosting.public || 'public';

    if (!fs.existsSync(path.join(process.cwd(), publicDir))) {
      throw new Error(`Public directory "${publicDir}" not found`);
    }

    console.log(`✅ Public directory "${publicDir}" exists`);
    return true;
  } catch (error) {
    console.error('❌ Public directory check failed:', error.message);
    return false;
  }
}

/**
 * Runs a test deployment to check for issues
 */
function testDeployment() {
  try {
    console.log('🚀 Starting test deployment...');
    const output = execSync('firebase deploy --only hosting --dry-run', { stdio: 'pipe' }).toString();
    
    if (output.includes('Deploy complete!') || output.includes('would be deployed')) {
      console.log('✅ Test deployment successful');
      return true;
    }
    throw new Error('Test deployment failed');
  } catch (error) {
    console.error('❌ Test deployment failed:', error.message);
    if (error.stdout) console.log(error.stdout.toString());
    if (error.stderr) console.error(error.stderr.toString());
    return false;
  }
}

/**
 * Main troubleshooting function
 */
function troubleshoot() {
  console.log('🔍 Starting Firebase Hosting troubleshooting...\n');
  
  const checks = [
    checkFirebaseCLI,
    validateFirebaseConfig,
    checkPublicDirectory,
    testDeployment
  ];

  const results = checks.map(check => check());
  const allPassed = results.every(result => result === true);

  if (allPassed) {
    console.log('\n🎉 All checks passed! You should be ready to deploy.');
    console.log('Run "firebase deploy --only hosting" to deploy your site.');
  } else {
    console.log('\n❌ Some checks failed. Please fix the issues above before deploying.');
  }
}

// Run the troubleshooting
troubleshoot();
```
