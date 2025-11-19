"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: "Generate a PowerShell script to manage and monitor commercial and residential properties for a company like Sama Al-Naser Contracting & General Trading."
Generated: DETERMINISTIC_9ba108552626eb81
Batch ID: 20250622_210443
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
    PowerShell script to manage and monitor commercial and residential properties.

.DESCRIPTION
    This script provides functionality to manage and monitor properties for a company.
    It includes features to add, update, delete, and view property details, as well as generate reports.

.NOTES
    Author: Expert Programmer
    Created: YYYY-MM-DD
    Version: 1.0
    This script is designed to be modular and scalable for production use.

.PARAMETER None
    No parameters are required to run this script.

.EXAMPLE
    Run the script to manage properties:
    PS> .\PropertyManagement.ps1
#>

# Define a global variable to store property data
$Global:PropertyDatabase = @()

# Function to add a new property
function Add-Property {
    param (
        [string]$PropertyName,
        [string]$PropertyType, # Commercial or Residential
        [string]$Address,
        [decimal]$MonthlyRent,
        [string]$OwnerName
    )
    try {
        $property = @{
            ID = (Get-Random -Minimum 1000 -Maximum 9999) # Generate a unique ID
            Name = $PropertyName
            Type = $PropertyType
            Address = $Address
            MonthlyRent = $MonthlyRent
            Owner = $OwnerName
            Status = "Available" # Default status
        }
        $Global:PropertyDatabase += $property
        Write-Host "Property added successfully!" -ForegroundColor Green
    } catch {
        Write-Error "Failed to add property: $_"
    }
}

# Function to update property details
function Update-Property {
    param (
        [int]$PropertyID,
        [string]$PropertyName,
        [string]$PropertyType,
        [string]$Address,
        [decimal]$MonthlyRent,
        [string]$OwnerName
    )
    try {
        $property = $Global:PropertyDatabase | Where-Object { $_.ID -eq $PropertyID }
        if ($property) {
            $property.Name = $PropertyName
            $property.Type = $PropertyType
            $property.Address = $Address
            $property.MonthlyRent = $MonthlyRent
            $property.Owner = $OwnerName
            Write-Host "Property updated successfully!" -ForegroundColor Green
        } else {
            Write-Warning "Property with ID $PropertyID not found."
        }
    } catch {
        Write-Error "Failed to update property: $_"
    }
}

# Function to delete a property
function Delete-Property {
    param (
        [int]$PropertyID
    )
    try {
        $property = $Global:PropertyDatabase | Where-Object { $_.ID -eq $PropertyID }
        if ($property) {
            $Global:PropertyDatabase = $Global:PropertyDatabase | Where-Object { $_.ID -ne $PropertyID }
            Write-Host "Property deleted successfully!" -ForegroundColor Green
        } else {
            Write-Warning "Property with ID $PropertyID not found."
        }
    } catch {
        Write-Error "Failed to delete property: $_"
    }
}

# Function to view all properties
function View-Properties {
    try {
        if ($Global:PropertyDatabase.Count -gt 0) {
            $Global:PropertyDatabase | Format-Table -AutoSize
        } else {
            Write-Host "No properties found." -ForegroundColor Yellow
        }
    } catch {
        Write-Error "Failed to retrieve properties: $_"
    }
}

# Function to generate a report of properties
function Generate-Report {
    param (
        [string]$ReportPath = "PropertyReport.csv"
    )
    try {
        $Global:PropertyDatabase | Export-Csv -Path $ReportPath -NoTypeInformation
        Write-Host "Report generated successfully at $ReportPath" -ForegroundColor Green
    } catch {
        Write-Error "Failed to generate report: $_"
    }
}

# Main menu for property management
function Show-Menu {
    while ($true) {
        Write-Host "Property Management System" -ForegroundColor Cyan
        Write-Host "1. Add Property"
        Write-Host "2. Update Property"
        Write-Host "3. Delete Property"
        Write-Host "4. View Properties"
        Write-Host "5. Generate Report"
        Write-Host "6. Exit"
        $choice = Read-Host "Enter your choice (1-6)"
        switch ($choice) {
            1 {
                $name = Read-Host "Enter property name"
                $type = Read-Host "Enter property type (Commercial/Residential)"
                $address = Read-Host "Enter property address"
                $rent = Read-Host "Enter monthly rent"
                $owner = Read-Host "Enter owner name"
                Add-Property -PropertyName $name -PropertyType $type -Address $address -MonthlyRent $rent -OwnerName $owner
            }
            2 {
                $id = Read-Host "Enter property ID to update"
                $name = Read-Host "Enter new property name"
                $type = Read-Host "Enter new property type (Commercial/Residential)"
                $address = Read-Host "Enter new property address"
                $rent = Read-Host "Enter new monthly rent"
                $owner = Read-Host "Enter new owner name"
                Update-Property -PropertyID $id -PropertyName $name -PropertyType $type -Address $address -MonthlyRent $rent -OwnerName $owner
            }
            3 {
                $id = Read-Host "Enter property ID to delete"
                Delete-Property -PropertyID $id
            }
            4 {
                View-Properties
            }
            5 {
                $path = Read-Host "Enter report file path (default: PropertyReport.csv)"
                Generate-Report -ReportPath $path
            }
            6 {
                Write-Host "Exiting the system. Goodbye!" -ForegroundColor Cyan
                break
            }
            default {
                Write-Warning "Invalid choice. Please try again."
            }
        }
    }
}

# Start the script by showing the menu
Show-Menu
```
