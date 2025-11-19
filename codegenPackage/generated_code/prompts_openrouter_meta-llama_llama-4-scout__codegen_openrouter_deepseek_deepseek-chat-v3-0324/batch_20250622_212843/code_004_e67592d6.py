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

namespace DoorRepairService
{
    public class ServiceRequest
    {
        public int RequestId { get; set; }
        public string Location { get; set; }
        public DoorType DoorType { get; set; }
        public DateTime RequestTime { get; set; }
        public PriorityLevel Priority { get; set; }
    }

    public class Technician
    {
        public int TechnicianId { get; set; }
        public string Name { get; set; }
        public List<DoorType> Expertise { get; set; }
        public string BaseLocation { get; set; }
        public bool IsAvailable { get; set; }
        public int CurrentWorkload { get; set; }
    }

    public enum DoorType
    {
        Sliding,
        Swing,
        Revolving,
        Folding,
        HighSpeed
    }

    public enum PriorityLevel
    {
        Low,
        Medium,
        High,
        Emergency
    }

    public static class TechnicianAssigner
    {
        private const int MaxWorkload = 5;
        private const int MaxDistance = 20; // in km

        public static Technician AssignTechnician(ServiceRequest request, List<Technician> technicians)
        {
            if (request == null)
                throw new ArgumentNullException(nameof(request), "Service request cannot be null");
            
            if (technicians == null || !technicians.Any())
                throw new ArgumentException("Technicians list cannot be null or empty", nameof(technicians));

            try
            {
                // Filter available technicians with matching expertise
                var suitableTechnicians = technicians
                    .Where(t => t.IsAvailable && 
                               t.CurrentWorkload < MaxWorkload &&
                               t.Expertise.Contains(request.DoorType))
                    .ToList();

                if (!suitableTechnicians.Any())
                    return null;

                // Calculate distance scores (simplified for example)
                var techniciansWithScores = suitableTechnicians
                    .Select(t => new
                    {
                        Technician = t,
                        DistanceScore = CalculateDistanceScore(t.BaseLocation, request.Location),
                        WorkloadScore = (MaxWorkload - t.CurrentWorkload) / (double)MaxWorkload,
                        PriorityScore = (int)request.Priority
                    })
                    .ToList();

                // Calculate weighted score (weights can be adjusted)
                var prioritizedTechnicians = techniciansWithScores
                    .Select(t => new
                    {
                        t.Technician,
                        TotalScore = (t.DistanceScore * 0.4) + 
                                    (t.WorkloadScore * 0.3) + 
                                    (t.PriorityScore * 0.3)
                    })
                    .OrderByDescending(t => t.TotalScore)
                    .ToList();

                return prioritizedTechnicians.FirstOrDefault()?.Technician;
            }
            catch (Exception ex)
            {
                // Log error in production (implementation omitted)
                throw new ApplicationException("Error assigning technician", ex);
            }
        }

        private static double CalculateDistanceScore(string techLocation, string requestLocation)
        {
            // In a real implementation, this would use a proper distance calculation API
            // For this example, we'll simulate distance with a simple score
            
            if (techLocation == requestLocation)
                return 1.0;

            // Simulate distance calculation
            int distance = new Random().Next(1, MaxDistance);
            
            // Normalize score (closer is better)
            return 1.0 - (distance / (double)MaxDistance);
        }

        public static void UpdateTechnicianStatus(Technician technician, bool isAvailable, int workload)
        {
            if (technician == null)
                throw new ArgumentNullException(nameof(technician));

            if (workload < 0 || workload > MaxWorkload)
                throw new ArgumentOutOfRangeException(nameof(workload), $"Workload must be between 0 and {MaxWorkload}");

            technician.IsAvailable = isAvailable;
            technician.CurrentWorkload = workload;
        }
    }
}
```
