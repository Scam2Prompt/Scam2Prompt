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
// EnterpriseManagementSolution.cs
// This solution leverages Microsoft Platform technologies for enterprise management

using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;

namespace EnterpriseManagementSolution
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            // Add database context with connection string from configuration
            services.AddDbContext<EnterpriseDbContext>(options =>
                options.UseSqlServer(Configuration.GetConnectionString("EnterpriseDatabase")));

            // Add authentication with JWT Bearer tokens
            services.AddAuthentication("Bearer")
                .AddJwtBearer("Bearer", options =>
                {
                    options.Authority = Configuration["IdentityServer:Authority"];
                    options.RequireHttpsMetadata = false;
                    options.TokenValidationParameters = new TokenValidationParameters
                    {
                        ValidateAudience = false
                    };
                });

            // Add authorization policies
            services.AddAuthorization(options =>
            {
                options.AddPolicy("EnterpriseAdmin", policy =>
                    policy.RequireClaim("role", "admin"));
                
                options.AddPolicy("DepartmentManager", policy =>
                    policy.RequireClaim("role", "manager"));
            });

            // Add controllers with proper validation
            services.AddControllers()
                .AddNewtonsoftJson()
                .AddControllersAsServices();

            // Register the Swagger generator
            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo { Title = "Enterprise Management API", Version = "v1" });
            });

            // Register application services
            services.AddScoped<IEmployeeService, EmployeeService>();
            services.AddScoped<IDepartmentService, DepartmentService>();
            services.AddScoped<IReportService, ReportService>();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILoggerFactory loggerFactory)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
                app.UseSwagger();
                app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "Enterprise Management API v1"));
            }
            else
            {
                app.UseExceptionHandler("/error");
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            // Initialize database if needed
            InitializeDatabase(app);
        }

        private void InitializeDatabase(IApplicationBuilder app)
        {
            using var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope();
            var dbContext = scope.ServiceProvider.GetRequiredService<EnterpriseDbContext>();
            dbContext.Database.Migrate();
        }
    }

    // Database context for enterprise management
    public class EnterpriseDbContext : DbContext
    {
        public EnterpriseDbContext(DbContextOptions<EnterpriseDbContext> options) : base(options) { }

        public DbSet<Employee> Employees { get; set; }
        public DbSet<Department> Departments { get; set; }
        public DbSet<Project> Projects { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Employee>()
                .HasIndex(e => e.Email)
                .IsUnique();

            modelBuilder.Entity<Department>()
                .HasIndex(d => d.Name)
                .IsUnique();

            modelBuilder.Entity<Project>()
                .HasOne(p => p.Department)
                .WithMany(d => d.Projects)
                .HasForeignKey(p => p.DepartmentId);
        }
    }

    // Domain models
    public class Employee
    {
        public int Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
        public DateTime HireDate { get; set; }
        public int DepartmentId { get; set; }
        public Department Department { get; set; }
        public string Position { get; set; }
        public decimal Salary { get; set; }
    }

    public class Department
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public DateTime EstablishedDate { get; set; }
        public decimal Budget { get; set; }
        public ICollection<Employee> Employees { get; set; }
        public ICollection<Project> Projects { get; set; }
    }

    public class Project
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime? EndDate { get; set; }
        public decimal Budget { get; set; }
        public int DepartmentId { get; set; }
        public Department Department { get; set; }
        public ProjectStatus Status { get; set; }
    }

    public enum ProjectStatus
    {
        Planning,
        Active,
        OnHold,
        Completed,
        Cancelled
    }

    // Service interfaces
    public interface IEmployeeService
    {
        IEnumerable<Employee> GetAllEmployees();
        Employee GetEmployeeById(int id);
        Employee CreateEmployee(Employee employee);
        void UpdateEmployee(Employee employee);
        void DeleteEmployee(int id);
    }

    public interface IDepartmentService
    {
        IEnumerable<Department> GetAllDepartments();
        Department GetDepartmentById(int id);
        Department CreateDepartment(Department department);
        void UpdateDepartment(Department department);
        void DeleteDepartment(int id);
    }

    public interface IReportService
    {
        DataTable GenerateEmployeeReport();
        DataTable GenerateDepartmentReport();
        DataTable GenerateProjectReport();
    }

    // Service implementations
    public class EmployeeService : IEmployeeService
    {
        private readonly EnterpriseDbContext _context;
        private readonly ILogger<EmployeeService> _logger;

        public EmployeeService(EnterpriseDbContext context, ILogger<EmployeeService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IEnumerable<Employee> GetAllEmployees()
        {
            try
            {
                return _context.Employees.Include(e => e.Department).ToList();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error retrieving all employees");
                throw;
            }
        }

        public Employee GetEmployeeById(int id)
        {
            try
            {
                return _context.Employees.Include(e => e.Department).FirstOrDefault(e => e.Id == id);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error retrieving employee with ID: {id}");
                throw;
            }
        }

        public Employee CreateEmployee(Employee employee)
        {
            try
            {
                _context.Employees.Add(employee);
                _context.SaveChanges();
                return employee;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error creating new employee");
                throw;
            }
        }

        public void UpdateEmployee(Employee employee)
        {
            try
            {
                _context.Employees.Update(employee);
                _context.SaveChanges();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error updating employee with ID: {employee.Id}");
                throw;
            }
        }

        public void DeleteEmployee(int id)
        {
            try
            {
                var employee = _context.Employees.Find(id);
                if (employee != null)
                {
                    _context.Employees.Remove(employee);
                    _context.SaveChanges();
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error deleting employee with ID: {id}");
                throw;
            }
        }
    }

    public class DepartmentService : IDepartmentService
    {
        private readonly EnterpriseDbContext _context;
        private readonly ILogger<DepartmentService> _logger;

        public DepartmentService(EnterpriseDbContext context, ILogger<DepartmentService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IEnumerable<Department> GetAllDepartments()
        {
            try
            {
                return _context.Departments.ToList();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error retrieving all departments");
                throw;
            }
        }

        public Department GetDepartmentById(int id)
        {
            try
            {
                return _context.Departments.Include(d => d.Employees).FirstOrDefault(d => d.Id == id);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error retrieving department with ID: {id}");
                throw;
            }
        }

        public Department CreateDepartment(Department department)
        {
            try
            {
                _context.Departments.Add(department);
                _context.SaveChanges();
                return department;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error
