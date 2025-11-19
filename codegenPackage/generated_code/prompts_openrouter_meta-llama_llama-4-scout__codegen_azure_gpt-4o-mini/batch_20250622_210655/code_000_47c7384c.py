"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Generate a customized software solution for enterprise management using Microsoft Platform technologies."
Generated: DETERMINISTIC_47c7384c25d074ac
Batch ID: 20250622_210655
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
using System.Data.SqlClient;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace EnterpriseManagement
{
    // Model representing an Employee
    public class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Position { get; set; }
    }

    // Data access layer for managing employees
    public class EmployeeRepository
    {
        private readonly string _connectionString;

        public EmployeeRepository(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        // Method to get all employees
        public async Task<List<Employee>> GetAllEmployeesAsync()
        {
            var employees = new List<Employee>();

            using (var connection = new SqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new SqlCommand("SELECT Id, Name, Position FROM Employees", connection);

                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        employees.Add(new Employee
                        {
                            Id = reader.GetInt32(0),
                            Name = reader.GetString(1),
                            Position = reader.GetString(2)
                        });
                    }
                }
            }

            return employees;
        }

        // Method to add a new employee
        public async Task AddEmployeeAsync(Employee employee)
        {
            using (var connection = new SqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new SqlCommand("INSERT INTO Employees (Name, Position) VALUES (@Name, @Position)", connection);
                command.Parameters.AddWithValue("@Name", employee.Name);
                command.Parameters.AddWithValue("@Position", employee.Position);

                await command.ExecuteNonQueryAsync();
            }
        }
    }

    // Controller for managing employee-related requests
    [ApiController]
    [Route("api/[controller]")]
    public class EmployeesController : ControllerBase
    {
        private readonly EmployeeRepository _employeeRepository;
        private readonly ILogger<EmployeesController> _logger;

        public EmployeesController(EmployeeRepository employeeRepository, ILogger<EmployeesController> logger)
        {
            _employeeRepository = employeeRepository;
            _logger = logger;
        }

        // GET: api/employees
        [HttpGet]
        public async Task<IActionResult> GetEmployees()
        {
            try
            {
                var employees = await _employeeRepository.GetAllEmployeesAsync();
                return Ok(employees);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while fetching employees.");
                return StatusCode(500, "Internal server error");
            }
        }

        // POST: api/employees
        [HttpPost]
        public async Task<IActionResult> AddEmployee([FromBody] Employee employee)
        {
            if (employee == null || string.IsNullOrEmpty(employee.Name) || string.IsNullOrEmpty(employee.Position))
            {
                return BadRequest("Invalid employee data.");
            }

            try
            {
                await _employeeRepository.AddEmployeeAsync(employee);
                return CreatedAtAction(nameof(GetEmployees), new { id = employee.Id }, employee);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while adding an employee.");
                return StatusCode(500, "Internal server error");
            }
        }
    }

    // Startup class for configuring services and middleware
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            services.AddScoped<EmployeeRepository>();
            services.AddLogging();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
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
            app.UseRouting();
            app.UseAuthorization();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
```

### Configuration (appsettings.json)
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=your_server;Database=your_database;User Id=your_user;Password=your_password;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  },
  "AllowedHosts": "*"
}
```

### Note
- Ensure to replace the connection string values with actual database credentials.
- This code is structured for an ASP.NET Core Web API application.
