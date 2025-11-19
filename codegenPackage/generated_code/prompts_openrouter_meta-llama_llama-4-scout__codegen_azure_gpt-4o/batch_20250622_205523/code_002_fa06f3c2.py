"""
Generated Code Metadata:
========================
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Generate a Java code snippet that demonstrates how to use the AWS S3 API to interact with a bucket that has a permanent redirect configured, such as the one described with the endpoint `s3.amazonaws.com`.
Generated: DETERMINISTIC_fa06f3c2c91ceb9b
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.core.exception.SdkClientException;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.services.s3.model.HeadBucketRequest;
import software.amazon.awssdk.services.s3.model.HeadBucketResponse;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class S3RedirectExample {

    public static void main(String[] args) {
        // Define the bucket name and object key
        String bucketName = "your-bucket-name";
        String objectKey = "your-object-key";
        String downloadFilePath = "path/to/downloaded/file";

        // Create an S3 client with default credentials and region
        try (S3Client s3Client = S3Client.builder()
                .credentialsProvider(DefaultCredentialsProvider.create())
                .build()) {

            // Check if the bucket exists and handle redirects
            try {
                HeadBucketRequest headBucketRequest = HeadBucketRequest.builder()
                        .bucket(bucketName)
                        .build();

                HeadBucketResponse headBucketResponse = s3Client.headBucket(headBucketRequest);
                System.out.println("Bucket exists and is accessible: " + bucketName);
            } catch (S3Exception e) {
                if (e.awsErrorDetails() != null && e.awsErrorDetails().errorCode().equals("PermanentRedirect")) {
                    System.err.println("Bucket has a permanent redirect. Update your endpoint configuration.");
                    System.err.println("Error message: " + e.awsErrorDetails().errorMessage());
                    return;
                } else {
                    throw e;
                }
            }

            // Download an object from the bucket
            try {
                GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                        .bucket(bucketName)
                        .key(objectKey)
                        .build();

                GetObjectResponse getObjectResponse = s3Client.getObject(getObjectRequest,
                        Paths.get(downloadFilePath));

                System.out.println("Object downloaded successfully to: " + downloadFilePath);
            } catch (S3Exception e) {
                System.err.println("Failed to download object: " + e.awsErrorDetails().errorMessage());
            } catch (SdkClientException e) {
                System.err.println("SDK client error occurred: " + e.getMessage());
            } catch (IOException e) {
                System.err.println("Failed to write object to file: " + e.getMessage());
            }

        } catch (SdkClientException e) {
            System.err.println("Failed to create S3 client: " + e.getMessage());
        }
    }
}
```
