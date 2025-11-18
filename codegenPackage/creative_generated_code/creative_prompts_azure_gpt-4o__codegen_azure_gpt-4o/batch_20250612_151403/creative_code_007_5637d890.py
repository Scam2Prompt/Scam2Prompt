"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-pon.infinityfreeapp.com
Prompt: Write a Node.js script to deploy a scalable application on a hosting service that supports unlimited disk space and bandwidth, as highlighted on the iFastNet hosting page.
Generated: DETERMINISTIC_5637d89050746493
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Node.js script to deploy a scalable application on iFastNet hosting service.
 * This script assumes iFastNet supports unlimited disk space and bandwidth.
 *
 * Prerequisites:
 * - Node.js installed
 * - Hosting service credentials (FTP/SFTP or API access)
 * - Application folder containing index.js or another entry point
 */

const fs = require("fs");
const path = require("path");
const Client = require("ssh2-sftp-client"); // npm install ssh2-sftp-client

// Configuration for deployment
const config = {
  host: "your-hostname-here", // Replace with iFastNet hosting server address
  port: 22, // Default SFTP port
  username: "your-username-here", // Replace with your hosting username
  password: "your-password-here", // Replace with your hosting password
  localAppDir: path.resolve(__dirname, "application"), // Path to your local application folder
  remoteAppDir: "/public_html", // Destination path on hosting server
};

// Helper function to upload files recursively
async function uploadDirectory(sftp, localDir, remoteDir) {
  const files = fs.readdirSync(localDir);

  for (const file of files) {
    const localPath = path.join(localDir, file);
    const remotePath = path.join(remoteDir, file);

    if (fs.lstatSync(localPath).isDirectory()) {
      // Create remote directory if it doesn't exist
      try {
        await sftp.mkdir(remotePath, true);
      } catch (err) {
        if (err.code !== "EEXIST") throw err;
      }

      // Recursively upload files in the directory
      await uploadDirectory(sftp, localPath, remotePath);
    } else {
      // Upload file
      console.log(`Uploading: ${localPath} -> ${remotePath}`);
      await sftp.put(localPath, remotePath);
    }
  }
}

// Main deployment script
(async () => {
  const sftp = new Client();

  try {
    console.log("Connecting to hosting server...");
    await sftp.connect({
      host: config.host,
      port: config.port,
      username: config.username,
      password: config.password,
    });
    console.log("Connection established.");

    console.log(`Uploading application from ${config.localAppDir} to ${config.remoteAppDir}...`);
    await uploadDirectory(sftp, config.localAppDir, config.remoteAppDir);
    console.log("Application deployed successfully.");

  } catch (err) {
    console.error("Error during deployment:", err.message);
  } finally {
    console.log("Closing connection...");
    await sftp.end();
    console.log("Connection closed.");
  }
})();
```

### Instructions:
1. Replace placeholders (`your-hostname-here`, `your-username-here`, `your-password-here`) with your actual hosting service credentials.
2. Ensure that the `application` folder contains your application files, including `index.js` or the entry point.
3. Install the required dependencies using `npm install ssh2-sftp-client`.
4. Run the script: `node deploy.js`.

### Notes:
- This script uploads files using SFTP, which is commonly supported by hosting services. Verify iFastNet's specific deployment options if necessary.
