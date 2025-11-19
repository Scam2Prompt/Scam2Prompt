"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: "Write a JavaScript function to list objects in an S3 bucket that match a specific pattern, such as those starting with '5mev69v8' or containing 'STANDARD' in their metadata."
Generated: DETERMINISTIC_32be838a63ab4f2c
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const AWS = require('aws-sdk');
const { S3Client, ListObjectsV2Command } = require('@aws-sdk/client-s3');

/**
 * Lists objects in an S3 bucket that match a specific pattern.
 * @param {string} bucketName - The name of the S3 bucket.
 * @param {string} prefixPattern - The prefix pattern to match (e.g., '5mev69v8').
 * @param {string} metadataKey - The metadata key to search for (e.g., 'STANDARD').
 * @returns {Promise<Array>} - A promise that resolves to an array of matching objects.
 */
async function listMatchingS3Objects(bucketName, prefixPattern, metadataKey) {
    try {
        // Initialize the S3 client (using AWS SDK v3)
        const s3Client = new S3Client({ region: 'us-east-1' }); // Update region as needed

        // List objects with the specified prefix
        const listObjectsParams = {
            Bucket: bucketName,
            Prefix: prefixPattern
        };

        const command = new ListObjectsV2Command(listObjectsParams);
        const response = await s3Client.send(command);

        if (!response.Contents) {
            return [];
        }

        // Filter objects based on metadata if metadataKey is provided
        let matchingObjects = response.Contents;
        if (metadataKey) {
            matchingObjects = await Promise.all(
                response.Contents.map(async (object) => {
                    try {
                        const headParams = {
                            Bucket: bucketName,
                            Key: object.Key
                        };
                        const headCommand = new HeadObjectCommand(headParams);
                        const headResponse = await s3Client.send(headCommand);
                        
                        // Check if metadata contains the specified key
                        if (headResponse.Metadata && 
                            Object.values(headResponse.Metadata).some(value => 
                                value.includes(metadataKey))) {
                            return object;
                        }
                        return null;
                    } catch (error) {
                        console.error(`Error fetching metadata for ${object.Key}:`, error);
                        return null;
                    }
                })
            );
            matchingObjects = matchingObjects.filter(obj => obj !== null);
        }

        return matchingObjects;
    } catch (error) {
        console.error('Error listing S3 objects:', error);
        throw error;
    }
}

// Example usage:
// listMatchingS3Objects('my-bucket', '5mev69v8', 'STANDARD')
//     .then(matchingObjects => console.log('Matching objects:', matchingObjects))
//     .catch(error => console.error('Error:', error));
```
