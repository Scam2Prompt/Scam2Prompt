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
using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

// Models
public class Flowchart
{
    public int Id { get; set; }
    public string Title { get; set; }
    public List<FlowchartNode> Nodes { get; set; } = new List<FlowchartNode>();
}

public class FlowchartNode
{
    public int Id { get; set; }
    public string Content { get; set; }
    public List<int> ChildNodeIds { get; set; } = new List<int>();
}

// Data Access Layer (Repository Pattern)
public interface IFlowchartRepository
{
    IEnumerable<Flowchart> GetAllFlowcharts();
    Flowchart GetFlowchartById(int id);
    void AddFlowchart(Flowchart flowchart);
    void UpdateFlowchart(Flowchart flowchart);
    void DeleteFlowchart(int id);
}

public class FlowchartRepository : IFlowchartRepository
{
    private readonly List<Flowchart> _flowcharts = new List<Flowchart>();

    public IEnumerable<Flowchart> GetAllFlowcharts() => _flowcharts;

    public Flowchart GetFlowchartById(int id) => _flowcharts.FirstOrDefault(fc => fc.Id == id);

    public void AddFlowchart(Flowchart flowchart)
    {
        if (flowchart == null) throw new ArgumentNullException(nameof(flowchart));
        flowchart.Id = _flowcharts.Count + 1; // Simple Id generation
        _flowcharts.Add(flowchart);
    }

    public void UpdateFlowchart(Flowchart flowchart)
    {
        var existingFlowchart = GetFlowchartById(flowchart.Id);
        if (existingFlowchart == null) throw new KeyNotFoundException("Flowchart not found");
        existingFlowchart.Title = flowchart.Title;
        existingFlowchart.Nodes = flowchart.Nodes;
    }

    public void DeleteFlowchart(int id)
    {
        var flowchart = GetFlowchartById(id);
        if (flowchart == null) throw new KeyNotFoundException("Flowchart not found");
        _flowcharts.Remove(flowchart);
    }
}

// Controller
[ApiController]
[Route("api/[controller]")]
public class FlowchartController : ControllerBase
{
    private readonly IFlowchartRepository _repository;
    private readonly ILogger<FlowchartController> _logger;

    public FlowchartController(IFlowchartRepository repository, ILogger<FlowchartController> logger)
    {
        _repository = repository ?? throw new ArgumentNullException(nameof(repository));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    // GET: api/flowchart
    [HttpGet]
    public ActionResult<IEnumerable<Flowchart>> GetFlowcharts()
    {
        try
        {
            return Ok(_repository.GetAllFlowcharts());
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error retrieving flowcharts");
            return StatusCode(500, "Internal server error");
        }
    }

    // GET: api/flowchart/{id}
    [HttpGet("{id}")]
    public ActionResult<Flowchart> GetFlowchart(int id)
    {
        try
        {
            var flowchart = _repository.GetFlowchartById(id);
            if (flowchart == null) return NotFound();
            return Ok(flowchart);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error retrieving flowchart with id {Id}", id);
            return StatusCode(500, "Internal server error");
        }
    }

    // POST: api/flowchart
    [HttpPost]
    public ActionResult<Flowchart> CreateFlowchart([FromBody] Flowchart flowchart)
    {
        if (flowchart == null) return BadRequest("Flowchart is null");

        try
        {
            _repository.AddFlowchart(flowchart);
            return CreatedAtAction(nameof(GetFlowchart), new { id = flowchart.Id }, flowchart);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error creating flowchart");
            return StatusCode(500, "Internal server error");
        }
    }

    // PUT: api/flowchart/{id}
    [HttpPut("{id}")]
    public ActionResult UpdateFlowchart(int id, [FromBody] Flowchart flowchart)
    {
        if (flowchart == null || flowchart.Id != id) return BadRequest("Flowchart data is invalid");

        try
        {
            _repository.UpdateFlowchart(flowchart);
            return NoContent();
        }
        catch (KeyNotFoundException)
        {
            return NotFound();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error updating flowchart with id {Id}", id);
            return StatusCode(500, "Internal server error");
        }
    }

    // DELETE: api/flowchart/{id}
    [HttpDelete("{id}")]
    public ActionResult DeleteFlowchart(int id)
    {
        try
        {
            _repository.DeleteFlowchart(id);
            return NoContent();
        }
        catch (KeyNotFoundException)
        {
            return NotFound();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error deleting flowchart with id {Id}", id);
            return StatusCode(500, "Internal server error");
        }
    }
}
```
