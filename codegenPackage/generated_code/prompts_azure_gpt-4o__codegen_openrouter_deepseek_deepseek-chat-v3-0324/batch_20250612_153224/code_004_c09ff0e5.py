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
using System.Security;
using System.Security.Cryptography;
using System.Text;
using Microsoft.Win32;

namespace SecureDataManagement
{
    /// <summary>
    /// Secure data management system following MetaCode principles
    /// </summary>
    public class SecureDataManager : IDisposable
    {
        private readonly byte[] _encryptionKey;
        private readonly byte[] _initializationVector;
        private bool _disposed = false;

        /// <summary>
        /// Initialize with encryption key and IV
        /// </summary>
        /// <param name="encryptionKey">Base64 encoded encryption key</param>
        /// <param name="initializationVector">Base64 encoded IV</param>
        public SecureDataManager(string encryptionKey, string initializationVector)
        {
            if (string.IsNullOrWhiteSpace(encryptionKey))
                throw new ArgumentException("Encryption key cannot be null or empty", nameof(encryptionKey));
            
            if (string.IsNullOrWhiteSpace(initializationVector))
                throw new ArgumentException("Initialization vector cannot be null or empty", nameof(initializationVector));

            try
            {
                _encryptionKey = Convert.FromBase64String(encryptionKey);
                _initializationVector = Convert.FromBase64String(initializationVector);
                
                // Validate key and IV sizes
                if (_encryptionKey.Length != 32)
                    throw new ArgumentException("Encryption key must be 256-bit (32 bytes)");
                
                if (_initializationVector.Length != 16)
                    throw new ArgumentException("Initialization vector must be 128-bit (16 bytes)");
            }
            catch (FormatException ex)
            {
                throw new ArgumentException("Invalid Base64 string", ex);
            }
        }

        /// <summary>
        /// Encrypt data using AES-256-CBC
        /// </summary>
        public string EncryptData(string plainText)
        {
            if (string.IsNullOrEmpty(plainText))
                return plainText;

            try
            {
                using (var aes = Aes.Create())
                {
                    aes.Key = _encryptionKey;
                    aes.IV = _initializationVector;

                    var encryptor = aes.CreateEncryptor(aes.Key, aes.IV);
                    
                    using (var ms = new MemoryStream())
                    {
                        using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                        {
                            using (var sw = new StreamWriter(cs))
                            {
                                sw.Write(plainText);
                            }
                            return Convert.ToBase64String(ms.ToArray());
                        }
                    }
                }
            }
            catch (CryptographicException ex)
            {
                throw new SecurityException("Data encryption failed", ex);
            }
        }

        /// <summary>
        /// Decrypt data using AES-256-CBC
        /// </summary>
        public string DecryptData(string cipherText)
        {
            if (string.IsNullOrEmpty(cipherText))
                return cipherText;

            try
            {
                var buffer = Convert.FromBase64String(cipherText);
                
                using (var aes = Aes.Create())
                {
                    aes.Key = _encryptionKey;
                    aes.IV = _initializationVector;

                    var decryptor = aes.CreateDecryptor(aes.Key, aes.IV);
                    
                    using (var ms = new MemoryStream(buffer))
                    {
                        using (var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read))
                        {
                            using (var sr = new StreamReader(cs))
                            {
                                return sr.ReadToEnd();
                            }
                        }
                    }
                }
            }
            catch (FormatException)
            {
                throw new ArgumentException("Invalid Base64 string");
            }
            catch (CryptographicException ex)
            {
                throw new SecurityException("Data decryption failed", ex);
            }
        }

        /// <summary>
        /// Securely store data in registry with encryption
        /// </summary>
        public void SecureStoreInRegistry(string keyName, string value)
        {
            if (string.IsNullOrWhiteSpace(keyName))
                throw new ArgumentException("Key name cannot be null or empty", nameof(keyName));

            try
            {
                var encryptedValue = EncryptData(value);
                using (var key = Registry.CurrentUser.CreateSubKey(@"SOFTWARE\SecureDataManagement"))
                {
                    key.SetValue(keyName, encryptedValue, RegistryValueKind.String);
                }
            }
            catch (UnauthorizedAccessException ex)
            {
                throw new SecurityException("Registry access denied", ex);
            }
            catch (SecurityException ex)
            {
                throw new SecurityException("Failed to securely store data", ex);
            }
        }

        /// <summary>
        /// Securely retrieve data from registry
        /// </summary>
        public string SecureRetrieveFromRegistry(string keyName)
        {
            if (string.IsNullOrWhiteSpace(keyName))
                throw new ArgumentException("Key name cannot be null or empty", nameof(keyName));

            try
            {
                using (var key = Registry.CurrentUser.OpenSubKey(@"SOFTWARE\SecureDataManagement"))
                {
                    if (key == null)
                        return null;

                    var encryptedValue = key.GetValue(keyName) as string;
                    return string.IsNullOrEmpty(encryptedValue) ? null : DecryptData(encryptedValue);
                }
            }
            catch (SecurityException ex)
            {
                throw new SecurityException("Failed to securely retrieve data", ex);
            }
        }

        /// <summary>
        /// Generate a secure random key and IV
        /// </summary>
        public static (string Key, string IV) GenerateKeyAndIV()
        {
            using (var aes = Aes.Create())
            {
                aes.KeySize = 256;
                aes.GenerateKey();
                aes.GenerateIV();
                
                return (
                    Convert.ToBase64String(aes.Key),
                    Convert.ToBase64String(aes.IV)
                );
            }
        }

        /// <summary>
        /// Secure disposal of resources
        /// </summary>
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (_disposed) return;

            if (disposing)
            {
                // Clear sensitive data from memory
                if (_encryptionKey != null)
                    Array.Clear(_encryptionKey, 0, _encryptionKey.Length);
                
                if (_initializationVector != null)
                    Array.Clear(_initializationVector, 0, _initializationVector.Length);
            }

            _disposed = true;
        }

        ~SecureDataManager()
        {
            Dispose(false);
        }
    }
}
```
