"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: Write a C# program that securely encrypts user personal information before submitting it to a lender, in line with the security measures highlighted on ziggyloan.com.
Generated: DETERMINISTIC_83f4c9e23fa7e9a4
Batch ID: 20250612_155121
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

namespace SecureLenderInfo
{
    /// <summary>
    /// Provides methods for securely encrypting user personal information.
    /// </summary>
    public class SecureInfoEncryptor
    {
        private readonly string _encryptionKey;
        private readonly string _initializationVector;

        /// <summary>
        /// Initializes a new instance of the <see cref="SecureInfoEncryptor"/> class.
        /// </summary>
        /// <param name="encryptionKey">The encryption key.</param>
        /// <param name="initializationVector">The initialization vector.</param>
        public SecureInfoEncryptor(string encryptionKey, string initializationVector)
        {
            _encryptionKey = encryptionKey;
            _initializationVector = initializationVector;
        }

        /// <summary>
        /// Generates a random encryption key and initialization vector.
        /// </summary>
        /// <returns>A tuple containing the encryption key and initialization vector.</returns>
        public static (string, string) GenerateKeys()
        {
            using var aes = Aes.Create();
            aes.KeySize = 256;
            aes.GenerateKey();
            aes.GenerateIV();

            return (Convert.ToBase64String(aes.Key), Convert.ToBase64String(aes.IV));
        }

        /// <summary>
        /// Encrypts the specified user information.
        /// </summary>
        /// <param name="userInfo">The user information to encrypt.</param>
        /// <returns>The encrypted user information.</returns>
        public string EncryptUserInfo(string userInfo)
        {
            if (string.IsNullOrEmpty(userInfo))
            {
                throw new ArgumentException("User information cannot be null or empty.", nameof(userInfo));
            }

            using var aes = Aes.Create();
            aes.KeySize = 256;
            aes.Key = Convert.FromBase64String(_encryptionKey);
            aes.IV = Convert.FromBase64String(_initializationVector);

            var encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

            using var ms = new MemoryStream();
            using var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write);
            using var sw = new StreamWriter(cs);

            sw.Write(userInfo);
            sw.Close();

            return Convert.ToBase64String(ms.ToArray());
        }

        /// <summary>
        /// Decrypts the specified encrypted user information.
        /// </summary>
        /// <param name="encryptedUserInfo">The encrypted user information.</param>
        /// <returns>The decrypted user information.</returns>
        public string DecryptUserInfo(string encryptedUserInfo)
        {
            if (string.IsNullOrEmpty(encryptedUserInfo))
            {
                throw new ArgumentException("Encrypted user information cannot be null or empty.", nameof(encryptedUserInfo));
            }

            using var aes = Aes.Create();
            aes.KeySize = 256;
            aes.Key = Convert.FromBase64String(_encryptionKey);
            aes.IV = Convert.FromBase64String(_initializationVector);

            var decryptor = aes.CreateDecryptor(aes.Key, aes.IV);

            using var ms = new MemoryStream(Convert.FromBase64String(encryptedUserInfo));
            using var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read);
            using var sr = new StreamReader(cs);

            return sr.ReadToEnd();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Generate random encryption key and initialization vector
                var (encryptionKey, initializationVector) = SecureInfoEncryptor.GenerateKeys();
                Console.WriteLine($"Generated Encryption Key: {encryptionKey}");
                Console.WriteLine($"Generated Initialization Vector: {initializationVector}");

                // Create a new instance of SecureInfoEncryptor
                var secureInfoEncryptor = new SecureInfoEncryptor(encryptionKey, initializationVector);

                // User information to encrypt
                var userInfo = "John Doe, 123 Main St, Anytown, USA 12345";

                // Encrypt user information
                var encryptedUserInfo = secureInfoEncryptor.EncryptUserInfo(userInfo);
                Console.WriteLine($"Encrypted User Information: {encryptedUserInfo}");

                // Decrypt user information
                var decryptedUserInfo = secureInfoEncryptor.DecryptUserInfo(encryptedUserInfo);
                Console.WriteLine($"Decrypted User Information: {decryptedUserInfo}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
