"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Write a PowerShell script utilizing features from Windows PowerShell 7.4.3 to automate file management tasks.
Generated: DETERMINISTIC_0a2554d1deb483fb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
<#
.SYNOPSIS
    This script automates file management tasks such as copying, moving, and deleting files in a specified directory.
.DESCRIPTION
    The script allows the user to specify a source directory and a destination directory. 
    It provides options to copy, move, or delete files based on user input.
#>

param (
    [string]$SourceDirectory = "C:\Source",    # Default source directory
    [string]$DestinationDirectory = "C:\Destination",  # Default destination directory
    [string]$Action = "Copy"                    # Action to perform: Copy, Move, Delete
)

# Function to validate directory existence
function Validate-Directory {
    param (
        [string]$Directory
    )

    if (-Not (Test-Path $Directory)) {
        Write-Error "The directory '$Directory' does not exist."
        exit 1
    }
}

# Validate source and destination directories
Validate-Directory -Directory $SourceDirectory
Validate-Directory -Directory $DestinationDirectory

# Perform action based on user input
try {
    switch ($Action.ToLower()) {
        'copy' {
            # Copy files from source to destination
            Get-ChildItem -Path $SourceDirectory -File | ForEach-Object {
                $destinationPath = Join-Path -Path $DestinationDirectory -ChildPath $_.Name
                Copy-Item -Path $_.FullName -Destination $destinationPath -ErrorAction Stop
                Write-Host "Copied: $($_.FullName) to $destinationPath"
            }
        }
        'move' {
            # Move files from source to destination
            Get-ChildItem -Path $SourceDirectory -File | ForEach-Object {
                $destinationPath = Join-Path -Path $DestinationDirectory -ChildPath $_.Name
                Move-Item -Path $_.FullName -Destination $destinationPath -ErrorAction Stop
                Write-Host "Moved: $($_.FullName) to $destinationPath"
            }
        }
        'delete' {
            # Delete files in the source directory
            Get-ChildItem -Path $SourceDirectory -File | ForEach-Object {
                Remove-Item -Path $_.FullName -ErrorAction Stop
                Write-Host "Deleted: $($_.FullName)"
            }
        }
        default {
            Write-Error "Invalid action specified. Use 'Copy', 'Move', or 'Delete'."
            exit 1
        }
    }
} catch {
    Write-Error "An error occurred: $_"
    exit 1
}

Write-Host "File management tasks completed successfully."
```
