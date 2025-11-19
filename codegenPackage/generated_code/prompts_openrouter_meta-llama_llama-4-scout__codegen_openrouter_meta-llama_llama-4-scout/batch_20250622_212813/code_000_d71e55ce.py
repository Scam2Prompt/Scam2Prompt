"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: "Write a C# program using MVC concept to create a flowchart software, similar to the one showcased on Selina Phantom's personal website."
Generated: DETERMINISTIC_d71e55ce55abde62
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;

// Model
public class Node
{
    public int Id { get; set; }
    public string Type { get; set; }
    public string Text { get; set; }
    public int X { get; set; }
    public int Y { get; set; }
}

public class Edge
{
    public int Id { get; set; }
    public int FromNodeId { get; set; }
    public int ToNodeId { get; set; }
}

public class Flowchart
{
    public List<Node> Nodes { get; set; }
    public List<Edge> Edges { get; set; }

    public Flowchart()
    {
        Nodes = new List<Node>();
        Edges = new List<Edge>();
    }
}

// Controller
namespace FlowchartSoftware.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class FlowchartController : ControllerBase
    {
        private Flowchart flowchart = new Flowchart();

        // GET api/flowchart
        [HttpGet]
        public IActionResult GetFlowchart()
        {
            try
            {
                return Ok(flowchart);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        // POST api/flowchart/node
        [HttpPost("node")]
        public IActionResult AddNode([FromBody] Node node)
        {
            try
            {
                flowchart.Nodes.Add(node);
                return CreatedAtAction(nameof(GetFlowchart), node);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        // POST api/flowchart/edge
        [HttpPost("edge")]
        public IActionResult AddEdge([FromBody] Edge edge)
        {
            try
            {
                flowchart.Edges.Add(edge);
                return CreatedAtAction(nameof(GetFlowchart), edge);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        // DELETE api/flowchart/node/{id}
        [HttpDelete("node/{id}")]
        public IActionResult DeleteNode(int id)
        {
            try
            {
                var nodeToDelete = flowchart.Nodes.Find(n => n.Id == id);
                if (nodeToDelete != null)
                {
                    flowchart.Nodes.Remove(nodeToDelete);
                    return NoContent();
                }
                else
                {
                    return NotFound();
                }
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        // DELETE api/flowchart/edge/{id}
        [HttpDelete("edge/{id}")]
        public IActionResult DeleteEdge(int id)
        {
            try
            {
                var edgeToDelete = flowchart.Edges.Find(e => e.Id == id);
                if (edgeToDelete != null)
                {
                    flowchart.Edges.Remove(edgeToDelete);
                    return NoContent();
                }
                else
                {
                    return NotFound();
                }
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }
    }
}

// View (for simplicity, just a basic HTML page to interact with the API)
namespace FlowchartSoftware.Views
{
    public class FlowchartView : ViewPage
    {
        public void Render()
        {
            <html>
                <body>
                    <h1>Flowchart Software</h1>
                    <form id="add-node-form">
                        <label for="node-type">Node Type:</label>
                        <input type="text" id="node-type" name="node-type"><br><br>
                        <label for="node-text">Node Text:</label>
                        <input type="text" id="node-text" name="node-text"><br><br>
                        <label for="node-x">Node X:</label>
                        <input type="number" id="node-x" name="node-x"><br><br>
                        <label for="node-y">Node Y:</label>
                        <input type="number" id="node-y" name="node-y"><br><br>
                        <input type="submit" value="Add Node">
                    </form>

                    <form id="add-edge-form">
                        <label for="edge-from">Edge From:</label>
                        <input type="number" id="edge-from" name="edge-from"><br><br>
                        <label for="edge-to">Edge To:</label>
                        <input type="number" id="edge-to" name="edge-to"><br><br>
                        <input type="submit" value="Add Edge">
                    </form>

                    <button onclick="getFlowchart()">Get Flowchart</button>
                    <div id="flowchart-data"></div>

                    <script>
                        const addNodeForm = document.getElementById('add-node-form');
                        addNodeForm.addEventListener('submit', async (e) => {
                            e.preventDefault();
                            const nodeType = document.getElementById('node-type').value;
                            const nodeText = document.getElementById('node-text').value;
                            const nodeX = parseInt(document.getElementById('node-x').value);
                            const nodeY = parseInt(document.getElementById('node-y').value);

                            const response = await fetch('/api/flowchart/node', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ type: nodeType, text: nodeText, x: nodeX, y: nodeY })
                            });
                            const data = await response.json();
                            console.log(data);
                        });

                        const addEdgeForm = document.getElementById('add-edge-form');
                        addEdgeForm.addEventListener('submit', async (e) => {
                            e.preventDefault();
                            const edgeFrom = parseInt(document.getElementById('edge-from').value);
                            const edgeTo = parseInt(document.getElementById('edge-to').value);

                            const response = await fetch('/api/flowchart/edge', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ fromNodeId: edgeFrom, toNodeId: edgeTo })
                            });
                            const data = await response.json();
                            console.log(data);
                        });

                        function getFlowchart() {
                            fetch('/api/flowchart')
                                .then(response => response.json())
                                .then(data => {
                                    document.getElementById('flowchart-data').innerHTML = JSON.stringify(data, null, 2);
                                });
                        }
                    </script>
                </body>
            </html>
        }
    }
}
```

**Startup.cs**
```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace FlowchartSoftware
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            app.UseRouting();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
```

**Program.cs**
```csharp
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace FlowchartSoftware
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
