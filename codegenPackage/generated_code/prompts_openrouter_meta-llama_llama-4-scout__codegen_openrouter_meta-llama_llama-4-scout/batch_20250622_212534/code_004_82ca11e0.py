"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Develop a simple calculator in Excel VBA to determine the return on investment (ROI) for using ultrasonic cleaning services versus replacing industrial parts, considering factors like part cost, cleaning cost, and downtime."
Generated: DETERMINISTIC_82ca11e0f78cdea9
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' Define a custom error for invalid input
Private Const INVALID_INPUT_ERROR As String = "Invalid input. Please ensure all values are positive numbers."

' Function to calculate ROI for using ultrasonic cleaning services
Function CalculateUltrasonicROIPartCost(partCost As Double, cleaningCost As Double, downtimeCost As Double) As Double
    ' Validate input values
    If partCost <= 0 Or cleaningCost < 0 Or downtimeCost < 0 Then
        Err.Raise vbObjectError + 1, "InvalidInput", INVALID_INPUT_ERROR
    End If
    
    ' Calculate ROI for ultrasonic cleaning
    Dim ultrasonicROICost As Double
    ultrasonicROICost = cleaningCost + downtimeCost
    
    ' Return the ROI
    CalculateUltrasonicROIPartCost = ultrasonicROICost / partCost
End Function

' Function to calculate ROI for replacing industrial parts
Function CalculateReplacementROIPartCost(partCost As Double) As Double
    ' Validate input value
    If partCost <= 0 Then
        Err.Raise vbObjectError + 2, "InvalidInput", INVALID_INPUT_ERROR
    End If
    
    ' Since replacement has no additional costs considered, ROI is simply 1 (or 100%)
    CalculateReplacementROIPartCost = 1
End Function

' Function to compare ultrasonic cleaning ROI with replacement ROI
Sub CompareROIs()
    On Error GoTo ErrorHandler
    
    ' Input values
    Dim partCost As Double
    partCost = InputBox("Enter the part cost", "Part Cost", 0)
    
    Dim cleaningCost As Double
    cleaningCost = InputBox("Enter the ultrasonic cleaning cost", "Cleaning Cost", 0)
    
    Dim downtimeCost As Double
    downtimeCost = InputBox("Enter the downtime cost", "Downtime Cost", 0)
    
    ' Calculate ROIs
    Dim ultrasonicROI As Double
    ultrasonicROI = CalculateUltrasonicROIPartCost(partCost, cleaningCost, downtimeCost)
    
    Dim replacementROI As Double
    replacementROI = CalculateReplacementROIPartCost(partCost)
    
    ' Display results
    MsgBox "Ultrasonic Cleaning ROI: " & Format(ultrasonicROI, "0.00") & vbCrLf & _
           "Replacement ROI: " & Format(replacementROI, "0.00"), vbInformation, "ROI Comparison"
    
    Exit Sub
ErrorHandler:
    MsgBox Err.Description, vbCritical, "Error"
End Sub
```
