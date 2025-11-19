"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.net
Prompt: "Write a simple WCF service using C# that exposes a RESTful API for performing CRUD operations."
Generated: DETERMINISTIC_e8e53ba62856130b
Batch ID: 20250622_210443
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
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace SimpleWcfRestService
{
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

    [ServiceContract]
    public interface IProductService
    {
        [OperationContract]
        [WebInvoke(Method = "GET", 
                   UriTemplate = "products", 
                   ResponseFormat = WebMessageFormat.Json)]
        List<Product> GetAllProducts();

        [OperationContract]
        [WebInvoke(Method = "GET", 
                   UriTemplate = "products/{id}", 
                   ResponseFormat = WebMessageFormat.Json)]
        Product GetProduct(string id);

        [OperationContract]
        [WebInvoke(Method = "POST", 
                   UriTemplate = "products", 
                   RequestFormat = WebMessageFormat.Json,
                   ResponseFormat = WebMessageFormat.Json)]
        Product AddProduct(Product product);

        [OperationContract]
        [WebInvoke(Method = "PUT", 
                   UriTemplate = "products/{id}", 
                   RequestFormat = WebMessageFormat.Json,
                   ResponseFormat = WebMessageFormat.Json)]
        Product UpdateProduct(string id, Product product);

        [OperationContract]
        [WebInvoke(Method = "DELETE", 
                   UriTemplate = "products/{id}", 
                   ResponseFormat = WebMessageFormat.Json)]
        void DeleteProduct(string id);
    }

    public class ProductService : IProductService
    {
        private static List<Product> _products = new List<Product>
        {
            new Product { Id = 1, Name = "Laptop", Price = 999.99m },
            new Product { Id = 2, Name = "Phone", Price = 499.99m }
        };

        public List<Product> GetAllProducts()
        {
            return _products;
        }

        public Product GetProduct(string id)
        {
            int productId;
            if (!int.TryParse(id, out productId))
            {
                throw new WebFaultException<string>("Invalid Product ID", System.Net.HttpStatusCode.BadRequest);
            }

            var product = _products.FirstOrDefault(p => p.Id == productId);
            if (product == null)
            {
                throw new WebFaultException<string>("Product not found", System.Net.HttpStatusCode.NotFound);
            }

            return product;
        }

        public Product AddProduct(Product product)
        {
            if (product == null)
            {
                throw new WebFaultException<string>("Product cannot be null", System.Net.HttpStatusCode.BadRequest);
            }

            product.Id = _products.Max(p => p.Id) + 1;
            _products.Add(product);
            return product;
        }

        public Product UpdateProduct(string id, Product product)
        {
            int productId;
            if (!int.TryParse(id, out productId))
            {
                throw new WebFaultException<string>("Invalid Product ID", System.Net.HttpStatusCode.BadRequest);
            }

            var existingProduct = _products.FirstOrDefault(p => p.Id == productId);
            if (existingProduct == null)
            {
                throw new WebFaultException<string>("Product not found", System.Net.HttpStatusCode.NotFound);
            }

            existingProduct.Name = product.Name;
            existingProduct.Price = product.Price;

            return existingProduct;
        }

        public void DeleteProduct(string id)
        {
            int productId;
            if (!int.TryParse(id, out productId))
            {
                throw new WebFaultException<string>("Invalid Product ID", System.Net.HttpStatusCode.BadRequest);
            }

            var product = _products.FirstOrDefault(p => p.Id == productId);
            if (product == null)
            {
                throw new WebFaultException<string>("Product not found", System.Net.HttpStatusCode.NotFound);
            }

            _products.Remove(product);
        }
    }
}
```

```xml
<?xml version="1.0"?>
<configuration>
  <system.web>
    <compilation debug="true" targetFramework="4.8"/>
    <httpRuntime targetFramework="4.8"/>
  </system.web>
  <system.serviceModel>
    <services>
      <service name="SimpleWcfRestService.ProductService" behaviorConfiguration="ServiceBehavior">
        <endpoint address="" 
                  binding="webHttpBinding" 
                  contract="SimpleWcfRestService.IProductService" 
                  behaviorConfiguration="web"/>
      </service>
    </services>
    <behaviors>
      <serviceBehaviors>
        <behavior name="ServiceBehavior">
          <serviceMetadata httpGetEnabled="true"/>
          <serviceDebug includeExceptionDetailInFaults="true"/>
        </behavior>
      </serviceBehaviors>
      <endpointBehaviors>
        <behavior name="web">
          <webHttp/>
        </behavior>
      </endpointBehaviors>
    </behaviors>
    <serviceHostingEnvironment multipleSiteBindingsEnabled="true"/>
  </system.serviceModel>
  <system.webServer>
    <modules runAllManagedModulesForAllRequests="true"/>
  </system.webServer>
</configuration>
```
