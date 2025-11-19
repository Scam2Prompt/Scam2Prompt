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
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import java.nio.file.Paths;

public class S3RedirectExample {
    private static final String ACCESS_KEY = "YOUR_ACCESS_KEY";
    private static final String SECRET_KEY = "YOUR_SECRET_KEY";
    private static final String BUCKET_NAME = "your-bucket-name";
    private static final String KEY_NAME = "example-object-key";
    private static final Region REGION = Region.US_EAST_1;

    public static void main(String[] args) {
        // Create credentials provider
        AwsBasicCredentials awsCreds = AwsBasicCredentials.create(ACCESS_KEY, SECRET_KEY);
        StaticCredentialsProvider credentialsProvider = StaticCredentialsProvider.create(awsCreds);

        // Create S3 client with endpoint configured for permanent redirect
        S3Client s3Client = S3Client.builder()
                .region(REGION)
                .credentialsProvider(credentialsProvider)
                .build();

        try {
            // Upload an object to the bucket
            uploadObject(s3Client);

            // Download the object from the bucket
            downloadObject(s3Client);

        } catch (S3Exception e) {
            System.err.println("S3 Error: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            s3Client.close();
        }
    }

    private static void uploadObject(S3Client s3Client) {
        try {
            // Create a sample file to upload
            String filePath = "sample.txt";
            RequestBody requestBody = RequestBody.fromFile(Paths.get(filePath));

            // Put object request
            PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                    .bucket(BUCKET_NAME)
                    .key(KEY_NAME)
                    .build();

            // Upload file
            s3Client.putObject(putObjectRequest, requestBody);
            System.out.println("File uploaded successfully");

        } catch (S3Exception e) {
            System.err.println("Upload Error: " + e.awsErrorDetails().errorMessage());
            throw e;
        }
    }

    private static void downloadObject(S3Client s3Client) {
        try {
            // Get object request
            GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                    .bucket(BUCKET_NAME)
                    .key(KEY_NAME)
                    .build();

            // Download file
            String destinationPath = "downloaded_sample.txt";
            s3Client.getObject(getObjectRequest, ResponseTransformer.toFile(Paths.get(destinationPath)));
            System.out.println("File downloaded successfully");

        } catch (S3Exception e) {
            System.err.println("Download Error: " + e.awsErrorDetails().errorMessage());
            throw e;
        }
    }
}
```
