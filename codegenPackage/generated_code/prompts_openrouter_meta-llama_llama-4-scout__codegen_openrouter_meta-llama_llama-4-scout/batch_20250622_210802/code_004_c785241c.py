"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Create a caregiver management system with functionalities for tracking caregiver availability, assigning caregivers to clients, and monitoring caregiver performance, using a programming language like Java or C#.
Generated: DETERMINISTIC_c785241c85e7dc12
Batch ID: 20250622_210802
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

namespace CaregiverManagementSystem
{
    /// <summary>
    /// Represents a caregiver with their details and availability.
    /// </summary>
    public class Caregiver
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public bool IsAvailable { get; set; }
        public List<Client> AssignedClients { get; set; }

        public Caregiver(int id, string name)
        {
            Id = id;
            Name = name;
            IsAvailable = true;
            AssignedClients = new List<Client>();
        }
    }

    /// <summary>
    /// Represents a client with their details.
    /// </summary>
    public class Client
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public Client(int id, string name)
        {
            Id = id;
            Name = name;
        }
    }

    /// <summary>
    /// Represents a performance record for a caregiver.
    /// </summary>
    public class PerformanceRecord
    {
        public int Id { get; set; }
        public Caregiver Caregiver { get; set; }
        public DateTime Date { get; set; }
        public string Notes { get; set; }

        public PerformanceRecord(int id, Caregiver caregiver, DateTime date, string notes)
        {
            Id = id;
            Caregiver = caregiver;
            Date = date;
            Notes = notes;
        }
    }

    /// <summary>
    /// Manages caregivers, their availability, assignments, and performance.
    /// </summary>
    public class CaregiverManagementSystem
    {
        private List<Caregiver> caregivers;
        private List<Client> clients;
        private List<PerformanceRecord> performanceRecords;

        public CaregiverManagementSystem()
        {
            caregivers = new List<Caregiver>();
            clients = new List<Client>();
            performanceRecords = new List<PerformanceRecord>();
        }

        /// <summary>
        /// Adds a caregiver to the system.
        /// </summary>
        /// <param name="caregiver">The caregiver to add.</param>
        public void AddCaregiver(Caregiver caregiver)
        {
            caregivers.Add(caregiver);
        }

        /// <summary>
        /// Adds a client to the system.
        /// </summary>
        /// <param name="client">The client to add.</param>
        public void AddClient(Client client)
        {
            clients.Add(client);
        }

        /// <summary>
        /// Assigns a caregiver to a client.
        /// </summary>
        /// <param name="caregiverId">The ID of the caregiver.</param>
        /// <param name="clientId">The ID of the client.</param>
        /// <exception cref="Exception">Thrown if caregiver or client is not found.</exception>
        public void AssignCaregiverToClient(int caregiverId, int clientId)
        {
            var caregiver = caregivers.Find(c => c.Id == caregiverId);
            var client = clients.Find(c => c.Id == clientId);

            if (caregiver == null)
            {
                throw new Exception("Caregiver not found.");
            }

            if (client == null)
            {
                throw new Exception("Client not found.");
            }

            if (!caregiver.IsAvailable)
            {
                throw new Exception("Caregiver is not available.");
            }

            caregiver.AssignedClients.Add(client);
            caregiver.IsAvailable = false;
        }

        /// <summary>
        /// Marks a caregiver as available.
        /// </summary>
        /// <param name="caregiverId">The ID of the caregiver.</param>
        /// <exception cref="Exception">Thrown if caregiver is not found.</exception>
        public void MarkCaregiverAsAvailable(int caregiverId)
        {
            var caregiver = caregivers.Find(c => c.Id == caregiverId);

            if (caregiver == null)
            {
                throw new Exception("Caregiver not found.");
            }

            caregiver.IsAvailable = true;
            caregiver.AssignedClients.Clear();
        }

        /// <summary>
        /// Adds a performance record for a caregiver.
        /// </summary>
        /// <param name="performanceRecord">The performance record to add.</param>
        public void AddPerformanceRecord(PerformanceRecord performanceRecord)
        {
            performanceRecords.Add(performanceRecord);
        }

        /// <summary>
        /// Displays all caregivers with their details.
        /// </summary>
        public void DisplayCaregivers()
        {
            foreach (var caregiver in caregivers)
            {
                Console.WriteLine($"ID: {caregiver.Id}, Name: {caregiver.Name}, Available: {caregiver.IsAvailable}");
            }
        }

        /// <summary>
        /// Displays all clients with their details.
        /// </summary>
        public void DisplayClients()
        {
            foreach (var client in clients)
            {
                Console.WriteLine($"ID: {client.Id}, Name: {client.Name}");
            }
        }

        /// <summary>
        /// Displays all performance records.
        /// </summary>
        public void DisplayPerformanceRecords()
        {
            foreach (var record in performanceRecords)
            {
                Console.WriteLine($"ID: {record.Id}, Caregiver: {record.Caregiver.Name}, Date: {record.Date}, Notes: {record.Notes}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var system = new CaregiverManagementSystem();

            // Create caregivers
            var caregiver1 = new Caregiver(1, "John Doe");
            var caregiver2 = new Caregiver(2, "Jane Doe");

            // Create clients
            var client1 = new Client(1, "Client 1");
            var client2 = new Client(2, "Client 2");

            // Add caregivers and clients to the system
            system.AddCaregiver(caregiver1);
            system.AddCaregiver(caregiver2);
            system.AddClient(client1);
            system.AddClient(client2);

            // Display caregivers and clients
            Console.WriteLine("Caregivers:");
            system.DisplayCaregivers();
            Console.WriteLine("Clients:");
            system.DisplayClients();

            // Assign caregivers to clients
            system.AssignCaregiverToClient(1, 1);
            system.AssignCaregiverToClient(2, 2);

            // Display updated caregiver availability
            Console.WriteLine("Updated Caregiver Availability:");
            system.DisplayCaregivers();

            // Add performance records
            var performanceRecord1 = new PerformanceRecord(1, caregiver1, DateTime.Now, "Excellent care provided.");
            var performanceRecord2 = new PerformanceRecord(2, caregiver2, DateTime.Now, "Good care provided.");

            system.AddPerformanceRecord(performanceRecord1);
            system.AddPerformanceRecord(performanceRecord2);

            // Display performance records
            Console.WriteLine("Performance Records:");
            system.DisplayPerformanceRecords();

            // Mark caregiver as available
            system.MarkCaregiverAsAvailable(1);

            // Display updated caregiver availability
            Console.WriteLine("Updated Caregiver Availability:");
            system.DisplayCaregivers();
        }
    }
}
```
