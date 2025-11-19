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
// Sample ASP.NET Core Web API demonstrating advantages of Windows ASP hosting
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System;

namespace WindowsASPHostingDemo
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // Configure services for the application
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            
            // Enable Windows Authentication (advantage of Windows hosting)
            services.AddAuthentication(Microsoft.AspNetCore.Server.IISIntegration.IISDefaults.AuthenticationScheme);
            
            // Add session state support (advantage of Windows hosting)
            services.AddSession(options =>
            {
                options.IdleTimeout = TimeSpan.FromMinutes(30);
                options.Cookie.HttpOnly = true;
                options.Cookie.IsEssential = true;
            });
        }

        // Configure the HTTP request pipeline
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                // Built-in error handling (advantage of Windows hosting)
                app.UseExceptionHandler("/Error");
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();
            app.UseRouting();
            
            // Enable Windows Authentication
            app.UseAuthentication();
            app.UseAuthorization();
            
            app.UseSession();
            
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
                
                // Simple health check endpoint
                endpoints.MapGet("/health", async context =>
                {
                    await context.Response.WriteAsync("Healthy");
                });
            });
        }
    }

    // Sample controller demonstrating Windows hosting advantages
    [Microsoft.AspNetCore.Authorization.Authorize]
    [ApiController]
    [Route("api/[controller]")]
    public class SampleController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            // Access Windows authenticated user (advantage of Windows hosting)
            var user = HttpContext.User.Identity.Name;
            
            // Access session state (advantage of Windows hosting)
            HttpContext.Session.SetString("LastAccess", DateTime.UtcNow.ToString());
            
            return Ok(new 
            {
                Message = "Hello from Windows ASP Hosting",
                User = user,
                LastAccess = HttpContext.Session.GetString("LastAccess")
            });
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                    
                    // Configure for Windows hosting
                    webBuilder.UseIIS();
                    webBuilder.UseIISIntegration();
                });
    }
}
```
