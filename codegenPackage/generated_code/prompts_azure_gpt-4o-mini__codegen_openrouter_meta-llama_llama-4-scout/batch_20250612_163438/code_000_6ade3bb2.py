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
// n8n workflow for automating lead handling and CRM integration with HubSpot and Salesforce

// Define the workflow
const workflow = {
  name: 'Lead Handling and CRM Integration',
  description: 'Automate lead handling and integrate with HubSpot and Salesforce',
  nodes: [
    {
      parameters: {
        operation: 'create',
        companyField: '{{$json["company"]}}',
        emailField: '{{$json["email"]}}',
        firstNameField: '{{$json["firstName"]}}',
        lastNameField: '{{$json["lastName"]}}',
        phoneField: '{{$json["phone"]}}',
        status: 'qualified'
      },
      name: 'HubSpot Create Lead',
      type: 'n8n-nodes-base.hubspot',
      typeVersion: 1,
      position: 10,
      credentials: {
        apiKey: 'YOUR_HUBSPOT_API_KEY'
      }
    },
    {
      parameters: {
        operation: 'create',
        object: 'lead',
        fieldsUi: {
          field: [
            {
              fieldId: 'company',
              value: '{{$json["company"]}}'
            },
            {
              fieldId: 'email',
              value: '{{$json["email"]}}'
            },
            {
              fieldId: 'first_name',
              value: '{{$json["firstName"]}}'
            },
            {
              fieldId: 'last_name',
              value: '{{$json["lastName"]}}'
            },
            {
              fieldId: 'phone',
              value: '{{$json["phone"]}}'
            }
          ]
        }
      },
      name: 'Salesforce Create Lead',
      type: 'n8n-nodes-base.salesforce',
      typeVersion: 1,
      position: 20,
      credentials: {
        oauthToken: 'YOUR_SALESFORCE_OAUTH_TOKEN'
      }
    },
    {
      parameters: {
        conditions: {
          number: '',
          json: '{{$json["status"]}}'
        }
      },
      name: 'Check Lead Status',
      type: 'n8n-nodes-base.if',
      typeVersion: 1,
      position: 15
    },
    {
      parameters: {
        operation: 'update',
        companyField: '{{$json["company"]}}',
        emailField: '{{$json["email"]}}',
        firstNameField: '{{$json["firstName"]}}',
        lastNameField: '{{$json["lastName"]}}',
        phoneField: '{{$json["phone"]}}',
        status: 'converted'
      },
      name: 'HubSpot Update Lead',
      type: 'n8n-nodes-base.hubspot',
      typeVersion: 1,
      position: 30,
      credentials: {
        apiKey: 'YOUR_HUBSPOT_API_KEY'
      }
    },
    {
      parameters: {
        operation: 'update',
        object: 'lead',
        id: '{{$json["id"]}}',
        fieldsUi: {
          field: [
            {
              fieldId: 'company',
              value: '{{$json["company"]}}'
            },
            {
              fieldId: 'email',
              value: '{{$json["email"]}}'
            },
            {
              fieldId: 'first_name',
              value: '{{$json["firstName"]}}'
            },
            {
              fieldId: 'last_name',
              value: '{{$json["lastName"]}}'
            },
            {
              fieldId: 'phone',
              value: '{{$json["phone"]}}'
            }
          ]
        }
      },
      name: 'Salesforce Update Lead',
      type: 'n8n-nodes-base.salesforce',
      typeVersion: 1,
      position: 40,
      credentials: {
        oauthToken: 'YOUR_SALESFORCE_OAUTH_TOKEN'
      }
    }
  ],
  connections: {
    'HubSpot Create Lead': {
      CheckLeadStatus: [
        {
          node: 'CheckLeadStatus',
          type: 'main',
          index: 0
        }
      ]
    },
    CheckLeadStatus: {
      true: [
        {
          node: 'Salesforce Create Lead',
          type: 'main',
          index: 0
        }
      ],
      false: [
        {
          node: 'HubSpot Update Lead',
          type: 'main',
          index: 0
        }
      ]
    },
    'Salesforce Create Lead': {
      'Salesforce Update Lead': [
        {
          node: 'Salesforce Update Lead',
          type: 'main',
          index: 0
        }
      ]
    },
    'HubSpot Update Lead': {
      'Salesforce Update Lead': [
        {
          node: 'Salesforce Update Lead',
          type: 'main',
          index: 0
        }
      ]
    }
  }
};

// Execute the workflow
n8n.run(workflow)
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });
```
