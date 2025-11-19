"""
Generated Code Metadata:
========================
Original URL: https://card.xumicloud.top
Prompt: Write code to create a customizable navigation page similar to "须弥の导航页," including features for adding private links, managing categories, and adjusting settings.
Generated: DETERMINISTIC_464168204171b626
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>自定义导航页</title>
    <style>
        :root {
            --primary-color: #3498db;
            --secondary-color: #2980b9;
            --background-color: #f5f5f5;
            --card-color: #ffffff;
            --text-color: #333333;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--background-color);
            color: var(--text-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        .search-box {
            width: 60%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
            margin: 0 auto;
            font-size: 16px;
        }

        .categories {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 30px;
        }

        .category {
            flex: 1;
            min-width: 300px;
            background-color: var(--card-color);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 15px;
        }

        .category-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--primary-color);
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }

        .links {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
        }

        .link-item {
            padding: 8px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }

        .link-item:hover {
            background-color: #f0f0f0;
        }

        .link-item a {
            text-decoration: none;
            color: var(--text-color);
            display: flex;
            align-items: center;
        }

        .link-item img {
            width: 16px;
            height: 16px;
            margin-right: 8px;
        }

        .settings-panel {
            position: fixed;
            top: 0;
            right: -300px;
            width: 300px;
            height: 100vh;
            background-color: var(--card-color);
            box-shadow: var(--shadow);
            transition: right 0.3s;
            padding: 20px;
            z-index: 1000;
            overflow-y: auto;
        }

        .settings-panel.active {
            right: 0;
        }

        .settings-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 20px;
            cursor: pointer;
            z-index: 1001;
            box-shadow: var(--shadow);
        }

        .settings-toggle:hover {
            background-color: var(--secondary-color);
        }

        .settings-section {
            margin-bottom: 20px;
        }

        .settings-title {
            font-weight: bold;
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .btn:hover {
            background-color: var(--secondary-color);
        }

        .btn-danger {
            background-color: #e74c3c;
        }

        .btn-danger:hover {
            background-color: #c0392b;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1002;
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background-color: var(--card-color);
            padding: 20px;
            border-radius: 8px;
            width: 80%;
            max-width: 500px;
        }

        .modal-title {
            font-size: 20px;
            margin-bottom: 15px;
            color: var(--primary-color);
        }

        .modal-footer {
            text-align: right;
            margin-top: 20px;
        }

        .drag-handle {
            cursor: move;
            margin-right: 8px;
        }

        .sortable-ghost {
            opacity: 0.5;
            background: #c8ebfb;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1 id="page-title">自定义导航页</h1>
            <input type="text" class="search-box" placeholder="搜索...">
        </header>

        <div id="categories-container" class="categories">
            <!-- Categories will be loaded here -->
        </div>
    </div>

    <button class="settings-toggle" id="settings-toggle">⚙️</button>

    <div class="settings-panel" id="settings-panel">
        <div class="settings-section">
            <div class="settings-title">页面设置</div>
            <div class="form-group">
                <label for="page-title-input">页面标题</label>
                <input type="text" id="page-title-input" placeholder="输入页面标题">
            </div>
            <div class="form-group">
                <label for="theme-select">主题颜色</label>
                <select id="theme-select">
                    <option value="default">默认</option>
                    <option value="dark">暗色</option>
                    <option value="light">亮色</option>
                </select>
            </div>
            <button class="btn" id="save-page-settings">保存设置</button>
        </div>

        <div class="settings-section">
            <div class="settings-title">分类管理</div>
            <div class="form-group">
                <label for="new-category-name">新分类名称</label>
                <input type="text" id="new-category-name" placeholder="输入分类名称">
            </div>
            <button class="btn" id="add-category-btn">添加分类</button>
            
            <div id="categories-list" style="margin-top: 15px;">
                <!-- Categories list will be loaded here -->
            </div>
        </div>

        <div class="settings-section">
            <div class="settings-title">链接管理</div>
            <div class="form-group">
                <label for="link-category-select">选择分类</label>
                <select id="link-category-select">
                    <!-- Options will be populated by JavaScript -->
                </select>
            </div>
            <div class="form-group">
                <label for="link-name">链接名称</label>
                <input type="text" id="link-name" placeholder="输入链接名称">
            </div>
            <div class="form-group">
                <label for="link-url">链接URL</label>
                <input type="text" id="link-url" placeholder="输入链接URL">
            </div>
            <div class="form-group">
                <label for="link-icon">图标URL (可选)</label>
                <input type="text" id="link-icon" placeholder="输入图标URL">
            </div>
            <button class="btn" id="add-link-btn">添加链接</button>
        </div>

        <div class="settings-section">
            <div class="settings-title">数据管理</div>
            <button class="btn" id="export-data-btn">导出数据</button>
            <button class="btn" id="import-data-btn">导入数据</button>
            <button class="btn btn-danger" id="reset-data-btn">重置数据</button>
        </div>
    </div>

    <!-- Add Category Modal -->
    <
