"""
Generated Code Metadata:
========================
Original URL: https://agromec.cl
Prompt: What are the advantages of using Windows ASP hosting for a .NET application, and can you provide a sample code snippet?
Generated: DETERMINISTIC_1e77e3badecf4891
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Sample code snippet demonstrating a simple ASP.NET Core application
// This code is production-ready, well-documented, and follows best practices.

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace SampleAspNetApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Create and run the host for the ASP.NET Core application
            var host = CreateHostBuilder(args).Build();
            host.Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    // Configure the web application to use the Startup class
                    webBuilder.UseStartup<Startup>();
                });
    }

    public class Startup
    {
        // Configure services for dependency injection
        public void ConfigureServices(IServiceCollection services)
        {
            // Add controllers with views to the service collection
            services.AddControllersWithViews();
        }

        // Configure the HTTP request pipeline
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILogger<Startup> logger)
        {
            // Enable detailed error pages in development mode
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                // Use a generic error handler in production
                app.UseExceptionHandler("/Home/Error");
                app.UseHsts(); // Enforce HTTPS
            }

            // Middleware to redirect HTTP requests to HTTPS
            app.UseHttpsRedirection();

            // Middleware to serve static files (e.g., CSS, JS, images)
            app.UseStaticFiles();

            // Middleware to route requests
            app.UseRouting();

            // Middleware to handle authentication and authorization
            app.UseAuthorization();

            // Define endpoint routing
            app.UseEndpoints(endpoints =>
            {
                // Map default route to the Home controller
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });

            // Log application startup
            logger.LogInformation("Application has started successfully.");
        }
    }

    // Sample HomeController demonstrating a basic controller
    public class HomeController : Microsoft.AspNetCore.Mvc.Controller
    {
        // Action method for the default route
        public IActionResult Index()
        {
            // Return a simple view
            return View();
        }

        // Action method for handling errors
        public IActionResult Error()
        {
            // Return an error view
            return View();
        }
    }
}
```

This code snippet demonstrates a basic ASP.NET Core application setup, including routing, middleware configuration, and a sample controller. It is designed to be production-ready and adheres to best practices.
