"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Provide a Python or PowerShell script to set up remote access and control for electronic security systems, such as cameras and alarms, as mentioned in WF Computing's security services.
Generated: DETERMINISTIC_a106ce689d2fdd18
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Remote Access and Control Script for Electronic Security Systems**
===========================================================

**Python Script**
---------------

```python
import paramiko
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecuritySystem:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
            logger.info(f"Connected to {self.hostname}")
        except paramiko.AuthenticationException:
            logger.error("Authentication failed")
            return False
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            return False
        return True

    def disconnect(self):
        self.ssh_client.close()
        logger.info(f"Disconnected from {self.hostname}")

    def execute_command(self, command):
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                logger.error(f"Error executing command: {error}")
            return output
        except Exception as e:
            logger.error(f"Error executing command: {e}")
            return None

def main():
    # Define security system devices
    devices = [
        {"hostname": "camera1", "username": "admin", "password": "password"},
        {"hostname": "alarm1", "username": "admin", "password": "password"}
    ]

    for device in devices:
        security_system = SecuritySystem(device["hostname"], device["username"], device["password"])
        if security_system.connect():
            # Execute commands to set up remote access and control
            commands = [
                "sudo systemctl start camera-streaming",
                "sudo systemctl enable alarm-monitoring"
            ]
            for command in commands:
                output = security_system.execute_command(command)
                logger.info(f"Executed command: {command}")
                logger.info(f"Output: {output}")
            security_system.disconnect()

if __name__ == "__main__":
    main()
```

**PowerShell Script**
-------------------

```powershell
#Requires -Version 3

param (
    [string[]]$DeviceHostnames,
    [string]$Username,
    [string]$Password
)

# Set up logging
$logFile = "remote_access.log"
$logStream = [System.IO.StreamWriter]::new($logFile, $true)
$logStream.AutoFlush = $true

function Connect-Device {
    param (
        [string]$Hostname,
        [string]$Username,
        [string]$Password
    )

    try {
        $session = New-PSSession -ComputerName $Hostname -Credential (New-Object System.Management.Automation.PSCredential ($Username, (ConvertTo-SecureString $Password -AsPlainText -Force)))
        Write-Output $session
    } catch {
        $logStream.WriteLine("Connection failed: $($Error[0].Message)")
    }
}

function Execute-Command {
    param (
        [string]$Command,
        [object]$Session
    )

    try {
        $output = Invoke-Command -Session $Session -ScriptBlock { param($cmd) & $cmd } -ArgumentList $Command
        Write-Output $output
    } catch {
        $logStream.WriteLine("Error executing command: $($Error[0].Message)")
    }
}

function main {
    # Define security system devices
    $devices = @(
        @{Hostname = "camera1"; Username = "admin"; Password = "password"},
        @{Hostname = "alarm1"; Username = "admin"; Password = "password"}
    )

    foreach ($device in $devices) {
        $session = Connect-Device -Hostname $device.Hostname -Username $device.Username -Password $device.Password
        if ($session) {
            # Execute commands to set up remote access and control
            $commands = @(
                "sudo systemctl start camera-streaming",
                "sudo systemctl enable alarm-monitoring"
            )
            foreach ($command in $commands) {
                $output = Execute-Command -Command $command -Session $session
                $logStream.WriteLine("Executed command: $command")
                $logStream.WriteLine("Output: $output")
            }
            Remove-PSSession -Session $session
        }
    }
}

main
```
