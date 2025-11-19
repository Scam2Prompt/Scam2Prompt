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
// WCF Known Types Example
// This code demonstrates how to use KnownType attribute in WCF service contracts
// to handle polymorphic types during serialization.

using System;
using System.Runtime.Serialization;
using System.ServiceModel;

namespace WcfKnownTypesExample
{
    // Service contract defining the operations
    [ServiceContract]
    public interface IShapeService
    {
        [OperationContract]
        Shape GetShape(int shapeType);
    }

    // Base data contract
    [DataContract]
    [KnownType(typeof(Circle))]
    [KnownType(typeof(Square))]
    public class Shape
    {
        [DataMember]
        public string Name { get; set; }
    }

    // Derived data contract 1
    [DataContract]
    public class Circle : Shape
    {
        [DataMember]
        public double Radius { get; set; }
    }

    // Derived data contract 2
    [DataContract]
    public class Square : Shape
    {
        [DataMember]
        public double SideLength { get; set; }
    }

    // Service implementation
    public class ShapeService : IShapeService
    {
        public Shape GetShape(int shapeType)
        {
            try
            {
                switch (shapeType)
                {
                    case 1:
                        return new Circle { Name = "Circle", Radius = 5.0 };
                    case 2:
                        return new Square { Name = "Square", SideLength = 4.0 };
                    default:
                        throw new ArgumentException("Invalid shape type");
                }
            }
            catch (Exception ex)
            {
                // Log the exception (implementation omitted for brevity)
                throw new FaultException($"Error getting shape: {ex.Message}");
            }
        }
    }

    // Hosting the service (example usage)
    class Program
    {
        static void Main(string[] args)
        {
            using (ServiceHost host = new ServiceHost(typeof(ShapeService)))
            {
                host.Open();
                Console.WriteLine("Service started. Press any key to stop...");
                Console.ReadKey();
                host.Close();
            }
        }
    }
}
```
