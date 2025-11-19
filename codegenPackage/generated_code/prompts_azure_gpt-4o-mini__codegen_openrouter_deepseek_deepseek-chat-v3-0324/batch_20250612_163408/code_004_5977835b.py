"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Develop a code snippet that demonstrates how to configure NodeBalancers in Linode for load balancing web applications.
Generated: DETERMINISTIC_5977835b00eea9aa
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const linode = require('@linode/api-v4');

/**
 * Configure a NodeBalancer for load balancing web applications
 * @param {Object} config - Configuration object
 * @param {string} config.apiKey - Linode API key
 * @param {string} config.region - Region for the NodeBalancer (e.g., 'us-east')
 * @param {string} config.label - Label for the NodeBalancer
 * @param {Array} config.nodes - Array of node objects { label: string, address: string, weight?: number }
 * @param {number} config.port - Port for the NodeBalancer (e.g., 80)
 * @param {string} config.protocol - Protocol to use (e.g., 'http')
 * @param {string} config.healthCheckType - Health check type (e.g., 'http')
 * @param {string} config.healthCheckPath - Health check path (e.g., '/health')
 * @returns {Promise<Object>} - NodeBalancer configuration result
 */
async function configureNodeBalancer(config) {
    try {
        // Initialize Linode client
        linode.setToken(config.apiKey);

        // Create NodeBalancer
        const nodeBalancer = await linode.nodebalancers.create({
            region: config.region,
            label: config.label,
            client_conn_throttle: 0
        });

        // Create NodeBalancer config
        const nbConfig = await linode.nodebalancers.createConfig(nodeBalancer.id, {
            port: config.port,
            protocol: config.protocol,
            check: config.healthCheckType,
            check_path: config.healthCheckPath,
            check_interval: 5,
            check_timeout: 3,
            check_attempts: 2,
            stickiness: 'http_cookie',
            algorithm: 'roundrobin'
        });

        // Add nodes to the NodeBalancer
        const nodePromises = config.nodes.map(node => 
            linode.nodebalancers.createNode(nodeBalancer.id, nbConfig.id, {
                label: node.label,
                address: `${node.address}:${config.port}`,
                weight: node.weight || 100,
                mode: 'accept'
            })
        );

        await Promise.all(nodePromises);

        return {
            success: true,
            nodeBalancerId: nodeBalancer.id,
            configId: nbConfig.id,
            message: 'NodeBalancer configured successfully'
        };
    } catch (error) {
        console.error('Error configuring NodeBalancer:', error);
        return {
            success: false,
            error: error.message
        };
    }
}

// Example usage
/*
const config = {
    apiKey: 'your-api-key',
    region: 'us-east',
    label: 'web-app-balancer',
    port: 80,
    protocol: 'http',
    healthCheckType: 'http',
    healthCheckPath: '/health',
    nodes: [
        { label: 'web-node-1', address: '192.0.2.1' },
        { label: 'web-node-2', address: '192.0.2.2' }
    ]
};

configureNodeBalancer(config)
    .then(result => console.log(result))
    .catch(error => console.error(error));
*/
```
