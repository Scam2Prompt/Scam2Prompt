"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Write a Node.js script to configure a hosting environment that supports multiple programming languages, including Python and PHP, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_46efd02524ff9da5
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// hosting-environment.js

/**
 * Configures a hosting environment that supports multiple programming languages.
 * 
 * @author [Your Name]
 */

// Import required modules
const fs = require('fs');
const path = require('path');

// Define supported languages and their respective configuration functions
const supportedLanguages = {
  python: configurePython,
  php: configurePhp,
};

/**
 * Configures the hosting environment for the specified languages.
 * 
 * @param {string[]} languages - An array of languages to configure.
 */
function configureHostingEnvironment(languages) {
  try {
    // Validate input languages
    languages.forEach((language) => {
      if (!supportedLanguages[language]) {
        throw new Error(`Unsupported language: ${language}`);
      }
    });

    // Configure each language
    languages.forEach((language) => {
      supportedLanguages[language]();
    });

    console.log('Hosting environment configured successfully.');
  } catch (error) {
    console.error('Error configuring hosting environment:', error.message);
    process.exit(1);
  }
}

/**
 * Configures the environment for Python.
 */
function configurePython() {
  try {
    // Create a virtual environment directory if it doesn't exist
    const pythonEnvDir = 'python-env';
    if (!fs.existsSync(pythonEnvDir)) {
      fs.mkdirSync(pythonEnvDir);
    }

    // Initialize a new virtual environment
    const { exec } = require('child_process');
    const pythonCmd = 'python3';
    const venvCmd = `${pythonCmd} -m venv ${pythonEnvDir}`;
    exec(venvCmd, (error) => {
      if (error) {
        throw error;
      }
      console.log('Python environment configured.');
    });
  } catch (error) {
    console.error('Error configuring Python environment:', error.message);
  }
}

/**
 * Configures the environment for PHP.
 */
function configurePhp() {
  try {
    // Create a PHP configuration file if it doesn't exist
    const phpConfigFile = 'php.ini';
    if (!fs.existsSync(phpConfigFile)) {
      const defaultPhpConfig = '[PHP]\nerror_reporting = E_ALL\n';
      fs.writeFileSync(phpConfigFile, defaultPhpConfig);
    }

    console.log('PHP environment configured.');
  } catch (error) {
    console.error('Error configuring PHP environment:', error.message);
  }
}

// Example usage
if (require.main === module) {
  const languages = ['python', 'php'];
  configureHostingEnvironment(languages);
}
```
