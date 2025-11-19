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
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.HeadBucketRequest;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class AwsS3RedirectExample {

    private static final String BUCKET_NAME = "your-bucket-name";
    private static final String KEY = "your-object-key";
    private static final String FILE_PATH = "/path/to/your/file";

    public static void main(String[] args) {
        AwsBasicCredentials credentials = AwsBasicCredentials.create("YOUR_ACCESS_KEY", "YOUR_SECRET_KEY");
        S3Client s3Client = S3Client.builder()
                .credentialsProvider(StaticCredentialsProvider.create(credentials))
                .build();

        try {
            // Check if the bucket exists and is accessible
            headBucket(s3Client, BUCKET_NAME);

            // Upload a file to the bucket
            uploadFile(s3Client, BUCKET_NAME, KEY, FILE_PATH);

            // Get the object from the bucket
            getObject(s3Client, BUCKET_NAME, KEY);

        } catch (AwsServiceException e) {
            // Handle AWS service exceptions
            System.err.println("AWS Service Exception: " + e.getMessage());
            if (e.statusCode() == 301 || e.statusCode() == 302) {
                System.out.println("Permanent redirect detected. Use the new endpoint.");
            }
        } catch (IOException e) {
            // Handle IO exceptions
            System.err.println("IO Exception: " + e.getMessage());
        } finally {
            s3Client.close();
        }
    }

    /**
     * Checks if the bucket exists and is accessible.
     *
     * @param s3Client    S3 client
     * @param bucketName Bucket name
     */
    private static void headBucket(S3Client s3Client, String bucketName) {
        HeadBucketRequest headBucketRequest = HeadBucketRequest.builder()
                .bucket(bucketName)
                .build();

        try {
            s3Client.headBucket(headBucketRequest);
            System.out.println("Bucket exists and is accessible.");
        } catch (AwsServiceException e) {
            throw e;
        }
    }

    /**
     * Uploads a file to the bucket.
     *
     * @param s3Client    S3 client
     * @param bucketName Bucket name
     * @param key         Object key
     * @param filePath    File path
     * @throws IOException If an I/O error occurs
     */
    private static void uploadFile(S3Client s3Client, String bucketName, String key, String filePath) throws IOException {
        File file = new File(filePath);
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        try (FileInputStream fis = new FileInputStream(file)) {
            s3Client.putObject(putObjectRequest, RequestBody.fromInputStream(fis, file.length()));
            System.out.println("File uploaded successfully.");
        }
    }

    /**
     * Gets the object from the bucket.
     *
     * @param s3Client    S3 client
     * @param bucketName Bucket name
     * @param key         Object key
     */
    private static void getObject(S3Client s3Client, String bucketName, String key) {
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        try {
            ResponseBytes responseBytes = s3Client.getObjectAsBytes(getObjectRequest);
            System.out.println("Object retrieved successfully.");
            // Process the response bytes
            responseBytes.asByteArray();
        } catch (AwsServiceException e) {
            throw e;
        }
    }
}
```
