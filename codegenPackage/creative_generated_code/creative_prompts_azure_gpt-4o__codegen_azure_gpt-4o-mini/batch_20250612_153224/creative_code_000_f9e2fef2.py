"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Write a code snippet using Microsoft technologies to create a secure, customizable software solution for enterprise management, referencing MetaCode's approach to personalized systems.
Generated: DETERMINISTIC_f9e2fef21b760d3e
Batch ID: 20250612_153224
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
using System.Data.SqlClient;
using System.Security.Cryptography;
using System.Text;

namespace EnterpriseManagement
{
    /// <summary>
    /// Represents a customizable enterprise management system.
    /// </summary>
    public class EnterpriseManager
    {
        private readonly string _connectionString;

        public EnterpriseManager(string connectionString)
        {
            _connectionString = connectionString;
        }

        /// <summary>
        /// Creates a new user in the enterprise system.
        /// </summary>
        /// <param name="username">The username of the new user.</param>
        /// <param name="password">The password of the new user.</param>
        /// <param name="role">The role of the new user.</param>
        /// <returns>True if user creation was successful, else false.</returns>
        public bool CreateUser(string username, string password, string role)
        {
            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    string hashedPassword = HashPassword(password);
                    var command = new SqlCommand("INSERT INTO Users (Username, PasswordHash, Role) VALUES (@Username, @PasswordHash, @Role)", connection);
                    command.Parameters.AddWithValue("@Username", username);
                    command.Parameters.AddWithValue("@PasswordHash", hashedPassword);
                    command.Parameters.AddWithValue("@Role", role);
                    return command.ExecuteNonQuery() > 0;
                }
            }
            catch (SqlException ex)
            {
                // Log the exception for further analysis (logging mechanism not implemented here)
                Console.WriteLine($"SQL Error: {ex.Message}");
                return false;
            }
            catch (Exception ex)
            {
                // Handle unexpected exceptions
                Console.WriteLine($"Unexpected Error: {ex.Message}");
                return false;
            }
        }

        /// <summary>
        /// Hashes the password using SHA256.
        /// </summary>
        /// <param name="password">The password to hash.</param>
        /// <returns>Hashed password as a string.</returns>
        private string HashPassword(string password)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
                StringBuilder builder = new StringBuilder();
                foreach (byte b in bytes)
                {
                    builder.Append(b.ToString("x2"));
                }
                return builder.ToString();
            }
        }

        /// <summary>
        /// Retrieves all users from the enterprise system.
        /// </summary>
        /// <returns>A list of users.</returns>
        public List<User> GetAllUsers()
        {
            var users = new List<User>();
            try
            {
                using (var connection = new SqlConnection(_connectionString))
                {
                    connection.Open();
                    var command = new SqlCommand("SELECT Username, Role FROM Users", connection);
                    using (var reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            users.Add(new User
                            {
                                Username = reader["Username"].ToString(),
                                Role = reader["Role"].ToString()
                            });
                        }
                    }
                }
            }
            catch (SqlException ex)
            {
                // Log the exception for further analysis
                Console.WriteLine($"SQL Error: {ex.Message}");
            }
            catch (Exception ex)
            {
                // Handle unexpected exceptions
                Console.WriteLine($"Unexpected Error: {ex.Message}");
            }
            return users;
        }
    }

    /// <summary>
    /// Represents a user in the enterprise management system.
    /// </summary>
    public class User
    {
        public string Username { get; set; }
        public string Role { get; set; }
    }
}
```
