"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lisk-snapshot.vercel.app
Prompt: Generate a script utilizing the `@liskhq/lisk-framework-dashboard-plugin` (v0.4.0) to monitor blockchain activity and display real-time statistics.
Generated: DETERMINISTIC_5ac11652113ae570
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Lisk SDK
const { Application } = require('@liskhq/lisk-framework');
const { DashboardPlugin } = require('@liskhq/lisk-framework-dashboard-plugin');

// Define the configuration for the application
const config = {
    // Configuration for the Dashboard plugin
    plugins: [
        {
            module: DashboardPlugin,
            options: {
                // Port where the dashboard will be hosted
                port: 3000,
                // Optional: You can set a specific endpoint for monitoring blockchain activity
                monitoring: true,
            },
        },
    ],
};

// Function to start the Lisk application
const startApplication = async () => {
    try {
        // Create a new Lisk application instance with the defined config
        const app = Application.default(config);

        // Run the application
        await app.run();

        console.log('Lisk application is running with Dashboard on port 3000');
    } catch (error) {
        // Handle any errors that occur during application startup
        console.error('Error starting the Lisk application:', error);
        process.exit(1); // Exit the process with an error code
    }
};

// Execute the function to start the application
startApplication();
```

Make sure to have the necessary dependencies installed in your project:

```bash
npm install @liskhq/lisk-framework @liskhq/lisk-framework-dashboard-plugin
```

To run the script, ensure you have a valid Lisk network configuration in place and execute the script using Node.js:

```bash
node your_script_name.js
```
