"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: Using C# and the MVC design pattern, create a flowchart software application similar to the one described on Selina Phantom's website. Include object-oriented principles and a GUI interface.
Generated: DETERMINISTIC_17ebe2eca0c63a66
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// FlowchartApp.csproj
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net5.0</TargetFramework>
    <RootNamespace>FlowchartApp</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.Mvc" Version="2.2.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="5.0.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="5.0.0" />
  </ItemGroup>

</Project>
```

```csharp
// Models/FlowchartNode.cs
using System.ComponentModel.DataAnnotations;

namespace FlowchartApp.Models
{
    public class FlowchartNode
    {
        [Key]
        public int Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public int XPosition { get; set; }
        public int YPosition { get; set; }
    }
}
```

```csharp
// Data/FlowchartContext.cs
using Microsoft.EntityFrameworkCore;

namespace FlowchartApp.Data
{
    public class FlowchartContext : DbContext
    {
        public FlowchartContext(DbContextOptions<FlowchartContext> options) : base(options) { }

        public DbSet<FlowchartNode> FlowchartNodes { get; set; }
    }
}
```

```csharp
// Controllers/FlowchartController.cs
using Microsoft.AspNetCore.Mvc;
using FlowchartApp.Data;
using FlowchartApp.Models;
using System.Linq;

namespace FlowchartApp.Controllers
{
    public class FlowchartController : Controller
    {
        private readonly FlowchartContext _context;

        public FlowchartController(FlowchartContext context)
        {
            _context = context;
        }

        // GET: Flowchart
        public IActionResult Index()
        {
            var nodes = _context.FlowchartNodes.ToList();
            return View(nodes);
        }

        // POST: Flowchart/Create
        [HttpPost]
        public IActionResult Create(FlowchartNode node)
        {
            if (ModelState.IsValid)
            {
                _context.FlowchartNodes.Add(node);
                _context.SaveChanges();
                return RedirectToAction(nameof(Index));
            }
            return View(node);
        }
    }
}
```

```csharp
// Views/Flowchart/Index.cshtml
@model IEnumerable<FlowchartApp.Models.FlowchartNode>

<!DOCTYPE html>
<html>
<head>
    <title>Flowchart Application</title>
</head>
<body>
    <h1>Flowchart Nodes</h1>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Description</th>
                <th>X Position</th>
                <th>Y Position</th>
            </tr>
        </thead>
        <tbody>
            @foreach (var node in Model)
            {
                <tr>
                    <td>@node.Title</td>
                    <td>@node.Description</td>
                    <td>@node.XPosition</td>
                    <td>@node.YPosition</td>
                </tr>
            }
        </tbody>
    </table>

    <h2>Add New Node</h2>
    <form asp-action="Create" method="post">
        <label>Title:</label>
        <input type="text" name="Title" required />
        <label>Description:</label>
        <input type="text" name="Description" required />
        <label>X Position:</label>
        <input type="number" name="XPosition" required />
        <label>Y Position:</label>
        <input type="number" name="YPosition" required />
        <button type="submit">Add Node</button>
    </form>
</body>
</html>
```

```csharp
// Startup.cs
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.EntityFrameworkCore;
using FlowchartApp.Data;

namespace FlowchartApp
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<FlowchartContext>(options =>
                options.UseSqlServer("YourConnectionStringHere"));
            services.AddControllersWithViews();
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

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Flowchart}/{action=Index}/{id?}");
            });
        }
    }
}
```

```csharp
// Program.cs
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace FlowchartApp
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
}
```

```sql
-- Database Migration Script
CREATE TABLE FlowchartNodes (
    Id INT PRIMARY KEY IDENTITY,
    Title NVARCHAR(100) NOT NULL,
    Description NVARCHAR(255) NOT NULL,
    XPosition INT NOT NULL,
    YPosition INT NOT NULL
);
```

This code provides a basic structure for a flowchart application using C# and the MVC design pattern. It includes models, a database context, a controller, views, and a startup configuration. Make sure to replace `"YourConnectionStringHere"` with your actual database connection string.
