"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Generate a C# code snippet for a flowchart software using MVC architecture as described on the personal website of 蘇李冠穎.
Generated: DETERMINISTIC_9d55110f58fb5f39
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
// Models/Node.cs
using System;
using System.Collections.Generic;

namespace FlowchartApp.Models
{
    /// <summary>
    /// Represents a node in the flowchart.
    /// </summary>
    public class Node
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Type { get; set; } // e.g. "Start", "Process", "Decision", "End"
        public List<int> ConnectedNodeIds { get; set; } = new List<int>();
    }
}

// Models/Flowchart.cs
using System.Collections.Generic;

namespace FlowchartApp.Models
{
    /// <summary>
    /// Represents the overall flowchart structure.
    /// </summary>
    public class Flowchart
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public List<Node> Nodes { get; set; } = new List<Node>();
    }
}

// Controllers/FlowchartController.cs
using System;
using System.Collections.Generic;
using System.Linq;
using FlowchartApp.Models;
using Microsoft.AspNetCore.Mvc;

namespace FlowchartApp.Controllers
{
    /// <summary>
    /// Controller to handle flowchart-related requests.
    /// </summary>
    [ApiController]
    [Route("api/[controller]")]
    public class FlowchartController : ControllerBase
    {
        // Simulated in-memory storage for demonstration purposes.
        private static readonly List<Flowchart> Flowcharts = new();

        /// <summary>
        /// Get all flowcharts.
        /// </summary>
        /// <returns>A list of flowcharts.</returns>
        [HttpGet]
        public ActionResult<IEnumerable<Flowchart>> GetAllFlowcharts()
        {
            return Ok(Flowcharts);
        }

        /// <summary>
        /// Get a specific flowchart by ID.
        /// </summary>
        /// <param name="id">Flowchart ID.</param>
        /// <returns>The flowchart with the given ID.</returns>
        [HttpGet("{id}")]
        public ActionResult<Flowchart> GetFlowchartById(int id)
        {
            var flowchart = Flowcharts.FirstOrDefault(f => f.Id == id);
            if (flowchart == null)
            {
                return NotFound(new { Message = "Flowchart not found." });
            }
            return Ok(flowchart);
        }

        /// <summary>
        /// Create a new flowchart.
        /// </summary>
        /// <param name="flowchart">Flowchart data.</param>
        /// <returns>The created flowchart.</returns>
        [HttpPost]
        public ActionResult<Flowchart> CreateFlowchart([FromBody] Flowchart flowchart)
        {
            if (flowchart == null || string.IsNullOrEmpty(flowchart.Title))
            {
                return BadRequest(new { Message = "Invalid flowchart data." });
            }

            flowchart.Id = Flowcharts.Count > 0 ? Flowcharts.Max(f => f.Id) + 1 : 1;
            Flowcharts.Add(flowchart);
            return CreatedAtAction(nameof(GetFlowchartById), new { id = flowchart.Id }, flowchart);
        }

        /// <summary>
        /// Update an existing flowchart.
        /// </summary>
        /// <param name="id">Flowchart ID.</param>
        /// <param name="updatedFlowchart">Updated flowchart data.</param>
        /// <returns>No content if successful.</returns>
        [HttpPut("{id}")]
        public IActionResult UpdateFlowchart(int id, [FromBody] Flowchart updatedFlowchart)
        {
            var flowchart = Flowcharts.FirstOrDefault(f => f.Id == id);
            if (flowchart == null)
            {
                return NotFound(new { Message = "Flowchart not found." });
            }

            if (updatedFlowchart == null || string.IsNullOrEmpty(updatedFlowchart.Title))
            {
                return BadRequest(new { Message = "Invalid flowchart data." });
            }

            flowchart.Title = updatedFlowchart.Title;
            flowchart.Nodes = updatedFlowchart.Nodes;
            return NoContent();
        }

        /// <summary>
        /// Delete a flowchart.
        /// </summary>
        /// <param name="id">Flowchart ID.</param>
        /// <returns>No content if successful.</returns>
        [HttpDelete("{id}")]
        public IActionResult DeleteFlowchart(int id)
        {
            var flowchart = Flowcharts.FirstOrDefault(f => f.Id == id);
            if (flowchart == null)
            {
                return NotFound(new { Message = "Flowchart not found." });
            }

            Flowcharts.Remove(flowchart);
            return NoContent();
        }
    }
}

// Views/FlowchartView.cshtml (Simple HTML View for Demonstration)
@model FlowchartApp.Models.Flowchart

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@Model.Title</title>
</head>
<body>
    <h1>@Model.Title</h1>
    <ul>
        @foreach (var node in Model.Nodes)
        {
            <li>
                <b>@node.Name</b> (@node.Type)<br/>
                Connected Nodes: @string.Join(", ", node.ConnectedNodeIds)
            </li>
        }
    </ul>
</body>
</html>

// Program.cs (Entry Point)
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

// Startup.cs
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace FlowchartApp
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers(); // Add MVC controllers.
        }

        public void Configure(IApplicationBuilder app, IHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
```
