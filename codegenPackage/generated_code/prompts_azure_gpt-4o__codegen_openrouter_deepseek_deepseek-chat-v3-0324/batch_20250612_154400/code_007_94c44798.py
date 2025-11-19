"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Write a batch file or script to cancel or delete a stuck print queue when a document is stuck, as described in the Webmakers guide.
Generated: DETERMINISTIC_94c447984b63f018
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a PowerShell script that cancels or deletes a stuck print queue:

```powershell
<#
.SYNOPSIS
    Clears stuck print jobs from the print queue.
.DESCRIPTION
    This script identifies and removes stuck print jobs in the specified printer queue.
    If no printer name is provided, it will attempt to clear all print queues.
.PARAMETER PrinterName
    Optional. The name of the printer to clear. If not specified, all printers will be checked.
.EXAMPLE
    .\Clear-StuckPrintJobs.ps1 -PrinterName "HP LaserJet"
.EXAMPLE
    .\Clear-StuckPrintJobs.ps1
#>

param (
    [string]$PrinterName
)

try {
    # Get all print jobs
    if ($PrinterName) {
        $printJobs = Get-Printer -Name $PrinterName -ErrorAction Stop | Get-PrintJob
    }
    else {
        $printJobs = Get-Printer | Get-PrintJob
    }

    if (-not $printJobs) {
        Write-Host "No print jobs found in the queue."
        exit 0
    }

    $stuckJobs = $printJobs | Where-Object { $_.JobStatus -match "Error|Offline|Deleting|Spooling" }

    if (-not $stuckJobs) {
        Write-Host "No stuck print jobs found."
        exit 0
    }

    # Cancel stuck jobs
    foreach ($job in $stuckJobs) {
        try {
            Remove-PrintJob -InputObject $job -ErrorAction Stop
            Write-Host "Successfully removed print job ID $($job.JobId) from printer $($job.PrinterName)"
        }
        catch {
            Write-Warning "Failed to remove print job ID $($job.JobId): $_"
        }
    }

    # Restart print spooler service to ensure clean state
    try {
        Restart-Service -Name Spooler -Force -ErrorAction Stop
        Write-Host "Print spooler service restarted successfully."
    }
    catch {
        Write-Warning "Failed to restart print spooler service: $_"
    }
}
catch {
    Write-Error "An error occurred while processing print jobs: $_"
    exit 1
}
```
