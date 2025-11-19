"""
Generated Code Metadata:
========================
Original URL: https://nodegenix.com
Prompt: Generate a code snippet that uses n8n to automate lead handling and CRM integration with HubSpot and Salesforce.
Generated: DETERMINISTIC_6ade3bb23a02a752
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// n8n workflow to automate lead handling and CRM integration with HubSpot and Salesforce

// Import necessary modules
const { Workflow } = require('n8n-core');
const { NodeApiError } = require('n8n-workflow');

// Define the workflow
const workflow = new Workflow({
    nodes: [
        {
            // Trigger node to start the workflow when a new lead is created
            name: 'Webhook Trigger',
            type: 'n8n-nodes-base.webhook',
            typeVersion: 1,
            position: [250, 300],
            parameters: {
                httpMethod: 'POST',
                path: 'new-lead',
                responseMode: 'onReceived',
            },
        },
        {
            // Node to create a lead in HubSpot
            name: 'Create HubSpot Lead',
            type: 'n8n-nodes-base.hubspot',
            typeVersion: 1,
            position: [500, 300],
            parameters: {
                operation: 'create',
                resource: 'contact',
                properties: {
                    email: '={{$json["email"]}}',
                    firstname: '={{$json["firstName"]}}',
                    lastname: '={{$json["lastName"]}}',
                },
            },
        },
        {
            // Node to create a lead in Salesforce
            name: 'Create Salesforce Lead',
            type: 'n8n-nodes-base.salesforce',
            typeVersion: 1,
            position: [750, 300],
            parameters: {
                operation: 'create',
                resource: 'lead',
                fields: {
                    LastName: '={{$json["lastName"]}}',
                    Email: '={{$json["email"]}}',
                    FirstName: '={{$json["firstName"]}}',
                },
            },
        },
        {
            // Node to respond back to the webhook
            name: 'Respond to Webhook',
            type: 'n8n-nodes-base.respondToWebhook',
            typeVersion: 1,
            position: [1000, 300],
            parameters: {
                responseCode: 200,
                responseData: 'Lead processed successfully',
            },
        },
    ],
    connections: {
        'Webhook Trigger': {
            main: [
                [
                    {
                        node: 'Create HubSpot Lead',
                        type: 'main',
                        index: 0,
                    },
                ],
            ],
        },
        'Create HubSpot Lead': {
            main: [
                [
                    {
                        node: 'Create Salesforce Lead',
                        type: 'main',
                        index: 0,
                    },
                ],
            ],
        },
        'Create Salesforce Lead': {
            main: [
                [
                    {
                        node: 'Respond to Webhook',
                        type: 'main',
                        index: 0,
                    },
                ],
            ],
        },
    },
});

// Execute the workflow
(async () => {
    try {
        await workflow.run();
    } catch (error) {
        // Handle errors gracefully
        console.error('Error executing workflow:', error);
        throw new NodeApiError(this.getNode(), error);
    }
})();
```
