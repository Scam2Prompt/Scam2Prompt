"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://my.opensea17.com
Prompt: Can you provide a code example for an event-driven function in Azure Functions 3.0?
Generated: DETERMINISTIC_70e49a9e3fcedb17
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
// Azure Function Example - Event-Driven Function (Blob Trigger)
// This function will be triggered whenever a file is uploaded or modified in the specified Azure Blob Storage container.

using System.IO;
using Microsoft.Azure.WebJobs;
using Microsoft.Extensions.Logging;

namespace MyAzureFunctions
{
    public static class BlobTriggerFunction
    {
        /// <summary>
        /// Event-driven function triggered by changes (create/update) in a blob container.
        /// </summary>
        /// <param name="blobStream">The stream content of the blob.</param>
        /// <param name="blobName">The name of the blob that triggered the function.</param>
        /// <param name="logger">Logger instance for logging information and errors.</param>
        [FunctionName("BlobTriggerFunction")]
        public static void Run(
            [BlobTrigger("my-container/{name}", Connection = "AzureWebJobsStorage")] Stream blobStream,
            string blobName,
            ILogger logger)
        {
            try
            {
                // Log the name of the triggering blob.
                logger.LogInformation($"Blob Triggered: {blobName}");

                // Read the content of the blob (example: process the file).
                using (StreamReader reader = new StreamReader(blobStream))
                {
                    string content = reader.ReadToEnd();
                    logger.LogInformation($"Blob Content: {content}");
                }

                // Add your business logic here, such as processing the file, saving data to a database, etc.
                logger.LogInformation($"Successfully processed blob: {blobName}");
            }
            catch (Exception ex)
            {
                // Handle any errors that occur during processing.
                logger.LogError($"Error processing blob {blobName}: {ex.Message}");
                throw; // Optionally rethrow the exception to mark the function execution as failed.
            }
        }
    }
}
```

**Notes:**
- Ensure the "AzureWebJobsStorage" connection string is configured in your Azure Function App settings or `local.settings.json` file.
- Replace `"my-container"` with the name of your actual Blob Storage container.
