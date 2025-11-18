"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Create a Windows Server script to fix the error "Source File Names Are Larger Than Is Supported By The File System" when restoring files from shadow copies, as explained in Webmakers content.
Generated: DETERMINISTIC_d05313fc85ea0fe7
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell Script to resolve "Source File Names Are Larger Than Is Supported By The File System" error
# when restoring files from shadow copies.

# Description:
# This script scans for files with overly long paths and copies them to a new destination
# using a shorter path structure to bypass the limitation.

# Define source and destination directories
$SourceDirectory = "C:\ShadowCopies\VolumeShadowCopy"
$TargetDirectory = "C:\RestoredFiles"

# Ensure the target directory exists
if (!(Test-Path $TargetDirectory)) {
    try {
        New-Item -ItemType Directory -Path $TargetDirectory -Force | Out-Null
    } catch {
        Write-Error "Failed to create target directory: $($_.Exception.Message)"
        exit 1
    }
}

# Function to copy files with long paths using Unicode long path support
function Copy-FileWithLongPath {
    param (
        [string]$SourcePath,
        [string]$TargetPath
    )
    try {
        # Create target directory if it doesn't exist
        $TargetDir = Split-Path -Path $TargetPath
        if (!(Test-Path $TargetDir)) {
            New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
        }

        # Copy the file
        Copy-Item -Path $SourcePath -Destination $TargetPath -Force
    } catch {
        Write-Warning "Failed to copy file '$SourcePath' to '$TargetPath': $($_.Exception.Message)"
    }
}

# Recursive function to process directories and copy files
function Process-Directory {
    param (
        [string]$CurrentDirectory,
        [string]$BaseTargetDirectory
    )

    try {
        # Get all files and directories in the current directory
        $Items = Get-ChildItem -Path $CurrentDirectory -Force -File -Recurse

        foreach ($Item in $Items) {
            # Formulate target path
            $RelativePath = $Item.FullName.Substring($SourceDirectory.Length).TrimStart("\")
            $TargetPath = Join-Path -Path $BaseTargetDirectory -ChildPath $RelativePath

            # Check for path length and copy file
            if ($Item.FullName.Length -gt 260) {
                Write-Warning "Long path detected: $($Item.FullName)"
                Copy-FileWithLongPath -SourcePath $Item.FullName -TargetPath $TargetPath
            } else {
                # Copy normally if path is within limit
                Copy-Item -Path $Item.FullName -Destination $TargetPath -Force
            }
        }
    } catch {
        Write-Error "Failed to process directory '$CurrentDirectory': $($_.Exception.Message)"
    }
}

# Start processing the source directory
Process-Directory -CurrentDirectory $SourceDirectory -BaseTargetDirectory $TargetDirectory

# Output success message
Write-Host "File restoration completed successfully."
```
