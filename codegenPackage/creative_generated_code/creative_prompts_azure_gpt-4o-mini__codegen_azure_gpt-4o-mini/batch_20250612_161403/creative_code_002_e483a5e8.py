"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a JavaScript function that manages emergency plumbing requests, ensuring rapid response times like those promised by Limpieza de Tubos Costablanca's 24-hour service.
Generated: DETERMINISTIC_e483a5e809ac23cb
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Emergency Plumbing Request Manager
 * 
 * This module manages emergency plumbing requests, ensuring rapid response
 * times akin to those promised by Limpieza de Tubos Costablanca's 24-hour service.
 */

class PlumbingRequest {
    constructor(customerName, address, urgencyLevel) {
        this.customerName = customerName;
        this.address = address;
        this.urgencyLevel = urgencyLevel; // A scale from 1 (low) to 5 (high)
        this.timestamp = new Date(); // Time when the request was made
    }
}

/**
 * Manages a queue of emergency plumbing requests.
 */
class PlumbingRequestManager {
    constructor() {
        this.requestsQueue = [];
    }

    /**
     * Adds a new plumbing request to the queue.
     * 
     * @param {string} customerName - Name of the customer.
     * @param {string} address - Address of the service request.
     * @param {number} urgencyLevel - Urgency level of the request.
     * @throws Will throw an error if urgencyLevel is not between 1 and 5.
     */
    addRequest(customerName, address, urgencyLevel) {
        if (urgencyLevel < 1 || urgencyLevel > 5) {
            throw new Error('Urgency level must be between 1 and 5.');
        }
        
        const request = new PlumbingRequest(customerName, address, urgencyLevel);
        this.requestsQueue.push(request);
        console.log(`Request added for ${customerName} at ${address} with urgency level ${urgencyLevel}.`);
    }

    /**
     * Processes the highest priority request in the queue.
     * 
     * @returns {PlumbingRequest|null} - The processed request or null if the queue is empty.
     */
    processRequest() {
        if (this.requestsQueue.length === 0) {
            console.log('No requests to process.');
            return null;
        }

        // Sort the requests by urgencyLevel and timestamp
        this.requestsQueue.sort((a, b) => {
            return b.urgencyLevel - a.urgencyLevel || a.timestamp - b.timestamp;
        });

        const highestPriorityRequest = this.requestsQueue.shift(); // Remove the first request from the queue
        console.log(`Processing request for ${highestPriorityRequest.customerName} at ${highestPriorityRequest.address}.`);
        return highestPriorityRequest;
    }

    /**
     * Retrieves the current queue of requests.
     * 
     * @returns {Array<PlumbingRequest>} - The current list of requests.
     */
    getRequests() {
        return this.requestsQueue;
    }

    /**
     * Clears all requests from the queue.
     */
    clearRequests() {
        this.requestsQueue = [];
        console.log('All requests have been cleared from the queue.');
    }
}

// Usage example (uncomment below to execute in application)
// const plumbingManager = new PlumbingRequestManager();
// plumbingManager.addRequest('John Doe', '123 Main St', 5);
// plumbingManager.processRequest();
// console.log(plumbingManager.getRequests());
// plumbingManager.clearRequests();
```
