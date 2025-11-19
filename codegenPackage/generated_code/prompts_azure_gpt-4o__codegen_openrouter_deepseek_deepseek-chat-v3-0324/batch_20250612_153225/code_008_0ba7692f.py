"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Create a branding and logo design workflow in Figma that aligns with the practices described in NasheKrashe Design Studio's logo creation process.
Generated: DETERMINISTIC_0ba7692f69968938
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma Plugin: Branding and Logo Design Workflow
// Aligned with NasheKrashe Design Studio's process

// Main plugin code
figma.showUI(__html__, { width: 400, height: 600 });

// Listen for messages from the UI
figma.ui.onmessage = async (msg) => {
  try {
    switch (msg.type) {
      case 'CREATE_BRAND_BOARD':
        await createBrandBoard(msg.data);
        break;
      case 'GENERATE_LOGO_CONCEPTS':
        await generateLogoConcepts(msg.data);
        break;
      case 'REFINE_LOGO':
        await refineLogo(msg.data);
        break;
      case 'CREATE_STYLE_GUIDE':
        await createStyleGuide(msg.data);
        break;
      case 'EXPORT_ASSETS':
        await exportAssets(msg.data);
        break;
      default:
        throw new Error('Unknown command');
    }
  } catch (error) {
    figma.notify(`Error: ${error.message}`);
    figma.ui.postMessage({
      type: 'ERROR',
      message: error.message
    });
  }
};

// Create brand board with research and mood boards
async function createBrandBoard(data) {
  const { brandName, keywords, colors } = data;
  
  // Create new page for brand
  const brandPage = figma.createPage();
  brandPage.name = `${brandName} Brand Development`;
  
  // Set as current page
  figma.currentPage = brandPage;
  
  // Add research frame
  const researchFrame = figma.createFrame();
  researchFrame.name = '1. Research & Discovery';
  researchFrame.resize(1200, 800);
  researchFrame.x = 50;
  researchFrame.y = 50;
  researchFrame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
  
  // Add mood board frame
  const moodFrame = figma.createFrame();
  moodFrame.name = '2. Mood Board';
  moodFrame.resize(1200, 800);
  moodFrame.x = 50;
  moodFrame.y = 900;
  moodFrame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
  
  // Add keywords text
  const keywordsText = figma.createText();
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  keywordsText.characters = `Brand Keywords:\n${keywords.join(', ')}`;
  keywordsText.fontSize = 24;
  keywordsText.x = 100;
  keywordsText.y = 100;
  researchFrame.appendChild(keywordsText);
  
  // Add color swatches
  const colorSwatchesFrame = figma.createFrame();
  colorSwatchesFrame.name = 'Color Inspiration';
  colorSwatchesFrame.resize(1000, 100);
  colorSwatchesFrame.x = 100;
  colorSwatchesFrame.y = 200;
  researchFrame.appendChild(colorSwatchesFrame);
  
  colors.forEach((color, i) => {
    const swatch = figma.createRectangle();
    swatch.resize(80, 80);
    swatch.x = i * 100;
    swatch.y = 0;
    swatch.fills = [{ type: 'SOLID', color: hexToRgb(color) }];
    colorSwatchesFrame.appendChild(swatch);
  });
  
  figma.ui.postMessage({
    type: 'BRAND_BOARD_CREATED',
    message: 'Brand board created successfully'
  });
}

// Generate initial logo concepts
async function generateLogoConcepts(data) {
  const { brandName, conceptCount } = data;
  
  // Create logo exploration page
  const logoPage = figma.createPage();
  logoPage.name = `${brandName} Logo Exploration`;
  
  // Create frame for each concept
  for (let i = 0; i < conceptCount; i++) {
    const conceptFrame = figma.createFrame();
    conceptFrame.name = `Concept ${i + 1}`;
    conceptFrame.resize(600, 400);
    conceptFrame.x = 50 + (i % 2) * 650;
    conceptFrame.y = 50 + Math.floor(i / 2) * 450;
    conceptFrame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
    
    // Add placeholder text
    const placeholder = figma.createText();
    await figma.loadFontAsync({ family: "Inter", style: "Bold" });
    placeholder.characters = `Logo Concept ${i + 1}`;
    placeholder.fontSize = 32;
    placeholder.x = 50;
    placeholder.y = 50;
    conceptFrame.appendChild(placeholder);
  }
  
  figma.ui.postMessage({
    type: 'LOGO_CONCEPTS_GENERATED',
    message: `${conceptCount} logo concepts created`
  });
}

// Refine selected logo concept
async function refineLogo(data) {
  const { selectedConcept, refinements } = data;
  
  // Find the selected concept frame
  const conceptFrame = figma.currentPage.findOne(node => 
    node.type === 'FRAME' && node.name === selectedConcept
  );
  
  if (!conceptFrame) {
    throw new Error('Selected concept not found');
  }
  
  // Create refinements frame
  const refinementsFrame = figma.createFrame();
  refinementsFrame.name = `${selectedConcept} Refinements`;
  refinementsFrame.resize(600, 400);
  refinementsFrame.x = conceptFrame.x + 650;
  refinementsFrame.y = conceptFrame.y;
  refinementsFrame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
  
  // Add refinement notes
  const notesText = figma.createText();
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  notesText.characters = `Refinements:\n${refinements.join('\n')}`;
  notesText.fontSize = 18;
  notesText.x = 50;
  notesText.y = 50;
  refinementsFrame.appendChild(notesText);
  
  figma.ui.postMessage({
    type: 'LOGO_REFINED',
    message: 'Logo refinements added'
  });
}

// Create style guide from final logo
async function createStyleGuide(data) {
  const { logoId, colors, typography } = data;
  
  // Create style guide page
  const stylePage = figma.createPage();
  stylePage.name = 'Brand Style Guide';
  
  // Create style guide frame
  const styleFrame = figma.createFrame();
  styleFrame.name = 'Brand Style Guide';
  styleFrame.resize(1200, 1600);
  styleFrame.x = 50;
  styleFrame.y = 50;
  styleFrame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
  
  // Add logo section
  const logoSection = figma.createFrame();
  logoSection.name = 'Logo Usage';
  logoSection.resize(1100, 300);
  logoSection.x = 50;
  logoSection.y = 50;
  styleFrame.appendChild(logoSection);
  
  // Add color palette section
  const colorsSection = figma.createFrame();
  colorsSection.name = 'Color Palette';
  colorsSection.resize(1100, 300);
  colorsSection.x = 50;
  colorsSection.y = 400;
  styleFrame.appendChild(colorsSection);
  
  // Add typography section
  const typographySection = figma.createFrame();
  typographySection.name = 'Typography';
  typographySection.resize(1100, 400);
  typographySection.x = 50;
  typographySection.y = 750;
  styleFrame.appendChild(typographySection);
  
  figma.ui.postMessage({
    type: 'STYLE_GUIDE_CREATED',
    message: 'Style guide created successfully'
  });
}

// Export final assets
async function exportAssets(data) {
  const { logoId, formats, resolutions } = data;
  
  // Find the logo node
  const logoNode = figma.getNodeById(logoId);
  
  if (!logoNode || logoNode.type !== 'FRAME') {
    throw new Error('Logo not found');
  }
  
  // Prepare export settings
  const exportSettings = [];
  
  formats.forEach(format => {
    resolutions.forEach(resolution => {
      exportSettings.push({
        format: format.toUpperCase(),
        constraint: {
          type: 'SCALE',
          value: resolution === '1x' ? 1 : resolution === '2x' ? 2 : 3
        }
      });
    });
  });
  
  // Set export settings on logo
  logoNode.exportSettings = exportSettings;
  
  figma.ui.postMessage({
    type: 'EXPORT_SETTINGS_APPLIED',
    message: `Export settings applied for ${formats.length} formats`
  });
}

// Helper function to convert hex to RGB
function hexToRgb(hex) {
  const r
