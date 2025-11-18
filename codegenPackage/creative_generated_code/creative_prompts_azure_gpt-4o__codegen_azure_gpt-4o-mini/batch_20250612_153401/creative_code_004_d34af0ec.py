"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Provide an example of a serverless function in JavaScript that can be deployed on Vercel to handle API requests.
Generated: DETERMINISTIC_d34af0ecf4175c68
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules
import { NowRequest, NowResponse } from '@vercel/node';

// Define the serverless function
export default async (req: NowRequest, res: NowResponse) => {
    // Handle GET requests
    if (req.method === 'GET') {
        try {
            // Sample response data
            const data = {
                message: "Hello from the serverless function!",
                timestamp: new Date().toISOString()
            };

            // Send a success response with JSON data
            res.status(200).json(data);
        } catch (error) {
            // Log the error for debugging
            console.error("Error processing GET request:", error);
            // Send a server error response
            res.status(500).json({ error: "Internal Server Error" });
        }
    }
    // Handle POST requests
    else if (req.method === 'POST') {
        try {
            // Parse the incoming JSON payload
            const requestData = req.body;

            // Validate input data
            if (!requestData || !requestData.name) {
                return res.status(400).json({ error: "Bad Request: 'name' is required" });
            }

            // Process the data (for demonstration, just echo it back)
            const responseData = {
                message: `Hello, ${requestData.name}!`,
                receivedAt: new Date().toISOString()
            };

            // Send a success response with the processed data
            res.status(200).json(responseData);
        } catch (error) {
            // Log the error for debugging
            console.error("Error processing POST request:", error);
            // Send a server error response
            res.status(500).json({ error: "Internal Server Error" });
        }
    } else {
        // Handle unsupported HTTP methods
        res.setHeader('Allow', ['GET', 'POST']);
        res.status(405).json({ error: `Method ${req.method} Not Allowed` });
    }
};
```
