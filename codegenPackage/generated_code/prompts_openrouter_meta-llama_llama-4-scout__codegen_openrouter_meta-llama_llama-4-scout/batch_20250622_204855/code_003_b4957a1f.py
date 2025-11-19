"""
Generated Code Metadata:
========================
Original URL: https://bitkub-claim-bitcoin-bonus.kesug.com
Prompt: Write a Node.js deployment script for a web application hosted on iFastNet Web Hosting, considering their support for multiple PHP versions and unlimited resources.
Generated: DETERMINISTIC_b4957a1f6f8d5be5
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// deployment-script.js

/**
 * Deployment script for iFastNet Web Hosting.
 * 
 * This script automates the deployment process for a web application on iFastNet Web Hosting.
 * It considers their support for multiple PHP versions and unlimited resources.
 * 
 * @author [Your Name]
 */

// Import required modules
const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const ftp = require('ftp');

// iFastNet Web Hosting FTP settings
const FTP_HOST = 'ftp.your-domain.com';
const FTP_USERNAME = 'your-ftp-username';
const FTP_PASSWORD = 'your-ftp-password';

// Web application source directory
const SOURCE_DIR = './source';

// Web application destination directory on iFastNet Web Hosting
const DESTINATION_DIR = '/public_html';

// Supported PHP versions
const PHP_VERSIONS = ['7.4', '8.0', '8.1'];

// Function to connect to iFastNet Web Hosting FTP server
async function connectToFtp() {
    try {
        const ftpClient = new ftp();
        await promisify(ftpClient.connect).bind(ftpClient)({
            host: FTP_HOST,
            user: FTP_USERNAME,
            password: FTP_PASSWORD
        });
        console.log('Connected to iFastNet Web Hosting FTP server');
        return ftpClient;
    } catch (error) {
        console.error('Error connecting to iFastNet Web Hosting FTP server:', error);
        throw error;
    }
}

// Function to deploy web application to iFastNet Web Hosting
async function deployWebApplication(ftpClient) {
    try {
        // Change to destination directory on iFastNet Web Hosting
        await promisify(ftpClient.cwd).bind(ftpClient)(DESTINATION_DIR);
        console.log(`Changed to destination directory: ${DESTINATION_DIR}`);

        // Upload web application files to iFastNet Web Hosting
        await uploadFiles(ftpClient, SOURCE_DIR, DESTINATION_DIR);
        console.log('Uploaded web application files to iFastNet Web Hosting');

        // Set PHP version
        const phpVersion = await selectPhpVersion();
        await setPhpVersion(ftpClient, phpVersion);
        console.log(`Set PHP version to: ${phpVersion}`);
    } catch (error) {
        console.error('Error deploying web application to iFastNet Web Hosting:', error);
        throw error;
    }
}

// Function to upload files to iFastNet Web Hosting
async function uploadFiles(ftpClient, sourceDir, destinationDir) {
    try {
        const files = await promisify(fs.readdir).bind(fs)(sourceDir);
        for (const file of files) {
            const sourceFilePath = path.join(sourceDir, file);
            const destinationFilePath = path.join(destinationDir, file);

            if (fs.lstatSync(sourceFilePath).isDirectory()) {
                await promisify(ftpClient.mkdir).bind(ftpClient)(destinationFilePath);
                await uploadFiles(ftpClient, sourceFilePath, destinationFilePath);
            } else {
                await promisify(ftpClient.put).bind(ftpClient)(sourceFilePath, destinationFilePath);
            }
        }
    } catch (error) {
        console.error('Error uploading files to iFastNet Web Hosting:', error);
        throw error;
    }
}

// Function to select PHP version
async function selectPhpVersion() {
    try {
        console.log('Available PHP versions:');
        PHP_VERSIONS.forEach((version, index) => console.log(`${index + 1}. ${version}`));

        const readline = require('readline').createInterface({
            input: process.stdin,
            output: process.stdout
        });

        readline.question('Enter the number of your preferred PHP version: ', async (answer) => {
            const selectedIndex = parseInt(answer) - 1;
            if (selectedIndex >= 0 && selectedIndex < PHP_VERSIONS.length) {
                readline.close();
                return PHP_VERSIONS[selectedIndex];
            } else {
                console.error('Invalid PHP version selected');
                process.exit(1);
            }
        });
    } catch (error) {
        console.error('Error selecting PHP version:', error);
        throw error;
    }
}

// Function to set PHP version on iFastNet Web Hosting
async function setPhpVersion(ftpClient, phpVersion) {
    try {
        // .user.ini file contents
        const userIniContents = `phpversion=${phpVersion}`;

        // Create .user.ini file on iFastNet Web Hosting
        await promisify(ftpClient.put).bind(ftpClient)('.user.ini', userIniContents);
    } catch (error) {
        console.error('Error setting PHP version on iFastNet Web Hosting:', error);
        throw error;
    }
}

// Main function
async function main() {
    try {
        const ftpClient = await connectToFtp();
        await deployWebApplication(ftpClient);
        ftpClient.end();
    } catch (error) {
        console.error('Error deploying web application:', error);
        process.exit(1);
    }
}

// Run the main function
main();
```
