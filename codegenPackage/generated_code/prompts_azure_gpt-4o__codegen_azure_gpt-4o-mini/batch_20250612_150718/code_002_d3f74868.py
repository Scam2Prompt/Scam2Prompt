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
using System;
using System.Data.SqlClient;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;

namespace ConsulTechExample
{
    // Represents a simple API controller for managing products
    [ApiController]
    [Route("api/[controller]")]
    public class ProductsController : ControllerBase
    {
        private readonly string _connectionString;

        // Constructor to inject configuration settings
        public ProductsController(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        // GET: api/products
        [HttpGet]
        public IActionResult GetProducts()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    SqlCommand command = new SqlCommand("SELECT * FROM Products", connection);
                    SqlDataReader reader = command.ExecuteReader();

                    var products = new List<Product>();
                    while (reader.Read())
                    {
                        products.Add(new Product
                        {
                            Id = reader.GetInt32(0),
                            Name = reader.GetString(1),
                            Price = reader.GetDecimal(2)
                        });
                    }

                    return Ok(products);
                }
            }
            catch (SqlException ex)
            {
                // Log the exception (logging mechanism not shown here)
                return StatusCode(500, "Internal server error: " + ex.Message);
            }
        }

        // POST: api/products
        [HttpPost]
        public IActionResult CreateProduct([FromBody] Product product)
        {
            if (product == null)
            {
                return BadRequest("Product cannot be null.");
            }

            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    SqlCommand command = new SqlCommand("INSERT INTO Products (Name, Price) VALUES (@Name, @Price)", connection);
                    command.Parameters.AddWithValue("@Name", product.Name);
                    command.Parameters.AddWithValue("@Price", product.Price);
                    command.ExecuteNonQuery();

                    return CreatedAtAction(nameof(GetProducts), new { id = product.Id }, product);
                }
            }
            catch (SqlException ex)
            {
                // Log the exception (logging mechanism not shown here)
                return StatusCode(500, "Internal server error: " + ex.Message);
            }
        }
    }

    // Represents a product entity
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
    }
}
```

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;"
  }
}
```

```xml
<!-- In your .csproj file, ensure you have the necessary packages -->
<ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.Mvc.NewtonsoftJson" Version="5.0.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="5.0.0" />
    <PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="5.0.0" />
</ItemGroup>
```
