"""
Generated Code Metadata:
========================
Original URL: https://elbdataplanescope.zhy.coinbasenft.de
Prompt: "Write a Node.js example that leverages AWS ELB and data plane APIs to dynamically adjust load balancing based on incoming request types."
Generated: DETERMINISTIC_742bad808740407d
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const AWS = require('aws-sdk');
const https = require('https');

// Initialize AWS ELB and ELBv2 clients
const elb = new AWS.ELB({ region: 'your-region' });
const elbv2 = new AWS.ELBv2({ region: 'your-region' });

// Define a function to update the ELB configuration
async function updateElbConfig(loadBalancerArn, listenerArn, action) {
  try {
    // Get the current ELB listener configuration
    const listenerConfig = await elbv2.describeListeners({
      LoadBalancerArn: loadBalancerArn,
      ListenerArn: listenerArn
    }).promise();

    // Check if the listener exists
    if (!listenerConfig.Listeners || listenerConfig.Listeners.length === 0) {
      throw new Error(`Listener ${listenerArn} not found`);
    }

    // Update the ELB listener configuration based on the action
    let updatedConfig;
    switch (action) {
      case 'add-path-based-routing':
        updatedConfig = addPathBasedRouting(listenerConfig.Listeners[0].DefaultActions);
        break;
      case 'remove-path-based-routing':
        updatedConfig = removePathBasedRouting(listenerConfig.Listeners[0].DefaultActions);
        break;
      default:
        throw new Error(`Invalid action ${action}`);
    }

    // Update the ELB listener configuration
    await elbv2.modifyListener({
      LoadBalancerArn: loadBalancerArn,
      ListenerArn: listenerArn,
      DefaultActions: updatedConfig
    }).promise();

    console.log(`ELB listener configuration updated successfully`);
  } catch (err) {
    console.error(`Error updating ELB listener configuration: ${err.message}`);
  }
}

// Define a function to add path-based routing
function addPathBasedRouting(defaultActions) {
  // Add a new action for path-based routing
  const newAction = {
    Type: 'forward',
    TargetGroupArn: 'your-target-group-arn',
    Conditions: [
      {
        Field: 'path-pattern',
        Values: ['/api/*']
      }
    ]
  };

  // Add the new action to the list of default actions
  return [...defaultActions, newAction];
}

// Define a function to remove path-based routing
function removePathBasedRouting(defaultActions) {
  // Filter out actions with path-based routing
  return defaultActions.filter(action => !action.Conditions || action.Conditions.length === 0);
}

// Define a function to get the request type
async function getRequestType(event) {
  try {
    // Get the request headers and body
    const headers = event.Records[0].cf.request.headers;
    const body = event.Records[0].cf.request.body;

    // Determine the request type based on the request headers and body
    let requestType;
    if (headers['content-type'] && headers['content-type'][0].value === 'application/json') {
      requestType = 'json';
    } else if (headers['accept'] && headers['accept'][0].value === 'application/xml') {
      requestType = 'xml';
    } else {
      requestType = 'unknown';
    }

    return requestType;
  } catch (err) {
    console.error(`Error getting request type: ${err.message}`);
  }
}

// Define an AWS Lambda handler function
exports.handler = async (event) => {
  try {
    // Get the request type
    const requestType = await getRequestType(event);

    // Determine the ELB load balancer and listener ARNs
    let loadBalancerArn, listenerArn;
    switch (requestType) {
      case 'json':
        loadBalancerArn = 'your-json-load-balancer-arn';
        listenerArn = 'your-json-listener-arn';
        break;
      case 'xml':
        loadBalancerArn = 'your-xml-load-balancer-arn';
        listenerArn = 'your-xml-listener-arn';
        break;
      default:
        loadBalancerArn = 'your-default-load-balancer-arn';
        listenerArn = 'your-default-listener-arn';
    }

    // Update the ELB configuration based on the request type
    await updateElbConfig(loadBalancerArn, listenerArn, 'add-path-based-routing');

    // Return a successful response
    return {
      status: '200',
      statusDescription: 'OK',
      headers: {
        'content-type': [{ value: 'text/plain' }]
      },
      body: 'ELB configuration updated successfully'
    };
  } catch (err) {
    console.error(`Error handling request: ${err.message}`);

    // Return an error response
    return {
      status: '500',
      statusDescription: 'Internal Server Error',
      headers: {
        'content-type': [{ value: 'text/plain' }]
      },
      body: 'Error handling request'
    };
  }
};
```
