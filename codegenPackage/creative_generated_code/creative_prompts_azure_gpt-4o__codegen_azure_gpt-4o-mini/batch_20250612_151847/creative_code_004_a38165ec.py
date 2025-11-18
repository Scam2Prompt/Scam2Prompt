"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Write code in Node.js using the AWS SDK to handle a "PermanentRedirect" error when accessing an S3 bucket.
Generated: DETERMINISTIC_a38165ec1ba1be4b
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required AWS SDK client
const AWS = require('aws-sdk');

// Configuring the region for the S3 client
AWS.config.update({ region: 'us-east-1' }); // Update to your desired region

// Creating an S3 service object
const s3 = new AWS.S3();

/**
 * Function to get an object from an S3 bucket.
 * @param {string} bucketName - The name of the S3 bucket.
 * @param {string} objectKey - The key of the object to retrieve.
 */
async function getObjectFromS3(bucketName, objectKey) {
    try {
        const params = {
            Bucket: bucketName,
            Key: objectKey,
        };

        // Attempting to retrieve the S3 object
        const data = await s3.getObject(params).promise();
        console.log('Object retrieved successfully:', data.Body.toString());
    } catch (error) {
        // Handling different types of errors
        if (error.code === 'PermanentRedirect') {
            console.error('PermanentRedirect error occurred:', error.message);
            console.log('The request was redirected. Please check the bucket region.');
        } else if (error.code === 'NoSuchKey') {
            console.error('No such key exists:', error.message);
        } else if (error.code === 'AccessDenied') {
            console.error('Access denied to the S3 bucket:', error.message);
        } else {
            console.error('An error occurred while fetching the object:', error.message);
        }
    }
}

// Example usage of the getObjectFromS3 function
const bucketName = 'your-bucket-name'; // Replace with your S3 bucket name
const objectKey = 'your-object-key'; // Replace with the S3 object key

getObjectFromS3(bucketName, objectKey);
```
