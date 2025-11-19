"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Write a script in PowerShell to monitor the performance of a diesel generator and send alerts when certain thresholds are exceeded."
Generated: DETERMINISTIC_0a37c4e0ed6dcb40
Batch ID: 20250622_210650
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
    Monitors diesel generator performance and sends alerts when thresholds are exceeded.
.DESCRIPTION
    This script monitors key performance metrics of a diesel generator and sends email alerts
    when specified thresholds are exceeded. Metrics include voltage, frequency, temperature,
    and oil pressure.
.PARAMETER ConfigFile
    Path to the JSON configuration file containing monitoring parameters and alert settings.
.NOTES
    File Name      : Monitor-DieselGenerator.ps1
    Prerequisite   : PowerShell 5.1 or later
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$ConfigFile
)

# Error handling setup
$ErrorActionPreference = "Stop"

try {
    # Load configuration
    $config = Get-Content -Path $ConfigFile -Raw | ConvertFrom-Json

    # Validate configuration
    if (-not $config.Thresholds -or -not $config.AlertSettings) {
        throw "Invalid configuration file. Missing required sections."
    }

    # Generator monitoring function
    function Get-GeneratorMetrics {
        param (
            [string]$GeneratorName
        )

        # Simulate getting metrics from actual monitoring system
        # In production, this would connect to the generator's monitoring interface
        $metrics = @{
            Voltage = [math]::Round((Get-Random -Minimum 200 -Maximum 250), 2)
            Frequency = [math]::Round((Get-Random -Minimum 55 -Maximum 65), 2)
            Temperature = [math]::Round((Get-Random -Minimum 70 -Maximum 120), 2)
            OilPressure = [math]::Round((Get-Random -Minimum 30 -Maximum 80), 2)
            Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            GeneratorName = $GeneratorName
        }

        return $metrics
    }

    # Check thresholds function
    function Test-Thresholds {
        param (
            [hashtable]$Metrics,
            [object]$Thresholds
        )

        $alerts = @()

        if ($Metrics.Voltage -lt $Thresholds.MinVoltage -or $Metrics.Voltage -gt $Thresholds.MaxVoltage) {
            $alerts += "Voltage out of range: $($Metrics.Voltage)V (Range: $($Thresholds.MinVoltage)V-$($Thresholds.MaxVoltage)V)"
        }

        if ($Metrics.Frequency -lt $Thresholds.MinFrequency -or $Metrics.Frequency -gt $Thresholds.MaxFrequency) {
            $alerts += "Frequency out of range: $($Metrics.Frequency)Hz (Range: $($Thresholds.MinFrequency)Hz-$($Thresholds.MaxFrequency)Hz)"
        }

        if ($Metrics.Temperature -gt $Thresholds.MaxTemperature) {
            $alerts += "High temperature: $($Metrics.Temperature)°C (Max: $($Thresholds.MaxTemperature)°C)"
        }

        if ($Metrics.OilPressure -lt $Thresholds.MinOilPressure) {
            $alerts += "Low oil pressure: $($Metrics.OilPressure)psi (Min: $($Thresholds.MinOilPressure)psi)"
        }

        return $alerts
    }

    # Send alert function
    function Send-Alert {
        param (
            [string[]]$Alerts,
            [string]$GeneratorName,
            [object]$AlertSettings
        )

        $subject = "[CRITICAL] Generator Alert: $GeneratorName"
        $body = @"
Generator Name: $GeneratorName
Timestamp: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

ALERTS:
$($Alerts -join "`n")

Please investigate immediately.
"@

        try {
            Send-MailMessage `
                -From $AlertSettings.FromEmail `
                -To $AlertSettings.ToEmail `
                -Subject $subject `
                -Body $body `
                -SmtpServer $AlertSettings.SmtpServer `
                -Port $AlertSettings.SmtpPort `
                -Credential (New-Object System.Management.Automation.PSCredential ($AlertSettings.SmtpUsername, (ConvertTo-SecureString $AlertSettings.SmtpPassword -AsPlainText -Force))) `
                -UseSsl
        }
        catch {
            Write-Error "Failed to send alert email: $_"
        }
    }

    # Main monitoring loop
    while ($true) {
        try {
            $metrics = Get-GeneratorMetrics -GeneratorName $config.GeneratorName
            $alerts = Test-Thresholds -Metrics $metrics -Thresholds $config.Thresholds

            if ($alerts.Count -gt 0) {
                Send-Alert -Alerts $alerts -GeneratorName $config.GeneratorName -AlertSettings $config.AlertSettings
            }

            # Log metrics
            $logEntry = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Generator: $($metrics.GeneratorName) | " +
                        "Voltage: $($metrics.Voltage)V | " +
                        "Frequency: $($metrics.Frequency)Hz | " +
                        "Temperature: $($metrics.Temperature)°C | " +
                        "OilPressure: $($metrics.OilPressure)psi"
            
            Write-Output $logEntry

            # Wait for next reading
            Start-Sleep -Seconds $config.PollingIntervalSeconds
        }
        catch {
            Write-Error "Monitoring error: $_"
            Start-Sleep -Seconds 60
        }
    }
}
catch {
    Write-Error "Script initialization failed: $_"
    exit 1
}
```
