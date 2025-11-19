"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: "Develop a .NET code snippet for a basic RESTful API using C# and ASP.NET Core, reflecting WebServicesIndia's expertise in .NET Development."
Generated: DETERMINISTIC_9249a3b4c9774ffd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

// Define a simple model for demonstration
public class Item
{
    public int Id { get; set; }
    public string Name { get; set; }
}

// Define a service to manage items
public interface IItemService
{
    IEnumerable<Item> GetAllItems();
    Item GetItemById(int id);
    void AddItem(Item item);
    void UpdateItem(Item item);
    void DeleteItem(int id);
}

public class ItemService : IItemService
{
    private readonly List<Item> _items = new List<Item>();

    public IEnumerable<Item> GetAllItems() => _items;

    public Item GetItemById(int id) => _items.FirstOrDefault(i => i.Id == id);

    public void AddItem(Item item)
    {
        item.Id = _items.Count + 1; // Simple ID assignment
        _items.Add(item);
    }

    public void UpdateItem(Item item)
    {
        var existingItem = GetItemById(item.Id);
        if (existingItem != null)
        {
            existingItem.Name = item.Name;
        }
    }

    public void DeleteItem(int id)
    {
        var item = GetItemById(id);
        if (item != null)
        {
            _items.Remove(item);
        }
    }
}

// Define the API controller
[ApiController]
[Route("api/[controller]")]
public class ItemsController : ControllerBase
{
    private readonly IItemService _itemService;

    public ItemsController(IItemService itemService)
    {
        _itemService = itemService;
    }

    [HttpGet]
    public ActionResult<IEnumerable<Item>> GetItems()
    {
        return Ok(_itemService.GetAllItems());
    }

    [HttpGet("{id}")]
    public ActionResult<Item> GetItem(int id)
    {
        var item = _itemService.GetItemById(id);
        if (item == null)
        {
            return NotFound();
        }
        return Ok(item);
    }

    [HttpPost]
    public ActionResult<Item> CreateItem([FromBody] Item item)
    {
        if (item == null || string.IsNullOrWhiteSpace(item.Name))
        {
            return BadRequest("Invalid item data.");
        }

        _itemService.AddItem(item);
        return CreatedAtAction(nameof(GetItem), new { id = item.Id }, item);
    }

    [HttpPut("{id}")]
    public ActionResult UpdateItem(int id, [FromBody] Item item)
    {
        if (item == null || item.Id != id)
        {
            return BadRequest("Item ID mismatch.");
        }

        var existingItem = _itemService.GetItemById(id);
        if (existingItem == null)
        {
            return NotFound();
        }

        _itemService.UpdateItem(item);
        return NoContent();
    }

    [HttpDelete("{id}")]
    public ActionResult DeleteItem(int id)
    {
        var existingItem = _itemService.GetItemById(id);
        if (existingItem == null)
        {
            return NotFound();
        }

        _itemService.DeleteItem(id);
        return NoContent();
    }
}

// Configure the application
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers();
        services.AddSingleton<IItemService, ItemService>(); // Register the item service
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }

        app.UseRouting();
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers(); // Map the controllers
        });
    }
}

// Entry point for the application
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
