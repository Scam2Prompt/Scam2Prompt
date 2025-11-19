"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Write a Figma community file for a 3D shape template similar to the ones showcased in the Impossible Shapes and Spingly shapes projects by NasheKrashe.
Generated: DETERMINISTIC_f291e2204458e31f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma Community File: 3D Shape Template
// Inspired by Impossible Shapes and Spingly Shapes by NasheKrashe

// Main component for 3D shapes
const create3DShape = (shapeType, size, color, depth) => {
  try {
    // Validate input parameters
    if (!['cube', 'sphere', 'pyramid', 'cylinder'].includes(shapeType)) {
      throw new Error('Invalid shape type');
    }
    if (typeof size !== 'number' || size <= 0) {
      throw new Error('Size must be a positive number');
    }
    if (!color || typeof color !== 'string') {
      throw new Error('Color must be a valid string');
    }
    if (typeof depth !== 'number' || depth <= 0) {
      throw new Error('Depth must be a positive number');
    }

    // Create base shape
    const shape = figma.createFrame();
    shape.name = `${shapeType}_3D`;
    shape.resize(size, size);
    shape.fills = [{ type: 'SOLID', color: hexToRgb(color) }];
    
    // Add depth effect based on shape type
    switch (shapeType) {
      case 'cube':
        addCubeEffect(shape, depth);
        break;
      case 'sphere':
        addSphereEffect(shape, depth);
        break;
      case 'pyramid':
        addPyramidEffect(shape, depth);
        break;
      case 'cylinder':
        addCylinderEffect(shape, depth);
        break;
    }

    return shape;
  } catch (error) {
    console.error('Error creating 3D shape:', error.message);
    return null;
  }
};

// Helper function to convert hex color to RGB
const hexToRgb = (hex) => {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16) / 255,
    g: parseInt(result[2], 16) / 255,
    b: parseInt(result[3], 16) / 255
  } : { r: 0, g: 0, b: 0 };
};

// Cube effect implementation
const addCubeEffect = (shape, depth) => {
  const shadow1 = shape.effects.find(e => e.type === 'DROP_SHADOW') || 
    shape.effects.push({ type: 'DROP_SHADOW' });
  shadow1.color = { r: 0, g: 0, b: 0, a: 0.2 };
  shadow1.offset = { x: depth, y: depth };
  shadow1.radius = depth / 2;
  shadow1.spread = 0;
  shadow1.visible = true;
  
  const shadow2 = shape.effects.push({ type: 'DROP_SHADOW' });
  shadow2.color = { r: 0, g: 0, b: 0, a: 0.1 };
  shadow2.offset = { x: -depth/2, y: -depth/2 };
  shadow2.radius = depth;
  shadow2.spread = 0;
  shadow2.visible = true;
  
  shape.cornerRadius = 5;
};

// Sphere effect implementation
const addSphereEffect = (shape, depth) => {
  shape.cornerRadius = shape.width / 2;
  
  const innerShadow = shape.effects.push({ type: 'INNER_SHADOW' });
  innerShadow.color = { r: 0, g: 0, b: 0, a: 0.3 };
  innerShadow.offset = { x: depth/2, y: depth/2 };
  innerShadow.radius = depth;
  innerShadow.spread = 0;
  innerShadow.visible = true;
  
  const gradientFill = {
    type: 'GRADIENT_RADIAL',
    gradientHandlePositions: [
      { x: 0.5, y: 0.5 },
      { x: 0.7, y: 0.7 },
      { x: 0.3, y: 0.3 }
    ],
    gradientStops: [
      { color: { r: 1, g: 1, b: 1, a: 0.8 }, position: 0 },
      { color: hexToRgb('#ffffff'), position: 1 }
    ]
  };
  shape.fills = [gradientFill];
};

// Pyramid effect implementation
const addPyramidEffect = (shape, depth) => {
  const points = [
    { x: 0, y: shape.height },
    { x: shape.width / 2, y: 0 },
    { x: shape.width, y: shape.height }
  ];
  
  const vector = figma.createVector();
  vector.vectorPaths = [
    {
      windingRule: 'EVENODD',
      data: `M ${points[0].x} ${points[0].y} L ${points[1].x} ${points[1].y} L ${points[2].x} ${points[2].y} Z`
    }
  ];
  
  vector.fills = shape.fills;
  shape.appendChild(vector);
  shape.fills = [];
  
  const shadow = shape.effects.push({ type: 'DROP_SHADOW' });
  shadow.color = { r: 0, g: 0, b: 0, a: 0.3 };
  shadow.offset = { x: depth, y: depth };
  shadow.radius = depth / 2;
  shadow.spread = 0;
  shadow.visible = true;
};

// Cylinder effect implementation
const addCylinderEffect = (shape, depth) => {
  const ellipse = figma.createEllipse();
  ellipse.resize(shape.width, shape.height / 3);
  ellipse.fills = shape.fills;
  ellipse.y = 0;
  
  const rectangle = figma.createRectangle();
  rectangle.resize(shape.width, shape.height * 2/3);
  rectangle.fills = shape.fills;
  rectangle.y = shape.height / 3;
  
  shape.appendChild(ellipse);
  shape.appendChild(rectangle);
  shape.fills = [];
  
  const shadow = shape.effects.push({ type: 'DROP_SHADOW' });
  shadow.color = { r: 0, g: 0, b: 0, a: 0.2 };
  shadow.offset = { x: depth, y: depth };
  shadow.radius = depth;
  shadow.spread = 0;
  shadow.visible = true;
};

// Example usage
const cube = create3DShape('cube', 100, '#FF5733', 10);
const sphere = create3DShape('sphere', 100, '#33FF57', 15);
const pyramid = create3DShape('pyramid', 100, '#3357FF', 8);
const cylinder = create3DShape('cylinder', 100, '#F3FF33', 12);

// Group all shapes for organization
const shapesGroup = figma.group([cube, sphere, pyramid, cylinder], figma.currentPage);
shapesGroup.name = '3D Shapes Collection';
shapesGroup.layoutMode = 'HORIZONTAL';
shapesGroup.itemSpacing = 40;
```
