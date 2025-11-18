"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Write a code example for implementing a secure data management system in a Microsoft-based platform, following MetaCode's principles of maximum security and ease of updates.
Generated: DETERMINISTIC_c09ff0e5ecdd91bf
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
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace SecureDataManagement
{
    /// <summary>
    /// Secure Data Management System.
    /// Handles encryption, decryption, and secure storage of sensitive data.
    /// </summary>
    public class SecureDataManager
    {
        private readonly string _encryptionKey;

        /// <summary>
        /// Constructor for SecureDataManager.
        /// Generates or retrieves an encryption key for secure operations.
        /// </summary>
        public SecureDataManager(string encryptionKey = null)
        {
            // If no encryption key is provided, generate a new one.
            // In production, store the encryption key securely (e.g., Azure Key Vault).
            _encryptionKey = encryptionKey ?? GenerateEncryptionKey();
        }

        /// <summary>
        /// Encrypts plaintext data using AES encryption.
        /// </summary>
        /// <param name="plainText">The plaintext to encrypt.</param>
        /// <returns>Base64 encoded encrypted string.</returns>
        public string EncryptData(string plainText)
        {
            if (string.IsNullOrEmpty(plainText))
                throw new ArgumentException("Plaintext cannot be null or empty");

            using (Aes aes = Aes.Create())
            {
                aes.Key = Convert.FromBase64String(_encryptionKey);
                aes.GenerateIV();

                using (var encryptor = aes.CreateEncryptor(aes.Key, aes.IV))
                using (var memoryStream = new MemoryStream())
                {
                    // Write the IV at the beginning of the stream for later use.
                    memoryStream.Write(aes.IV, 0, aes.IV.Length);

                    using (var cryptoStream = new CryptoStream(memoryStream, encryptor, CryptoStreamMode.Write))
                    using (var writer = new StreamWriter(cryptoStream))
                    {
                        writer.Write(plainText);
                    }

                    return Convert.ToBase64String(memoryStream.ToArray());
                }
            }
        }

        /// <summary>
        /// Decrypts encrypted data back to plaintext.
        /// </summary>
        /// <param name="encryptedData">Base64 encoded encrypted data.</param>
        /// <returns>Decrypted plaintext string.</returns>
        public string DecryptData(string encryptedData)
        {
            if (string.IsNullOrEmpty(encryptedData))
                throw new ArgumentException("Encrypted data cannot be null or empty");

            byte[] cipherBytes = Convert.FromBase64String(encryptedData);

            using (Aes aes = Aes.Create())
            {
                aes.Key = Convert.FromBase64String(_encryptionKey);

                // Extract IV from the beginning of the cipher bytes.
                byte[] iv = new byte[aes.BlockSize / 8];
                Array.Copy(cipherBytes, 0, iv, 0, iv.Length);
                aes.IV = iv;

                using (var decryptor = aes.CreateDecryptor(aes.Key, aes.IV))
                using (var memoryStream = new MemoryStream(cipherBytes, iv.Length, cipherBytes.Length - iv.Length))
                using (var cryptoStream = new CryptoStream(memoryStream, decryptor, CryptoStreamMode.Read))
                using (var reader = new StreamReader(cryptoStream))
                {
                    return reader.ReadToEnd();
                }
            }
        }

        /// <summary>
        /// Generates a secure AES encryption key.
        /// </summary>
        /// <returns>Base64 encoded key string.</returns>
        private string GenerateEncryptionKey()
        {
            using (Aes aes = Aes.Create())
            {
                aes.GenerateKey();
                return Convert.ToBase64String(aes.Key);
            }
        }

        /// <summary>
        /// Securely saves encrypted data to a file.
        /// </summary>
        /// <param name="filePath">Path to the file.</param>
        /// <param name="data">The plaintext data to encrypt and save.</param>
        public void SaveEncryptedData(string filePath, string data)
        {
            if (string.IsNullOrEmpty(filePath))
                throw new ArgumentException("File path cannot be null or empty");

            string encryptedData = EncryptData(data);
            File.WriteAllText(filePath, encryptedData);
        }

        /// <summary>
        /// Securely reads and decrypts data from a file.
        /// </summary>
        /// <param name="filePath">Path to the file.</param>
        /// <returns>Decrypted plaintext data.</returns>
        public string ReadEncryptedData(string filePath)
        {
            if (string.IsNullOrEmpty(filePath))
                throw new ArgumentException("File path cannot be null or empty");

            if (!File.Exists(filePath))
                throw new FileNotFoundException($"File not found: {filePath}");

            string encryptedData = File.ReadAllText(filePath);
            return DecryptData(encryptedData);
        }
    }

    /// <summary>
    /// Example usage of SecureDataManager.
    /// </summary>
    internal class Program
    {
        private static void Main()
        {
            // Production: Store encryption key securely.
            SecureDataManager secureDataManager = new SecureDataManager();

            string filePath = "securedata.txt";
            string sensitiveData = "This is highly confidential data.";

            try
            {
                // Save encrypted data.
                secureDataManager.SaveEncryptedData(filePath, sensitiveData);
                Console.WriteLine("Data encrypted and saved successfully.");

                // Read and decrypt data.
                string decryptedData = secureDataManager.ReadEncryptedData(filePath);
                Console.WriteLine($"Decrypted Data: {decryptedData}");
            }
            catch (Exception ex)
            {
                // Handle exceptions gracefully.
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
