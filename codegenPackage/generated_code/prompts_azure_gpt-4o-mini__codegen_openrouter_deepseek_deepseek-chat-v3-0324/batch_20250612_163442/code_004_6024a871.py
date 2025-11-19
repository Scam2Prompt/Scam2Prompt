"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Outline a library in C# that manages client information and project details for a contracting company, inspired by AKNAN's organizational structure and client services.
Generated: DETERMINISTIC_6024a87153f19076
Batch ID: 20250612_163442
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

namespace AKNAN.Contracting
{
    /// <summary>
    /// Represents a client of the contracting company
    /// </summary>
    public class Client
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string ContactPerson { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
        public string Address { get; set; }
        public DateTime RegistrationDate { get; set; }
        public List<Project> Projects { get; set; } = new List<Project>();

        /// <summary>
        /// Validates client information
        /// </summary>
        /// <returns>True if client data is valid</returns>
        public bool Validate()
        {
            if (string.IsNullOrWhiteSpace(Name))
                throw new ArgumentException("Client name is required");
            
            if (string.IsNullOrWhiteSpace(ContactPerson))
                throw new ArgumentException("Contact person is required");
            
            if (string.IsNullOrWhiteSpace(Email) || !Email.Contains("@"))
                throw new ArgumentException("Valid email is required");
            
            if (string.IsNullOrWhiteSpace(Phone))
                throw new ArgumentException("Phone number is required");

            return true;
        }
    }

    /// <summary>
    /// Represents a project for a client
    /// </summary>
    public class Project
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime? EndDate { get; set; }
        public decimal Budget { get; set; }
        public ProjectStatus Status { get; set; }
        public int ClientId { get; set; }

        /// <summary>
        /// Validates project information
        /// </summary>
        /// <returns>True if project data is valid</returns>
        public bool Validate()
        {
            if (string.IsNullOrWhiteSpace(Name))
                throw new ArgumentException("Project name is required");
            
            if (StartDate == default)
                throw new ArgumentException("Start date is required");
            
            if (EndDate.HasValue && EndDate < StartDate)
                throw new ArgumentException("End date cannot be before start date");
            
            if (Budget <= 0)
                throw new ArgumentException("Budget must be positive");

            return true;
        }
    }

    /// <summary>
    /// Project status enumeration
    /// </summary>
    public enum ProjectStatus
    {
        Planning,
        InProgress,
        OnHold,
        Completed,
        Cancelled
    }

    /// <summary>
    /// Manages client and project data for the contracting company
    /// </summary>
    public class ContractingService
    {
        private readonly List<Client> _clients = new List<Client>();
        private int _nextClientId = 1;
        private int _nextProjectId = 1;

        /// <summary>
        /// Adds a new client to the system
        /// </summary>
        /// <param name="client">Client to add</param>
        /// <returns>Added client with assigned ID</returns>
        public Client AddClient(Client client)
        {
            client.Validate();
            client.Id = _nextClientId++;
            _clients.Add(client);
            return client;
        }

        /// <summary>
        /// Retrieves a client by ID
        /// </summary>
        /// <param name="id">Client ID</param>
        /// <returns>Client or null if not found</returns>
        public Client GetClient(int id)
        {
            return _clients.FirstOrDefault(c => c.Id == id);
        }

        /// <summary>
        /// Retrieves all clients
        /// </summary>
        /// <returns>List of all clients</returns>
        public List<Client> GetAllClients()
        {
            return _clients.ToList();
        }

        /// <summary>
        /// Adds a project to a client
        /// </summary>
        /// <param name="clientId">Client ID</param>
        /// <param name="project">Project to add</param>
        /// <returns>Added project with assigned ID</returns>
        public Project AddProject(int clientId, Project project)
        {
            project.Validate();
            var client = GetClient(clientId) ?? throw new ArgumentException("Client not found");
            
            project.Id = _nextProjectId++;
            project.ClientId = clientId;
            client.Projects.Add(project);
            
            return project;
        }

        /// <summary>
        /// Updates project status
        /// </summary>
        /// <param name="projectId">Project ID</param>
        /// <param name="newStatus">New status</param>
        /// <returns>Updated project</returns>
        public Project UpdateProjectStatus(int projectId, ProjectStatus newStatus)
        {
            var project = _clients
                .SelectMany(c => c.Projects)
                .FirstOrDefault(p => p.Id == projectId) 
                ?? throw new ArgumentException("Project not found");

            project.Status = newStatus;
            return project;
        }

        /// <summary>
        /// Gets all projects for a client
        /// </summary>
        /// <param name="clientId">Client ID</param>
        /// <returns>List of projects</returns>
        public List<Project> GetClientProjects(int clientId)
        {
            var client = GetClient(clientId);
            return client?.Projects.ToList() ?? new List<Project>();
        }

        /// <summary>
        /// Gets all projects with a specific status
        /// </summary>
        /// <param name="status">Status to filter by</param>
        /// <returns>List of projects</returns>
        public List<Project> GetProjectsByStatus(ProjectStatus status)
        {
            return _clients
                .SelectMany(c => c.Projects)
                .Where(p => p.Status == status)
                .ToList();
        }
    }
}
```
