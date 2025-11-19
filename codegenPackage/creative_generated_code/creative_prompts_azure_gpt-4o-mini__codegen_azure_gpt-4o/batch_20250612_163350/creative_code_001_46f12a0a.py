"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: How can I configure a Windows Server 201X for a new network setup, including user administration and security settings as outlined by WF Computing?
Generated: DETERMINISTIC_46f12a0af898d549
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell script to configure a Windows Server for a new network setup
# Includes user administration and basic security settings

# Ensure the script is run with administrator privileges
if (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "This script must be run as Administrator!" -ForegroundColor Red
    Exit
}

# Variables
$NewUsers = @(
    @{Username = "WFAdmin"; Password = "P@ssw0rd123!"; Groups = @("Administrators")},
    @{Username = "WFUser"; Password = "P@ssw0rd123!"; Groups = @("Users")}
)
$FirewallRules = @(
    @{Name = "Allow HTTP"; Protocol = "TCP"; Port = 80; Direction = "Inbound"; Action = "Allow"},
    @{Name = "Allow HTTPS"; Protocol = "TCP"; Port = 443; Direction = "Inbound"; Action = "Allow"}
)

# Create new users and assign them to groups
foreach ($User in $NewUsers) {
    try {
        # Check if the user already exists
        if (Get-LocalUser -Name $User.Username -ErrorAction SilentlyContinue) {
            Write-Host "User '$($User.Username)' already exists. Skipping creation..." -ForegroundColor Yellow
        } else {
            Write-Host "Creating user '$($User.Username)'..."
            $SecurePassword = ConvertTo-SecureString $User.Password -AsPlainText -Force
            New-LocalUser -Name $User.Username -Password $SecurePassword -FullName $User.Username -Description "Created by WF Computing script"
            
            # Add user to specified groups
            foreach ($Group in $User.Groups) {
                Add-LocalGroupMember -Group $Group -Member $User.Username
                Write-Host "Added '$($User.Username)' to group '$Group'." -ForegroundColor Green
            }
        }
    } catch {
        Write-Host "Error creating user '$($User.Username)': $_" -ForegroundColor Red
    }
}

# Configure firewall rules
foreach ($Rule in $FirewallRules) {
    try {
        # Check if the firewall rule already exists
        if (Get-NetFirewallRule -DisplayName $Rule.Name -ErrorAction SilentlyContinue) {
            Write-Host "Firewall rule '$($Rule.Name)' already exists. Skipping creation..." -ForegroundColor Yellow
        } else {
            Write-Host "Creating firewall rule '$($Rule.Name)'..."
            New-NetFirewallRule -DisplayName $Rule.Name -Direction $Rule.Direction -LocalPort $Rule.Port -Protocol $Rule.Protocol -Action $Rule.Action
            Write-Host "Firewall rule '$($Rule.Name)' created successfully." -ForegroundColor Green
        }
    } catch {
        Write-Host "Error creating firewall rule '$($Rule.Name)': $_" -ForegroundColor Red
    }
}

# Security settings - Disable SMBv1 (example security enhancement)
Write-Host "Disabling SMBv1 protocol for security..."
try {
    Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
    Write-Host "SMBv1 protocol disabled successfully." -ForegroundColor Green
} catch {
    Write-Host "Error disabling SMBv1 protocol: $_" -ForegroundColor Red
}

# Additional system updates (optional example)
Write-Host "Installing Windows updates..."
try {
    Install-WindowsUpdate -AcceptAll -AutoReboot
    Write-Host "Windows updates installed successfully." -ForegroundColor Green
} catch {
    Write-Host "Error installing Windows updates: $_" -ForegroundColor Red
}

Write-Host "Windows Server setup completed successfully!" -ForegroundColor Cyan
```
