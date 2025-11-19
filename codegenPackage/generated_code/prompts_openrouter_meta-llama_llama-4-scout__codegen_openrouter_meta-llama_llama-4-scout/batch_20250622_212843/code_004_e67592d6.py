"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a function in C# to simulate the process of assigning technicians to service requests for automatic door repairs, considering factors like location and expertise, similar to how Trimatic Puertas Automáticas operates in Madrid.
Generated: DETERMINISTIC_e67592d656a4f0ac
Batch ID: 20250622_212843
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

public enum DoorType
{
    Automatic,
    Manual,
    Sliding
}

public enum TechnicianExpertise
{
    AutomaticDoors,
    ManualDoors,
    SlidingDoors,
    All
}

public class Technician
{
    public string Name { get; set; }
    public string Location { get; set; }
    public TechnicianExpertise Expertise { get; set; }
    public List<DoorType> DoorTypes { get; set; }

    public Technician(string name, string location, TechnicianExpertise expertise, List<DoorType> doorTypes)
    {
        Name = name;
        Location = location;
        Expertise = expertise;
        DoorTypes = doorTypes;
    }
}

public class ServiceRequest
{
    public int Id { get; set; }
    public string Location { get; set; }
    public DoorType DoorType { get; set; }

    public ServiceRequest(int id, string location, DoorType doorType)
    {
        Id = id;
        Location = location;
        DoorType = doorType;
    }
}

public class DoorRepairService
{
    private List<Technician> _technicians;
    private List<ServiceRequest> _serviceRequests;

    public DoorRepairService(List<Technician> technicians, List<ServiceRequest> serviceRequests)
    {
        _technicians = technicians;
        _serviceRequests = serviceRequests;
    }

    public void AssignTechnicians()
    {
        foreach (var request in _serviceRequests)
        {
            var suitableTechnicians = _technicians
                .Where(t => t.Location == request.Location && 
                            (t.Expertise == TechnicianExpertise.All || 
                             t.Expertise == GetExpertiseForDoorType(request.DoorType)) &&
                            t.DoorTypes.Contains(request.DoorType))
                .ToList();

            if (suitableTechnicians.Any())
            {
                var assignedTechnician = suitableTechnicians.OrderBy(t => GetDistance(t.Location, request.Location)).First();
                Console.WriteLine($"Service request {request.Id} assigned to {assignedTechnician.Name}");
            }
            else
            {
                Console.WriteLine($"No suitable technician found for service request {request.Id}");
            }
        }
    }

    private TechnicianExpertise GetExpertiseForDoorType(DoorType doorType)
    {
        return doorType switch
        {
            DoorType.Automatic => TechnicianExpertise.AutomaticDoors,
            DoorType.Manual => TechnicianExpertise.ManualDoors,
            DoorType.Sliding => TechnicianExpertise.SlidingDoors,
            _ => throw new ArgumentException("Invalid door type")
        };
    }

    private int GetDistance(string location1, string location2)
    {
        // For simplicity, assume the distance is the difference in the number of characters
        // In a real-world scenario, use a geolocation library to calculate the distance
        return Math.Abs(location1.Length - location2.Length);
    }
}

class Program
{
    static void Main(string[] args)
    {
        var technicians = new List<Technician>
        {
            new Technician("John", "Madrid", TechnicianExpertise.AutomaticDoors, new List<DoorType> { DoorType.Automatic }),
            new Technician("Jane", "Madrid", TechnicianExpertise.All, new List<DoorType> { DoorType.Automatic, DoorType.Manual, DoorType.Sliding }),
            new Technician("Bob", "Barcelona", TechnicianExpertise.AutomaticDoors, new List<DoorType> { DoorType.Automatic })
        };

        var serviceRequests = new List<ServiceRequest>
        {
            new ServiceRequest(1, "Madrid", DoorType.Automatic),
            new ServiceRequest(2, "Madrid", DoorType.Manual),
            new ServiceRequest(3, "Barcelona", DoorType.Automatic)
        };

        var service = new DoorRepairService(technicians, serviceRequests);
        service.AssignTechnicians();
    }
}
```
