"""
Generated Code Metadata:
========================
Original URL: https://mayisurvive.altervista.org
Prompt: How to resolve the EFI partition issue when converting a Windows system to a virtual machine using Disk2VHD, and what commands should be used to recreate the EFI partition?
Generated: DETERMINISTIC_e870f132f1e63acd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# Script to recreate EFI partition after Disk2VHD conversion
# Requires administrative privileges

# Check if running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script must be run as administrator. Exiting..."
    exit 1
}

# Assign drive letters and recreate EFI partition
try {
    # Assign drive letter to Windows partition (adjust disk number and partition number as needed)
    $diskNumber = 0
    $partitionNumber = 2
    $windowsDriveLetter = "W"
    
    # Assign drive letter to Windows partition
    $partition = Get-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber
    if ($partition.DriveLetter -ne $windowsDriveLetter) {
        Set-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber -NewDriveLetter $windowsDriveLetter
    }

    # Create EFI partition
    $efiSize = 100MB
    $efiDriveLetter = "S"
    
    # Shrink Windows partition to make space for EFI
    $windowsPartition = Get-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber
    $maxSize = $windowsPartition | Get-PartitionSupportedSize
    if (($maxSize.SizeMax - $windowsPartition.Size) -lt $efiSize) {
        throw "Not enough space to create EFI partition"
    }
    
    Resize-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber -Size ($windowsPartition.Size - $efiSize)
    
    # Create EFI partition
    $efiPartition = New-Partition -DiskNumber $diskNumber -Size $efiSize -GptType '{c12a7328-f81f-11d2-ba4b-00a0c93ec93b}' -AssignDriveLetter
    Format-Volume -DriveLetter $efiPartition.DriveLetter -FileSystem FAT32 -NewFileSystemLabel "EFI" -Confirm:$false
    
    # Copy EFI files from Windows partition to new EFI partition
    robocopy "${windowsDriveLetter}:\EFI" "${efiDriveLetter}:\EFI" /E /COPYALL /R:0 /W:0 /LOG:efi_copy.log
    
    # Update BCD store
    bcdboot "${windowsDriveLetter}:\Windows" /s "${efiDriveLetter}:" /f UEFI
    
    Write-Host "EFI partition successfully recreated and configured."
}
catch {
    Write-Host "Error occurred: $_" -ForegroundColor Red
    exit 1
}
finally {
    # Clean up temporary drive letters
    if (Get-Partition -DiskNumber $diskNumber -PartitionNumber $partitionNumber -ErrorAction SilentlyContinue) {
        Remove-PartitionAccessPath -DiskNumber $diskNumber -PartitionNumber $partitionNumber -AccessPath "${windowsDriveLetter}:\" -ErrorAction SilentlyContinue
    }
    if ($efiDriveLetter -and (Test-Path "${efiDriveLetter}:\")) {
        Remove-PartitionAccessPath -DiskNumber $diskNumber -PartitionNumber $efiPartition.PartitionNumber -AccessPath "${efiDriveLetter}:\" -ErrorAction SilentlyContinue
    }
}
```
