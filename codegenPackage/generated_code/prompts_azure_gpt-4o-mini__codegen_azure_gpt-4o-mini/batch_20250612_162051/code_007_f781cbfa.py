"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Provide a detailed explanation of WCF known types and how they are used in service contracts, as discussed in the WCF Tutorial.
Generated: DETERMINISTIC_f781cbfae9758612
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.ServiceModel;

// Define a known type for polymorphism in WCF
[KnownType(typeof(SpecialProduct))]
[DataContract]
public class Product
{
    [DataMember]
    public int Id { get; set; }

    [DataMember]
    public string Name { get; set; }

    [DataMember]
    public decimal Price { get; set; }
}

// Define a derived type
[DataContract]
public class SpecialProduct : Product
{
    [DataMember]
    public string SpecialFeature { get; set; }
}

// Define the service contract
[ServiceContract]
public interface IProductService
{
    [OperationContract]
    Product GetProduct(int id);

    [OperationContract]
    List<Product> GetAllProducts();
}

// Implement the service contract
public class ProductService : IProductService
{
    private readonly List<Product> products = new List<Product>
    {
        new Product { Id = 1, Name = "Regular Product", Price = 10.99m },
        new SpecialProduct { Id = 2, Name = "Special Product", Price = 19.99m, SpecialFeature = "Limited Edition" }
    };

    // Retrieve a product by ID
    public Product GetProduct(int id)
    {
        try
        {
            // Find the product by ID
            var product = products.Find(p => p.Id == id);
            if (product == null)
            {
                throw new ArgumentException("Product not found.");
            }
            return product;
        }
        catch (Exception ex)
        {
            // Log the exception (logging mechanism not implemented here)
            throw new FaultException($"An error occurred while retrieving the product: {ex.Message}");
        }
    }

    // Retrieve all products
    public List<Product> GetAllProducts()
    {
        try
        {
            return products;
        }
        catch (Exception ex)
        {
            // Log the exception (logging mechanism not implemented here)
            throw new FaultException($"An error occurred while retrieving the products: {ex.Message}");
        }
    }
}

// Host the service
class Program
{
    static void Main(string[] args)
    {
        using (ServiceHost host = new ServiceHost(typeof(ProductService)))
        {
            try
            {
                host.Open();
                Console.WriteLine("Service is running...");
                Console.WriteLine("Press <Enter> to terminate the service.");
                Console.ReadLine();
            }
            catch (Exception ex)
            {
                // Log the exception (logging mechanism not implemented here)
                Console.WriteLine($"An error occurred while starting the service: {ex.Message}");
            }
            finally
            {
                host.Close();
            }
        }
    }
}
```
