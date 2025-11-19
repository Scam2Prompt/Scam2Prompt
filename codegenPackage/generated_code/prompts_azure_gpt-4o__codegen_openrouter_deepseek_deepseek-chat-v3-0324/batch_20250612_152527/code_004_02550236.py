"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write VBA code for Microsoft Visio to automate the alignment and distribution of objects in patent drawings, inspired by the "Mastering Alignment and Distribution in Patent Drawings" course.
Generated: DETERMINISTIC_025502365237d0d8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

' Module: PatentDrawingAlignment
' Purpose: Automates alignment and distribution of objects in Visio patent drawings
' Author: AI Assistant
' Date: [Current Date]

' Constants for alignment and distribution options
Private Const ALIGN_LEFT As Integer = 0
Private Const ALIGN_CENTER As Integer = 1
Private Const ALIGN_RIGHT As Integer = 2
Private Const ALIGN_TOP As Integer = 3
Private Const ALIGN_MIDDLE As Integer = 4
Private Const ALIGN_BOTTOM As Integer = 5

Private Const DISTRIBUTE_HORIZONTAL As Integer = 0
Private Const DISTRIBUTE_VERTICAL As Integer = 1
Private Const DISTRIBUTE_CENTER_HORIZONTAL As Integer = 2
Private Const DISTRIBUTE_CENTER_VERTICAL As Integer = 3

' Main function to align selected shapes
Public Sub AlignShapes(alignmentType As Integer)
    On Error GoTo ErrorHandler
    
    Dim vsoSelection As Visio.Selection
    Dim vsoPage As Visio.Page
    Dim vsoShape As Visio.Shape
    Dim referenceShape As Visio.Shape
    Dim referenceValue As Double
    Dim i As Integer
    
    ' Check if we have a document and selection
    If Visio.ActiveDocument Is Nothing Then
        MsgBox "No active document found.", vbExclamation
        Exit Sub
    End If
    
    Set vsoPage = Visio.ActivePage
    Set vsoSelection = Visio.ActiveWindow.Selection
    
    ' Validate selection
    If vsoSelection.Count < 2 Then
        MsgBox "Please select at least two shapes to align.", vbExclamation
        Exit Sub
    End If
    
    ' Get reference shape (first selected shape)
    Set referenceShape = vsoSelection(1)
    
    ' Determine reference value based on alignment type
    Select Case alignmentType
        Case ALIGN_LEFT
            referenceValue = referenceShape.Cells("PinX").Result("in")
        Case ALIGN_CENTER
            referenceValue = referenceShape.Cells("LocPinX").Result("in") + referenceShape.Cells("PinX").Result("in")
        Case ALIGN_RIGHT
            referenceValue = referenceShape.Cells("Width").Result("in") + referenceShape.Cells("PinX").Result("in")
        Case ALIGN_TOP
            referenceValue = referenceShape.Cells("Height").Result("in") + referenceShape.Cells("PinY").Result("in")
        Case ALIGN_MIDDLE
            referenceValue = referenceShape.Cells("LocPinY").Result("in") + referenceShape.Cells("PinY").Result("in")
        Case ALIGN_BOTTOM
            referenceValue = referenceShape.Cells("PinY").Result("in")
        Case Else
            MsgBox "Invalid alignment type.", vbExclamation
            Exit Sub
    End Select
    
    ' Apply alignment to all selected shapes except reference shape
    For i = 2 To vsoSelection.Count
        Set vsoShape = vsoSelection(i)
        
        Select Case alignmentType
            Case ALIGN_LEFT, ALIGN_CENTER, ALIGN_RIGHT
                vsoShape.Cells("PinX").Result("in") = referenceValue - IIf(alignmentType = ALIGN_CENTER, vsoShape.Cells("LocPinX").Result("in"), 0)
            Case ALIGN_TOP, ALIGN_MIDDLE, ALIGN_BOTTOM
                vsoShape.Cells("PinY").Result("in") = referenceValue - IIf(alignmentType = ALIGN_MIDDLE, vsoShape.Cells("LocPinY").Result("in"), 0)
        End Select
    Next i
    
    Exit Sub
    
ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub

' Main function to distribute selected shapes
Public Sub DistributeShapes(distributionType As Integer)
    On Error GoTo ErrorHandler
    
    Dim vsoSelection As Visio.Selection
    Dim vsoPage As Visio.Page
    Dim vsoShapes() As Visio.Shape
    Dim i As Integer, j As Integer
    Dim minValue As Double, maxValue As Double
    Dim totalSpace As Double, spacing As Double
    Dim currentPosition As Double
    Dim shapeValues() As Double
    Dim sortedIndices() As Integer
    
    ' Check if we have a document and selection
    If Visio.ActiveDocument Is Nothing Then
        MsgBox "No active document found.", vbExclamation
        Exit Sub
    End If
    
    Set vsoPage = Visio.ActivePage
    Set vsoSelection = Visio.ActiveWindow.Selection
    
    ' Validate selection
    If vsoSelection.Count < 3 Then
        MsgBox "Please select at least three shapes to distribute.", vbExclamation
        Exit Sub
    End If
    
    ' Store shapes in array for easier processing
    ReDim vsoShapes(1 To vsoSelection.Count)
    ReDim shapeValues(1 To vsoSelection.Count)
    ReDim sortedIndices(1 To vsoSelection.Count)
    
    For i = 1 To vsoSelection.Count
        Set vsoShapes(i) = vsoSelection(i)
        sortedIndices(i) = i
        
        ' Calculate shape position based on distribution type
        Select Case distributionType
            Case DISTRIBUTE_HORIZONTAL
                shapeValues(i) = vsoShapes(i).Cells("PinX").Result("in")
            Case DISTRIBUTE_VERTICAL
                shapeValues(i) = vsoShapes(i).Cells("PinY").Result("in")
            Case DISTRIBUTE_CENTER_HORIZONTAL
                shapeValues(i) = vsoShapes(i).Cells("PinX").Result("in") + vsoShapes(i).Cells("LocPinX").Result("in")
            Case DISTRIBUTE_CENTER_VERTICAL
                shapeValues(i) = vsoShapes(i).Cells("PinY").Result("in") + vsoShapes(i).Cells("LocPinY").Result("in")
            Case Else
                MsgBox "Invalid distribution type.", vbExclamation
                Exit Sub
        End Select
    Next i
    
    ' Sort shapes based on their position (bubble sort for simplicity)
    For i = 1 To vsoSelection.Count - 1
        For j = i + 1 To vsoSelection.Count
            If shapeValues(sortedIndices(i)) > shapeValues(sortedIndices(j)) Then
                Dim temp As Integer
                temp = sortedIndices(i)
                sortedIndices(i) = sortedIndices(j)
                sortedIndices(j) = temp
            End If
        Next j
    Next i
    
    ' Calculate min and max values
    minValue = shapeValues(sortedIndices(1))
    maxValue = shapeValues(sortedIndices(vsoSelection.Count))
    
    ' Calculate total space needed
    Select Case distributionType
        Case DISTRIBUTE_HORIZONTAL, DISTRIBUTE_CENTER_HORIZONTAL
            totalSpace = 0
            For i = 1 To vsoSelection.Count
                totalSpace = totalSpace + vsoShapes(sortedIndices(i)).Cells("Width").Result("in")
            Next i
        Case DISTRIBUTE_VERTICAL, DISTRIBUTE_CENTER_VERTICAL
            totalSpace = 0
            For i = 1 To vsoSelection.Count
                totalSpace = totalSpace + vsoShapes(sortedIndices(i)).Cells("Height").Result("in")
            Next i
    End Select
    
    ' Calculate spacing between shapes
    spacing = (maxValue - minValue - totalSpace) / (vsoSelection.Count - 1)
    
    ' Position shapes with equal spacing
    currentPosition = minValue
    For i = 1 To vsoSelection.Count
        Select Case distributionType
            Case DISTRIBUTE_HORIZONTAL
                vsoShapes(sortedIndices(i)).Cells("PinX").Result("in") = currentPosition
                currentPosition = currentPosition + vsoShapes(sortedIndices(i)).Cells("Width").Result("in") + spacing
            Case DISTRIBUTE_VERTICAL
                vsoShapes(sortedIndices(i)).Cells("PinY").Result("in") = currentPosition
                currentPosition = currentPosition + vsoShapes(sortedIndices(i)).Cells("Height").Result("in") + spacing
            Case DISTRIBUTE_CENTER_HORIZONTAL
                vsoShapes(sortedIndices(i)).Cells("PinX").Result("in") = currentPosition - vsoShapes(sortedIndices(i)).Cells("LocPinX").Result("in")
                currentPosition = currentPosition + vsoShapes(sortedIndices(i)).Cells("Width").Result("in") + spacing
            Case DISTRIBUTE_CENTER_VERTICAL
                vsoShapes(sortedIndices(i)).Cells("PinY").Result("in") = currentPosition - vsoShapes(sortedIndices(i)).Cells("LocPinY").Result("in")
                currentPosition = currentPosition + vso
