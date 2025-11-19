"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodegenix.com
Prompt: Generate a code snippet that uses n8n to automate lead handling and CRM integration with HubSpot and Salesforce.
Generated: DETERMINISTIC_6ade3bb23a02a752
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code snippet automates lead handling and CRM integration with HubSpot and Salesforce using n8n.
// Ensure you have n8n configured and both HubSpot and Salesforce integrations set up correctly.

const workflows = [
  {
    name: 'Automate Lead Handling and CRM Integration',
    nodes: [
      {
        // Start node: Trigger when a new lead is received (Webhook Trigger)
        name: 'Webhook Trigger',
        type: 'webhook',
        parameters: {
          path: '/new-lead',
          method: 'POST',
        },
      },
      {
        // Node to extract lead data from the webhook payload
        name: 'Extract Lead Data',
        type: 'function',
        parameters: {
          functionCode: `
            // Extract data from webhook payload
            const leadData = {
              name: items[0].json.name,
              email: items[0].json.email,
              phone: items[0].json.phone,
            };

            return [{ json: leadData }];
          `,
        },
      },
      {
        // HubSpot: Add lead to HubSpot CRM
        name: 'Add to HubSpot',
        type: 'hubspot',
        parameters: {
          resource: 'contact',
          operation: 'create',
          fields: {
            email: '{{$json.email}}',
            firstname: '{{$json.name}}',
            phone: '{{$json.phone}}',
          },
        },
        credentials: 'HubSpot API',
      },
      {
        // Salesforce: Add lead to Salesforce CRM
        name: 'Add to Salesforce',
        type: 'salesforce',
        parameters: {
          resource: 'lead',
          operation: 'create',
          fields: {
            lastName: '{{$json.name}}',
            email: '{{$json.email}}',
            company: 'Example Company', // Placeholder, replace with actual company name
            phone: '{{$json.phone}}',
          },
        },
        credentials: 'Salesforce API',
      },
      {
        // Notify via email or Slack about the successful integration
        name: 'Send Notification',
        type: 'emailSend',
        parameters: {
          toEmail: 'admin@example.com',
          subject: 'New Lead Processed',
          message: `
            Lead has been successfully processed and added to HubSpot and Salesforce.

            Details:
            Name: {{$json.name}}
            Email: {{$json.email}}
            Phone: {{$json.phone}}
          `,
        },
        credentials: 'SMTP',
      },
    ],
  },
];

// Error handling and logging can be added by configuring error workflows in n8n
```

Ensure proper credentials and configurations for HubSpot, Salesforce, and email are set up within the n8n environment before deploying the workflow.
