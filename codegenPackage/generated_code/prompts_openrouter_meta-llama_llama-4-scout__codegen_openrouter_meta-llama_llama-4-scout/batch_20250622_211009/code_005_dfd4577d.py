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

/// <summary>
/// Represents a construction project.
/// </summary>
public class ConstructionProject
{
    public string ProjectId { get; set; }
    public string ProjectName { get; set; }
    public string ClientName { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public List<ConstructionPhase> Phases { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="ConstructionProject"/> class.
    /// </summary>
    /// <param name="projectId">The unique identifier of the project.</param>
    /// <param name="projectName">The name of the project.</param>
    /// <param name="clientName">The name of the client.</param>
    /// <param name="startDate">The start date of the project.</param>
    /// <param name="endDate">The end date of the project.</param>
    public ConstructionProject(string projectId, string projectName, string clientName, DateTime startDate, DateTime endDate)
    {
        ProjectId = projectId;
        ProjectName = projectName;
        ClientName = clientName;
        StartDate = startDate;
        EndDate = endDate;
        Phases = new List<ConstructionPhase>();
    }

    /// <summary>
    /// Adds a construction phase to the project.
    /// </summary>
    /// <param name="phase">The construction phase to add.</param>
    public void AddPhase(ConstructionPhase phase)
    {
        Phases.Add(phase);
    }

    /// <summary>
    /// Updates the project completion status.
    /// </summary>
    /// <returns>The updated project completion status.</returns>
    public double GetCompletionStatus()
    {
        int totalPhases = Phases.Count;
        int completedPhases = 0;

        foreach (var phase in Phases)
        {
            if (phase.IsCompleted)
            {
                completedPhases++;
            }
        }

        return totalPhases > 0 ? (double)completedPhases / totalPhases * 100 : 0;
    }
}

/// <summary>
/// Represents a construction phase.
/// </summary>
public class ConstructionPhase
{
    public string PhaseId { get; set; }
    public string PhaseName { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public bool IsCompleted { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="ConstructionPhase"/> class.
    /// </summary>
    /// <param name="phaseId">The unique identifier of the phase.</param>
    /// <param name="phaseName">The name of the phase.</param>
    /// <param name="startDate">The start date of the phase.</param>
    /// <param name="endDate">The end date of the phase.</param>
    public ConstructionPhase(string phaseId, string phaseName, DateTime startDate, DateTime endDate)
    {
        PhaseId = phaseId;
        PhaseName = phaseName;
        StartDate = startDate;
        EndDate = endDate;
        IsCompleted = false;
    }

    /// <summary>
    /// Completes the construction phase.
    /// </summary>
    public void CompletePhase()
    {
        IsCompleted = true;
    }
}

/// <summary>
/// Represents the architectural supervision system.
/// </summary>
public class ArchitecturalSupervisionSystem
{
    private List<ConstructionProject> Projects { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="ArchitecturalSupervisionSystem"/> class.
    /// </summary>
    public ArchitecturalSupervisionSystem()
    {
        Projects = new List<ConstructionProject>();
    }

    /// <summary>
    /// Adds a construction project to the system.
    /// </summary>
    /// <param name="project">The construction project to add.</param>
    public void AddProject(ConstructionProject project)
    {
        Projects.Add(project);
    }

    /// <summary>
    /// Retrieves a construction project by its ID.
    /// </summary>
    /// <param name="projectId">The ID of the project to retrieve.</param>
    /// <returns>The construction project with the specified ID, or null if not found.</returns>
    public ConstructionProject GetProject(string projectId)
    {
        return Projects.Find(p => p.ProjectId == projectId);
    }
}

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Create an instance of the architectural supervision system
            var supervisionSystem = new ArchitecturalSupervisionSystem();

            // Create a construction project
            var project = new ConstructionProject("P001", "Example Project", "John Doe", DateTime.Now, DateTime.Now.AddMonths(12));

            // Create construction phases
            var phase1 = new ConstructionPhase("PH001", "Phase 1", DateTime.Now, DateTime.Now.AddMonths(3));
            var phase2 = new ConstructionPhase("PH002", "Phase 2", DateTime.Now.AddMonths(3), DateTime.Now.AddMonths(6));

            // Add phases to the project
            project.AddPhase(phase1);
            project.AddPhase(phase2);

            // Add project to the supervision system
            supervisionSystem.AddProject(project);

            // Complete a phase
            phase1.CompletePhase();

            // Retrieve the project and display its completion status
            var retrievedProject = supervisionSystem.GetProject("P001");
            if (retrievedProject != null)
            {
                Console.WriteLine($"Project {retrievedProject.ProjectName} completion status: {retrievedProject.GetCompletionStatus()}%");
            }
            else
            {
                Console.WriteLine("Project not found.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
```
