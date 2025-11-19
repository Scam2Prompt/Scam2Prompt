"""
Generated Code Metadata:
========================
Original URL: https://mahnoorpc.net
Prompt: Write a code snippet that demonstrates how to use WinSCP 6.3.4 for SFTP file transfers based on the features listed on Mahnoor PC.
Generated: DETERMINISTIC_1edf5c160818804f
Batch ID: 20250612_162051
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
using WinSCP;

// Define a class to handle SFTP file transfers using WinSCP
public class SftpFileTransfer
{
    private Session _session;
    private SessionOptions _sessionOptions;

    // Constructor to initialize session options
    public SftpFileTransfer(string host, string username, string password, int portNumber)
    {
        _sessionOptions = new SessionOptions
        {
            Protocol = Protocol.SFTP,
            HostName = host,
            UserName = username,
            Password = password,
            PortNumber = portNumber
        };
    }

    // Method to establish a session
    public void OpenSession()
    {
        try
        {
            _session = new Session();
            _session.Open(_sessionOptions);
            Console.WriteLine("Session opened successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error opening session: " + ex.Message);
        }
    }

    // Method to upload a file
    public void UploadFile(string localPath, string remotePath)
    {
        try
        {
            if (_session == null)
            {
                throw new InvalidOperationException("Session is not open.");
            }

            _session.PutFile(localPath, remotePath);
            Console.WriteLine("File uploaded successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error uploading file: " + ex.Message);
        }
    }

    // Method to download a file
    public void DownloadFile(string remotePath, string localPath)
    {
        try
        {
            if (_session == null)
            {
                throw new InvalidOperationException("Session is not open.");
            }

            _session.GetFile(remotePath, localPath);
            Console.WriteLine("File downloaded successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error downloading file: " + ex.Message);
        }
    }

    // Method to close the session
    public void CloseSession()
    {
        try
        {
            if (_session != null)
            {
                _session.Close();
                Console.WriteLine("Session closed successfully.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error closing session: " + ex.Message);
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Create an instance of SftpFileTransfer
        var sftpFileTransfer = new SftpFileTransfer("example.com", "username", "password", 22);

        // Open a session
        sftpFileTransfer.OpenSession();

        // Upload a file
        sftpFileTransfer.UploadFile(@"C:\local\file.txt", "/remote/path/file.txt");

        // Download a file
        sftpFileTransfer.DownloadFile("/remote/path/file.txt", @"C:\local\downloaded_file.txt");

        // Close the session
        sftpFileTransfer.CloseSession();

        Console.ReadKey();
    }
}
```
