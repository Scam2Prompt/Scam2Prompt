"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Illustrate how to implement a digital patient file system in C# that customizes patient records as described in the Luxteb software features.
Generated: DETERMINISTIC_c661eefbe13d8c92
Batch ID: 20250612_161520
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
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace LuxtebPatientFileSystem
{
    /// <summary>
    /// Represents a patient record with customizable fields
    /// </summary>
    public class PatientRecord
    {
        [JsonPropertyName("id")]
        public string Id { get; set; }

        [JsonPropertyName("firstName")]
        public string FirstName { get; set; }

        [JsonPropertyName("lastName")]
        public string LastName { get; set; }

        [JsonPropertyName("dateOfBirth")]
        public DateTime DateOfBirth { get; set; }

        [JsonPropertyName("customFields")]
        public Dictionary<string, object> CustomFields { get; set; } = new Dictionary<string, object>();

        [JsonPropertyName("lastModified")]
        public DateTime LastModified { get; set; }

        [JsonPropertyName("version")]
        public int Version { get; set; } = 1;
    }

    /// <summary>
    /// Manages patient records with encryption and version control
    /// </summary>
    public class PatientFileSystem
    {
        private readonly string _dataDirectory;
        private readonly byte[] _encryptionKey;
        private readonly JsonSerializerOptions _jsonOptions;

        /// <summary>
        /// Initialize the patient file system
        /// </summary>
        /// <param name="dataDirectory">Directory to store patient records</param>
        /// <param name="encryptionKey">32-byte encryption key</param>
        public PatientFileSystem(string dataDirectory, byte[] encryptionKey)
        {
            if (encryptionKey.Length != 32)
                throw new ArgumentException("Encryption key must be 32 bytes long");

            _dataDirectory = dataDirectory ?? throw new ArgumentNullException(nameof(dataDirectory));
            _encryptionKey = encryptionKey;

            if (!Directory.Exists(_dataDirectory))
            {
                Directory.CreateDirectory(_dataDirectory);
            }

            _jsonOptions = new JsonSerializerOptions
            {
                WriteIndented = true,
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
                DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
            };
        }

        /// <summary>
        /// Creates or updates a patient record
        /// </summary>
        public void SavePatientRecord(PatientRecord record)
        {
            if (record == null)
                throw new ArgumentNullException(nameof(record));

            try
            {
                record.LastModified = DateTime.UtcNow;
                record.Version++;

                string jsonData = JsonSerializer.Serialize(record, _jsonOptions);
                byte[] encryptedData = Encrypt(jsonData);

                string filePath = Path.Combine(_dataDirectory, $"{record.Id}.patient");
                File.WriteAllBytes(filePath, encryptedData);
            }
            catch (Exception ex)
            {
                throw new PatientFileSystemException("Failed to save patient record", ex);
            }
        }

        /// <summary>
        /// Retrieves a patient record by ID
        /// </summary>
        public PatientRecord GetPatientRecord(string patientId)
        {
            if (string.IsNullOrWhiteSpace(patientId))
                throw new ArgumentException("Patient ID cannot be empty", nameof(patientId));

            try
            {
                string filePath = Path.Combine(_dataDirectory, $"{patientId}.patient");
                if (!File.Exists(filePath))
                    return null;

                byte[] encryptedData = File.ReadAllBytes(filePath);
                string jsonData = Decrypt(encryptedData);

                return JsonSerializer.Deserialize<PatientRecord>(jsonData, _jsonOptions);
            }
            catch (Exception ex)
            {
                throw new PatientFileSystemException("Failed to retrieve patient record", ex);
            }
        }

        /// <summary>
        /// Searches for patient records matching the criteria
        /// </summary>
        public IEnumerable<PatientRecord> SearchPatients(Func<PatientRecord, bool> predicate)
        {
            try
            {
                var patientFiles = Directory.GetFiles(_dataDirectory, "*.patient");
                foreach (var file in patientFiles)
                {
                    byte[] encryptedData = File.ReadAllBytes(file);
                    string jsonData = Decrypt(encryptedData);
                    var record = JsonSerializer.Deserialize<PatientRecord>(jsonData, _jsonOptions);

                    if (predicate(record))
                    {
                        yield return record;
                    }
                }
            }
            catch (Exception ex)
            {
                throw new PatientFileSystemException("Failed to search patient records", ex);
            }
        }

        /// <summary>
        /// Gets all patient records
        /// </summary>
        public IEnumerable<PatientRecord> GetAllPatients()
        {
            return SearchPatients(_ => true);
        }

        /// <summary>
        /// Deletes a patient record
        /// </summary>
        public void DeletePatientRecord(string patientId)
        {
            if (string.IsNullOrWhiteSpace(patientId))
                throw new ArgumentException("Patient ID cannot be empty", nameof(patientId));

            try
            {
                string filePath = Path.Combine(_dataDirectory, $"{patientId}.patient");
                if (File.Exists(filePath))
                {
                    File.Delete(filePath);
                }
            }
            catch (Exception ex)
            {
                throw new PatientFileSystemException("Failed to delete patient record", ex);
            }
        }

        private byte[] Encrypt(string plainText)
        {
            using var aes = Aes.Create();
            aes.Key = _encryptionKey;
            aes.GenerateIV();

            using var encryptor = aes.CreateEncryptor(aes.Key, aes.IV);
            using var ms = new MemoryStream();
            
            // Write IV first
            ms.Write(aes.IV, 0, aes.IV.Length);
            
            // Write encrypted data
            using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
            using (var sw = new StreamWriter(cs))
            {
                sw.Write(plainText);
            }

            return ms.ToArray();
        }

        private string Decrypt(byte[] cipherText)
        {
            using var aes = Aes.Create();
            aes.Key = _encryptionKey;

            using var ms = new MemoryStream(cipherText);
            byte[] iv = new byte[aes.IV.Length];
            ms.Read(iv, 0, iv.Length);
            aes.IV = iv;

            using var decryptor = aes.CreateDecryptor(aes.Key, aes.IV);
            using var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read);
            using var sr = new StreamReader(cs);
            
            return sr.ReadToEnd();
        }
    }

    /// <summary>
    /// Custom exception for patient file system errors
    /// </summary>
    public class PatientFileSystemException : Exception
    {
        public PatientFileSystemException(string message) : base(message) { }
        public PatientFileSystemException(string message, Exception inner) : base(message, inner) { }
    }

    /// <summary>
    /// Helper class for generating secure patient IDs
    /// </summary>
    public static class PatientIdGenerator
    {
        private static readonly RandomNumberGenerator _rng = RandomNumberGenerator.Create();
        private const string ValidChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        public static string GeneratePatientId(int length = 12)
        {
            var result = new StringBuilder(length);
            var byteBuffer = new byte[1];

            for (int i = 0; i < length; i++)
            {
                _rng.GetBytes(byteBuffer);
                result.Append(ValidChars[byteBuffer[0] % ValidChars.Length]);
            }

            return result.ToString();
        }
    }
}
```
