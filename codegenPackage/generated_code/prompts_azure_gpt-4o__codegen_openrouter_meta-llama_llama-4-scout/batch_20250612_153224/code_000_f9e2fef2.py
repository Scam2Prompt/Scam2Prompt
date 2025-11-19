"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Write a code snippet using Microsoft technologies to create a secure, customizable software solution for enterprise management, referencing MetaCode's approach to personalized systems.
Generated: DETERMINISTIC_f9e2fef21b760d3e
Batch ID: 20250612_153224
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
using System.Security.Cryptography;
using System.Text;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.IdentityModel.Tokens;

// Define a custom exception for handling errors
public class EnterpriseManagementException : Exception
{
    public EnterpriseManagementException(string message) : base(message) { }
}

// Define a model for user authentication
public class UserModel
{
    public string Username { get; set; }
    public string Password { get; set; }
}

// Define a model for enterprise management
public class EnterpriseModel
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
}

// Define a service for user authentication
public interface IUserService
{
    string Authenticate(UserModel user);
}

public class UserService : IUserService
{
    private readonly IConfiguration _configuration;

    public UserService(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public string Authenticate(UserModel user)
    {
        // Implement authentication logic here
        // For demonstration purposes, assume username and password are valid
        if (user.Username == "admin" && user.Password == "password")
        {
            var token = GenerateJwtToken(user.Username);
            return token;
        }
        throw new EnterpriseManagementException("Invalid username or password");
    }

    private string GenerateJwtToken(string username)
    {
        var claims = new[]
        {
            new Claim(ClaimTypes.Name, username),
            new Claim(ClaimTypes.NameIdentifier, Guid.NewGuid().ToString())
        };

        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["Jwt:Key"]));
        var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

        var token = new JwtSecurityToken(_configuration["Jwt:Issuer"],
            _configuration["Jwt:Audience"],
            claims,
            expires: DateTime.UtcNow.AddMinutes(30),
            signingCredentials: creds);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }
}

// Define a service for enterprise management
public interface IEnterpriseService
{
    List<EnterpriseModel> GetEnterprises();
}

public class EnterpriseService : IEnterpriseService
{
    public List<EnterpriseModel> GetEnterprises()
    {
        // Implement logic to retrieve enterprises here
        // For demonstration purposes, return a sample list
        return new List<EnterpriseModel>
        {
            new EnterpriseModel { Id = 1, Name = "Enterprise 1", Description = "Description 1" },
            new EnterpriseModel { Id = 2, Name = "Enterprise 2", Description = "Description 2" }
        };
    }
}

// Define a controller for enterprise management
[ApiController]
[Route("api/[controller]")]
[Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
public class EnterpriseController : ControllerBase
{
    private readonly IEnterpriseService _enterpriseService;

    public EnterpriseController(IEnterpriseService enterpriseService)
    {
        _enterpriseService = enterpriseService;
    }

    [HttpGet]
    public IActionResult GetEnterprises()
    {
        try
        {
            var enterprises = _enterpriseService.GetEnterprises();
            return Ok(enterprises);
        }
        catch (Exception ex)
        {
            return StatusCode(500, ex.Message);
        }
    }
}

// Define a startup class for the application
public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddAuthentication(options =>
        {
            options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
            options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
        })
        .AddJwtBearer(options =>
        {
            options.TokenValidationParameters = new TokenValidationParameters
            {
                ValidateIssuer = true,
                ValidateAudience = true,
                ValidateLifetime = true,
                ValidateIssuerSigningKey = true,
                ValidIssuer = Configuration["Jwt:Issuer"],
                ValidAudience = Configuration["Jwt:Audience"],
                IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration["Jwt:Key"]))
            };
        });

        services.AddTransient<IUserService, UserService>();
        services.AddTransient<IEnterpriseService, EnterpriseService>();

        services.AddControllers();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        app.UseRouting();
        app.UseAuthentication();
        app.UseAuthorization();
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers();
        });
    }
}

// Define a main class for the application
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
```

appsettings.json:
```json
{
  "Jwt": {
    "Key": "your_secret_key_here",
    "Issuer": "your_issuer_here",
    "Audience": "your_audience_here"
  }
}
```
