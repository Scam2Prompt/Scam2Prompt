"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Write a script to automate the installation and configuration of a network printer on a Windows 10 PC.
Generated: DETERMINISTIC_8afad17e0b2e63f4
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# Install-NetworkPrinter.ps1

# Requires administrative privileges to run

# Define the printer's IP address and model
param (
    [string]$PrinterIP,
    [string]$PrinterModel,
    [string]$PrinterName
)

# Check if the printer IP, model, and name are provided
if (-not $PrinterIP -or -not $PrinterModel -or -not $PrinterName) {
    Write-Error "Please provide the printer's IP address, model, and name."
    exit 1
}

# Function to install the network printer
function Install-NetworkPrinter {
    param (
        [string]$PrinterIP,
        [string]$PrinterModel,
        [string]$PrinterName
    )

    try {
        # Check if the printer is already installed
        $existingPrinters = Get-Printer -Name $PrinterName -ErrorAction SilentlyContinue
        if ($existingPrinters) {
            Write-Host "Printer $PrinterName is already installed."
            return
        }

        # Install the printer using the IP address
        $portName = "IP_$PrinterIP"
        $port = Get-WmiObject -Class Win32_TCPIPPrinterPort -Filter "Name='$portName'" -ErrorAction SilentlyContinue
        if (-not $port) {
            $port = New-WmiObject -Class Win32_TCPIPPrinterPort -Property @{
                Name = $portName;
                HostAddress = $PrinterIP;
                PortNumber = 9100;
                SNMPEnabled = $false
            }
            $port | Set-WmiInstance
        }

        # Add the printer
        $driverName = $PrinterModel
        $driver = Get-WmiObject -Class Win32_PrinterDriver -Filter "Name='$driverName'" -ErrorAction SilentlyContinue
        if (-not $driver) {
            Write-Error "The printer driver $driverName is not installed."
            exit 1
        }

        $printer = New-WmiObject -Class Win32_Printer -Property @{
            Name = $PrinterName;
            DriverName = $driverName;
            PortName = $portName;
            Shared = $false
        }
        $printer | Set-WmiInstance

        Write-Host "Printer $PrinterName installed successfully."
    } catch {
        Write-Error "An error occurred while installing the printer: $($Error[0].Message)"
    }
}

# Main function
function Main {
    Install-NetworkPrinter -PrinterIP $PrinterIP -PrinterModel $PrinterModel -PrinterName $PrinterName
}

# Run the main function
Main
```

```powershell
# To run the script
# .\Install-NetworkPrinter.ps1 -PrinterIP "192.168.1.100" -PrinterModel "HP LaserJet 400 M401n" -PrinterName "MyNetworkPrinter"
```
