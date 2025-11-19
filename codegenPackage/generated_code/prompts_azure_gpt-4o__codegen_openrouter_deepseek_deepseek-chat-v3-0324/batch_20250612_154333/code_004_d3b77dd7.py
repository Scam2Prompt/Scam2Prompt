"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write code to integrate a label customization feature into a web application, allowing users to design labels for daycare, camps, or small businesses, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_d3b77dd749f8b3bc
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Label Customization Web Application

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Label Customization Tool</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .editor-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .controls {
            flex: 1;
            min-width: 300px;
        }
        .preview {
            flex: 1;
            min-width: 300px;
            border: 1px dashed #ccc;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 300px;
        }
        .label {
            width: 200px;
            height: 100px;
            padding: 10px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .color-picker {
            display: flex;
            align-items: center;
        }
        .color-picker input {
            width: 50px;
            margin-right: 10px;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Label Customization Tool</h1>
        
        <div class="editor-container">
            <div class="controls">
                <div class="form-group">
                    <label for="labelType">Label Type</label>
                    <select id="labelType">
                        <option value="daycare">Daycare</option>
                        <option value="camp">Camp</option>
                        <option value="business">Small Business</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="labelText">Label Text</label>
                    <textarea id="labelText" rows="3" placeholder="Enter text for your label"></textarea>
                    <div id="textError" class="error"></div>
                </div>
                
                <div class="form-group">
                    <label for="fontFamily">Font</label>
                    <select id="fontFamily">
                        <option value="Arial">Arial</option>
                        <option value="Times New Roman">Times New Roman</option>
                        <option value="Courier New">Courier New</option>
                        <option value="Comic Sans MS">Comic Sans MS</option>
                        <option value="Verdana">Verdana</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="fontSize">Font Size</label>
                    <input type="number" id="fontSize" min="8" max="72" value="14">
                </div>
                
                <div class="form-group">
                    <label>Text Color</label>
                    <div class="color-picker">
                        <input type="color" id="textColor" value="#000000">
                        <span id="textColorValue">#000000</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>Background Color</label>
                    <div class="color-picker">
                        <input type="color" id="bgColor" value="#ffffff">
                        <span id="bgColorValue">#ffffff</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="borderStyle">Border Style</label>
                    <select id="borderStyle">
                        <option value="none">None</option>
                        <option value="solid">Solid</option>
                        <option value="dashed">Dashed</option>
                        <option value="dotted">Dotted</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="borderColor">Border Color</label>
                    <div class="color-picker">
                        <input type="color" id="borderColor" value="#000000">
                        <span id="borderColorValue">#000000</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="borderWidth">Border Width</label>
                    <input type="number" id="borderWidth" min="0" max="10" value="1">
                </div>
                
                <div class="form-group">
                    <label for="labelShape">Shape</label>
                    <select id="labelShape">
                        <option value="rectangle">Rectangle</option>
                        <option value="rounded">Rounded</option>
                        <option value="circle">Circle</option>
                    </select>
                </div>
                
                <button id="previewBtn">Update Preview</button>
                <button id="saveBtn">Save Design</button>
                <button id="resetBtn">Reset</button>
            </div>
            
            <div class="preview">
                <div class="label" id="labelPreview">
                    Sample Label Text
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // DOM elements
            const labelPreview = document.getElementById('labelPreview');
            const labelText = document.getElementById('labelText');
            const fontFamily = document.getElementById('fontFamily');
            const fontSize = document.getElementById('fontSize');
            const textColor = document.getElementById('textColor');
            const textColorValue = document.getElementById('textColorValue');
            const bgColor = document.getElementById('bgColor');
            const bgColorValue = document.getElementById('bgColorValue');
            const borderStyle = document.getElementById('borderStyle');
            const borderColor = document.getElementById('borderColor');
            const borderColorValue = document.getElementById('borderColorValue');
            const borderWidth = document.getElementById('borderWidth');
            const labelShape = document.getElementById('labelShape');
            const previewBtn = document.getElementById('previewBtn');
            const saveBtn = document.getElementById('saveBtn');
            const resetBtn = document.getElementById('resetBtn');
            const textError = document.getElementById('textError');
            
            // Color picker event listeners
            textColor.addEventListener('input', function() {
                textColorValue.textContent = this.value;
            });
            
            bgColor.addEventListener('input', function() {
                bgColorValue.textContent = this.value;
            });
            
            borderColor.addEventListener('input', function() {
                borderColorValue.textContent = this.value;
            });
            
            // Update preview
            function updatePreview() {
                // Validate input
                if (labelText.value.trim() === '') {
                    textError.textContent = 'Label text cannot be empty';
                    return;
                }
                textError.textContent = '';
                
                // Update label text
                labelPreview.textContent = labelText.value;
                
                // Update styles
                labelPreview.style.fontFamily = fontFamily.value;
                labelPreview.style.fontSize = fontSize.value + 'px';
                labelPreview.style.color = textColor.value;
                labelPreview.style.backgroundColor = bgColor.value;
                labelPreview.style.borderStyle = borderStyle.value;
                labelPreview.style.borderColor = borderColor.value;
                labelPreview.style.borderWidth = borderWidth.value + 'px';
                
                // Update shape
                if (labelShape.value === 'rounded') {
                    labelPreview.style.borderRadius = '10px';
                } else if (labelShape.value === 'circle') {
                    labelPreview.style.borderRadius = '50%';
                } else {
                    labelPreview.style.borderRadius = '0';
                }
            }
            
            // Save design
            function saveDesign() {
                updatePreview();
                
                // In a real application, this would save to a database or generate a file
                // For this demo, we'll just show an alert
                alert
