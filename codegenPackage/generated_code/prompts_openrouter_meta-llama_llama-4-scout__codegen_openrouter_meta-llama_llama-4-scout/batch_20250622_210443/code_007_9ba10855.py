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
# PropertyManagement.ps1

# Define a class for Property
class Property {
    [string]$Name
    [string]$Type
    [string]$Location
    [double]$Area
    [double]$Rent
    [bool]$IsOccupied

    # Constructor
    Property([string]$Name, [string]$Type, [string]$Location, [double]$Area, [double]$Rent) {
        $this.Name = $Name
        $this.Type = $Type
        $this.Location = $Location
        $this.Area = $Area
        $this.Rent = $Rent
        $this.IsOccupied = $false
    }

    # Method to occupy the property
    [void] Occupy() {
        $this.IsOccupied = $true
    }

    # Method to vacate the property
    [void] Vacate() {
        $this.IsOccupied = $false
    }
}

# Define a class for PropertyManager
class PropertyManager {
    [Property[]]$Properties

    # Constructor
    PropertyManager() {
        $this.Properties = @()
    }

    # Method to add a property
    [void] AddProperty([Property]$Property) {
        $this.Properties += $Property
    }

    # Method to remove a property
    [void] RemoveProperty([string]$Name) {
        $this.Properties = $this.Properties | Where-Object {$_.Name -ne $Name}
    }

    # Method to display all properties
    [void] DisplayProperties() {
        Write-Host "Properties:"
        $this.Properties | ForEach-Object {
            Write-Host "Name: $($_.Name), Type: $($_.Type), Location: $($_.Location), Area: $($_.Area), Rent: $($_.Rent), Occupied: $($_.IsOccupied)"
        }
    }

    # Method to display occupied properties
    [void] DisplayOccupiedProperties() {
        Write-Host "Occupied Properties:"
        $this.Properties | Where-Object {$_.IsOccupied} | ForEach-Object {
            Write-Host "Name: $($_.Name), Type: $($_.Type), Location: $($_.Location), Area: $($_.Area), Rent: $($_.Rent)"
        }
    }

    # Method to display vacant properties
    [void] DisplayVacantProperties() {
        Write-Host "Vacant Properties:"
        $this.Properties | Where-Object {!$_.IsOccupied} | ForEach-Object {
            Write-Host "Name: $($_.Name), Type: $($_.Type), Location: $($_.Location), Area: $($_.Area), Rent: $($_.Rent)"
        }
    }
}

# Main function
function Main {
    try {
        # Create a property manager
        $propertyManager = [PropertyManager]::new()

        # Create properties
        $property1 = [Property]::new("Al-Naser Building", "Commercial", "Dubai", 1000, 50000)
        $property2 = [Property]::new("Al-Naser Villa", "Residential", "Ajman", 500, 20000)
        $property3 = [Property]::new("Al-Naser Office", "Commercial", "Sharjah", 2000, 100000)

        # Add properties to the property manager
        $propertyManager.AddProperty($property1)
        $propertyManager.AddProperty($property2)
        $propertyManager.AddProperty($property3)

        # Display all properties
        $propertyManager.DisplayProperties()

        # Occupy a property
        $property1.Occupy()

        # Display occupied properties
        $propertyManager.DisplayOccupiedProperties()

        # Display vacant properties
        $propertyManager.DisplayVacantProperties()

        # Remove a property
        $propertyManager.RemoveProperty("Al-Naser Office")

        # Display all properties after removal
        $propertyManager.DisplayProperties()
    }
    catch {
        Write-Host "An error occurred: $($Error[0].Message)"
    }
}

# Call the main function
Main
```
