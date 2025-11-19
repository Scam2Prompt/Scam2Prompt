"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a code snippet in C# to develop a simple architectural supervision system, tracking construction phase progress and project completion, inspired by Remas Engineering Consultants' services.
Generated: DETERMINISTIC_dfd4577da192ead0
Batch ID: 20250622_211009
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

namespace ArchitecturalSupervisionSystem
{
    // Enum to represent construction phases
    public enum ConstructionPhase
    {
        Planning,
        Foundation,
        Structure,
        Finishing,
        Completed
    }

    // Class to represent a construction project
    public class ConstructionProject
    {
        public string ProjectName { get; private set; }
        public ConstructionPhase CurrentPhase { get; private set; }
        public DateTime StartDate { get; private set; }
        public DateTime? CompletionDate { get; private set; }

        public ConstructionProject(string projectName, DateTime startDate)
        {
            if (string.IsNullOrWhiteSpace(projectName))
                throw new ArgumentException("Project name cannot be null or empty.", nameof(projectName));

            ProjectName = projectName;
            StartDate = startDate;
            CurrentPhase = ConstructionPhase.Planning;
        }

        // Method to update the construction phase
        public void UpdatePhase(ConstructionPhase newPhase)
        {
            if (newPhase <= CurrentPhase)
                throw new InvalidOperationException("Cannot move to a previous or the same phase.");

            CurrentPhase = newPhase;

            if (newPhase == ConstructionPhase.Completed)
                CompletionDate = DateTime.Now;
        }

        // Method to display project details
        public void DisplayProjectDetails()
        {
            Console.WriteLine($"Project Name: {ProjectName}");
            Console.WriteLine($"Start Date: {StartDate.ToShortDateString()}");
            Console.WriteLine($"Current Phase: {CurrentPhase}");
            Console.WriteLine($"Completion Date: {(CompletionDate.HasValue ? CompletionDate.Value.ToShortDateString() : "Not Completed")}");
        }
    }

    // Main program
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Create a new construction project
                ConstructionProject project = new ConstructionProject("Residential Tower", DateTime.Now);

                // Simulate phase updates
                project.DisplayProjectDetails();
                Console.WriteLine();

                project.UpdatePhase(ConstructionPhase.Foundation);
                project.DisplayProjectDetails();
                Console.WriteLine();

                project.UpdatePhase(ConstructionPhase.Structure);
                project.DisplayProjectDetails();
                Console.WriteLine();

                project.UpdatePhase(ConstructionPhase.Finishing);
                project.DisplayProjectDetails();
                Console.WriteLine();

                project.UpdatePhase(ConstructionPhase.Completed);
                project.DisplayProjectDetails();
            }
            catch (Exception ex)
            {
                // Handle any errors gracefully
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
