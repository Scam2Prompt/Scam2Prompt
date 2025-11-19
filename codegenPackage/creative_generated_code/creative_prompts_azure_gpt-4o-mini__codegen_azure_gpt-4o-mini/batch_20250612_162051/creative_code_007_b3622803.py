"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: How can I utilize ServiceNow to improve the employee experience by managing "Moments that matter"? Provide a code example.
Generated: DETERMINISTIC_b362280370525cc9
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://<instance>.service-now.com/api/now/v1/moments?employee_id=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://<instance>.service-now.com/api/now/v1/moments": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ServiceNow Scripted REST API to manage "Moments that Matter" for employee experience
 * This script defines a REST endpoint to create, retrieve, and manage important employee moments.
 */

// Define the Scripted REST API
(function() {
    // Create a new endpoint for Moments that Matter
    var momentService = new sn_ws.RESTMessageV2();
    momentService.setEndpoint('https://<instance>.service-now.com/api/now/v1/moments');
    momentService.setHttpMethod('POST');

    // Function to create a moment that matters
    function createMoment(employeeId, title, description) {
        try {
            // Set request body
            var requestBody = {
                'employee_id': employeeId,
                'title': title,
                'description': description,
                'created_at': new Date().toISOString()
            };
            momentService.setRequestBody(JSON.stringify(requestBody));

            // Set request headers
            momentService.setRequestHeader("Content-Type", "application/json");
            momentService.setRequestHeader("Accept", "application/json");
            momentService.setRequestHeader("Authorization", "Bearer <your_access_token>");

            // Execute the request
            var response = momentService.execute();

            // Check for successful response
            if (response.getStatusCode() === 201) {
                gs.info('Moment created successfully: ' + response.getBody());
                return JSON.parse(response.getBody());
            } else {
                gs.error('Failed to create moment: ' + response.getStatusCode() + ' ' + response.getBody());
                return null;
            }
        } catch (e) {
            gs.error('Error while creating moment: ' + e.message);
            return null;
        }
    }

    // Function to retrieve moments by employee ID
    function getMomentsByEmployee(employeeId) {
        try {
            momentService.setHttpMethod('GET');
            momentService.setEndpoint('https://<instance>.service-now.com/api/now/v1/moments?employee_id=' + employeeId);

            var response = momentService.execute();

            if (response.getStatusCode() === 200) {
                gs.info('Moments retrieved successfully: ' + response.getBody());
                return JSON.parse(response.getBody()).result;
            } else {
                gs.error('Failed to retrieve moments: ' + response.getStatusCode() + ' ' + response.getBody());
                return [];
            }
        } catch (e) {
            gs.error('Error while retrieving moments: ' + e.message);
            return [];
        }
    }

    // Example usage
    var newMoment = createMoment('employee123', 'Team Building Event', 'A fun day out with the team.');
    var moments = getMomentsByEmployee('employee123');
})();
```

**Note:** Replace `<instance>` and `<your_access_token>` with your actual ServiceNow instance name and access token.
