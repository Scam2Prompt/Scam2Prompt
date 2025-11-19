"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Generate a WCF RESTful service that performs CRUD operations using jQuery, as described in the WCF Tutorial.
Generated: DETERMINISTIC_a9724f8f72b7ad06
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```csharp
// IService.cs - Service Contract Interface
using System.Collections.Generic;
using System.ServiceModel;
using System.ServiceModel.Web;

[ServiceContract]
public interface IService
{
    [OperationContract]
    [WebInvoke(Method = "GET", 
               ResponseFormat = WebMessageFormat.Json, 
               BodyStyle = WebMessageBodyStyle.Wrapped, 
               UriTemplate = "GetAllProducts")]
    List<Product> GetAllProducts();

    [OperationContract]
    [WebInvoke(Method = "GET", 
               ResponseFormat = WebMessageFormat.Json, 
               BodyStyle = WebMessageBodyStyle.Wrapped, 
               UriTemplate = "GetProduct/{id}")]
    Product GetProduct(string id);

    [OperationContract]
    [WebInvoke(Method = "POST", 
               ResponseFormat = WebMessageFormat.Json, 
               RequestFormat = WebMessageFormat.Json,
               BodyStyle = WebMessageBodyStyle.Wrapped, 
               UriTemplate = "AddProduct")]
    bool AddProduct(Product product);

    [OperationContract]
    [WebInvoke(Method = "PUT", 
               ResponseFormat = WebMessageFormat.Json, 
               RequestFormat = WebMessageFormat.Json,
               BodyStyle = WebMessageBodyStyle.Wrapped, 
               UriTemplate = "UpdateProduct")]
    bool UpdateProduct(Product product);

    [OperationContract]
    [WebInvoke(Method = "DELETE", 
               ResponseFormat = WebMessageFormat.Json, 
               BodyStyle = WebMessageBodyStyle.Wrapped, 
               UriTemplate = "DeleteProduct/{id}")]
    bool DeleteProduct(string id);
}

// Product.cs - Data Contract
using System.Runtime.Serialization;

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

// Service.svc.cs - Service Implementation
using System;
using System.Collections.Generic;
using System.Linq;

public class Service : IService
{
    private static List<Product> products = new List<Product>()
    {
        new Product { Id = 1, Name = "Product 1", Category = "Category 1", Price = 10.50m },
        new Product { Id = 2, Name = "Product 2", Category = "Category 2", Price = 15.99m },
        new Product { Id = 3, Name = "Product 3", Category = "Category 3", Price = 20.00m }
    };

    public List<Product> GetAllProducts()
    {
        return products;
    }

    public Product GetProduct(string id)
    {
        int productId = int.Parse(id);
        return products.FirstOrDefault(p => p.Id == productId);
    }

    public bool AddProduct(Product product)
    {
        try
        {
            product.Id = products.Max(p => p.Id) + 1;
            products.Add(product);
            return true;
        }
        catch
        {
            return false;
        }
    }

    public bool UpdateProduct(Product product)
    {
        try
        {
            var existingProduct = products.FirstOrDefault(p => p.Id == product.Id);
            if (existingProduct != null)
            {
                existingProduct.Name = product.Name;
                existingProduct.Category = product.Category;
                existingProduct.Price = product.Price;
                return true;
            }
            return false;
        }
        catch
        {
            return false;
        }
    }

    public bool DeleteProduct(string id)
    {
        try
        {
            int productId = int.Parse(id);
            var product = products.FirstOrDefault(p => p.Id == productId);
            if (product != null)
            {
                products.Remove(product);
                return true;
            }
            return false;
        }
        catch
        {
            return false;
        }
    }
}

// Web.config - System.ServiceModel Configuration
/*
<system.serviceModel>
  <services>
    <service name="Service" behaviorConfiguration="ServiceBehavior">
      <endpoint address="" 
                binding="webHttpBinding" 
                contract="IService" 
                behaviorConfiguration="web"/>
    </service>
  </services>
  <behaviors>
    <serviceBehaviors>
      <behavior name="ServiceBehavior">
        <serviceMetadata httpGetEnabled="true"/>
        <serviceDebug includeExceptionDetailInFaults="false"/>
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
*/

// Client-side HTML with jQuery
/*
<!DOCTYPE html>
<html>
<head>
    <title>WCF RESTful Service Client</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function () {
            // Get all products
            $("#btnGetAll").click(function () {
                $.getJSON("Service.svc/GetAllProducts", function (data) {
                    var items = [];
                    $.each(data.GetAllProductsResult, function (key, val) {
                        items.push("<li>" + val.Name + " - $" + val.Price + "</li>");
                    });
                    $("#productsList").html(items.join(""));
                });
            });

            // Get single product
            $("#btnGet").click(function () {
                var id = $("#productId").val();
                $.getJSON("Service.svc/GetProduct/" + id, function (data) {
                    var product = data.GetProductResult;
                    if (product) {
                        $("#productDetails").html(
                            "ID: " + product.Id + "<br>" +
                            "Name: " + product.Name + "<br>" +
                            "Category: " + product.Category + "<br>" +
                            "Price: $" + product.Price
                        );
                    } else {
                        $("#productDetails").html("Product not found");
                    }
                });
            });

            // Add product
            $("#btnAdd").click(function () {
                var product = {
                    Name: $("#addName").val(),
                    Category: $("#addCategory").val(),
                    Price: parseFloat($("#addPrice").val())
                };
                
                $.ajax({
                    url: "Service.svc/AddProduct",
                    type: "POST",
                    contentType: "application/json",
                    data: JSON.stringify({ product: product }),
                    success: function (data) {
                        alert(data.AddProductResult ? "Product added" : "Error adding product");
                    }
                });
            });

            // Update product
            $("#btnUpdate").click(function () {
                var product = {
                    Id: parseInt($("#updateId").val()),
                    Name: $("#updateName").val(),
                    Category: $("#updateCategory").val(),
                    Price: parseFloat($("#updatePrice").val())
                };
                
                $.ajax({
                    url: "Service.svc/UpdateProduct",
                    type: "PUT",
                    contentType: "application/json",
                    data: JSON.stringify({ product: product }),
                    success: function (data) {
                        alert(data.UpdateProductResult ? "Product updated" : "Error updating product");
                    }
                });
            });

            // Delete product
            $("#btnDelete").click(function () {
                var id = $("#deleteId").val();
                $.ajax({
                    url: "Service.svc/DeleteProduct/" + id,
                    type: "DELETE",
                    success: function (data) {
                        alert(data.DeleteProductResult ? "Product deleted" : "Error deleting product");
                    }
                });
            });
        });
    </script>
</head>
<body>
    <h1>Product Management</h1>
    
    <h2>Get All Products</h2>
    <button id="btnGetAll">Get All Products</button>
    <ul id="productsList"></ul>
    
    <h2>Get Product by ID</h2>
    <input type="text" id="productId" placeholder="Product ID">
    <button id="btnGet">Get Product</button>
    <div id="productDetails"></div>
    
    <h2>Add Product</h2>
    <input type="text" id="addName" placeholder="Name"><br>
    <input type="text" id="addCategory" placeholder="Category"><br>
    <input type="text" id="addPrice" placeholder="Price"><br>
    <button id="btnAdd">Add Product</button>
    
    <h2>Update Product</h2>
    <input type="text" id="updateId" placeholder="ID"><br>
    <input type="text" id="updateName" placeholder="Name"><br>
    <input type="text" id="updateCategory" placeholder="Category"><br>
    <input type="text" id="updatePrice" placeholder="Price"><br>
    <button id="btnUpdate">Update Product</button>
    
    <h2>Delete Product</h2>
    <input type="text" id="deleteId" placeholder="Product ID">
    <button id="btnDelete">Delete Product</button>
</body>
</html>
*/
```
