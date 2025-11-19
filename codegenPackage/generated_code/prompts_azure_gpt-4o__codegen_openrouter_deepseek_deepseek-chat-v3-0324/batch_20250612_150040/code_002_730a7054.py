"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Generate code for designing a multimedia-rich webpage that includes photo and video editing features, inspired by Fantom Internet Dienst's multimedia services.
Generated: DETERMINISTIC_730a7054d6d9b10a
Batch ID: 20250612_150040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fantom Multimedia Editor</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #4a6bff;
            --secondary-color: #ff6b6b;
            --dark-color: #2c3e50;
            --light-color: #f8f9fa;
            --success-color: #28a745;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f7fa;
            color: var(--dark-color);
        }

        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo img {
            height: 40px;
        }

        .logo h1 {
            font-size: 1.5rem;
            color: var(--primary-color);
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
        }

        nav a {
            text-decoration: none;
            color: var(--dark-color);
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--primary-color);
        }

        .main-container {
            display: flex;
            min-height: calc(100vh - 80px);
        }

        .sidebar {
            width: 250px;
            background-color: white;
            padding: 1.5rem;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
        }

        .sidebar h3 {
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        .tool-group {
            margin-bottom: 1.5rem;
        }

        .tool-btn {
            display: block;
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 0.5rem;
            background: none;
            border: none;
            text-align: left;
            cursor: pointer;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        .tool-btn:hover {
            background-color: rgba(74, 107, 255, 0.1);
        }

        .tool-btn i {
            margin-right: 8px;
            color: var(--primary-color);
        }

        .content-area {
            flex: 1;
            padding: 2rem;
            display: flex;
            flex-direction: column;
        }

        .workspace {
            flex: 1;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.05);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
        }

        .toolbar {
            display: flex;
            gap: 10px;
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #eee;
        }

        .toolbar-btn {
            padding: 0.5rem 1rem;
            background-color: var(--light-color);
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .toolbar-btn:hover {
            background-color: #e9ecef;
        }

        .toolbar-btn.active {
            background-color: var(--primary-color);
            color: white;
        }

        .canvas-container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f8f9fa;
            border-radius: 4px;
            position: relative;
            overflow: hidden;
        }

        #media-canvas {
            max-width: 100%;
            max-height: 100%;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }

        .media-controls {
            margin-top: 1rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
        }

        .control-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: var(--primary-color);
            color: white;
            border: none;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: transform 0.2s;
        }

        .control-btn:hover {
            transform: scale(1.1);
        }

        .media-timeline {
            width: 100%;
            height: 4px;
            background-color: #ddd;
            margin-top: 1rem;
            border-radius: 2px;
            position: relative;
            cursor: pointer;
        }

        .progress {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background-color: var(--primary-color);
            border-radius: 2px;
            width: 0%;
        }

        .file-input {
            display: none;
        }

        .upload-btn {
            padding: 0.75rem 1.5rem;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        .upload-btn:hover {
            background-color: #3a5bef;
        }

        .action-buttons {
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
            margin-top: 1rem;
        }

        .save-btn {
            padding: 0.75rem 1.5rem;
            background-color: var(--success-color);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        .save-btn:hover {
            background-color: #218838;
        }

        .cancel-btn {
            padding: 0.75rem 1.5rem;
            background-color: #6c757d;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        .cancel-btn:hover {
            background-color: #5a6268;
        }

        .adjustment-panel {
            margin-top: 1rem;
            padding: 1rem;
            background-color: #f8f9fa;
            border-radius: 4px;
            display: none;
        }

        .adjustment-panel.active {
            display: block;
        }

        .slider-container {
            margin-bottom: 1rem;
        }

        .slider-container label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .slider {
            width: 100%;
            height: 4px;
            -webkit-appearance: none;
            background: #ddd;
            outline: none;
            border-radius: 2px;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 16px;
            height: 16px;
            background: var(--primary-color);
            border-radius: 50%;
            cursor: pointer;
        }

        .filter-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .filter-item {
            cursor: pointer;
            text-align: center;
        }

        .filter-preview {
            width: 80px;
            height: 80px;
            border-radius: 4px;
            background-color: #eee;
            margin-bottom: 0.5rem;
            overflow: hidden;
        }

        .filter-name {
            font-size: 0.8rem;
        }

        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
            }

            .sidebar {
                width: 100%;
                padding: 1rem;
            }

            .content-area {
                padding: 1rem;
            }
        }
    </style>
</head>
