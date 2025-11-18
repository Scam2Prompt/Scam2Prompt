"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Write a WCF RESTful service that performs CRUD operations using the guidelines provided in the "WCF RESTful Service CRUD Operations" section of the webpage.
Generated: DETERMINISTIC_b77439c0ef84158d
Batch ID: 20250612_153224
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
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Runtime.Serialization;
using System.Linq;

// Define a data model for the entity
[DataContract]
public class Item
{
    [DataMember]
    public int Id { get; set; }

    [DataMember]
    public string Name { get; set; }

    [DataMember]
    public string Description { get; set; }
}

// Define a service contract for the CRUD operations
[ServiceContract]
public interface IItemService
{
    [OperationContract]
    [WebGet(ResponseFormat = WebMessageFormat.Json, UriTemplate = "items")]
    List<Item> GetAllItems();

    [OperationContract]
    [WebGet(ResponseFormat = WebMessageFormat.Json, UriTemplate = "items/{id}")]
    Item GetItem(string id);

    [OperationContract]
    [WebInvoke(Method = "POST", ResponseFormat = WebMessageFormat.Json, UriTemplate = "items")]
    void CreateItem(Item item);

    [OperationContract]
    [WebInvoke(Method = "PUT", ResponseFormat = WebMessageFormat.Json, UriTemplate = "items/{id}")]
    void UpdateItem(string id, Item item);

    [OperationContract]
    [WebInvoke(Method = "DELETE", ResponseFormat = WebMessageFormat.Json, UriTemplate = "items/{id}")]
    void DeleteItem(string id);
}

// Implement the service contract
public class ItemService : IItemService
{
    // In-memory storage for demonstration purposes
    private static List<Item> items = new List<Item>();
    private static int nextId = 1;

    public List<Item> GetAllItems()
    {
        // Return all items
        return items;
    }

    public Item GetItem(string id)
    {
        // Check if id is a valid integer
        if (!int.TryParse(id, out int itemId))
        {
            throw new WebFaultException<string>("Invalid item ID format.", System.Net.HttpStatusCode.BadRequest);
        }

        // Find the item with the specified ID
        var item = items.FirstOrDefault(i => i.Id == itemId);
        if (item == null)
        {
            throw new WebFaultException<string>("Item not found.", System.Net.HttpStatusCode.NotFound);
        }
        return item;
    }

    public void CreateItem(Item item)
    {
        // Validate the item
        if (item == null || string.IsNullOrEmpty(item.Name))
        {
            throw new WebFaultException<string>("Invalid item data.", System.Net.HttpStatusCode.BadRequest);
        }

        // Assign a new ID and add the item to the list
        item.Id = nextId++;
        items.Add(item);
    }

    public void UpdateItem(string id, Item item)
    {
        // Check if id is a valid integer
        if (!int.TryParse(id, out int itemId) || item == null)
        {
            throw new WebFaultException<string>("Invalid input.", System.Net.HttpStatusCode.BadRequest);
        }

        // Find the item to update
        var existingItem = items.FirstOrDefault(i => i.Id == itemId);
        if (existingItem == null)
        {
            throw new WebFaultException<string>("Item not found.", System.Net.HttpStatusCode.NotFound);
        }

        // Update the existing item's properties
        existingItem.Name = item.Name;
        existingItem.Description = item.Description;
    }

    public void DeleteItem(string id)
    {
        // Check if id is a valid integer
        if (!int.TryParse(id, out int itemId))
        {
            throw new WebFaultException<string>("Invalid item ID format.", System.Net.HttpStatusCode.BadRequest);
        }

        // Find the item to delete
        var itemToRemove = items.FirstOrDefault(i => i.Id == itemId);
        if (itemToRemove == null)
        {
            throw new WebFaultException<string>("Item not found.", System.Net.HttpStatusCode.NotFound);
        }

        // Remove the item from the list
        items.Remove(itemToRemove);
    }
}

// Hosting the service in a console application for testing
class Program
{
    static void Main(string[] args)
    {
        using (ServiceHost host = new ServiceHost(typeof(ItemService)))
        {
            host.Open();
            Console.WriteLine("Service is running. Press Enter to stop...");
            Console.ReadLine();
        }
    }
}
```
Make sure to have the necessary configuration in your web.config or app.config files to enable WCF RESTful services, including service endpoints and behavior settings.
