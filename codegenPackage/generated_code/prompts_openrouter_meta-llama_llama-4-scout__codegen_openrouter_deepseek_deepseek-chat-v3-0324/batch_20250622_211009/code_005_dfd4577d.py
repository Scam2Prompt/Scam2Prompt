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

namespace ConstructionProgressTracker
{
    /// <summary>
    /// Represents a construction project phase
    /// </summary>
    public class ConstructionPhase
    {
        public string Name { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EstimatedEndDate { get; set; }
        public DateTime? ActualEndDate { get; set; }
        public bool IsCompleted => ActualEndDate.HasValue;
        public double PercentageComplete { get; set; }
        public List<string> Dependencies { get; set; } = new List<string>();
    }

    /// <summary>
    /// Represents a construction project
    /// </summary>
    public class ConstructionProject
    {
        public string ProjectId { get; }
        public string ProjectName { get; set; }
        public string ClientName { get; set; }
        public string Location { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EstimatedCompletionDate { get; set; }
        public Dictionary<string, ConstructionPhase> Phases { get; } = new Dictionary<string, ConstructionPhase>();

        public ConstructionProject(string projectId)
        {
            ProjectId = projectId ?? throw new ArgumentNullException(nameof(projectId));
        }

        /// <summary>
        /// Adds a new phase to the project
        /// </summary>
        public void AddPhase(ConstructionPhase phase)
        {
            if (phase == null)
                throw new ArgumentNullException(nameof(phase));

            if (Phases.ContainsKey(phase.Name))
                throw new ArgumentException($"Phase '{phase.Name}' already exists in project");

            Phases.Add(phase.Name, phase);
        }

        /// <summary>
        /// Marks a phase as completed
        /// </summary>
        public void CompletePhase(string phaseName, DateTime completionDate)
        {
            if (!Phases.TryGetValue(phaseName, out var phase))
                throw new KeyNotFoundException($"Phase '{phaseName}' not found in project");

            if (phase.IsCompleted)
                throw new InvalidOperationException($"Phase '{phaseName}' is already completed");

            phase.ActualEndDate = completionDate;
            phase.PercentageComplete = 100;
        }

        /// <summary>
        /// Updates phase progress percentage
        /// </summary>
        public void UpdatePhaseProgress(string phaseName, double percentage)
        {
            if (percentage < 0 || percentage > 100)
                throw new ArgumentOutOfRangeException(nameof(percentage), "Percentage must be between 0 and 100");

            if (!Phases.TryGetValue(phaseName, out var phase))
                throw new KeyNotFoundException($"Phase '{phaseName}' not found in project");

            if (phase.IsCompleted)
                throw new InvalidOperationException($"Cannot update progress for completed phase '{phaseName}'");

            phase.PercentageComplete = percentage;
        }

        /// <summary>
        /// Calculates overall project completion percentage
        /// </summary>
        public double CalculateOverallProgress()
        {
            if (Phases.Count == 0)
                return 0;

            double totalWeight = 0;
            double weightedSum = 0;

            foreach (var phase in Phases.Values)
            {
                // Simple weighting - each phase contributes equally
                double weight = 1.0;
                totalWeight += weight;
                weightedSum += phase.PercentageComplete * weight;
            }

            return weightedSum / totalWeight;
        }
    }

    /// <summary>
    /// Manages multiple construction projects
    /// </summary>
    public class ProjectManager
    {
        private readonly Dictionary<string, ConstructionProject> _projects = new Dictionary<string, ConstructionProject>();

        /// <summary>
        /// Adds a new project to the manager
        /// </summary>
        public void AddProject(ConstructionProject project)
        {
            if (project == null)
                throw new ArgumentNullException(nameof(project));

            if (_projects.ContainsKey(project.ProjectId))
                throw new ArgumentException($"Project with ID '{project.ProjectId}' already exists");

            _projects.Add(project.ProjectId, project);
        }

        /// <summary>
        /// Gets a project by ID
        /// </summary>
        public ConstructionProject GetProject(string projectId)
        {
            if (!_projects.TryGetValue(projectId, out var project))
                throw new KeyNotFoundException($"Project with ID '{projectId}' not found");

            return project;
        }

        /// <summary>
        /// Gets all projects
        /// </summary>
        public IEnumerable<ConstructionProject> GetAllProjects()
        {
            return _projects.Values;
        }

        /// <summary>
        /// Gets projects that are behind schedule
        /// </summary>
        public IEnumerable<ConstructionProject> GetDelayedProjects(DateTime currentDate)
        {
            foreach (var project in _projects.Values)
            {
                if (project.CalculateOverallProgress() < 100 && currentDate > project.EstimatedCompletionDate)
                {
                    yield return project;
                }
            }
        }
    }
}
```
