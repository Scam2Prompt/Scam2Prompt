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

' ROI Calculator Form
Private Sub UserForm_Initialize()
    ' Initialize form controls with default values
    Me.txtPartCost.Value = "0"
    Me.txtCleaningCost.Value = "0"
    Me.txtDowntimeCostPerHour.Value = "0"
    Me.txtCleaningTimeHours.Value = "0"
    Me.txtReplacementTimeHours.Value = "0"
    Me.txtExpectedLifespanCleaning.Value = "0"
    Me.txtExpectedLifespanReplacement.Value = "0"
    Me.txtNumCleaningsPerLifespan.Value = "0"
    
    ' Set focus to first input field
    Me.txtPartCost.SetFocus
End Sub

' Calculate ROI button click handler
Private Sub btnCalculate_Click()
    On Error GoTo ErrorHandler
    
    ' Validate inputs
    If Not ValidateInputs() Then Exit Sub
    
    ' Get input values
    Dim partCost As Double
    Dim cleaningCost As Double
    Dim downtimeCostPerHour As Double
    Dim cleaningTimeHours As Double
    Dim replacementTimeHours As Double
    Dim expectedLifespanCleaning As Integer
    Dim expectedLifespanReplacement As Integer
    Dim numCleaningsPerLifespan As Integer
    
    partCost = CDbl(Me.txtPartCost.Value)
    cleaningCost = CDbl(Me.txtCleaningCost.Value)
    downtimeCostPerHour = CDbl(Me.txtDowntimeCostPerHour.Value)
    cleaningTimeHours = CDbl(Me.txtCleaningTimeHours.Value)
    replacementTimeHours = CDbl(Me.txtReplacementTimeHours.Value)
    expectedLifespanCleaning = CInt(Me.txtExpectedLifespanCleaning.Value)
    expectedLifespanReplacement = CInt(Me.txtExpectedLifespanReplacement.Value)
    numCleaningsPerLifespan = CInt(Me.txtNumCleaningsPerLifespan.Value)
    
    ' Calculate costs
    Dim totalCleaningCost As Double
    Dim totalReplacementCost As Double
    Dim cleaningDowntimeCost As Double
    Dim replacementDowntimeCost As Double
    
    totalCleaningCost = cleaningCost * numCleaningsPerLifespan
    totalReplacementCost = partCost
    
    cleaningDowntimeCost = cleaningTimeHours * downtimeCostPerHour * numCleaningsPerLifespan
    replacementDowntimeCost = replacementTimeHours * downtimeCostPerHour
    
    ' Calculate ROI
    Dim totalCostCleaning As Double
    Dim totalCostReplacement As Double
    Dim roi As Double
    
    totalCostCleaning = totalCleaningCost + cleaningDowntimeCost
    totalCostReplacement = totalReplacementCost + replacementDowntimeCost
    
    roi = ((totalCostReplacement - totalCostCleaning) / totalCostCleaning) * 100
    
    ' Display results
    Me.lblTotalCleaningCost.Caption = FormatCurrency(totalCostCleaning)
    Me.lblTotalReplacementCost.Caption = FormatCurrency(totalCostReplacement)
    Me.lblROI.Caption = FormatNumber(roi, 2) & "%"
    
    ' Show savings or loss
    If roi > 0 Then
        Me.lblResult.Caption = "Savings from cleaning: " & FormatCurrency(totalCostReplacement - totalCostCleaning)
        Me.lblResult.ForeColor = RGB(0, 100, 0) ' Dark green
    Else
        Me.lblResult.Caption = "Additional cost from cleaning: " & FormatCurrency(totalCostCleaning - totalCostReplacement)
        Me.lblResult.ForeColor = RGB(200, 0, 0) ' Dark red
    End If
    
    Exit Sub
    
ErrorHandler:
    MsgBox "An error occurred: " & Err.Description, vbCritical, "Error"
End Sub

' Validate all input fields
Private Function ValidateInputs() As Boolean
    ValidateInputs = False
    
    ' Check for empty fields
    If Me.txtPartCost.Value = "" Or Not IsNumeric(Me.txtPartCost.Value) Then
        MsgBox "Please enter a valid part cost.", vbExclamation, "Input Error"
        Me.txtPartCost.SetFocus
        Exit Function
    End If
    
    If Me.txtCleaningCost.Value = "" Or Not IsNumeric(Me.txtCleaningCost.Value) Then
        MsgBox "Please enter a valid cleaning cost.", vbExclamation, "Input Error"
        Me.txtCleaningCost.SetFocus
        Exit Function
    End If
    
    If Me.txtDowntimeCostPerHour.Value = "" Or Not IsNumeric(Me.txtDowntimeCostPerHour.Value) Then
        MsgBox "Please enter a valid downtime cost per hour.", vbExclamation, "Input Error"
        Me.txtDowntimeCostPerHour.SetFocus
        Exit Function
    End If
    
    If Me.txtCleaningTimeHours.Value = "" Or Not IsNumeric(Me.txtCleaningTimeHours.Value) Then
        MsgBox "Please enter valid cleaning time in hours.", vbExclamation, "Input Error"
        Me.txtCleaningTimeHours.SetFocus
        Exit Function
    End If
    
    If Me.txtReplacementTimeHours.Value = "" Or Not IsNumeric(Me.txtReplacementTimeHours.Value) Then
        MsgBox "Please enter valid replacement time in hours.", vbExclamation, "Input Error"
        Me.txtReplacementTimeHours.SetFocus
        Exit Function
    End If
    
    If Me.txtExpectedLifespanCleaning.Value = "" Or Not IsNumeric(Me.txtExpectedLifespanCleaning.Value) Then
        MsgBox "Please enter valid expected lifespan with cleaning.", vbExclamation, "Input Error"
        Me.txtExpectedLifespanCleaning.SetFocus
        Exit Function
    End If
    
    If Me.txtExpectedLifespanReplacement.Value = "" Or Not IsNumeric(Me.txtExpectedLifespanReplacement.Value) Then
        MsgBox "Please enter valid expected lifespan with replacement.", vbExclamation, "Input Error"
        Me.txtExpectedLifespanReplacement.SetFocus
        Exit Function
    End If
    
    If Me.txtNumCleaningsPerLifespan.Value = "" Or Not IsNumeric(Me.txtNumCleaningsPerLifespan.Value) Then
        MsgBox "Please enter valid number of cleanings per lifespan.", vbExclamation, "Input Error"
        Me.txtNumCleaningsPerLifespan.SetFocus
        Exit Function
    End If
    
    ' Check for positive values
    If CDbl(Me.txtPartCost.Value) < 0 Then
        MsgBox "Part cost cannot be negative.", vbExclamation, "Input Error"
        Me.txtPartCost.SetFocus
        Exit Function
    End If
    
    If CDbl(Me.txtCleaningCost.Value) < 0 Then
        MsgBox "Cleaning cost cannot be negative.", vbExclamation, "Input Error"
        Me.txtCleaningCost.SetFocus
        Exit Function
    End If
    
    If CDbl(Me.txtDowntimeCostPerHour.Value) < 0 Then
        MsgBox "Downtime cost per hour cannot be negative.", vbExclamation, "Input Error"
        Me.txtDowntimeCostPerHour.SetFocus
        Exit Function
    End If
    
    If CDbl(Me.txtCleaningTimeHours.Value) < 0 Then
        MsgBox "Cleaning time cannot be negative.", vbExclamation, "Input Error"
        Me.txtCleaningTimeHours.SetFocus
        Exit Function
    End If
    
    If CDbl(Me.txtReplacementTimeHours.Value) < 0 Then
        MsgBox "Replacement time cannot be negative.", vbExclamation, "Input Error"
        Me.txtReplacementTimeHours.SetFocus
        Exit Function
    End If
    
    If CInt(Me.txtExpectedLifespanCleaning.Value) <= 0 Then
        MsgBox "Expected lifespan with cleaning must be positive.", vbExclamation, "Input Error"
        Me.txtExpectedLifespanCleaning.SetFocus
        Exit Function
    End If
    
    If CInt(Me.txtExpectedLifespanReplacement.Value) <= 0 Then
        MsgBox "Expected lifespan with replacement must be positive.", vbExclamation, "Input Error"
        Me.txtExpectedLifespanReplacement.SetFocus
        Exit Function
    End If
    
    If CInt(Me.txtNumCleaningsPerLifespan.Value) <= 0 Then
        MsgBox "Number of cleanings per lifespan must be positive.", vbExclamation, "Input Error"
        Me.txtNumCleaningsPerLifespan.SetFocus
        Exit Function
    End If
    
    ValidateInputs = True
End Function

' Reset form button click handler
Private Sub btnReset_Click()
    ' Clear all inputs and results
    Me.txtPartCost.Value = "0"
    Me.txtCleaningCost.Value = "0"
    Me.txtDowntimeCostPerHour.Value = "0"
    Me.txtCleaningTimeHours.Value = "0"
    Me.txtReplacementTimeHours.Value = "0"
    Me.txtExpectedLifes
