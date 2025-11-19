"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Generate code to customize the editor functionality in GitBook documentation, based on the features described in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_451f01b0d4ddbcca
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GitBook Editor Customization Script
// Based on Polymarket GitBook starter template features

(function() {
    'use strict';

    // Configuration object for editor customization
    const editorConfig = {
        // Enable/disable features
        features: {
            emoji: true,
            mentions: true,
            advancedTables: true,
            codeBlockLanguages: ['javascript', 'python', 'solidity', 'json'],
            customBlocks: ['warning', 'info', 'tip'],
            spellcheck: true
        },
        // UI customization
        ui: {
            theme: 'light', // 'light' or 'dark'
            fontSize: 14,
            lineHeight: 1.6,
            showLineNumbers: true
        },
        // Keyboard shortcuts
        shortcuts: {
            bold: 'Cmd-B',
            italic: 'Cmd-I',
            code: 'Cmd-K',
            save: 'Cmd-S'
        }
    };

    // Initialize GitBook editor with custom configuration
    function initEditor() {
        if (typeof gitbook === 'undefined' || !gitbook.editor) {
            console.error('GitBook editor not found');
            return;
        }

        try {
            const editor = gitbook.editor.getEditor();
            
            // Apply configuration
            if (editorConfig.features) {
                // Enable/disable features
                editor.setOption('emoji', editorConfig.features.emoji);
                editor.setOption('mentions', editorConfig.features.mentions);
                editor.setOption('advancedTables', editorConfig.features.advancedTables);
                
                if (editorConfig.features.codeBlockLanguages) {
                    editor.setOption('codeBlockLanguages', editorConfig.features.codeBlockLanguages);
                }
                
                if (editorConfig.features.customBlocks) {
                    editor.setOption('customBlocks', editorConfig.features.customBlocks);
                }
                
                editor.setOption('spellcheck', editorConfig.features.spellcheck);
            }

            // Apply UI settings
            if (editorConfig.ui) {
                editor.setOption('theme', editorConfig.ui.theme);
                editor.setOption('fontSize', editorConfig.ui.fontSize);
                editor.setOption('lineHeight', editorConfig.ui.lineHeight);
                editor.setOption('lineNumbers', editorConfig.ui.showLineNumbers);
            }

            // Apply keyboard shortcuts
            if (editorConfig.shortcuts) {
                editor.setOption('keyboardShortcuts', editorConfig.shortcuts);
            }

            // Add custom toolbar buttons
            addCustomToolbarButtons(editor);

            console.log('GitBook editor customized successfully');
        } catch (error) {
            console.error('Error customizing GitBook editor:', error);
        }
    }

    // Add custom toolbar buttons
    function addCustomToolbarButtons(editor) {
        if (!editor || !editor.toolbar) return;

        // Add custom block buttons
        editor.toolbar.addButton({
            icon: 'fa-exclamation-triangle',
            label: 'Warning',
            action: function() {
                editor.insertBlock('warning');
            }
        });

        editor.toolbar.addButton({
            icon: 'fa-info-circle',
            label: 'Info',
            action: function() {
                editor.insertBlock('info');
            }
        });

        editor.toolbar.addButton({
            icon: 'fa-lightbulb',
            label: 'Tip',
            action: function() {
                editor.insertBlock('tip');
            }
        });

        // Add custom format button
        editor.toolbar.addButton({
            icon: 'fa-code',
            label: 'Code Block',
            action: function() {
                editor.insertCodeBlock();
            }
        });
    }

    // Wait for GitBook to be ready
    if (typeof gitbook !== 'undefined') {
        gitbook.events.on('start', function() {
            initEditor();
        });
    } else {
        document.addEventListener('gitbook:ready', initEditor);
    }
})();
```
