"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Generate a Figma plugin that organizes components, layers, and frames following the best practices mentioned in NasheKrashe Design Studio's Figma community work.
Generated: DETERMINISTIC_c7159b8a9b28c494
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma Plugin: Component Organizer
// Follows NasheKrashe Design Studio's best practices for organizing components, layers, and frames

// Main plugin code
figma.showUI(__html__, { width: 400, height: 600 });

// Listen for messages from the UI
figma.ui.onmessage = async (msg) => {
  try {
    switch (msg.type) {
      case 'organize-components':
        await organizeComponents();
        break;
      case 'organize-layers':
        await organizeLayers();
        break;
      case 'organize-frames':
        await organizeFrames();
        break;
      case 'cancel':
        figma.closePlugin();
        break;
      default:
        throw new Error(`Unknown message type: ${msg.type}`);
    }
  } catch (error) {
    figma.notify(`Error: ${error.message}`);
    figma.closePlugin();
  }
};

// Organize components according to best practices
async function organizeComponents() {
  const components = figma.currentPage.findAll(node => node.type === 'COMPONENT');
  
  if (components.length === 0) {
    figma.notify('No components found on this page');
    return;
  }

  // Create components frame if it doesn't exist
  let componentsFrame = figma.currentPage.findOne(node => 
    node.type === 'FRAME' && node.name === '⚡️ Components'
  );

  if (!componentsFrame) {
    componentsFrame = figma.createFrame();
    componentsFrame.name = '⚡️ Components';
    componentsFrame.x = 0;
    componentsFrame.y = 0;
    componentsFrame.fills = [];
    figma.currentPage.appendChild(componentsFrame);
  }

  // Move all components to the components frame
  for (const component of components) {
    if (component.parent !== componentsFrame) {
      componentsFrame.appendChild(component);
    }
  }

  // Group similar components
  const componentGroups = {};
  for (const component of components) {
    const baseName = component.name.split('/')[0];
    if (!componentGroups[baseName]) {
      componentGroups[baseName] = [];
    }
    componentGroups[baseName].push(component);
  }

  // Create frames for each component group
  let yOffset = 0;
  for (const [groupName, groupComponents] of Object.entries(componentGroups)) {
    let groupFrame = componentsFrame.findOne(node => 
      node.type === 'FRAME' && node.name === groupName
    );

    if (!groupFrame) {
      groupFrame = figma.createFrame();
      groupFrame.name = groupName;
      groupFrame.fills = [];
      componentsFrame.appendChild(groupFrame);
    }

    groupFrame.x = 0;
    groupFrame.y = yOffset;

    // Position components in a grid within the group frame
    let xOffset = 0;
    let rowHeight = 0;
    const padding = 32;
    const maxRowWidth = 1000;

    for (const component of groupComponents) {
      if (component.parent !== groupFrame) {
        groupFrame.appendChild(component);
      }

      if (xOffset + component.width > maxRowWidth) {
        xOffset = 0;
        yOffset += rowHeight + padding;
        rowHeight = 0;
      }

      component.x = xOffset;
      component.y = yOffset;
      xOffset += component.width + padding;
      rowHeight = Math.max(rowHeight, component.height);
    }

    yOffset += rowHeight + padding;
    groupFrame.resize(groupFrame.width, yOffset);
  }

  figma.notify(`Organized ${components.length} components`);
}

// Organize layers within frames
async function organizeLayers() {
  const frames = figma.currentPage.findAll(node => 
    node.type === 'FRAME' || node.type === 'COMPONENT'
  );

  if (frames.length === 0) {
    figma.notify('No frames found on this page');
    return;
  }

  let totalLayersOrganized = 0;

  for (const frame of frames) {
    // Skip empty frames
    if (frame.children.length === 0) continue;

    // Sort layers by type and name
    const sortedChildren = [...frame.children].sort((a, b) => {
      // Group by type first
      const typeOrder = {
        'GROUP': 0,
        'FRAME': 1,
        'COMPONENT': 2,
        'INSTANCE': 3,
        'RECTANGLE': 4,
        'ELLIPSE': 5,
        'POLYGON': 6,
        'STAR': 7,
        'VECTOR': 8,
        'LINE': 9,
        'TEXT': 10
      };

      const aOrder = typeOrder[a.type] || 99;
      const bOrder = typeOrder[b.type] || 99;

      if (aOrder !== bOrder) return aOrder - bOrder;
      
      // Then sort alphabetically
      return a.name.localeCompare(b.name);
    });

    // Position layers vertically with padding
    const padding = 16;
    let yOffset = 0;

    for (const child of sortedChildren) {
      child.y = yOffset;
      yOffset += child.height + padding;
      totalLayersOrganized++;
    }
  }

  figma.notify(`Organized layers in ${frames.length} frames`);
}

// Organize frames on the page
async function organizeFrames() {
  const frames = figma.currentPage.findAll(node => 
    node.type === 'FRAME' && node.parent === figma.currentPage
  );

  if (frames.length === 0) {
    figma.notify('No top-level frames found on this page');
    return;
  }

  // Sort frames by name
  frames.sort((a, b) => a.name.localeCompare(b.name));

  // Position frames in a vertical stack with padding
  const padding = 64;
  let yOffset = 0;

  for (const frame of frames) {
    frame.x = 0;
    frame.y = yOffset;
    yOffset += frame.height + padding;
  }

  figma.notify(`Organized ${frames.length} frames`);
}

// HTML for the plugin UI
const __html__ = `
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
      padding: 16px;
      color: #333;
    }
    h1 {
      font-size: 18px;
      margin: 0 0 16px 0;
    }
    button {
      background: #18A0FB;
      color: white;
      border: none;
      border-radius: 4px;
      padding: 10px 16px;
      font-size: 14px;
      cursor: pointer;
      width: 100%;
      margin-bottom: 12px;
      transition: background 0.2s;
    }
    button:hover {
      background: #0D8BD9;
    }
    button.secondary {
      background: #F0F0F0;
      color: #333;
    }
    button.secondary:hover {
      background: #E0E0E0;
    }
    .section {
      margin-bottom: 24px;
      padding-bottom: 24px;
      border-bottom: 1px solid #E5E5E5;
    }
    .section-title {
      font-weight: 600;
      margin-bottom: 12px;
    }
    .description {
      font-size: 13px;
      color: #666;
      margin-bottom: 16px;
      line-height: 1.4;
    }
  </style>
</head>
<body>
  <h1>Design Organizer</h1>
  
  <div class="section">
    <div class="section-title">Components</div>
    <div class="description">
      Organizes all components into a structured hierarchy following NasheKrashe best practices.
    </div>
    <button id="organize-components">Organize Components</button>
  </div>
  
  <div class="section">
    <div class="section-title">Layers</div>
    <div class="description">
      Sorts and arranges layers within frames by type and name for better readability.
    </div>
    <button id="organize-layers">Organize Layers</button>
  </div>
  
  <div class="section">
    <div class="section-title">Frames</div>
    <div class="description">
      Arranges top-level frames in a vertical stack sorted alphabetically.
    </div>
    <button id="organize-frames">Organize Frames</button>
  </div>
  
  <button id="cancel" class="secondary">Close Plugin</button>

  <script>
    document.getElementById('organize-components').addEventListener('click', () => {
      parent.postMessage({ pluginMessage: { type: 'organize-components' } }, '*');
    });
    
    document.getElementById('organize-layers').addEventListener('click', () => {
      parent.postMessage({ pluginMessage: { type: 'organ
