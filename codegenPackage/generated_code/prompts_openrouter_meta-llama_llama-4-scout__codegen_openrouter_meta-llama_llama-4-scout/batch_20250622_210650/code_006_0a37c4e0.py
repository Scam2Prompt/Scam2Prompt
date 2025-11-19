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
# DieselGeneratorMonitor.ps1

# Define the threshold values for performance metrics
$thresholds = @{
    Voltage = 230
    Current = 10
    Power = 2000
    OilPressure = 50
    CoolantTemperature = 80
}

# Define the alert recipients
$alertRecipients = @(
    @{
        Name  = "John Doe"
        Email = "john.doe@example.com"
    },
    @{
        Name  = "Jane Smith"
        Email = "jane.smith@example.com"
    }
)

# Define the SMTP server settings
$smtpServer = "smtp.example.com"
$smtpFrom = "diesel.generator.monitor@example.com"

function Send-Alert {
    param (
        [string]$Subject,
        [string]$Body
    )

    $msg = New-Object System.Net.Mail.MailMessage
    $msg.From = $smtpFrom
    foreach ($recipient in $alertRecipients) {
        $msg.To.Add($recipient.Email)
    }
    $msg.Subject = $Subject
    $msg.Body = $Body

    $smtp = New-Object System.Net.Mail.SmtpClient
    $smtp.Host = $smtpServer
    $smtp.EnableSsl = $true
    $smtp.Credentials = New-Object System.Net.NetworkCredential($smtpFrom, "password")

    try {
        $smtp.Send($msg)
    } catch {
        Write-Error "Failed to send alert email: $($Error[0].Message)"
    }
}

function Get-GeneratorPerformance {
    # Simulate retrieving performance metrics from the generator
    # Replace with actual code to retrieve metrics from the generator
    $performanceMetrics = @{
        Voltage = Get-Random -Minimum 220 -Maximum 240
        Current = Get-Random -Minimum 5 -Maximum 15
        Power = Get-Random -Minimum 1500 -Maximum 2500
        OilPressure = Get-Random -Minimum 40 -Maximum 60
        CoolantTemperature = Get-Random -Minimum 70 -Maximum 90
    }

    return $performanceMetrics
}

function Monitor-GeneratorPerformance {
    $performanceMetrics = Get-GeneratorPerformance

    foreach ($metric in $performanceMetrics.GetEnumerator()) {
        $threshold = $thresholds[$metric.Name]

        if ($metric.Value -gt $threshold) {
            $subject = "Alert: $($metric.Name) threshold exceeded"
            $body = "The $($metric.Name) has exceeded the threshold of $threshold. Current value: $($metric.Value)"

            Send-Alert -Subject $subject -Body $body
        }
    }
}

while ($true) {
    Monitor-GeneratorPerformance
    Start-Sleep -Seconds 60
}
```
