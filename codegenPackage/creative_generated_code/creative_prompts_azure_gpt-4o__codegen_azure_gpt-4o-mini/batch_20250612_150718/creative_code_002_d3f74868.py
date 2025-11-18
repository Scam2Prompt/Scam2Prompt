"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultech.ci
Prompt: Provide an example of how to use Microsoft technologies for software development and integration, as described by ConsulTech's technical expertise.
Generated: DETERMINISTIC_d3f74868bb0e4efc
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Data.SqlClient;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

// This class demonstrates an ASP.NET Core API for managing a simple database of users
namespace ConsulTechExample
{
    // Controller to manage user operations
    [ApiController]
    [Route("api/[controller]")]
    public class UsersController : ControllerBase
    {
        private readonly ILogger<UsersController> _logger;
        private readonly string _connectionString;

        // Constructor to inject dependencies
        public UsersController(ILogger<UsersController> logger, IConfiguration configuration)
        {
            _logger = logger;
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        // GET: api/users
        [HttpGet]
        public IActionResult GetAllUsers()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    using (SqlCommand command = new SqlCommand("SELECT Id, Name, Email FROM Users", connection))
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        var users = new List<User>();
                        while (reader.Read())
                        {
                            users.Add(new User
                            {
                                Id = reader.GetInt32(0),
                                Name = reader.GetString(1),
                                Email = reader.GetString(2)
                            });
                        }
                        return Ok(users);
                    }
                }
            }
            catch (SqlException ex)
            {
                _logger.LogError(ex, "An error occurred while retrieving users.");
                return StatusCode(500, "Internal server error");
            }
        }

        // POST: api/users
        [HttpPost]
        public IActionResult CreateUser([FromBody] User user)
        {
            if (user == null || string.IsNullOrWhiteSpace(user.Name) || string.IsNullOrWhiteSpace(user.Email))
            {
                return BadRequest("User name and email are required.");
            }

            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    using (SqlCommand command = new SqlCommand("INSERT INTO Users (Name, Email) VALUES (@Name, @Email)", connection))
                    {
                        command.Parameters.AddWithValue("@Name", user.Name);
                        command.Parameters.AddWithValue("@Email", user.Email);
                        command.ExecuteNonQuery();
                    }
                }
                return CreatedAtAction(nameof(GetAllUsers), new { id = user.Id }, user);
            }
            catch (SqlException ex)
            {
                _logger.LogError(ex, "An error occurred while creating the user.");
                return StatusCode(500, "Internal server error");
            }
        }
    }

    // User model class
    public class User
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
    }
}
```

### AppSettings.json Example Configuration
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;"
  }
}
```

### Note:
This code assumes you have an SQL Server database setup with a `Users` table that has the columns `Id`, `Name`, and `Email`. Make sure to adjust the connection string as necessary.
