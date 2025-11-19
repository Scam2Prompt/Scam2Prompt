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
Sub AlignAndDistributeShapes()
    ' This macro automates the alignment and distribution of shapes in a Visio document.
    ' It aligns selected shapes to the left and distributes them evenly vertically.

    Dim vsoSelection As Visio.Selection
    Dim vsoPage As Visio.Page
    Dim vsoShape As Visio.Shape
    Dim shapeCount As Integer
    Dim i As Integer
    Dim leftMost As Double
    Dim rightMost As Double
    Dim totalHeight As Double
    Dim spacing As Double
    Dim currentTop As Double

    ' Get the active page
    Set vsoPage = ActivePage

    ' Get the current selection
    Set vsoSelection = vsoPage.Selection

    ' Check if any shapes are selected
    If vsoSelection.Count = 0 Then
        MsgBox "Please select at least one shape to align and distribute.", vbExclamation
        Exit Sub
    End If

    ' Initialize variables for alignment
    leftMost = vsoSelection(1).Cells("PinX").Result("inches")
    rightMost = leftMost
    totalHeight = 0

    ' Loop through selected shapes to find the leftmost, rightmost, and total height
    For i = 1 To vsoSelection.Count
        Set vsoShape = vsoSelection(i)
        If vsoShape.Cells("PinX").Result("inches") < leftMost Then
            leftMost = vsoShape.Cells("PinX").Result("inches")
        End If
        If vsoShape.Cells("PinX").Result("inches") > rightMost Then
            rightMost = vsoShape.Cells("PinX").Result("inches")
        End If
        totalHeight = totalHeight + vsoShape.Cells("Height").Result("inches")
    Next i

    ' Calculate spacing based on the number of shapes
    spacing = (vsoSelection.Count - 1) * 0.5 ' 0.5 inches spacing between shapes
    totalHeight = totalHeight + spacing

    ' Align shapes to the leftmost position
    For i = 1 To vsoSelection.Count
        Set vsoShape = vsoSelection(i)
        vsoShape.Cells("PinX").FormulaU = leftMost
    Next i

    ' Distribute shapes evenly
    currentTop = (vsoPage.PageSheet.Cells("PageHeight").Result("inches") - totalHeight) / 2

    For i = 1 To vsoSelection.Count
        Set vsoShape = vsoSelection(i)
        vsoShape.Cells("PinY").FormulaU = currentTop
        currentTop = currentTop + vsoShape.Cells("Height").Result("inches") + 0.5 ' Add height and spacing
    Next i

    ' Notify user of completion
    MsgBox "Shapes have been aligned and distributed successfully.", vbInformation
End Sub
```
