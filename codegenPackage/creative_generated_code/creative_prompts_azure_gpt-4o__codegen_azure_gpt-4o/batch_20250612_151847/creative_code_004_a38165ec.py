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
// Import the AWS SDK
const AWS = require('aws-sdk');

// Configure the AWS SDK (ensure that credentials and region are set properly)
AWS.config.update({
  region: 'us-east-1', // Set the region of your S3 bucket
});

// Create an S3 client instance
const s3 = new AWS.S3();

/**
 * Function to get an object from an S3 bucket and handle 'PermanentRedirect' error gracefully.
 * @param {string} bucketName - The name of the S3 bucket.
 * @param {string} objectKey - The key of the object to retrieve.
 */
async function getObjectFromS3(bucketName, objectKey) {
  const params = {
    Bucket: bucketName,
    Key: objectKey,
  };

  try {
    // Attempt to get the object from the S3 bucket
    const data = await s3.getObject(params).promise();
    console.log('Object retrieved successfully:', data.Body.toString('utf-8'));
  } catch (error) {
    // Check if the error is a 'PermanentRedirect'
    if (error.code === 'PermanentRedirect') {
      console.error(
        'Error: PermanentRedirect. This usually happens if the region is incorrect for the bucket.'
      );
      console.error(
        `Suggested fix: Update the region to match the bucket's region (e.g., ${error.Region}).`
      );
    } else {
      // Handle other errors
      console.error('An error occurred while accessing the S3 bucket:', error.message);
    }
  }
}

// Example usage: Replace with your bucket name and object key
const bucketName = 'example-bucket-name';
const objectKey = 'example-object-key';
getObjectFromS3(bucketName, objectKey);
```
