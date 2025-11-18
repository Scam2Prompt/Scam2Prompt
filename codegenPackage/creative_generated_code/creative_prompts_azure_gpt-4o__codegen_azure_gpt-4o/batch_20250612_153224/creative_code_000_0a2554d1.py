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
# PowerShell Script: File Management Automation
# Version: Windows PowerShell 7.4.3
# Description: This script automates file management tasks, including organizing files by type,
#              archiving old files, and cleaning up empty directories.
# Author: [Your Name]
# Date: [Date]

# Set the working directory (change this path as needed)
$WorkingDirectory = "C:\Path\To\Your\Directory"

# Archive folder to store old files
$ArchiveFolder = "$WorkingDirectory\Archive"

# Log file to track actions
$LogFile = "$WorkingDirectory\FileManagementLog.txt"

# Maximum file age in days before archiving
$MaxFileAgeInDays = 30

# Ensure the working directory exists
if (!(Test-Path $WorkingDirectory)) {
    Write-Error "The specified working directory does not exist: $WorkingDirectory"
    exit 1
}

# Ensure the archive folder exists
if (!(Test-Path $ArchiveFolder)) {
    try {
        New-Item -ItemType Directory -Path $ArchiveFolder -Force | Out-Null
        Write-Output "Archive folder created: $ArchiveFolder" | Tee-Object -FilePath $LogFile -Append
    } catch {
        Write-Error "Failed to create archive folder: $_"
        exit 1
    }
}

try {
    # Organize files by type
    $Files = Get-ChildItem -Path $WorkingDirectory -File
    foreach ($File in $Files) {
        $Extension = $File.Extension.TrimStart(".")
        if ([string]::IsNullOrWhiteSpace($Extension)) {
            $Extension = "NoExtension"
        }
        $TypeFolder = "$WorkingDirectory\$Extension"

        if (!(Test-Path $TypeFolder)) {
            New-Item -ItemType Directory -Path $TypeFolder -Force | Out-Null
        }

        Move-Item -Path $File.FullName -Destination $TypeFolder -Force
        Write-Output "Moved file '$($File.Name)' to folder '$TypeFolder'" | Tee-Object -FilePath $LogFile -Append
    }

    # Archive old files
    $OldFiles = Get-ChildItem -Path $WorkingDirectory -File | Where-Object {
        $_.LastWriteTime -lt (Get-Date).AddDays(-$MaxFileAgeInDays)
    }

    foreach ($OldFile in $OldFiles) {
        Move-Item -Path $OldFile.FullName -Destination $ArchiveFolder -Force
        Write-Output "Archived file '$($OldFile.Name)' to '$ArchiveFolder'" | Tee-Object -FilePath $LogFile -Append
    }

    # Clean up empty directories
    $Directories = Get-ChildItem -Path $WorkingDirectory -Directory
    foreach ($Directory in $Directories) {
        if (-Not (Get-ChildItem -Path $Directory.FullName -Recurse)) {
            Remove-Item -Path $Directory.FullName -Force
            Write-Output "Removed empty directory '$($Directory.FullName)'" | Tee-Object -FilePath $LogFile -Append
        }
    }
} catch {
    Write-Error "An error occurred during file management: $_"
    Write-Output "An error occurred: $_" | Tee-Object -FilePath $LogFile -Append
    exit 1
}

Write-Output "File management tasks completed successfully." | Tee-Object -FilePath $LogFile -Append
```
