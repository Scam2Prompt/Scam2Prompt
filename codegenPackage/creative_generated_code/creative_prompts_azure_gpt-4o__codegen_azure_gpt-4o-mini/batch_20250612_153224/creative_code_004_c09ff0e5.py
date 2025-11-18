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
    public class SecureDataManager
    {
        private readonly string _encryptionKey;

        public SecureDataManager(string encryptionKey)
        {
            // Validate the provided encryption key
            if (string.IsNullOrWhiteSpace(encryptionKey) || encryptionKey.Length < 16)
            {
                throw new ArgumentException("Encryption key must be at least 16 characters long.");
            }
            _encryptionKey = encryptionKey;
        }

        // Method to encrypt data
        public string Encrypt(string plainText)
        {
            if (string.IsNullOrEmpty(plainText))
            {
                throw new ArgumentNullException(nameof(plainText), "Input text cannot be null or empty.");
            }

            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.UTF8.GetBytes(_encryptionKey);
                aes.GenerateIV();
                
                // Encrypt the data
                using (var encryptor = aes.CreateEncryptor(aes.Key, aes.IV))
                using (var ms = new MemoryStream())
                {
                    ms.Write(aes.IV, 0, aes.IV.Length); // Prepend IV to the ciphertext
                    using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                    using (var sw = new StreamWriter(cs))
                    {
                        sw.Write(plainText);
                    }
                    return Convert.ToBase64String(ms.ToArray());
                }
            }
        }

        // Method to decrypt data
        public string Decrypt(string cipherText)
        {
            if (string.IsNullOrEmpty(cipherText))
            {
                throw new ArgumentNullException(nameof(cipherText), "Input text cannot be null or empty.");
            }

            // Convert from Base64 string to byte array
            byte[] cipherBytes = Convert.FromBase64String(cipherText);
            
            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.UTF8.GetBytes(_encryptionKey);
                
                // Extract the IV from the beginning of the ciphertext
                byte[] iv = new byte[aes.BlockSize / 8];
                Array.Copy(cipherBytes, 0, iv, 0, iv.Length);
                aes.IV = iv;

                // Decrypt the data
                using (var decryptor = aes.CreateDecryptor(aes.Key, aes.IV))
                using (var ms = new MemoryStream(cipherBytes, iv.Length, cipherBytes.Length - iv.Length))
                using (var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read))
                using (var sr = new StreamReader(cs))
                {
                    return sr.ReadToEnd();
                }
            }
        }

        // Example usage
        public static void Main(string[] args)
        {
            try
            {
                string key = "thisisaverysecure"; // Ensure key is at least 16 characters
                SecureDataManager secureDataManager = new SecureDataManager(key);

                string originalData = "Sensitive Information";
                string encryptedData = secureDataManager.Encrypt(originalData);
                string decryptedData = secureDataManager.Decrypt(encryptedData);

                Console.WriteLine($"Original: {originalData}");
                Console.WriteLine($"Encrypted: {encryptedData}");
                Console.WriteLine($"Decrypted: {decryptedData}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
