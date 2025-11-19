"""
Generated Code Metadata:
========================
Original URL: https://corn-staging.com
Prompt: "Write an example of how to deploy a prebuilt asset to Cloudflare Pages using the Wrangler CLI."
Generated: DETERMINISTIC_1e594482fab31509
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// Configuration
const config = {
  projectName: 'my-project',
  buildDir: path.join(__dirname, 'dist'),
  accountId: process.env.CLOUDFLARE_ACCOUNT_ID,
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
  branch: 'production',
  commitHash: process.env.COMMIT_HASH || 'latest',
  wranglerVersion: '3.0.0'
};

/**
 * Deploy prebuilt assets to Cloudflare Pages using Wrangler CLI
 * @throws {Error} If deployment fails
 */
function deployToCloudflarePages() {
  try {
    // Validate required environment variables
    if (!config.accountId || !config.apiToken) {
      throw new Error('Missing required environment variables: CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN');
    }

    // Verify build directory exists
    if (!fs.existsSync(config.buildDir)) {
      throw new Error(`Build directory not found at ${config.buildDir}`);
    }

    // Install Wrangler CLI if not already installed
    try {
      execSync('wrangler --version');
    } catch {
      console.log('Installing Wrangler CLI...');
      execSync(`npm install -g wrangler@${config.wranglerVersion}`);
    }

    // Execute deployment command
    console.log('Deploying to Cloudflare Pages...');
    const deployCommand = [
      'wrangler pages deploy',
      `--project-name=${config.projectName}`,
      `--branch=${config.branch}`,
      `--commit-hash=${config.commitHash}`,
      `--account-id=${config.accountId}`,
      `--api-token=${config.apiToken}`,
      config.buildDir
    ].join(' ');

    const output = execSync(deployCommand, { stdio: 'inherit' });
    console.log('Deployment successful!');
    return output;
  } catch (error) {
    console.error('Deployment failed:', error.message);
    throw error;
  }
}

// Execute deployment
if (require.main === module) {
  deployToCloudflarePages();
}

module.exports = { deployToCloudflarePages };
```
