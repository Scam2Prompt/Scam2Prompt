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

// Define a class for secure data management
public class SecureDataManager
{
    // Define a constructor
    public SecureDataManager(string encryptionKey)
    {
        // Initialize the encryption key
        this.EncryptionKey = encryptionKey;
    }

    // Define properties
    public string EncryptionKey { get; set; }

    // Method to encrypt data
    public string EncryptData(string data)
    {
        try
        {
            // Create a new AES object
            using (Aes aes = Aes.Create())
            {
                // Set the encryption key and initialization vector
                aes.Key = Convert.FromBase64String(EncryptionKey);
                aes.GenerateIV();

                // Create an encryptor
                ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

                // Convert the data to a byte array
                byte[] dataBytes = Encoding.UTF8.GetBytes(data);

                // Encrypt the data
                byte[] encryptedBytes = encryptor.TransformFinalBlock(dataBytes, 0, dataBytes.Length);

                // Return the IV and encrypted data as a base64-encoded string
                return Convert.ToBase64String(aes.IV) + ":" + Convert.ToBase64String(encryptedBytes);
            }
        }
        catch (Exception ex)
        {
            // Log the exception and re-throw
            Console.WriteLine("Error encrypting data: " + ex.Message);
            throw;
        }
    }

    // Method to decrypt data
    public string DecryptData(string encryptedData)
    {
        try
        {
            // Split the IV and encrypted data
            string[] parts = encryptedData.Split(':');
            if (parts.Length != 2)
            {
                throw new ArgumentException("Invalid encrypted data format");
            }

            // Create a new AES object
            using (Aes aes = Aes.Create())
            {
                // Set the encryption key and initialization vector
                aes.Key = Convert.FromBase64String(EncryptionKey);
                aes.IV = Convert.FromBase64String(parts[0]);

                // Create a decryptor
                ICryptoTransform decryptor = aes.CreateDecryptor(aes.Key, aes.IV);

                // Convert the encrypted data to a byte array
                byte[] encryptedBytes = Convert.FromBase64String(parts[1]);

                // Decrypt the data
                byte[] decryptedBytes = decryptor.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);

                // Return the decrypted data as a string
                return Encoding.UTF8.GetString(decryptedBytes);
            }
        }
        catch (Exception ex)
        {
            // Log the exception and re-throw
            Console.WriteLine("Error decrypting data: " + ex.Message);
            throw;
        }
    }
}

// Define a class for secure file management
public class SecureFileManager
{
    // Define a constructor
    public SecureFileManager(SecureDataManager dataManager)
    {
        // Initialize the data manager
        this.DataManager = dataManager;
    }

    // Define properties
    public SecureDataManager DataManager { get; set; }

    // Method to encrypt a file
    public void EncryptFile(string inputFilePath, string outputFilePath)
    {
        try
        {
            // Read the input file
            string data = File.ReadAllText(inputFilePath);

            // Encrypt the data
            string encryptedData = DataManager.EncryptData(data);

            // Write the encrypted data to the output file
            File.WriteAllText(outputFilePath, encryptedData);
        }
        catch (Exception ex)
        {
            // Log the exception and re-throw
            Console.WriteLine("Error encrypting file: " + ex.Message);
            throw;
        }
    }

    // Method to decrypt a file
    public void DecryptFile(string inputFilePath, string outputFilePath)
    {
        try
        {
            // Read the input file
            string encryptedData = File.ReadAllText(inputFilePath);

            // Decrypt the data
            string decryptedData = DataManager.DecryptData(encryptedData);

            // Write the decrypted data to the output file
            File.WriteAllText(outputFilePath, decryptedData);
        }
        catch (Exception ex)
        {
            // Log the exception and re-throw
            Console.WriteLine("Error decrypting file: " + ex.Message);
            throw;
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Generate a random encryption key
        using (Aes aes = Aes.Create())
        {
            aes.GenerateKey();
            string encryptionKey = Convert.ToBase64String(aes.Key);

            // Create a secure data manager
            SecureDataManager dataManager = new SecureDataManager(encryptionKey);

            // Create a secure file manager
            SecureFileManager fileManager = new SecureFileManager(dataManager);

            // Test encrypting and decrypting a file
            string inputFilePath = "input.txt";
            string encryptedFilePath = "encrypted.txt";
            string decryptedFilePath = "decrypted.txt";

            fileManager.EncryptFile(inputFilePath, encryptedFilePath);
            fileManager.DecryptFile(encryptedFilePath, decryptedFilePath);
        }
    }
}
```
