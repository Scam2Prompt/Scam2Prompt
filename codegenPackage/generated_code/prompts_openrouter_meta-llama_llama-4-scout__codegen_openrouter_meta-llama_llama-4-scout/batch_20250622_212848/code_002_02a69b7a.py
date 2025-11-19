"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Generate a PowerShell script to automate the installation of Microsoft Office on multiple PCs in a network.
Generated: DETERMINISTIC_02a69b7a921827c4
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# OfficeInstallation.ps1

# Define the Office installation source and configuration
$officeSource = "\\path\to\office\source"
$officeConfig = "configuration.xml"

# Define the PCs to install Office on
$pcList = @(
    "PC1",
    "PC2",
    "PC3"
)

# Function to install Office on a single PC
function Install-Office {
    param (
        [string]$pcName
    )

    # Check if PC is online
    if (Test-Connection -ComputerName $pcName -Count 1 -Quiet) {
        Write-Host "Installing Office on $pcName..."
        
        # Copy Office source to PC
        $remoteSession = New-PSSession -ComputerName $pcName
        Copy-Item -Path $officeSource -Destination "C:\Temp\Office" -ToSession $remoteSession -Recurse

        # Run Office installation
        $installCommand = "C:\Temp\Office\setup.exe /configure C:\Temp\Office\$officeConfig"
        Invoke-Command -Session $remoteSession -ScriptBlock {
            param($command) 
            Start-Process -FilePath "powershell.exe" -ArgumentList "-Command $command" -Wait
        } -ArgumentList $installCommand

        # Remove Office source from PC
        Remove-Item -Path "C:\Temp\Office" -Force -Recurse -ToSession $remoteSession

        Remove-PSSession -Session $remoteSession
    } else {
        Write-Host "$pcName is offline. Skipping..."
    }
}

# Main function to install Office on multiple PCs
function Main {
    foreach ($pc in $pcList) {
        Install-Office -pcName $pc
    }
}

# Error handling
trap {
    Write-Host "An error occurred: $($Error[0].Message)"
}

# Run the main function
Main
```

```powershell
# configuration.xml example

<Configuration>
    <Product>
        <Name>ProPlus2019</Name>
        <Version>16.0</Version>
        <Channel>PerpetualVL2019</Channel>
        <Install>
            <Type>Full</Type>
        </Install>
    </Product>
    <Display>
        <Level>None</Level>
        <AcceptEULA>TRUE</AcceptEULA>
    </Display>
    <Property>
        <Name>PIDKEY</Name>
        <Value>your_office_product_key</Value>
    </Property>
</Configuration>
```
