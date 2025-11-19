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
# Script to monitor the performance of a diesel generator and send alerts when thresholds are exceeded.
# Author: [Your Name]
# Date: [Insert Date]
# Version: 1.0

# Define thresholds for alerts
$temperatureThreshold = 90   # Maximum temperature in Celsius
$oilPressureThreshold = 20   # Minimum oil pressure in PSI
$rpmThreshold = 3000         # Maximum RPM

# Define email settings for alerts
$emailFrom = "alerts@generator-monitor.com"
$emailTo = "admin@generator-monitor.com"
$smtpServer = "smtp.generator-monitor.com"
$smtpPort = 587

# Function to send an email alert
function Send-AlertEmail {
    param (
        [string]$subject,
        [string]$body
    )
    try {
        Send-MailMessage -From $emailFrom -To $emailTo -Subject $subject -Body $body -SmtpServer $smtpServer -Port $smtpPort -UseSsl
        Write-Host "Alert email sent successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to send alert email: $_" -ForegroundColor Red
    }
}

# Function to simulate fetching generator performance data
function Get-GeneratorPerformance {
    # Simulated data (replace with actual data fetching logic)
    return @{
        Temperature = Get-Random -Minimum 70 -Maximum 100
        OilPressure = Get-Random -Minimum 10 -Maximum 30
        RPM = Get-Random -Minimum 2500 -Maximum 3500
    }
}

# Main monitoring loop
Write-Host "Starting diesel generator performance monitoring..." -ForegroundColor Cyan
while ($true) {
    try {
        # Fetch generator performance data
        $performanceData = Get-GeneratorPerformance

        # Log performance data
        Write-Host "Performance Data: Temperature=$($performanceData.Temperature)°C, OilPressure=$($performanceData.OilPressure) PSI, RPM=$($performanceData.RPM)" -ForegroundColor Yellow

        # Check thresholds and send alerts if necessary
        if ($performanceData.Temperature -gt $temperatureThreshold) {
            Send-AlertEmail -subject "Generator Alert: High Temperature" -body "The generator temperature has exceeded the threshold of $temperatureThreshold°C. Current temperature: $($performanceData.Temperature)°C."
        }
        if ($performanceData.OilPressure -lt $oilPressureThreshold) {
            Send-AlertEmail -subject "Generator Alert: Low Oil Pressure" -body "The generator oil pressure has dropped below the threshold of $oilPressureThreshold PSI. Current oil pressure: $($performanceData.OilPressure) PSI."
        }
        if ($performanceData.RPM -gt $rpmThreshold) {
            Send-AlertEmail -subject "Generator Alert: High RPM" -body "The generator RPM has exceeded the threshold of $rpmThreshold. Current RPM: $($performanceData.RPM)."
        }

        # Wait for a specified interval before the next check
        Start-Sleep -Seconds 60
    } catch {
        Write-Host "An error occurred during monitoring: $_" -ForegroundColor Red
    }
}
```
