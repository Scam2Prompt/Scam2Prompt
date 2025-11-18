"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boredturtleyc.netlify.app
Prompt: Write code to dynamically load JavaScript modules for a web app hosted on Netlify, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_3dc2960ee7eb3741
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ModuleLoader.js
/**
 * A dynamic module loader for JavaScript that loads ES6 modules on demand.
 * This loader is designed to work seamlessly with modern browsers.
 * 
 * Usage:
 * const module = await loadModule('./path/to/module.js');
 */

async function loadModule(modulePath) {
    try {
        // Check if the module path is a valid string
        if (typeof modulePath !== 'string' || !modulePath.trim()) {
            throw new Error('Invalid module path provided. Must be a non-empty string.');
        }

        // Dynamically import the module
        const module = await import(modulePath);

        // Ensure the module is loaded successfully
        if (!module) {
            throw new Error(`Failed to load module from path: ${modulePath}`);
        }

        // Return the loaded module
        return module;

    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error loading module:', error.message);
        throw error; // Re-throw the error for further handling if necessary
    }
}

// Example usage:
// (Uncomment the following lines to test the module loader)
// loadModule('./someModule.js')
//     .then(module => {
//         console.log('Module loaded successfully:', module);
//     })
//     .catch(err => {
//         console.error('Error during module loading:', err);
//     });

export { loadModule };
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Module Loader</title>
    <script type="module" src="app.js"></script>
</head>
<body>
    <h1>Dynamic Module Loader Example</h1>
    <button id="loadModuleBtn">Load Module</button>
    <div id="output"></div>
    
    <script type="module">
        import { loadModule } from './ModuleLoader.js';

        document.getElementById('loadModuleBtn').addEventListener('click', async () => {
            try {
                const module = await loadModule('./path/to/your/module.js');
                // You can call functions or access variables from the loaded module here
                console.log('Loaded module:', module);
                document.getElementById('output').innerText = 'Module loaded successfully!';
            } catch (error) {
                document.getElementById('output').innerText = `Error loading module: ${error.message}`;
            }
        });
    </script>
</body>
</html>
```

**Note**: Replace `./path/to/your/module.js` with the path to the actual module you wish to load dynamically.
