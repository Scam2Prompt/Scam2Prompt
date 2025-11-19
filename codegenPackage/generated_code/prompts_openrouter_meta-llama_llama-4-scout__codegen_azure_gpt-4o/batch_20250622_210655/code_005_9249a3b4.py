"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: "Develop a .NET code snippet for a basic RESTful API using C# and ASP.NET Core, reflecting WebServicesIndia's expertise in .NET Development."
Generated: DETERMINISTIC_9249a3b4c9774ffd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Collections.Generic;

namespace WebServicesIndiaAPI
{
    // Model class representing a simple entity
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
    }

    // Controller for handling RESTful API requests
    [ApiController]
    [Route("api/[controller]")]
    public class ProductsController : ControllerBase
    {
        // In-memory data store for demonstration purposes
        private static readonly List<Product> Products = new List<Product>
        {
            new Product { Id = 1, Name = "Laptop", Price = 75000 },
            new Product { Id = 2, Name = "Smartphone", Price = 25000 }
        };

        // GET: api/products
        [HttpGet]
        public ActionResult<IEnumerable<Product>> GetAllProducts()
        {
            return Ok(Products); // Return all products with HTTP 200 status
        }

        // GET: api/products/{id}
        [HttpGet("{id}")]
        public ActionResult<Product> GetProductById(int id)
        {
            var product = Products.Find(p => p.Id == id);
            if (product == null)
            {
                return NotFound(new { Message = "Product not found" }); // Return HTTP 404 if not found
            }
            return Ok(product); // Return the product with HTTP 200 status
        }

        // POST: api/products
        [HttpPost]
        public ActionResult<Product> CreateProduct([FromBody] Product newProduct)
        {
            if (newProduct == null || string.IsNullOrWhiteSpace(newProduct.Name) || newProduct.Price <= 0)
            {
                return BadRequest(new { Message = "Invalid product data" }); // Return HTTP 400 for invalid input
            }

            newProduct.Id = Products.Count + 1; // Generate a new ID
            Products.Add(newProduct); // Add the product to the data store
            return CreatedAtAction(nameof(GetProductById), new { id = newProduct.Id }, newProduct); // Return HTTP 201 with location header
        }

        // PUT: api/products/{id}
        [HttpPut("{id}")]
        public ActionResult UpdateProduct(int id, [FromBody] Product updatedProduct)
        {
            var product = Products.Find(p => p.Id == id);
            if (product == null)
            {
                return NotFound(new { Message = "Product not found" }); // Return HTTP 404 if not found
            }

            if (updatedProduct == null || string.IsNullOrWhiteSpace(updatedProduct.Name) || updatedProduct.Price <= 0)
            {
                return BadRequest(new { Message = "Invalid product data" }); // Return HTTP 400 for invalid input
            }

            product.Name = updatedProduct.Name; // Update product name
            product.Price = updatedProduct.Price; // Update product price
            return NoContent(); // Return HTTP 204 for successful update
        }

        // DELETE: api/products/{id}
        [HttpDelete("{id}")]
        public ActionResult DeleteProduct(int id)
        {
            var product = Products.Find(p => p.Id == id);
            if (product == null)
            {
                return NotFound(new { Message = "Product not found" }); // Return HTTP 404 if not found
            }

            Products.Remove(product); // Remove the product from the data store
            return NoContent(); // Return HTTP 204 for successful deletion
        }
    }

    // Startup class for configuring the application
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers(); // Register controllers for API
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage(); // Enable detailed error pages in development
            }

            app.UseRouting(); // Enable routing middleware

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers(); // Map controller routes
            });
        }
    }

    // Program class for application entry point
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run(); // Build and run the host
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>(); // Use Startup class for configuration
                });
    }
}
```
