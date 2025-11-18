"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write VBA code for Microsoft Visio to automate the alignment and distribution of objects in patent drawings, inspired by the "Mastering Alignment and Distribution in Patent Drawings" course.
Generated: DETERMINISTIC_025502365237d0d8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vba
' VBA Code to Automate Alignment and Distribution of Objects in Microsoft Visio
' This code aligns and distributes selected shapes in a Visio drawing based on user input

Option Explicit

Sub AlignAndDistributeShapes()
    Dim visApp As Visio.Application
    Dim visDoc As Visio.Document
    Dim visPage As Visio.Page
    Dim visSelection As Visio.Selection
    Dim userChoice As Integer
    
    ' Set references to the Visio application, active document, and page
    Set visApp = Application
    Set visDoc = visApp.ActiveDocument
    Set visPage = visApp.ActivePage
    Set visSelection = visApp.ActiveWindow.Selection
    
    ' Check if there are shapes selected
    If visSelection.Count < 2 Then
        MsgBox "Please select at least two shapes to align and distribute.", vbExclamation, "Error"
        Exit Sub
    End If
    
    ' Prompt user for alignment and distribution options
    userChoice = MsgBox("Choose an operation:" & vbCrLf & _
                        "Yes = Align Shapes" & vbCrLf & _
                        "No = Distribute Shapes" & vbCrLf & _
                        "Cancel = Exit", vbYesNoCancel + vbQuestion, "Align and Distribute Shapes")
    
    Select Case userChoice
        Case vbYes
            AlignShapes visSelection
        Case vbNo
            DistributeShapes visSelection
        Case vbCancel
            ' Exit the procedure
            Exit Sub
        Case Else
            MsgBox "Invalid choice. Please try again.", vbExclamation, "Error"
            Exit Sub
    End Select
End Sub

Sub AlignShapes(visSelection As Visio.Selection)
    Dim i As Integer
    Dim targetShape As Visio.Shape
    Dim xPos As Double, yPos As Double
    
    ' Prompt user for alignment direction
    Dim alignDirection As Integer
    alignDirection = MsgBox("Do you want to align shapes vertically (Yes) or horizontally (No)?", vbYesNoCancel + vbQuestion, "Align Shapes")
    
    If alignDirection = vbCancel Then Exit Sub
    
    ' Use the first shape as the target for alignment
    Set targetShape = visSelection.Item(1)
    xPos = targetShape.Cells("PinX").Result("inches")
    yPos = targetShape.Cells("PinY").Result("inches")
    
    ' Align shapes based on user's choice
    For i = 2 To visSelection.Count
        With visSelection.Item(i)
            If alignDirection = vbYes Then
                ' Align vertically: Set X position to match target shape
                .Cells("PinX").Result("inches") = xPos
            Else
                ' Align horizontally: Set Y position to match target shape
                .Cells("PinY").Result("inches") = yPos
            End If
        End With
    Next i
    
    MsgBox "Shapes successfully aligned.", vbInformation, "Success"
End Sub

Sub DistributeShapes(visSelection As Visio.Selection)
    Dim i As Integer
    Dim totalWidth As Double, totalHeight As Double
    Dim spacing As Double
    
    ' Prompt user for distribution type
    Dim distributeType As Integer
    distributeType = MsgBox("Do you want to distribute shapes horizontally (Yes) or vertically (No)?", vbYesNoCancel + vbQuestion, "Distribute Shapes")
    
    If distributeType = vbCancel Then Exit Sub
    
    ' Calculate total space based on bounding box of shapes
    totalWidth = visSelection(visSelection.Count).Cells("PinX").Result("inches") - visSelection(1).Cells("PinX").Result("inches")
