"""
Generated Code Metadata:
========================
Original URL: https://consultech.ci
Prompt: Provide an example of how to use Microsoft technologies for software development and integration, as described by ConsulTech's technical expertise.
Generated: DETERMINISTIC_d3f74868bb0e4efc
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Example demonstrating Microsoft technologies integration as per ConsulTech's expertise
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.EntityFrameworkCore;
using Microsoft.Azure.ServiceBus;
using Microsoft.Azure.Storage.Blob;
using Newtonsoft.Json;

namespace ConsulTechIntegrationDemo
{
    // Entity Framework Core model
    public class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
    }

    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
        public DbSet<Customer> Customers { get; set; }
    }

    // Azure Service Bus message handler
    public class ServiceBusHandler
    {
        private readonly IQueueClient _queueClient;
        private readonly ILogger<ServiceBusHandler> _logger;

        public ServiceBusHandler(IQueueClient queueClient, ILogger<ServiceBusHandler> logger)
        {
            _queueClient = queueClient;
            _logger = logger;
        }

        public async Task SendMessageAsync(object message)
        {
            try
            {
                var jsonMessage = JsonConvert.SerializeObject(message);
                var busMessage = new Message(System.Text.Encoding.UTF8.GetBytes(jsonMessage));
                await _queueClient.SendAsync(busMessage);
                _logger.LogInformation("Message sent to Service Bus");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error sending message to Service Bus");
                throw;
            }
        }
    }

    // Azure Blob Storage service
    public class BlobStorageService
    {
        private readonly CloudBlobContainer _container;
        private readonly ILogger<BlobStorageService> _logger;

        public BlobStorageService(CloudBlobContainer container, ILogger<BlobStorageService> logger)
        {
            _container = container;
            _logger = logger;
        }

        public async Task UploadFileAsync(string blobName, byte[] content)
        {
            try
            {
                var blob = _container.GetBlockBlobReference(blobName);
                await blob.UploadFromByteArrayAsync(content, 0, content.Length);
                _logger.LogInformation($"File {blobName} uploaded to Blob Storage");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error uploading file {blobName} to Blob Storage");
                throw;
            }
        }
    }

    // Main application
    public class Program
    {
        public static async Task Main(string[] args)
        {
            var host = CreateHostBuilder(args).Build();

            using (var scope = host.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                try
                {
                    var dbContext = services.GetRequiredService<AppDbContext>();
                    await dbContext.Database.EnsureCreatedAsync();

                    var serviceBusHandler = services.GetRequiredService<ServiceBusHandler>();
                    await serviceBusHandler.SendMessageAsync(new { Message = "Hello from ConsulTech" });

                    var blobService = services.GetRequiredService<BlobStorageService>();
                    await blobService.UploadFileAsync("sample.txt", System.Text.Encoding.UTF8.GetBytes("Sample content"));

                    Console.WriteLine("Integration demo completed successfully");
                }
                catch (Exception ex)
                {
                    var logger = services.GetRequiredService<ILogger<Program>>();
                    logger.LogError(ex, "An error occurred during the integration demo");
                }
            }

            await host.RunAsync();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    // Configuration
                    var configuration = hostContext.Configuration;

                    // Database
                    services.AddDbContext<AppDbContext>(options =>
                        options.UseSqlServer(configuration.GetConnectionString("DefaultConnection")));

                    // Azure Service Bus
                    services.AddSingleton<IQueueClient>(provider =>
                        new QueueClient(configuration["ServiceBus:ConnectionString"], 
                                      configuration["ServiceBus:QueueName"]));

                    services.AddScoped<ServiceBusHandler>();

                    // Azure Blob Storage
                    services.AddSingleton(provider =>
                    {
                        var account = Microsoft.Azure.Storage.CloudStorageAccount.Parse(
                            configuration["BlobStorage:ConnectionString"]);
                        var client = account.CreateCloudBlobClient();
                        return client.GetContainerReference(configuration["BlobStorage:ContainerName"]);
                    });

                    services.AddScoped<BlobStorageService>();

                    // HTTP Client
                    services.AddHttpClient();
                })
                .ConfigureLogging(logging =>
                {
                    logging.ClearProviders();
                    logging.AddConsole();
                    logging.AddAzureWebAppDiagnostics();
                });
    }
}
```
