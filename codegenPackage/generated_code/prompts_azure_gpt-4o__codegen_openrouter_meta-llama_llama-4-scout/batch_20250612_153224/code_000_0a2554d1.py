"""
Generated Code Metadata:
========================
Original URL: https://mahnoorpc.net
Prompt: Write a PowerShell script utilizing features from Windows PowerShell 7.4.3 to automate file management tasks.
Generated: DETERMINISTIC_0a2554d1deb483fb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# FileManagement.ps1

# Define a function to create a new directory
function New-Directory {
    <#
    .SYNOPSIS
        Creates a new directory.

    .DESCRIPTION
        Creates a new directory at the specified path.

    .PARAMETER Path
        The path where the new directory will be created.

    .EXAMPLE
        New-Directory -Path "C:\Example\NewDirectory"
    #>
    param (
        [string]$Path
    )

    try {
        # Check if the directory already exists
        if (Test-Path -Path $Path) {
            Write-Warning "Directory '$Path' already exists."
            return
        }

        # Create the new directory
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "Directory '$Path' created successfully."
    } catch {
        Write-Error "Failed to create directory: $($Error[0].Message)"
    }
}

# Define a function to copy files
function Copy-Files {
    <#
    .SYNOPSIS
        Copies files from a source directory to a destination directory.

    .DESCRIPTION
        Copies files from a source directory to a destination directory.

    .PARAMETER SourcePath
        The path to the source directory.

    .PARAMETER DestinationPath
        The path to the destination directory.

    .EXAMPLE
        Copy-Files -SourcePath "C:\Example\Source" -DestinationPath "C:\Example\Destination"
    #>
    param (
        [string]$SourcePath,
        [string]$DestinationPath
    )

    try {
        # Check if the source and destination directories exist
        if (-not (Test-Path -Path $SourcePath)) {
            Write-Error "Source directory '$SourcePath' does not exist."
            return
        }

        if (-not (Test-Path -Path $DestinationPath)) {
            Write-Error "Destination directory '$DestinationPath' does not exist."
            return
        }

        # Copy files from source to destination
        Get-ChildItem -Path $SourcePath -File | Copy-Item -Destination $DestinationPath
        Write-Host "Files copied successfully from '$SourcePath' to '$DestinationPath'."
    } catch {
        Write-Error "Failed to copy files: $($Error[0].Message)"
    }
}

# Define a function to delete files older than a specified number of days
function Remove-OldFiles {
    <#
    .SYNOPSIS
        Deletes files older than a specified number of days.

    .DESCRIPTION
        Deletes files older than a specified number of days in a given directory.

    .PARAMETER Path
        The path to the directory.

    .PARAMETER Days
        The number of days.

    .EXAMPLE
        Remove-OldFiles -Path "C:\Example\Files" -Days 30
    #>
    param (
        [string]$Path,
        [int]$Days
    )

    try {
        # Check if the directory exists
        if (-not (Test-Path -Path $Path)) {
            Write-Error "Directory '$Path' does not exist."
            return
        }

        # Calculate the date for the specified number of days ago
        $date = (Get-Date).AddDays(-$Days)

        # Get files older than the specified number of days and delete them
        Get-ChildItem -Path $Path -File | Where-Object {$_.LastWriteTime -lt $date} | Remove-Item -Force
        Write-Host "Files older than $Days days deleted successfully from '$Path'."
    } catch {
        Write-Error "Failed to delete old files: $($Error[0].Message)"
    }
}

# Main script
$sourcePath = "C:\Example\Source"
$destinationPath = "C:\Example\Destination"
$newDirectoryPath = "C:\Example\NewDirectory"
$days = 30

# Create a new directory
New-Directory -Path $newDirectoryPath

# Copy files
Copy-Files -SourcePath $sourcePath -DestinationPath $destinationPath

# Delete old files
Remove-OldFiles -Path $destinationPath -Days $days
```
