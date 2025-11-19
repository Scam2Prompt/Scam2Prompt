"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Provide a detailed explanation of WCF known types and how they are used in service contracts, as discussed in the WCF Tutorial.
Generated: DETERMINISTIC_f781cbfae9758612
Batch ID: 20250612_162051
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
using System.Runtime.Serialization;
using System.ServiceModel;

// Define the known types for polymorphic behavior in WCF services
[KnownType(typeof(Car))]
[KnownType(typeof(Truck))]
[DataContract]
[Serializable]
public abstract class Vehicle
{
    [DataMember]
    public string Make { get; set; }

    [DataMember]
    public string Model { get; set; }

    public abstract void DisplayInfo();
}

// Derived class representing a Car
[DataContract]
public class Car : Vehicle
{
    [DataMember]
    public int NumberOfDoors { get; set; }

    public override void DisplayInfo()
    {
        Console.WriteLine($"Car: {Make} {Model}, Doors: {NumberOfDoors}");
    }
}

// Derived class representing a Truck
[DataContract]
public class Truck : Vehicle
{
    [DataMember]
    public int LoadCapacity { get; set; }

    public override void DisplayInfo()
    {
        Console.WriteLine($"Truck: {Make} {Model}, Load Capacity: {LoadCapacity} tons");
    }
}

// Service contract interface
[ServiceContract]
public interface IVehicleService
{
    [OperationContract]
    Vehicle GetVehicle(int id);
}

// Implementation of the service contract
public class VehicleService : IVehicleService
{
    // Sample data for demonstration purposes
    private static Dictionary<int, Vehicle> vehicles = new Dictionary<int, Vehicle>
    {
        { 1, new Car { Make = "Toyota", Model = "Camry", NumberOfDoors = 4 } },
        { 2, new Truck { Make = "Ford", Model = "F-150", LoadCapacity = 2 } }
    };

    // Method to retrieve a vehicle by id
    public Vehicle GetVehicle(int id)
    {
        if (vehicles.TryGetValue(id, out Vehicle vehicle))
        {
            return vehicle;
        }
        
        // Throw an exception if the vehicle is not found
        throw new KeyNotFoundException($"Vehicle with ID {id} not found.");
    }
}

// Host configuration and service initialization
class Program
{
    static void Main(string[] args)
    {
        try
        {
            using (ServiceHost host = new ServiceHost(typeof(VehicleService)))
            {
                host.Open();
                Console.WriteLine("Vehicle Service is running...");
                Console.WriteLine("Press any key to stop the service.");
                Console.ReadKey();
                host.Close();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
