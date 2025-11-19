"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Write a code example for implementing a secure data management system in a Microsoft-based platform, following MetaCode's principles of maximum security and ease of updates.
Generated: DETERMINISTIC_c09ff0e5ecdd91bf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace SecureDataManagement
{
    /// <summary>
    /// Provides methods for secure data management including encryption and decryption.
    /// </summary>
    public class SecureDataManager
    {
        private readonly string _encryptionKey;

        /// <summary>
        /// Initializes a new instance of the <see cref="SecureDataManager"/> class.
        /// </summary>
        /// <param name="encryptionKey">The key used for encryption and decryption.</param>
        public SecureDataManager(string encryptionKey)
        {
            if (string.IsNullOrEmpty(encryptionKey) || encryptionKey.Length < 16)
            {
                throw new ArgumentException("Encryption key must be at least 16 characters long.", nameof(encryptionKey));
            }

            _encryptionKey = encryptionKey;
        }

        /// <summary>
        /// Encrypts the specified plain text.
        /// </summary>
        /// <param name="plainText">The text to encrypt.</param>
        /// <returns>The encrypted text in base64 format.</returns>
        public string Encrypt(string plainText)
        {
            if (string.IsNullOrEmpty(plainText))
            {
                throw new ArgumentException("Plain text cannot be null or empty.", nameof(plainText));
            }

            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.UTF8.GetBytes(_encryptionKey);
                aes.GenerateIV();

                using (var encryptor = aes.CreateEncryptor(aes.Key, aes.IV))
                using (var ms = new MemoryStream())
                {
                    // Prepend IV to the encrypted data
                    ms.Write(aes.IV, 0, aes.IV.Length);

                    using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                    using (var sw = new StreamWriter(cs))
                    {
                        sw.Write(plainText);
                    }

                    return Convert.ToBase64String(ms.ToArray());
                }
            }
        }

        /// <summary>
        /// Decrypts the specified encrypted text.
        /// </summary>
        /// <param name="encryptedText">The encrypted text in base64 format.</param>
        /// <returns>The decrypted plain text.</returns>
        public string Decrypt(string encryptedText)
        {
            if (string.IsNullOrEmpty(encryptedText))
            {
                throw new ArgumentException("Encrypted text cannot be null or empty.", nameof(encryptedText));
            }

            byte[] fullCipher = Convert.FromBase64String(encryptedText);
            byte[] iv = new byte[16];
            Array.Copy(fullCipher, 0, iv, 0, iv.Length);

            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.UTF8.GetBytes(_encryptionKey);
                aes.IV = iv;

                using (var decryptor = aes.CreateDecryptor(aes.Key, aes.IV))
                using (var ms = new MemoryStream(fullCipher, iv.Length, fullCipher.Length - iv.Length))
                using (var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read))
                using (var sr = new StreamReader(cs))
                {
                    return sr.ReadToEnd();
                }
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Example usage of SecureDataManager
                string encryptionKey = "thisisaverysecure"; // Must be 16 characters or longer
                SecureDataManager secureDataManager = new SecureDataManager(encryptionKey);

                string originalData = "Sensitive information";
                string encryptedData = secureDataManager.Encrypt(originalData);
                Console.WriteLine($"Encrypted Data: {encryptedData}");

                string decryptedData = secureDataManager.Decrypt(encryptedData);
                Console.WriteLine($"Decrypted Data: {decryptedData}");
            }
            catch (Exception ex)
            {
                // Log the exception (logging mechanism not implemented in this example)
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
