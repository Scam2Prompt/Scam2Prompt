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
// EnterpriseManagementSystem.cs
// A secure, customizable enterprise management solution inspired by MetaCode's approach

using System;
using System.Collections.Generic;
using System.Security;
using System.Security.Cryptography;
using System.Text;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.IdentityModel.Tokens;

namespace EnterpriseManagementSystem
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // Configure services
        public void ConfigureServices(IServiceCollection services)
        {
            // Add database context with secure connection
            services.AddDbContext<EnterpriseDbContext>(options =>
                options.UseSqlServer(
                    Configuration.GetConnectionString("SecureEnterpriseConnection"),
                    sqlOptions => sqlOptions.EnableRetryOnFailure()));

            // Configure JWT authentication
            var jwtSettings = Configuration.GetSection("JwtSettings");
            services.AddAuthentication(options =>
            {
                options.DefaultAuthenticateScheme = "JwtBearer";
                options.DefaultChallengeScheme = "JwtBearer";
            })
            .AddJwtBearer("JwtBearer", jwtBearerOptions =>
            {
                jwtBearerOptions.TokenValidationParameters = new TokenValidationParameters
                {
                    ValidateIssuerSigningKey = true,
                    IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtSettings["SecretKey"])),
                    ValidateIssuer = true,
                    ValidIssuer = jwtSettings["Issuer"],
                    ValidateAudience = true,
                    ValidAudience = jwtSettings["Audience"],
                    ValidateLifetime = true,
                    ClockSkew = TimeSpan.FromMinutes(5)
                };
            });

            // Add authorization policies
            services.AddAuthorization(options =>
            {
                options.AddPolicy("AdminOnly", policy => policy.RequireRole("Admin"));
                options.AddPolicy("CustomAccess", policy => 
                    policy.Requirements.Add(new CustomAccessRequirement()));
            });

            // Register custom services
            services.AddScoped<IAuthorizationHandler, CustomAccessHandler>();
            services.AddScoped<IEnterpriseService, EnterpriseService>();
            services.AddScoped<ISecurityService, SecurityService>();

            // Add controllers with validation
            services.AddControllers(options =>
            {
                options.Filters.Add(new ValidateModelAttribute());
            });

            // Configure Swagger for API documentation
            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new Microsoft.OpenApi.Models.OpenApiInfo { Title = "Enterprise API", Version = "v1" });
            });
        }

        // Configure HTTP request pipeline
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
                app.UseSwagger();
                app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "Enterprise API v1"));
            }
            else
            {
                app.UseHsts();
                app.UseExceptionHandler("/error");
            }

            app.UseHttpsRedirection();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }

    // Custom authorization requirement
    public class CustomAccessRequirement : IAuthorizationRequirement
    {
        public string RequiredPermission { get; }

        public CustomAccessRequirement(string requiredPermission = null)
        {
            RequiredPermission = requiredPermission;
        }
    }

    // Custom authorization handler
    public class CustomAccessHandler : AuthorizationHandler<CustomAccessRequirement>
    {
        protected override Task HandleRequirementAsync(AuthorizationHandlerContext context, CustomAccessRequirement requirement)
        {
            if (context.User.HasClaim(c => c.Type == "permissions" && 
                (requirement.RequiredPermission == null || c.Value == requirement.RequiredPermission)))
            {
                context.Succeed(requirement);
            }
            return Task.CompletedTask;
        }
    }

    // Model validation attribute
    public class ValidateModelAttribute : ActionFilterAttribute
    {
        public override void OnActionExecuting(ActionExecutingContext context)
        {
            if (!context.ModelState.IsValid)
            {
                context.Result = new BadRequestObjectResult(context.ModelState);
            }
        }
    }

    // Database context
    public class EnterpriseDbContext : DbContext
    {
        public EnterpriseDbContext(DbContextOptions<EnterpriseDbContext> options) : base(options) { }

        public DbSet<EnterpriseUser> Users { get; set; }
        public DbSet<EnterpriseModule> Modules { get; set; }
        public DbSet<UserPermission> Permissions { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<EnterpriseUser>().HasIndex(u => u.Email).IsUnique();
            modelBuilder.Entity<EnterpriseModule>().HasIndex(m => m.Name).IsUnique();
        }
    }

    // Domain models
    public class EnterpriseUser
    {
        public int Id { get; set; }
        public string Email { get; set; }
        public byte[] PasswordHash { get; set; }
        public byte[] PasswordSalt { get; set; }
        public string Role { get; set; }
        public bool IsActive { get; set; }
        public DateTime LastLogin { get; set; }
        public ICollection<UserPermission> Permissions { get; set; }
    }

    public class EnterpriseModule
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public bool IsEnabled { get; set; }
        public string Configuration { get; set; }
    }

    public class UserPermission
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public EnterpriseUser User { get; set; }
        public string PermissionName { get; set; }
        public string Scope { get; set; }
    }

    // Core services
    public interface IEnterpriseService
    {
        Task<EnterpriseModule> GetModuleAsync(int id);
        Task<IEnumerable<EnterpriseModule>> GetAllModulesAsync();
        Task<EnterpriseModule> ConfigureModuleAsync(int id, string configuration);
    }

    public interface ISecurityService
    {
        Task<EnterpriseUser> AuthenticateAsync(string email, string password);
        Task<EnterpriseUser> RegisterAsync(EnterpriseUser user, string password);
        string GenerateJwtToken(EnterpriseUser user);
    }

    public class EnterpriseService : IEnterpriseService
    {
        private readonly EnterpriseDbContext _context;

        public EnterpriseService(EnterpriseDbContext context)
        {
            _context = context;
        }

        public async Task<EnterpriseModule> GetModuleAsync(int id)
        {
            return await _context.Modules.FindAsync(id);
        }

        public async Task<IEnumerable<EnterpriseModule>> GetAllModulesAsync()
        {
            return await _context.Modules.ToListAsync();
        }

        public async Task<EnterpriseModule> ConfigureModuleAsync(int id, string configuration)
        {
            var module = await _context.Modules.FindAsync(id);
            if (module == null)
                throw new KeyNotFoundException("Module not found");

            module.Configuration = configuration;
            await _context.SaveChangesAsync();
            return module;
        }
    }

    public class SecurityService : ISecurityService
    {
        private readonly EnterpriseDbContext _context;
        private readonly IConfiguration _configuration;

        public SecurityService(EnterpriseDbContext context, IConfiguration configuration)
        {
            _context = context;
            _configuration = configuration;
        }

        public async Task<EnterpriseUser> AuthenticateAsync(string email, string password)
        {
            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
                return null;

            var user = await _context.Users.Include(u => u.Permissions)
                .FirstOrDefaultAsync(x => x.Email == email);

            if (user == null || !VerifyPasswordHash(password, user.PasswordHash, user.PasswordSalt))
                return null;

            user.LastLogin = DateTime.UtcNow;
            await _context.SaveChangesAsync();

            return user;
        }

        public async Task<EnterpriseUser> RegisterAsync(EnterpriseUser user, string password)
        {
            if (await _context.Users.AnyAsync(x => x.Email == user.Email))
                throw new ApplicationException("Email already exists");

            CreatePasswordHash(password, out var passwordHash, out var passwordSalt);

            user.PasswordHash = passwordHash;
            user.PasswordSalt = passwordSalt;
            user.IsActive = true;

            await _context.Users.AddAsync(user);
            await _context.SaveChangesAsync();

            return user;
        }

        public string GenerateJwtToken(EnterpriseUser user)
        {
            var tokenHandler = new System.IdentityModel.Tokens.Jwt.JwtSecurityTokenHandler();
            var key = Encoding.ASCII.GetBytes(_configuration["JwtSettings:SecretKey"]);
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new System.Security.Claims.ClaimsIdentity(new[]
                {
                    new System.Security.Claims.Claim(System.Security.Claims.ClaimTypes.Name, user.Id.ToString()),
                    new System.Security.Claims.Claim(System.Security.Claims.ClaimTypes.Role, user.Role),
                    new System.Security.Claims.
