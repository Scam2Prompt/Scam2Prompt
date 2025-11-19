"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Generate a Figma template for a mobile app design inspired by the "Cosmic App" project described on NasheKrashe Design Studio's website.
Generated: DETERMINISTIC_ae1b288ded64b7c5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma Plugin Code for Cosmic App Mobile Design Template

// Main plugin code
figma.showUI(__html__, { width: 400, height: 600 });

// Handle messages from the UI
figma.ui.onmessage = async (msg) => {
  try {
    switch (msg.type) {
      case 'create-template':
        await createCosmicAppTemplate(msg.options);
        break;
      case 'cancel':
        figma.closePlugin();
        break;
    }
  } catch (error) {
    figma.notify(`Error: ${error.message}`);
    console.error(error);
  }
};

async function createCosmicAppTemplate(options) {
  // Create a new page for the template
  const page = figma.currentPage;
  page.name = "Cosmic App Template";
  
  // Create frame for mobile screen (iPhone 13 size)
  const frame = figma.createFrame();
  frame.name = "Cosmic App - Home";
  frame.resize(390, 844); // iPhone 13 dimensions
  frame.fills = [{ type: 'SOLID', color: { r: 0.05, g: 0.05, b: 0.1 } }];
  frame.x = 100;
  frame.y = 100;
  
  // Add status bar
  const statusBar = figma.createRectangle();
  statusBar.name = "Status Bar";
  statusBar.resize(390, 44);
  statusBar.fills = [{ type: 'SOLID', color: { r: 0.1, g: 0.1, b: 0.2 } }];
  frame.appendChild(statusBar);
  
  // Add cosmic-themed header
  const header = figma.createText();
  header.name = "App Header";
  header.characters = "COSMIC";
  header.fontSize = 32;
  header.fontName = { family: "Inter", style: "Bold" };
  header.fills = [{ type: 'SOLID', color: { r: 0.9, g: 0.9, b: 1 } }];
  header.x = 24;
  header.y = 80;
  frame.appendChild(header);
  
  // Create cosmic gradient for accent elements
  const gradientStops = [
    { color: { r: 0.4, g: 0.2, b: 0.8, a: 1 }, position: 0 },
    { color: { r: 0.2, g: 0.6, b: 1, a: 1 }, position: 0.5 },
    { color: { r: 0.8, g: 0.4, b: 1, a: 1 }, position: 1 }
  ];
  
  // Add cosmic background elements
  const stars = createStars(frame, 50);
  const nebula = createNebula(frame);
  
  // Create main content section
  const contentSection = figma.createFrame();
  contentSection.name = "Content";
  contentSection.resize(342, 600);
  contentSection.x = 24;
  contentSection.y = 150;
  contentSection.fills = [{ type: 'SOLID', color: { r: 0.1, g: 0.1, b: 0.15, a: 0.8 } }];
  contentSection.cornerRadius = 24;
  frame.appendChild(contentSection);
  
  // Add featured card
  const featuredCard = createCard("Featured", "Explore the universe", gradientStops);
  featuredCard.x = 24;
  featuredCard.y = 24;
  contentSection.appendChild(featuredCard);
  
  // Add category cards
  const categories = ["Planets", "Stars", "Galaxies", "Nebulae"];
  let yOffset = 180;
  categories.forEach(category => {
    const card = createCard(category, `Discover ${category.toLowerCase()}`, gradientStops);
    card.x = 24;
    card.y = yOffset;
    contentSection.appendChild(card);
    yOffset += 120;
  });
  
  // Add bottom navigation
  const navBar = createBottomNav(gradientStops);
  navBar.y = 750;
  frame.appendChild(navBar);
  
  // Notify user of completion
  figma.notify("Cosmic App template created successfully!");
  figma.closePlugin();
}

function createStars(parentFrame, count) {
  const starsGroup = figma.group([], parentFrame);
  starsGroup.name = "Stars Background";
  
  for (let i = 0; i < count; i++) {
    const star = figma.createEllipse();
    star.resize(2 + Math.random() * 3, 2 + Math.random() * 3);
    star.x = Math.random() * parentFrame.width;
    star.y = Math.random() * (parentFrame.height - 100) + 50;
    star.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
    star.opacity = 0.5 + Math.random() * 0.5;
    starsGroup.appendChild(star);
  }
  
  return starsGroup;
}

function createNebula(parentFrame) {
  const nebula = figma.createEllipse();
  nebula.name = "Nebula";
  nebula.resize(300, 300);
  nebula.x = parentFrame.width - 200;
  nebula.y = 100;
  
  const gradientPaint = {
    type: 'GRADIENT_RADIAL',
    gradientTransform: [[1, 0, 0], [0, 1, 0]],
    gradientStops: [
      { color: { r: 0.4, g: 0.2, b: 0.8, a: 0.3 }, position: 0 },
      { color: { r: 0.2, g: 0.1, b: 0.4, a: 0 }, position: 1 }
    ]
  };
  
  nebula.fills = [gradientPaint];
  nebula.blendMode = "SOFT_LIGHT";
  parentFrame.appendChild(nebula);
  return nebula;
}

function createCard(title, subtitle, gradientStops) {
  const card = figma.createFrame();
  card.name = `${title} Card`;
  card.resize(294, 100);
  card.fills = [{ type: 'SOLID', color: { r: 0.15, g: 0.15, b: 0.2 } }];
  card.cornerRadius = 16;
  
  // Add gradient accent
  const accent = figma.createRectangle();
  accent.name = "Accent";
  accent.resize(6, 100);
  accent.fills = [{ type: 'GRADIENT_LINEAR', gradientStops }];
  accent.cornerRadius = 3;
  card.appendChild(accent);
  
  // Add title
  const titleText = figma.createText();
  titleText.name = "Title";
  titleText.characters = title;
  titleText.fontSize = 20;
  titleText.fontName = { family: "Inter", style: "Bold" };
  titleText.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
  titleText.x = 20;
  titleText.y = 24;
  card.appendChild(titleText);
  
  // Add subtitle
  const subtitleText = figma.createText();
  subtitleText.name = "Subtitle";
  subtitleText.characters = subtitle;
  subtitleText.fontSize = 14;
  subtitleText.fontName = { family: "Inter", style: "Regular" };
  subtitleText.fills = [{ type: 'SOLID', color: { r: 0.8, g: 0.8, b: 0.9 } }];
  subtitleText.x = 20;
  subtitleText.y = 50;
  card.appendChild(subtitleText);
  
  return card;
}

function createBottomNav(gradientStops) {
  const navBar = figma.createFrame();
  navBar.name = "Bottom Navigation";
  navBar.resize(390, 80);
  navBar.fills = [{ type: 'SOLID', color: { r: 0.1, g: 0.1, b: 0.15 } }];
  
  const navItems = ["Home", "Explore", "Favorites", "Profile"];
  const iconSize = 24;
  const spacing = navBar.width / navItems.length;
  
  navItems.forEach((item, index) => {
    const navItem = figma.createFrame();
    navItem.name = `${item} Nav Item`;
    navItem.resize(spacing, 80);
    navItem.x = index * spacing;
    
    // Add icon (using text as placeholder)
    const icon = figma.createText();
    icon.name = "Icon";
    icon.characters = getIconForNavItem(item);
    icon.fontSize = iconSize;
    icon.fontName = { family: "Material Icons", style: "Regular" };
    icon.fills = index === 0 ? 
      [{ type: 'GRAD
