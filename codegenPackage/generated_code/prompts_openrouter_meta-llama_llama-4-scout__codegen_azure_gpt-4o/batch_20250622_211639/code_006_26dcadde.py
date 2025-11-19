"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Write a C# code snippet to cancel or delete a stuck print queue using Windows API.
Generated: DETERMINISTIC_26dcaddef0d8fa36
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Runtime.InteropServices;

class PrintQueueManager
{
    // Importing necessary Windows API functions
    [DllImport("winspool.drv", SetLastError = true, CharSet = CharSet.Auto)]
    private static extern bool OpenPrinter(string pPrinterName, out IntPtr hPrinter, IntPtr pDefault);

    [DllImport("winspool.drv", SetLastError = true)]
    private static extern bool ClosePrinter(IntPtr hPrinter);

    [DllImport("winspool.drv", SetLastError = true)]
    private static extern bool SetPrinter(IntPtr hPrinter, uint Level, IntPtr pPrinter, uint Command);

    // Constants for printer commands
    private const uint PRINTER_CONTROL_PURGE = 3; // Command to purge the print queue

    public static void ClearPrintQueue(string printerName)
    {
        IntPtr hPrinter = IntPtr.Zero;

        try
        {
            // Open the printer
            if (!OpenPrinter(printerName, out hPrinter, IntPtr.Zero))
            {
                throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error(), "Failed to open printer.");
            }

            // Purge the print queue
            if (!SetPrinter(hPrinter, 0, IntPtr.Zero, PRINTER_CONTROL_PURGE))
            {
                throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error(), "Failed to purge the print queue.");
            }

            Console.WriteLine($"Successfully cleared the print queue for printer: {printerName}");
        }
        catch (Exception ex)
        {
            // Log or handle the error appropriately
            Console.Error.WriteLine($"Error: {ex.Message}");
        }
        finally
        {
            // Ensure the printer handle is closed
            if (hPrinter != IntPtr.Zero)
            {
                ClosePrinter(hPrinter);
            }
        }
    }

    static void Main(string[] args)
    {
        // Example usage
        Console.Write("Enter the printer name: ");
        string printerName = Console.ReadLine();

        if (!string.IsNullOrWhiteSpace(printerName))
        {
            ClearPrintQueue(printerName);
        }
        else
        {
            Console.WriteLine("Invalid printer name.");
        }
    }
}
```
