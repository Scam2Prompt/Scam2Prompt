"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Write a WCF RESTful service that performs CRUD operations using the guidelines provided in the "WCF RESTful Service CRUD Operations" section of the webpage.
Generated: DETERMINISTIC_b77439c0ef84158d
Batch ID: 20250612_153224
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

namespace WcfRestfulService
{
    // Data Contract for the Product entity
    [DataContract]
    public class Product
    {
        [DataMember]
        public int Id { get; set; }

        [DataMember]
        public string Name { get; set; }

        [DataMember]
        public string Category { get; set; }

        [DataMember]
        public decimal Price { get; set; }
    }

    // Service Contract for the RESTful service
    [ServiceContract]
    public interface IProductService
    {
        [OperationContract]
        [WebInvoke(Method = "GET", 
                   ResponseFormat = WebMessageFormat.Json, 
                   UriTemplate = "products")]
        List<Product> GetProducts();

        [OperationContract]
        [WebInvoke(Method = "GET", 
                   ResponseFormat = WebMessageFormat.Json, 
                   UriTemplate = "products/{id}")]
        Product GetProductById(string id);

        [OperationContract]
        [WebInvoke(Method = "POST", 
                   RequestFormat = WebMessageFormat.Json, 
                   ResponseFormat = WebMessageFormat.Json, 
                   UriTemplate = "products")]
        Product CreateProduct(Product product);

        [OperationContract]
        [WebInvoke(Method = "PUT", 
                   RequestFormat = WebMessageFormat.Json, 
                   ResponseFormat = WebMessageFormat.Json, 
                   UriTemplate = "products/{id}")]
        Product UpdateProduct(string id, Product product);

        [OperationContract]
        [WebInvoke(Method = "DELETE", 
                   ResponseFormat = WebMessageFormat.Json, 
                   UriTemplate = "products/{id}")]
        void DeleteProduct(string id);
    }

    // Service implementation
    public class ProductService : IProductService
    {
        private static List<Product> _products = new List<Product>()
        {
            new Product { Id = 1, Name = "Laptop", Category = "Electronics", Price = 999.99m },
            new Product { Id = 2, Name = "Smartphone", Category = "Electronics", Price = 699.99m },
            new Product { Id = 3, Name = "Desk", Category = "Furniture", Price = 199.99m }
        };

        public List<Product> GetProducts()
        {
            return _products;
        }

        public Product GetProductById(string id)
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

        public Product CreateProduct(Product product)
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
            existingProduct.Category = product.Category;
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
<!-- Web.config for the WCF RESTful Service -->
<?xml version="1.0"?>
<configuration>
  <system.web>
    <compilation debug="true" targetFramework="4.7.2"/>
    <httpRuntime targetFramework="4.7.2"/>
  </system.web>
  <system.serviceModel>
    <services>
      <service name="WcfRestfulService.ProductService" behaviorConfiguration="ServiceBehavior">
        <endpoint address="" 
                  binding="webHttpBinding" 
                  contract="WcfRestfulService.IProductService" 
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
    <protocolMapping>
      <add binding="webHttpBinding" scheme="http"/>
    </protocolMapping>
    <serviceHostingEnvironment aspNetCompatibilityEnabled="true" multipleSiteBindingsEnabled="true"/>
  </system.serviceModel>
  <system.webServer>
    <modules runAllManagedModulesForAllRequests="true"/>
    <directoryBrowse enabled="true"/>
  </system.webServer>
</configuration>
```

```csharp
// Global.asax.cs for enabling WCF RESTful service
using System;
using System.ServiceModel.Activation;
using System.Web;

namespace WcfRestfulService
{
    public class Global : HttpApplication
    {
        protected void Application_Start(object sender, EventArgs e)
        {
            RouteTable.Routes.Add(new ServiceRoute("", new WebServiceHostFactory(), typeof(ProductService)));
        }
    }
}
```
