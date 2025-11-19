"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a C# code snippet that implements a prayer request system, allowing users to submit and view prayer requests, inspired by the "Prayer" section on lifes.quest.
Generated: DETERMINISTIC_847589f680221c6c
Batch ID: 20250622_210108
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
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace PrayerRequestSystem
{
    public class PrayerRequest
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Request { get; set; }
        public DateTime SubmittedDate { get; set; }
        public bool IsAnonymous { get; set; }
    }

    public class PrayerRequestRepository
    {
        private readonly string _connectionString;

        public PrayerRequestRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        /// <summary>
        /// Adds a new prayer request to the database
        /// </summary>
        public int AddRequest(PrayerRequest request)
        {
            if (string.IsNullOrWhiteSpace(request.Request))
            {
                throw new ArgumentException("Prayer request cannot be empty");
            }

            const string sql = @"
                INSERT INTO PrayerRequests (Name, Request, SubmittedDate, IsAnonymous)
                VALUES (@Name, @Request, @SubmittedDate, @IsAnonymous);
                SELECT CAST(SCOPE_IDENTITY() as int)";

            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    using (var command = new SqlCommand(sql, connection))
                    {
                        command.Parameters.AddWithValue("@Name", request.Name ?? string.Empty);
                        command.Parameters.AddWithValue("@Request", request.Request);
                        command.Parameters.AddWithValue("@SubmittedDate", DateTime.UtcNow);
                        command.Parameters.AddWithValue("@IsAnonymous", request.IsAnonymous);

                        return (int)command.ExecuteScalar();
                    }
                }
            }
            catch (SqlException ex)
            {
                throw new ApplicationException("Error saving prayer request to database", ex);
            }
        }

        /// <summary>
        /// Retrieves all prayer requests from the database
        /// </summary>
        public List<PrayerRequest> GetAllRequests()
        {
            const string sql = "SELECT Id, Name, Request, SubmittedDate, IsAnonymous FROM PrayerRequests ORDER BY SubmittedDate DESC";

            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    using (var command = new SqlCommand(sql, connection))
                    {
                        using (var reader = command.ExecuteReader())
                        {
                            var requests = new List<PrayerRequest>();
                            while (reader.Read())
                            {
                                requests.Add(new PrayerRequest
                                {
                                    Id = reader.GetInt32(0),
                                    Name = reader.GetString(1),
                                    Request = reader.GetString(2),
                                    SubmittedDate = reader.GetDateTime(3),
                                    IsAnonymous = reader.GetBoolean(4)
                                });
                            }
                            return requests;
                        }
                    }
                }
            }
            catch (SqlException ex)
            {
                throw new ApplicationException("Error retrieving prayer requests from database", ex);
            }
        }

        /// <summary>
        /// Retrieves prayer requests with pagination support
        /// </summary>
        public List<PrayerRequest> GetRequests(int pageNumber, int pageSize)
        {
            const string sql = @"
                SELECT Id, Name, Request, SubmittedDate, IsAnonymous 
                FROM PrayerRequests 
                ORDER BY SubmittedDate DESC
                OFFSET @Offset ROWS FETCH NEXT @PageSize ROWS ONLY";

            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    using (var command = new SqlCommand(sql, connection))
                    {
                        command.Parameters.AddWithValue("@Offset", (pageNumber - 1) * pageSize);
                        command.Parameters.AddWithValue("@PageSize", pageSize);

                        using (var reader = command.ExecuteReader())
                        {
                            var requests = new List<PrayerRequest>();
                            while (reader.Read())
                            {
                                requests.Add(new PrayerRequest
                                {
                                    Id = reader.GetInt32(0),
                                    Name = reader.GetString(1),
                                    Request = reader.GetString(2),
                                    SubmittedDate = reader.GetDateTime(3),
                                    IsAnonymous = reader.GetBoolean(4)
                                });
                            }
                            return requests;
                        }
                    }
                }
            }
            catch (SqlException ex)
            {
                throw new ApplicationException("Error retrieving paginated prayer requests", ex);
            }
        }
    }

    public class PrayerRequestService
    {
        private readonly PrayerRequestRepository _repository;

        public PrayerRequestService(PrayerRequestRepository repository)
        {
            _repository = repository;
        }

        /// <summary>
        /// Submits a new prayer request
        /// </summary>
        public PrayerRequest SubmitRequest(string name, string request, bool isAnonymous = false)
        {
            if (string.IsNullOrWhiteSpace(request))
            {
                throw new ArgumentException("Prayer request text is required");
            }

            var prayerRequest = new PrayerRequest
            {
                Name = isAnonymous ? "Anonymous" : name,
                Request = request,
                SubmittedDate = DateTime.UtcNow,
                IsAnonymous = isAnonymous
            };

            prayerRequest.Id = _repository.AddRequest(prayerRequest);
            return prayerRequest;
        }

        /// <summary>
        /// Gets all prayer requests
        /// </summary>
        public List<PrayerRequest> GetAllRequests()
        {
            return _repository.GetAllRequests();
        }

        /// <summary>
        /// Gets prayer requests with pagination
        /// </summary>
        public List<PrayerRequest> GetRequests(int pageNumber, int pageSize = 10)
        {
            if (pageNumber < 1)
            {
                throw new ArgumentException("Page number must be greater than 0");
            }

            if (pageSize < 1 || pageSize > 100)
            {
                throw new ArgumentException("Page size must be between 1 and 100");
            }

            return _repository.GetRequests(pageNumber, pageSize);
        }
    }
}
```
