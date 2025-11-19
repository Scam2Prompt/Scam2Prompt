"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Outline a library in C# that manages client information and project details for a contracting company, inspired by AKNAN's organizational structure and client services.
Generated: DETERMINISTIC_6024a87153f19076
Batch ID: 20250612_163442
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

namespace ContractingCompanyLibrary
{
    /// <summary>
    /// Represents a client of the contracting company.
    /// </summary>
    public class Client
    {
        public int Id { get; private set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public string PhoneNumber { get; set; }

        /// <summary>
        /// Constructor for Client class.
        /// </summary>
        /// <param name="id">Unique identifier for the client.</param>
        /// <param name="name">Name of the client.</param>
        /// <param name="email">Email address of the client.</param>
        /// <param name="phoneNumber">Phone number of the client.</param>
        public Client(int id, string name, string email, string phoneNumber)
        {
            Id = id;
            Name = name;
            Email = email;
            PhoneNumber = phoneNumber;
        }
    }

    /// <summary>
    /// Represents a project handled by the contracting company.
    /// </summary>
    public class Project
    {
        public int Id { get; private set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public Client Client { get; private set; }

        /// <summary>
        /// Constructor for Project class.
        /// </summary>
        /// <param name="id">Unique identifier for the project.</param>
        /// <param name="name">Name of the project.</param>
        /// <param name="description">Description of the project.</param>
        /// <param name="startDate">Start date of the project.</param>
        /// <param name="endDate">End date of the project.</param>
        /// <param name="client">Client associated with the project.</param>
        public Project(int id, string name, string description, DateTime startDate, DateTime endDate, Client client)
        {
            Id = id;
            Name = name;
            Description = description;
            StartDate = startDate;
            EndDate = endDate;
            Client = client;
        }
    }

    /// <summary>
    /// Manages client data and project details for the contracting company.
    /// </summary>
    public class ContractingCompanyManager
    {
        private readonly List<Client> _clients = new List<Client>();
        private readonly List<Project> _projects = new List<Project>();

        /// <summary>
        /// Adds a new client to the system.
        /// </summary>
        /// <param name="client">Client object to add.</param>
        public void AddClient(Client client)
        {
            if (client == null)
                throw new ArgumentNullException(nameof(client), "Client cannot be null.");

            _clients.Add(client);
        }

        /// <summary>
        /// Adds a new project to the system.
        /// </summary>
        /// <param name="project">Project object to add.</param>
        public void AddProject(Project project)
        {
            if (project == null)
                throw new ArgumentNullException(nameof(project), "Project cannot be null.");

            if (!_clients.Contains(project.Client))
                throw new ArgumentException("The project must be associated with an existing client.", nameof(project));

            _projects.Add(project);
        }

        /// <summary>
        /// Retrieves all clients in the system.
        /// </summary>
        /// <returns>List of clients.</returns>
        public List<Client> GetClients()
        {
            return new List<Client>(_clients);
        }

        /// <summary>
        /// Retrieves all projects in the system.
        /// </summary>
        /// <returns>List of projects.</returns>
        public List<Project> GetProjects()
        {
            return new List<Project>(_projects);
        }

        /// <summary>
        /// Retrieves projects for a specific client.
        /// </summary>
        /// <param name="clientId">ID of the client.</param>
        /// <returns>List of projects associated with the client.</returns>
        public List<Project> GetProjectsByClient(int clientId)
        {
            return _projects.FindAll(project => project.Client.Id == clientId);
        }
    }
}
```
