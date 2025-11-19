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

// Enum to represent the different phases of construction
public enum ConstructionPhase
{
    Planning,
    Foundation,
    Framing,
    Roofing,
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
    public List<string> ProgressUpdates { get; private set; }

    // Constructor to initialize a new construction project
    public ConstructionProject(string projectName)
    {
        if (string.IsNullOrWhiteSpace(projectName))
        {
            throw new ArgumentException("Project name cannot be null or empty.", nameof(projectName));
        }

        ProjectName = projectName;
        CurrentPhase = ConstructionPhase.Planning;
        StartDate = DateTime.Now;
        ProgressUpdates = new List<string>();
    }

    // Method to advance the project to the next phase
    public void AdvancePhase()
    {
        if (CurrentPhase == ConstructionPhase.Completed)
        {
            throw new InvalidOperationException("Cannot advance phase. The project is already completed.");
        }

        CurrentPhase++;
        ProgressUpdates.Add($"Advanced to phase: {CurrentPhase} on {DateTime.Now}");
        
        // Check if the project is completed
        if (CurrentPhase == ConstructionPhase.Completed)
        {
            CompletionDate = DateTime.Now;
            ProgressUpdates.Add($"Project completed on {CompletionDate}");
        }
    }

    // Method to get a summary of the project
    public string GetProjectSummary()
    {
        return $"Project: {ProjectName}\n" +
               $"Current Phase: {CurrentPhase}\n" +
               $"Start Date: {StartDate}\n" +
               $"Completion Date: {CompletionDate?.ToString() ?? "In Progress"}\n" +
               $"Progress Updates:\n{string.Join("\n", ProgressUpdates)}";
    }
}

// Example usage
public class Program
{
    public static void Main(string[] args)
    {
        try
        {
            // Create a new construction project
            ConstructionProject project = new ConstructionProject("New Office Building");

            // Simulate advancing through construction phases
            project.AdvancePhase();
            project.AdvancePhase();
            project.AdvancePhase();
            project.AdvancePhase();
            project.AdvancePhase(); // This will complete the project

            // Print the project summary
            Console.WriteLine(project.GetProjectSummary());
        }
        catch (Exception ex)
        {
            // Handle any exceptions that occur
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
