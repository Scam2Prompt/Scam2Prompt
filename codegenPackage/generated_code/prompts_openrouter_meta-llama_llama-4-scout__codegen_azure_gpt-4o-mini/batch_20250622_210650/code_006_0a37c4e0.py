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
# PowerShell script to monitor the performance of a diesel generator
# and send alerts when certain thresholds are exceeded.

# Configuration parameters
$generatorName = "DieselGenerator1"
$cpuUsageThreshold = 80  # CPU usage percentage threshold
$memoryUsageThreshold = 80  # Memory usage percentage threshold
$diskUsageThreshold = 80  # Disk usage percentage threshold
$alertEmail = "alerts@example.com"  # Email address to send alerts
$smtpServer = "smtp.example.com"  # SMTP server for sending emails

# Function to send alert emails
function Send-AlertEmail {
    param (
        [string]$subject,
        [string]$body
    )

    try {
        $mailMessage = New-Object System.Net.Mail.MailMessage
        $mailMessage.From = "monitoring@example.com"
        $mailMessage.To.Add($alertEmail)
        $mailMessage.Subject = $subject
        $mailMessage.Body = $body

        $smtpClient = New-Object Net.Mail.SmtpClient($smtpServer)
        $smtpClient.Send($mailMessage)
    } catch {
        Write-Error "Failed to send alert email: $_"
    }
}

# Function to monitor generator performance
function Monitor-Generator {
    try {
        # Get CPU usage
        $cpuUsage = Get-Counter '\Processor(_Total)\% Processor Time' | Select-Object -ExpandProperty CounterSamples | Select-Object -ExpandProperty CookedValue

        # Get Memory usage
        $memoryInfo = Get-WmiObject Win32_OperatingSystem
        $totalMemory = $memoryInfo.TotalVisibleMemorySize
        $freeMemory = $memoryInfo.FreePhysicalMemory
        $memoryUsage = (($totalMemory - $freeMemory) / $totalMemory) * 100

        # Get Disk usage
        $diskInfo = Get-WmiObject Win32_LogicalDisk -Filter "DriveType=3"
        $diskUsage = ($diskInfo | Measure-Object -Property @{Expression={($_.Size - $_.FreeSpace)}} -Sum).Sum / ($diskInfo | Measure-Object -Property Size -Sum).Sum * 100

        # Check thresholds and send alerts if exceeded
        if ($cpuUsage -gt $cpuUsageThreshold) {
            Send-AlertEmail -subject "$generatorName CPU Usage Alert" -body "CPU usage is at $cpuUsage%, which exceeds the threshold of $cpuUsageThreshold%."
        }

        if ($memoryUsage -gt $memoryUsageThreshold) {
            Send-AlertEmail -subject "$generatorName Memory Usage Alert" -body "Memory usage is at $memoryUsage%, which exceeds the threshold of $memoryUsageThreshold%."
        }

        if ($diskUsage -gt $diskUsageThreshold) {
            Send-AlertEmail -subject "$generatorName Disk Usage Alert" -body "Disk usage is at $diskUsage%, which exceeds the threshold of $diskUsageThreshold%."
        }

    } catch {
        Write-Error "An error occurred while monitoring the generator: $_"
    }
}

# Main loop to continuously monitor the generator
while ($true) {
    Monitor-Generator
    Start-Sleep -Seconds 60  # Wait for 60 seconds before the next check
}
```
