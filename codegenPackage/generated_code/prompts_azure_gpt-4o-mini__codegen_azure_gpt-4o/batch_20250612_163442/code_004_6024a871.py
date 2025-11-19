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

namespace ContractingCompanyLibrary
{
    /// <summary>
    /// Represents a client in the contracting company.
    /// </summary>
    public class Client
    {
        public int ClientId { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public string PhoneNumber { get; set; }

        /// <summary>
        /// Constructor to initialize a client.
        /// </summary>
        /// <param name="clientId">Unique identifier for the client.</param>
        /// <param name="name">Name of the client.</param>
        /// <param name="email">Email address of the client.</param>
        /// <param name="phoneNumber">Phone number of the client.</param>
        public Client(int clientId, string name, string email, string phoneNumber)
        {
            ClientId = clientId;
            Name = name;
            Email = email;
            PhoneNumber = phoneNumber;
        }
    }

    /// <summary>
    /// Represents a project in the contracting company.
    /// </summary>
    public class Project
    {
        public int ProjectId { get; set; }
        public string ProjectName { get; set; }
        public int ClientId { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public decimal Budget { get; set; }

        /// <summary>
        /// Constructor to initialize a project.
        /// </summary>
        /// <param name="projectId">Unique identifier for the project.</param>
        /// <param name="projectName">Name of the project.</param>
        /// <param name="clientId">ID of the client associated with the project.</param>
        /// <param name="startDate">Start date of the project.</param>
        /// <param name="endDate">End date of the project.</param>
        /// <param name="budget">Budget allocated for the project.</param>
        public Project(int projectId, string projectName, int clientId, DateTime startDate, DateTime endDate, decimal budget)
        {
            ProjectId = projectId;
            ProjectName = projectName;
            ClientId = clientId;
            StartDate = startDate;
            EndDate = endDate;
            Budget = budget;
        }
    }

    /// <summary>
    /// Manages client and project information for the contracting company.
    /// </summary>
    public class ContractingCompanyManager
    {
        private readonly List<Client> _clients = new List<Client>();
        private readonly List<Project> _projects = new List<Project>();

        /// <summary>
        /// Adds a new client to the system.
        /// </summary>
        /// <param name="client">Client object to be added.</param>
        public void AddClient(Client client)
        {
            if (client == null)
                throw new ArgumentNullException(nameof(client), "Client cannot be null.");

            _clients.Add(client);
        }

        /// <summary>
        /// Adds a new project to the system.
        /// </summary>
        /// <param name="project">Project object to be added.</param>
        public void AddProject(Project project)
        {
            if (project == null)
                throw new ArgumentNullException(nameof(project), "Project cannot be null.");

            if (!_clients.Exists(c => c.ClientId == project.ClientId))
                throw new ArgumentException("Client ID does not exist.", nameof(project.ClientId));

            _projects.Add(project);
        }

        /// <summary>
        /// Retrieves all clients.
        /// </summary>
        /// <returns>List of all clients.</returns>
        public List<Client> GetAllClients()
        {
            return new List<Client>(_clients);
        }

        /// <summary>
        /// Retrieves all projects.
        /// </summary>
        /// <returns>List of all projects.</returns>
        public List<Project> GetAllProjects()
        {
            return new List<Project>(_projects);
        }

        /// <summary>
        /// Retrieves projects associated with a specific client.
        /// </summary>
        /// <param name="clientId">ID of the client.</param>
        /// <returns>List of projects for the specified client.</returns>
        public List<Project> GetProjectsByClientId(int clientId)
        {
            return _projects.FindAll(p => p.ClientId == clientId);
        }

        /// <summary>
        /// Deletes a client and all associated projects.
        /// </summary>
        /// <param name="clientId">ID of the client to be deleted.</param>
        public void DeleteClient(int clientId)
        {
            _clients.RemoveAll(c => c.ClientId == clientId);
            _projects.RemoveAll(p => p.ClientId == clientId);
        }

        /// <summary>
        /// Deletes a project by its ID.
        /// </summary>
        /// <param name="projectId">ID of the project to be deleted.</param>
        public void DeleteProject(int projectId)
        {
            _projects.RemoveAll(p => p.ProjectId == projectId);
        }
    }
}
```
