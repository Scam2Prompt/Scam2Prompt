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
<#
.SYNOPSIS
    Automates common file management tasks in Windows PowerShell 7.4.3.
.DESCRIPTION
    This script provides functions for organizing files by extension, cleaning up temporary files,
    and archiving old files. It includes error handling and logging capabilities.
.NOTES
    File Name      : FileManagementAutomation.ps1
    Author         : Your Name
    Prerequisite   : PowerShell 7.4.3
    Copyright 2023 - Your Company
#>

#Requires -Version 7.4.3

# Global variables
$Script:LogFile = "$env:TEMP\FileManagement_$(Get-Date -Format 'yyyyMMdd').log"
$Script:DefaultArchiveDays = 30
$Script:DefaultTempFileAge = 7

function Write-Log {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Message,
        
        [ValidateSet('INFO','WARNING','ERROR')]
        [string]$Level = 'INFO'
    )
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp][$Level] $Message"
    
    try {
        Add-Content -Path $Script:LogFile -Value $logEntry -ErrorAction Stop
    }
    catch {
        Write-Host "Failed to write to log file: $_" -ForegroundColor Red
    }
}

function Organize-FilesByExtension {
    param (
        [Parameter(Mandatory=$true)]
        [string]$SourcePath,
        
        [string]$DestinationPath = $SourcePath,
        
        [switch]$Recurse,
        
        [switch]$WhatIf
    )
    
    try {
        if (-not (Test-Path -Path $SourcePath -PathType Container)) {
            throw "Source path does not exist or is not a directory"
        }
        
        if (-not (Test-Path -Path $DestinationPath -PathType Container)) {
            Write-Log -Message "Creating destination directory: $DestinationPath" -Level INFO
            New-Item -Path $DestinationPath -ItemType Directory -Force | Out-Null
        }
        
        $params = @{
            Path = $SourcePath
            File = $true
        }
        
        if ($Recurse) {
            $params['Recurse'] = $true
        }
        
        $files = Get-ChildItem @params
        
        foreach ($file in $files) {
            $extension = $file.Extension.TrimStart('.')
            if ([string]::IsNullOrEmpty($extension)) {
                $extension = "NoExtension"
            }
            
            $targetDir = Join-Path -Path $DestinationPath -ChildPath $extension
            if (-not (Test-Path -Path $targetDir)) {
                Write-Log -Message "Creating directory for extension $extension" -Level INFO
                New-Item -Path $targetDir -ItemType Directory | Out-Null
            }
            
            $targetPath = Join-Path -Path $targetDir -ChildPath $file.Name
            
            if ($WhatIf) {
                Write-Host "WhatIf: Would move $($file.FullName) to $targetPath"
            }
            else {
                Move-Item -Path $file.FullName -Destination $targetPath -Force
                Write-Log -Message "Moved $($file.Name) to $targetDir" -Level INFO
            }
        }
    }
    catch {
        Write-Log -Message "Error organizing files: $_" -Level ERROR
        throw $_
    }
}

function Cleanup-TempFiles {
    param (
        [string[]]$Paths = @($env:TEMP, "$env:SystemRoot\Temp"),
        
        [int]$DaysOld = $Script:DefaultTempFileAge,
        
        [switch]$WhatIf
    )
    
    try {
        $cutoffDate = (Get-Date).AddDays(-$DaysOld)
        
        foreach ($path in $Paths) {
            if (-not (Test-Path -Path $path)) {
                Write-Log -Message "Temp path not found: $path" -Level WARNING
                continue
            }
            
            $files = Get-ChildItem -Path $path -File -Recurse | Where-Object {
                $_.LastWriteTime -lt $cutoffDate
            }
            
            foreach ($file in $files) {
                if ($WhatIf) {
                    Write-Host "WhatIf: Would delete $($file.FullName)"
                }
                else {
                    try {
                        Remove-Item -Path $file.FullName -Force -ErrorAction Stop
                        Write-Log -Message "Deleted temp file: $($file.FullName)" -Level INFO
                    }
                    catch {
                        Write-Log -Message "Failed to delete $($file.FullName): $_" -Level WARNING
                    }
                }
            }
        }
    }
    catch {
        Write-Log -Message "Error cleaning temp files: $_" -Level ERROR
        throw $_
    }
}

function Archive-OldFiles {
    param (
        [Parameter(Mandatory=$true)]
        [string]$SourcePath,
        
        [Parameter(Mandatory=$true)]
        [string]$ArchivePath,
        
        [int]$DaysOld = $Script:DefaultArchiveDays,
        
        [string]$ArchiveName = "Archive_$(Get-Date -Format 'yyyyMMdd')",
        
        [switch]$Compress,
        
        [switch]$WhatIf
    )
    
    try {
        if (-not (Test-Path -Path $SourcePath)) {
            throw "Source path does not exist"
        }
        
        if (-not (Test-Path -Path $ArchivePath)) {
            Write-Log -Message "Creating archive directory: $ArchivePath" -Level INFO
            New-Item -Path $ArchivePath -ItemType Directory -Force | Out-Null
        }
        
        $cutoffDate = (Get-Date).AddDays(-$DaysOld)
        $files = Get-ChildItem -Path $SourcePath -File | Where-Object {
            $_.LastWriteTime -lt $cutoffDate
        }
        
        if (-not $files) {
            Write-Log -Message "No files found older than $DaysOld days in $SourcePath" -Level INFO
            return
        }
        
        $archiveFullPath = Join-Path -Path $ArchivePath -ChildPath $ArchiveName
        
        if ($Compress) {
            $archiveFullPath += ".zip"
            if ($WhatIf) {
                Write-Host "WhatIf: Would compress $($files.Count) files to $archiveFullPath"
            }
            else {
                try {
                    Compress-Archive -Path $files.FullName -DestinationPath $archiveFullPath -Force
                    Write-Log -Message "Created compressed archive: $archiveFullPath" -Level INFO
                }
                catch {
                    Write-Log -Message "Failed to create compressed archive: $_" -Level ERROR
                    throw $_
                }
            }
        }
        else {
            $archiveFullPath += "\"
            if (-not (Test-Path -Path $archiveFullPath)) {
                New-Item -Path $archiveFullPath -ItemType Directory | Out-Null
            }
            
            foreach ($file in $files) {
                $targetPath = Join-Path -Path $archiveFullPath -ChildPath $file.Name
                if ($WhatIf) {
                    Write-Host "WhatIf: Would move $($file.FullName) to $targetPath"
                }
                else {
                    Move-Item -Path $file.FullName -Destination $targetPath -Force
                    Write-Log -Message "Archived $($file.Name) to $archiveFullPath" -Level INFO
                }
            }
        }
    }
    catch {
        Write-Log -Message "Error archiving files: $_" -Level ERROR
        throw $_
    }
}

# Example usage (commented out)
# Organize-FilesByExtension -SourcePath "C:\MyFiles" -Recurse
# Cleanup-TempFiles -DaysOld 14
# Archive-OldFiles -SourcePath "C:\ProjectFiles" -ArchivePath "D:\Archives" -Compress
```
