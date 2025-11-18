"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-pepe.net
Prompt: Recommend tools for testing REST APIs and write an example script using Postman, based on the software testing tutorials on https://events-pepe.net.
Generated: DETERMINISTIC_215782b87a3a6fd2
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to test REST APIs using Postman.
This script provides an example of how to send a GET request to an API endpoint
and validate the response using Python and Postman test scripts.
Ensure you have Postman installed and are familiar with its interface.

Recommended tools for testing REST APIs:
1. Postman (GUI-based tool for testing APIs)
2. Curl (Command-line tool)
3. SoapUI (For SOAP and REST protocols)
4. JMeter (For load testing APIs)
5. REST Assured (Java-based framework)
"""

# Postman Test Script Example
# Below is a Postman script to be placed in the "Tests" tab of Postman:

pm.test("Status code is 200", function () {
    // Validate that the response status code is 200
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    // Check if the response time is within acceptable limits
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Response body contains expected keys", function () {
    // Parse the JSON response and validate expected keys and values
    let jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('key1'); // Replace 'key1' with actual key
    pm.expect(jsonData.key1).to.eql('expectedValue'); // Validate the value
});

pm.test("Header contains Content-Type application/json", function () {
    // Validate that the Content-Type header matches expected value
    pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json');
});

pm.test("Error handling for missing property", function () {
    // Validate if an optional property exists, handle errors gracefully
    let jsonData = pm.response.json();
    if (jsonData.optionalKey) {
        pm.expect(jsonData.optionalKey).to.eql('expectedValue'); // Validate optional key
    } else {
        console.warn("optionalKey not found in response."); // Log warning
    }
});
```

This Postman script can be copied directly into the `Tests` tab of a Postman request to validate various aspects of the API response.
