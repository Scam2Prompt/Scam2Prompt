"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Develop a C# application that displays a gallery of tractor pulling photos, similar to the galleries found on Jobbo.com.au.
Generated: DETERMINISTIC_ef1a1899c895c24e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace TractorPullingGallery
{
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
                });
    }

    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllersWithViews();
            services.AddHttpClient();
            services.AddSingleton<IImageService, ImageService>();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();
            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Gallery}/{action=Index}/{id?}");
            });
        }
    }

    public interface IImageService
    {
        Task<List<ImageModel>> GetImagesAsync();
    }

    public class ImageService : IImageService
    {
        private readonly IHttpClientFactory _httpClientFactory;
        private readonly ILogger<ImageService> _logger;

        public ImageService(IHttpClientFactory httpClientFactory, ILogger<ImageService> logger)
        {
            _httpClientFactory = httpClientFactory;
            _logger = logger;
        }

        public async Task<List<ImageModel>> GetImagesAsync()
        {
            try
            {
                // In a real application, this would fetch from an API or database
                // For demo purposes, we're using mock data
                return await Task.FromResult(new List<ImageModel>
                {
                    new ImageModel { Id = 1, Title = "Tractor Pull 1", Url = "/images/tractor1.jpg", Description = "Powerful tractor in action" },
                    new ImageModel { Id = 2, Title = "Tractor Pull 2", Url = "/images/tractor2.jpg", Description = "Heavyweight competition" },
                    new ImageModel { Id = 3, Title = "Tractor Pull 3", Url = "/images/tractor3.jpg", Description = "Championship event" },
                    new ImageModel { Id = 4, Title = "Tractor Pull 4", Url = "/images/tractor4.jpg", Description = "Vintage tractor pull" },
                    new ImageModel { Id = 5, Title = "Tractor Pull 5", Url = "/images/tractor5.jpg", Description = "Night event highlights" },
                    new ImageModel { Id = 6, Title = "Tractor Pull 6", Url = "/images/tractor6.jpg", Description = "Crowd favorite" }
                });
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error fetching images");
                throw;
            }
        }
    }

    public class ImageModel
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Url { get; set; }
        public string Description { get; set; }
    }

    public class GalleryController : Controller
    {
        private readonly IImageService _imageService;
        private readonly ILogger<GalleryController> _logger;

        public GalleryController(IImageService imageService, ILogger<GalleryController> logger)
        {
            _imageService = imageService;
            _logger = logger;
        }

        public async Task<IActionResult> Index()
        {
            try
            {
                var images = await _imageService.GetImagesAsync();
                return View(images);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error loading gallery");
                return View("Error", new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
            }
        }

        public IActionResult Details(int id)
        {
            try
            {
                // In a real application, this would fetch a specific image
                var image = new ImageModel
                {
                    Id = id,
                    Title = $"Tractor Pull {id}",
                    Url = $"/images/tractor{id}.jpg",
                    Description = $"Details for tractor pull image {id}"
                };
                return View(image);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error loading details for image {id}");
                return View("Error", new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
            }
        }
    }

    public class ErrorViewModel
    {
        public string RequestId { get; set; }

        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
    }
}

// Views would be in separate files, but for completeness here's what they would contain:

/*
Gallery/Index.cshtml:
@model List<ImageModel>
@{
    ViewData["Title"] = "Tractor Pulling Gallery";
}

<div class="container">
    <h1 class="text-center my-4">@ViewData["Title"]</h1>
    <div class="row">
        @foreach (var image in Model)
        {
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="@image.Url" class="card-img-top" alt="@image.Title">
                    <div class="card-body">
                        <h5 class="card-title">@image.Title</h5>
                        <p class="card-text">@image.Description</p>
                        <a href="@Url.Action("Details", new { id = image.Id })" class="btn btn-primary">View Details</a>
                    </div>
                </div>
            </div>
        }
    </div>
</div>

Gallery/Details.cshtml:
@model ImageModel
@{
    ViewData["Title"] = Model.Title;
}

<div class="container">
    <h1 class="text-center my-4">@Model.Title</h1>
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <img src="@Model.Url" class="card-img-top" alt="@Model.Title">
                <div class="card-body">
                    <h5 class="card-title">@Model.Title</h5>
                    <p class="card-text">@Model.Description</p>
                    <a href="@Url.Action("Index")" class="btn btn-primary">Back to Gallery</a>
                </div>
            </div>
        </div>
    </div>
</div>

Shared/Error.cshtml:
@model ErrorViewModel
@{
    ViewData["Title"] = "Error";
}

<div class="container">
    <h1 class="text-danger">Error.</h1>
    <h2 class="text-danger">An error occurred while processing your request.</h2>

    @if (Model.ShowRequestId)
    {
        <p>
            <strong>Request ID:</strong> <code>@Model.RequestId</code>
        </p>
    }
</div>
*/
```
