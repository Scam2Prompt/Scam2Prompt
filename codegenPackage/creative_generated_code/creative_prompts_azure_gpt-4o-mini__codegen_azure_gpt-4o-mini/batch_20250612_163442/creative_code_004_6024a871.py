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

/// <summary>
/// Represents a client with associated information.
/// </summary>
public class Client
{
    public string ClientId { get; set; }
    public string Name { get; set; }
    public string ContactInformation { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="Client"/> class.
    /// </summary>
    /// <param name="clientId">Unique identifier for the client.</param>
    /// <param name="name">Name of the client.</param>
    /// <param name="contactInformation">Contact information of the client.</param>
    public Client(string clientId, string name, string contactInformation)
    {
        ClientId = clientId ?? throw new ArgumentNullException(nameof(clientId));
        Name = name ?? throw new ArgumentNullException(nameof(name));
        ContactInformation = contactInformation ?? throw new ArgumentNullException(nameof(contactInformation));
    }
}

/// <summary>
/// Represents a project associated with a client.
/// </summary>
public class Project
{
    public string ProjectId { get; set; }
    public string ProjectName { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public string Status { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="Project"/> class.
    /// </summary>
    /// <param name="projectId">Unique identifier for the project.</param>
    /// <param name="projectName">Name of the project.</param>
    /// <param name="startDate">Start date of the project.</param>
    /// <param name="endDate">End date of the project.</param>
    /// <param name="status">Current status of the project.</param>
    public Project(string projectId, string projectName, DateTime startDate, DateTime endDate, string status)
    {
        ProjectId = projectId ?? throw new ArgumentNullException(nameof(projectId));
        ProjectName = projectName ?? throw new ArgumentNullException(nameof(projectName));
        StartDate = startDate;
        EndDate = endDate;
        Status = status ?? throw new ArgumentNullException(nameof(status));
    }
}

/// <summary>
/// Manages client information and project details for a contracting company.
/// </summary>
public class ClientProjectManager
{
    private readonly Dictionary<string, Client> clients = new Dictionary<string, Client>();
    private readonly Dictionary<string, List<Project>> clientProjects = new Dictionary<string, List<Project>>();

    /// <summary>
    /// Adds a new client to the system.
    /// </summary>
    /// <param name="client">The client to add.</param>
    public void AddClient(Client client)
    {
        if (client == null)
            throw new ArgumentNullException(nameof(client));
        
        if (clients.ContainsKey(client.ClientId))
            throw new InvalidOperationException($"Client with ID {client.ClientId} already exists.");

        clients[client.ClientId] = client;
    }

    /// <summary>
    /// Adds a new project for a specific client.
    /// </summary>
    /// <param name="clientId">The ID of the client.</param>
    /// <param name="project">The project to add.</param>
    public void AddProject(string clientId, Project project)
    {
        if (string.IsNullOrWhiteSpace(clientId))
            throw new ArgumentNullException(nameof(clientId));
        
        if (project == null)
            throw new ArgumentNullException(nameof(project));
        
        if (!clients.ContainsKey(clientId))
            throw new KeyNotFoundException($"Client with ID {clientId} not found.");

        if (!clientProjects.ContainsKey(clientId))
            clientProjects[clientId] = new List<Project>();

        clientProjects[clientId].Add(project);
    }

    /// <summary>
    /// Retrieves a list of projects for a specific client.
    /// </summary>
    /// <param name="clientId">The ID of the client.</param>
    /// <returns>A list of projects associated with the client.</returns>
    public List<Project> GetProjectsForClient(string clientId)
    {
        if (string.IsNullOrWhiteSpace(clientId))
            throw new ArgumentNullException(nameof(clientId));
        
        if (!clientProjects.ContainsKey(clientId))
            return new List<Project>(); // Return an empty list if no projects found.

        return clientProjects[clientId];
    }

    /// <summary>
    /// Retrieves a client by their ID.
    /// </summary>
    /// <param name="clientId">The ID of the client.</param>
    /// <returns>The client associated with the provided ID.</returns>
    public Client GetClientById(string clientId)
    {
        if (string.IsNullOrWhiteSpace(clientId))
            throw new ArgumentNullException(nameof(clientId));
        
        if (!clients.TryGetValue(clientId, out var client))
            throw new KeyNotFoundException($"Client with ID {clientId} not found.");

        return client;
    }
}
```
