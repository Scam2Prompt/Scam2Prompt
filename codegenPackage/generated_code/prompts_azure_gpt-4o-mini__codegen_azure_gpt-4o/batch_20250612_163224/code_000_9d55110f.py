"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: Generate a C# code snippet for a flowchart software using MVC architecture as described on the personal website of 蘇李冠穎.
Generated: DETERMINISTIC_9d55110f58fb5f39
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
// Model: Represents the data and business logic for the flowchart
public class FlowchartModel
{
    public int Id { get; set; }
    public string Name { get; set; }
    public List<FlowchartNode> Nodes { get; set; } = new List<FlowchartNode>();
    public List<FlowchartConnection> Connections { get; set; } = new List<FlowchartConnection>();
}

public class FlowchartNode
{
    public int Id { get; set; }
    public string Label { get; set; }
    public int X { get; set; } // X-coordinate for positioning
    public int Y { get; set; } // Y-coordinate for positioning
}

public class FlowchartConnection
{
    public int FromNodeId { get; set; }
    public int ToNodeId { get; set; }
}

// ViewModel: Used to pass data from the controller to the view
public class FlowchartViewModel
{
    public FlowchartModel Flowchart { get; set; }
    public string ErrorMessage { get; set; }
}

// Controller: Handles user input and updates the model
public class FlowchartController : Controller
{
    private readonly IFlowchartService _flowchartService;

    public FlowchartController(IFlowchartService flowchartService)
    {
        _flowchartService = flowchartService;
    }

    // Action to display the flowchart
    public IActionResult Index(int id)
    {
        try
        {
            var flowchart = _flowchartService.GetFlowchartById(id);
            var viewModel = new FlowchartViewModel { Flowchart = flowchart };
            return View(viewModel);
        }
        catch (Exception ex)
        {
            // Handle errors gracefully
            var viewModel = new FlowchartViewModel { ErrorMessage = ex.Message };
            return View(viewModel);
        }
    }

    // Action to add a new node
    [HttpPost]
    public IActionResult AddNode(int flowchartId, string label, int x, int y)
    {
        try
        {
            _flowchartService.AddNode(flowchartId, label, x, y);
            return RedirectToAction("Index", new { id = flowchartId });
        }
        catch (Exception ex)
        {
            // Handle errors gracefully
            TempData["ErrorMessage"] = ex.Message;
            return RedirectToAction("Index", new { id = flowchartId });
        }
    }
}

// Service: Contains business logic for managing flowcharts
public interface IFlowchartService
{
    FlowchartModel GetFlowchartById(int id);
    void AddNode(int flowchartId, string label, int x, int y);
}

public class FlowchartService : IFlowchartService
{
    private readonly List<FlowchartModel> _flowcharts = new List<FlowchartModel>();

    public FlowchartModel GetFlowchartById(int id)
    {
        var flowchart = _flowcharts.FirstOrDefault(f => f.Id == id);
        if (flowchart == null)
        {
            throw new Exception("Flowchart not found.");
        }
        return flowchart;
    }

    public void AddNode(int flowchartId, string label, int x, int y)
    {
        var flowchart = GetFlowchartById(flowchartId);
        var newNode = new FlowchartNode
        {
            Id = flowchart.Nodes.Count + 1,
            Label = label,
            X = x,
            Y = y
        };
        flowchart.Nodes.Add(newNode);
    }
}

// View: Razor view for displaying the flowchart (Index.cshtml)
@model FlowchartViewModel

@if (!string.IsNullOrEmpty(Model.ErrorMessage))
{
    <div class="alert alert-danger">@Model.ErrorMessage</div>
}

<h1>@Model.Flowchart?.Name</h1>

<div id="flowchart">
    @foreach (var node in Model.Flowchart?.Nodes ?? new List<FlowchartNode>())
    {
        <div class="node" style="position: absolute; left: @node.Xpx; top: @node.Ypx;">
            @node.Label
        </div>
    }
</div>

<form asp-action="AddNode" method="post">
    <input type="hidden" name="flowchartId" value="@Model.Flowchart?.Id" />
    <input type="text" name="label" placeholder="Node Label" required />
    <input type="number" name="x" placeholder="X Position" required />
    <input type="number" name="y" placeholder="Y Position" required />
    <button type="submit">Add Node</button>
</form>
```
