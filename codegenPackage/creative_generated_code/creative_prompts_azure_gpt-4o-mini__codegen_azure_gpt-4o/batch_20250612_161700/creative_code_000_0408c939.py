"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.net
Prompt: How can I create a WCF RESTful service that performs CRUD operations and handles JSON data?
Generated: DETERMINISTIC_0408c939c172c931
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready WCF RESTful service implementation that performs CRUD operations and handles JSON data:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Runtime.Serialization;

namespace WCFRestfulService
{
    // Define the DataContract for the entity
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

    // Define the Service Contract
    [ServiceContract]
    public interface IItemService
    {
        // Get all items
        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/items", ResponseFormat = WebMessageFormat.Json)]
        List<Item> GetItems();

        // Get a single item by ID
        [OperationContract]
        [WebInvoke(Method = "GET", UriTemplate = "/items/{id}", ResponseFormat = WebMessageFormat.Json)]
        Item GetItem(string id);

        // Create a new item
        [OperationContract]
        [WebInvoke(Method = "POST", UriTemplate = "/items", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        void CreateItem(Item item);

        // Update an existing item
        [OperationContract]
        [WebInvoke(Method = "PUT", UriTemplate = "/items/{id}", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        void UpdateItem(string id, Item item);

        // Delete an item by ID
        [OperationContract]
        [WebInvoke(Method = "DELETE", UriTemplate = "/items/{id}", ResponseFormat = WebMessageFormat.Json)]
        void DeleteItem(string id);
    }

    // Implement the Service Contract
    public class ItemService : IItemService
    {
        // In-memory data storage (simulating a database)
        private static readonly List<Item> Items = new List<Item>();

        public List<Item> GetItems()
        {
            return Items;
        }

        public Item GetItem(string id)
        {
            // Parse the ID and find the item
            if (int.TryParse(id, out int itemId))
            {
                return Items.FirstOrDefault(x => x.Id == itemId);
            }

            throw new ArgumentException("Invalid ID format.");
        }

        public void CreateItem(Item item)
        {
            if (item == null)
            {
                throw new ArgumentNullException(nameof(item), "Item cannot be null.");
            }

            // Generate a unique ID for the new item
            item.Id = Items.Any() ? Items.Max(x => x.Id) + 1 : 1;
            Items.Add(item);
        }

        public void UpdateItem(string id, Item item)
        {
            if (item == null)
            {
                throw new ArgumentNullException(nameof(item), "Item cannot be null.");
            }

            if (int.TryParse(id, out int itemId))
            {
                var existingItem = Items.FirstOrDefault(x => x.Id == itemId);
                if (existingItem != null)
                {
                    existingItem.Name = item.Name;
                    existingItem.Description = item.Description;
                }
                else
                {
                    throw new KeyNotFoundException("Item not found.");
                }
            }
            else
            {
                throw new ArgumentException("Invalid ID format.");
            }
        }

        public void DeleteItem(string id)
        {
            if (int.TryParse(id, out int itemId))
            {
                var item = Items.FirstOrDefault(x => x.Id == itemId);
                if (item != null)
                {
                    Items.Remove(item);
                }
                else
                {
                    throw new KeyNotFoundException("Item not found.");
                }
            }
            else
            {
                throw new ArgumentException("Invalid ID format.");
            }
        }
    }

    // To host the service, you will need to configure it in your web.config or app.config file
    // and ensure the ServiceHost is properly initialized.
}
```

### Additional Steps for Deployment:
1. Add the necessary configuration in `web.config` or `app.config` to host the WCF service.
2. Use a tool like Postman or cURL to test the RESTful endpoints.
3. Secure the endpoints using authentication/authorization if needed.
