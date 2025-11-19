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
    /// Represents a client with their details.
    /// </summary>
    public class Client
    {
        public int ClientId { get; private set; }
        public string Name { get; private set; }
        public string ContactInfo { get; private set; }

        public Client(int clientId, string name, string contactInfo)
        {
            ClientId = clientId;
            Name = name ?? throw new ArgumentNullException(nameof(name), "Client name cannot be null.");
            ContactInfo = contactInfo ?? throw new ArgumentNullException(nameof(contactInfo), "Contact information cannot be null.");
        }
    }

    /// <summary>
    /// Represents a project associated with a client.
    /// </summary>
    public class Project
    {
        public int ProjectId { get; private set; }
        public string ProjectName { get; private set; }
        public DateTime StartDate { get; private set; }
        public DateTime EndDate { get; private set; }
        public Client Client { get; private set; }

        public Project(int projectId, string projectName, DateTime startDate, DateTime endDate, Client client)
        {
            ProjectId = projectId;
            ProjectName = projectName ?? throw new ArgumentNullException(nameof(projectName), "Project name cannot be null.");
            StartDate = startDate;
            EndDate = endDate;
            Client = client ?? throw new ArgumentNullException(nameof(client), "Client cannot be null.");
        }
    }

    /// <summary>
    /// Manages client information and project details.
    /// </summary>
    public class ClientProjectManager
    {
        private readonly List<Client> clients = new List<Client>();
        private readonly List<Project> projects = new List<Project>();

        /// <summary>
        /// Adds a new client to the manager.
        /// </summary>
        /// <param name="client">The client to add.</param>
        public void AddClient(Client client)
        {
            if (client == null) throw new ArgumentNullException(nameof(client), "Client cannot be null.");
            clients.Add(client);
        }

        /// <summary>
        /// Adds a new project to the manager.
        /// </summary>
        /// <param name="project">The project to add.</param>
        public void AddProject(Project project)
        {
            if (project == null) throw new ArgumentNullException(nameof(project), "Project cannot be null.");
            projects.Add(project);
        }

        /// <summary>
        /// Retrieves a client by their ID.
        /// </summary>
        /// <param name="clientId">The ID of the client to retrieve.</param>
        /// <returns>The client with the specified ID.</returns>
        public Client GetClient(int clientId)
        {
            var client = clients.Find(c => c.ClientId == clientId);
            if (client == null) throw new KeyNotFoundException($"Client with ID {clientId} not found.");
            return client;
        }

        /// <summary>
        /// Retrieves a project by its ID.
        /// </summary>
        /// <param name="projectId">The ID of the project to retrieve.</param>
        /// <returns>The project with the specified ID.</returns>
        public Project GetProject(int projectId)
        {
            var project = projects.Find(p => p.ProjectId == projectId);
            if (project == null) throw new KeyNotFoundException($"Project with ID {projectId} not found.");
            return project;
        }

        /// <summary>
        /// Lists all clients.
        /// </summary>
        /// <returns>A list of all clients.</returns>
        public List<Client> ListClients()
        {
            return new List<Client>(clients);
        }

        /// <summary>
        /// Lists all projects.
        /// </summary>
        /// <returns>A list of all projects.</returns>
        public List<Project> ListProjects()
        {
            return new List<Project>(projects);
        }
    }
}
```
