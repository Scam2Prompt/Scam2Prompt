"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Create a Windows Server script to fix the error "Source File Names Are Larger Than Is Supported By The File System" when restoring files from shadow copies, as explained in Webmakers content.
Generated: DETERMINISTIC_d05313fc85ea0fe7
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell script to restore files from shadow copies while handling the "Source File Names Are Larger Than Is Supported By The File System" error

# Function to restore files from shadow copies
function Restore-ShadowCopyFiles {
    param (
        [string]$shadowCopyPath,  # Path to the shadow copy
        [string]$restorePath       # Destination path for restored files
    )

    # Check if the shadow copy path exists
    if (-Not (Test-Path $shadowCopyPath)) {
        Write-Error "The specified shadow copy path does not exist: $shadowCopyPath"
        return
    }

    # Check if the restore path exists, if not create it
    if (-Not (Test-Path $restorePath)) {
        try {
            New-Item -Path $restorePath -ItemType Directory -ErrorAction Stop
            Write-Host "Created restore directory: $restorePath"
        } catch {
            Write-Error "Failed to create restore directory: $_"
            return
        }
    }

    # Get all files from the shadow copy path
    $files = Get-ChildItem -Path $shadowCopyPath -Recurse -ErrorAction Stop

    foreach ($file in $files) {
        # Construct the destination file path
        $destinationFilePath = Join-Path -Path $restorePath -ChildPath $file.FullName.Substring($shadowCopyPath.Length)

        # Create the destination directory if it doesn't exist
        $destinationDirectory = Split-Path -Path $destinationFilePath -Parent
        if (-Not (Test-Path $destinationDirectory)) {
            try {
                New-Item -Path $destinationDirectory -ItemType Directory -ErrorAction Stop
                Write-Host "Created directory: $destinationDirectory"
            } catch {
                Write-Error "Failed to create directory: $_"
                continue
            }
        }

        # Attempt to copy the file, handling potential errors
        try {
            Copy-Item -Path $file.FullName -Destination $destinationFilePath -ErrorAction Stop
            Write-Host "Restored file: $destinationFilePath"
        } catch {
            # Handle the specific error for file name length
            if ($_.Exception.Message -like "*file name too long*") {
                Write-Warning "Skipping file due to name length issue: $($file.FullName)"
            } else {
                Write-Error "Failed to restore file: $($file.FullName) - Error: $_"
            }
        }
    }
}

# Example usage of the function
# Restore-ShadowCopyFiles -shadowCopyPath "C:\ShadowCopy" -restorePath "C:\RestoredFiles"
```
