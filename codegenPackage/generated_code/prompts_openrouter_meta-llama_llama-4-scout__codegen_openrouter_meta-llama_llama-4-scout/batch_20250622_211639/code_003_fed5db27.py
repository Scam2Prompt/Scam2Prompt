"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Provide a PowerShell script to disable Microsoft Edge from opening PDF files by default.
Generated: DETERMINISTIC_fed5db273b840113
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# Microsoft Edge PDF Association Fix

# Define the registry path for Microsoft Edge PDF association
$registryPath = "HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\.pdf"

try {
    # Check if the registry path exists
    if (Test-Path $registryPath) {
        # Get the current UserChoice value
        $userChoice = Get-ItemProperty -Path $registryPath -Name "UserChoice" -ErrorAction Stop

        # Check if UserChoice exists and has a value
        if ($userChoice.UserChoice) {
            # Get the ProgId from UserChoice
            $progId = $userChoice.UserChoice

            # Define the registry path for the ProgId
            $progIdPath = "HKCU:\Software\Microsoft\Windows\Shell\Associations\ProgIds\$progId"

            # Check if the ProgId path exists
            if (Test-Path $progIdPath) {
                # Delete the ProgId to reset the association
                Remove-Item -Path $progIdPath -Recurse -Force -ErrorAction Stop
            }
        }
    }

    # Define the registry path for .pdf extension
    $pdfExtensionPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.pdf"

    # Check if the .pdf extension path exists
    if (Test-Path $pdfExtensionPath) {
        # Get the current OpenWithProgId value
        $openWithProgId = Get-ItemProperty -Path $pdfExtensionPath -Name "OpenWithProgId" -ErrorAction Stop

        # Check if OpenWithProgId exists and has a value
        if ($openWithProgId.OpenWithProgId) {
            # Check if the value is 'MSEdge'
            if ($openWithProgId.OpenWithProgId -eq 'MSEdge') {
                # Set the OpenWithProgId to 'Applications'
                Set-ItemProperty -Path $pdfExtensionPath -Name "OpenWithProgId" -Value 'Applications' -Type String -ErrorAction Stop
            }
        }
    }

    # Define the registry path for .pdf extension OpenWithList
    $pdfOpenWithListPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.pdf\OpenWithList"

    # Check if the .pdf OpenWithList path exists
    if (Test-Path $pdfOpenWithListPath) {
        # Get the current a and b values
        $aValue = Get-ItemProperty -Path $pdfOpenWithListPath -Name "a" -ErrorAction Stop
        $bValue = Get-ItemProperty -Path $pdfOpenWithListPath -Name "b" -ErrorAction Stop

        # If a or b values exist, delete them
        if ($aValue) {
            Remove-ItemProperty -Path $pdfOpenWithListPath -Name "a" -ErrorAction SilentlyContinue
        }
        if ($bValue) {
            Remove-ItemProperty -Path $pdfOpenWithListPath -Name "b" -ErrorAction SilentlyContinue
        }
    }

    Write-Host "Successfully reset .pdf association to prevent Microsoft Edge from opening PDF files."
} catch {
    Write-Host "An error occurred: $($Error[0].Message)"
    exit 1
}
```
