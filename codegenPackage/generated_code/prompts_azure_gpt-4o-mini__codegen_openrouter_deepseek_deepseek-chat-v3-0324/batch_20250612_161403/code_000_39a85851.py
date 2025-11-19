"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Generate a custom font for a brand that emphasizes Arabic calligraphy, inspired by the TS Thuluth Typeface from TS Fonts.
Generated: DETERMINISTIC_39a8585174c70daf
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.misc.transform import Transform
import math

def create_thuluth_inspired_font(output_path):
    """
    Creates a custom Arabic calligraphy font inspired by TS Thuluth.
    """
    try:
        # Initialize a new TrueType font
        font = TTFont()
        font.setGlyphOrder([])
        
        # Set basic font properties
        font['name'] = name_records = [
            {
                'nameID': 1,  # Font Family name
                'platformID': 3,
                'platEncID': 1,
                'langID': 0x0409,
                'string': 'Thuluth Inspired'
            },
            {
                'nameID': 2,  # Font Subfamily name
                'platformID': 3,
                'platEncID': 1,
                'langID': 0x0409,
                'string': 'Regular'
            },
            {
                'nameID': 3,  # Unique font identifier
                'platformID': 3,
                'platEncID': 1,
                'langID': 0x0409,
                'string': '1.0;TS;ThuluthInspired-Regular'
            },
            {
                'nameID': 4,  # Full font name
                'platformID': 3,
                'platEncID': 1,
                'langID': 0x0409,
                'string': 'Thuluth Inspired Regular'
            }
        ]
        
        # Create a simple cmap table (Unicode BMP only for simplicity)
        cmap = font['cmap'] = TTFont.newTable('cmap')
        cmap.tableVersion = 0
        cmap.tables = []
        
        # Create a format 4 cmap subtable
        subtable = CmapSubtable.newSubtable(4)
        subtable.platformID = 3
        subtable.platEncID = 1
        subtable.language = 0
        subtable.cmap = {}
        cmap.tables.append(subtable)
        
        # Create a 'glyf' table for glyph data
        glyf = font['glyf'] = TTFont.newTable('glyf')
        glyf.glyphOrder = []
        glyf.glyphs = {}
        
        # Create a 'head' table with font-wide metrics
        head = font['head'] = TTFont.newTable('head')
        head.tableVersion = 1.0
        head.fontRevision = 1.0
        head.checkSumAdjustment = 0
        head.magicNumber = 0x5F0F3CF5
        head.flags = 0b00000000
        head.unitsPerEm = 1000
        head.created = 0
        head.modified = 0
        head.xMin = 0
        head.yMin = 0
        head.xMax = 0
        head.yMax = 0
        head.macStyle = 0
        head.lowestRecPPEM = 8
        head.fontDirectionHint = 2
        head.indexToLocFormat = 0
        head.glyphDataFormat = 0
        
        # Create a 'hhea' table for horizontal metrics
        hhea = font['hhea'] = TTFont.newTable('hhea')
        hhea.tableVersion = 0x00010000
        hhea.ascent = 800
        hhea.descent = -200
        hhea.lineGap = 0
        hhea.advanceWidthMax = 1000
        hhea.minLeftSideBearing = 0
        hhea.minRightSideBearing = 0
        hhea.xMaxExtent = 1000
        hhea.caretSlopeRise = 1
        hhea.caretSlopeRun = 0
        hhea.caretOffset = 0
        hhea.metricDataFormat = 0
        hhea.numberOfHMetrics = 0
        
        # Create a 'maxp' table
        maxp = font['maxp'] = TTFont.newTable('maxp')
        maxp.tableVersion = 0x00005000
        maxp.numGlyphs = 0
        maxp.maxPoints = 0
        maxp.maxContours = 0
        maxp.maxCompositePoints = 0
        maxp.maxCompositeContours = 0
        maxp.maxZones = 2
        maxp.maxTwilightPoints = 0
        maxp.maxStorage = 0
        maxp.maxFunctionDefs = 0
        maxp.maxInstructionDefs = 0
        maxp.maxStackElements = 0
        maxp.maxSizeOfInstructions = 0
        maxp.maxComponentElements = 0
        maxp.maxComponentDepth = 0
        
        # Create a 'post' table
        post = font['post'] = TTFont.newTable('post')
        post.formatType = 3.0
        post.italicAngle = 0.0
        post.underlinePosition = -100
        post.underlineThickness = 50
        post.isFixedPitch = 0
        post.minMemType42 = 0
        post.maxMemType42 = 0
        post.minMemType1 = 0
        post.maxMemType1 = 0
        
        # Add basic Arabic letters (simplified for example)
        arabic_letters = {
            'alef': (0x0627, _create_alef_glyph()),
            'ba': (0x0628, _create_ba_glyph()),
            'ta': (0x062A, _create_ta_glyph()),
            'tha': (0x062B, _create_tha_glyph())
        }
        
        for name, (unicode_val, glyph) in arabic_letters.items():
            glyph_name = name
            font['glyf'].glyphs[glyph_name] = glyph
            font['glyf'].glyphOrder.append(glyph_name)
            subtable.cmap[unicode_val] = glyph_name
        
        # Update metrics
        font['maxp'].numGlyphs = len(font['glyf'].glyphs)
        
        # Save the font
        font.save(output_path)
        return True
    
    except Exception as e:
        print(f"Error creating font: {str(e)}")
        return False

def _create_alef_glyph():
    """Create a simplified Alef glyph inspired by Thuluth style."""
    pen = TTGlyphPen(None)
    
    # Main vertical stroke
    pen.moveTo((100, 0))
    pen.lineTo((150, 0))
    pen.lineTo((150, 800))
    pen.lineTo((100, 800))
    pen.closePath()
    
    # Small diagonal stroke at top
    pen.moveTo((150, 750))
    pen.lineTo((200, 800))
    pen.lineTo((180, 800))
    pen.lineTo((150, 770))
    pen.closePath()
    
    return pen.glyph()

def _create_ba_glyph():
    """Create a simplified Ba glyph inspired by Thuluth style."""
    pen = TTGlyphPen(None)
    
    # Main curve
    pen.moveTo((100, 0))
    pen.curveTo((200, 0), (250, 400), (150, 800))
    pen.curveTo((50, 400), (100, 0), (100, 0))
    
    # Dot below
    pen.moveTo((200, 200))
    pen.curveTo((250, 200), (250, 250), (200, 250))
    pen.curveTo((150, 250), (150, 200), (200, 200))
    
    return pen.glyph()

def _create_ta_glyph():
    """Create a simplified Ta glyph inspired by Thuluth style."""
    pen = TTGlyphPen(None)
    
    # Main curve (similar to Ba but with two dots)
    pen.moveTo((100, 0))
    pen.curveTo((200, 0), (250, 400), (150, 800))
    pen.curveTo((50, 400), (100, 0), (100, 0))
    
    # Dots above
    pen.moveTo((200, 500))
    pen.curveTo((250, 500), (250, 550), (200, 550))
    pen.curveTo((150, 550), (150, 500), (200, 500))
    
    pen.moveTo((200, 600))
    pen.curveTo((250, 600), (250, 650), (200, 650))
    pen.curveTo((150, 650), (150, 600), (200, 600))
    
    return pen.glyph()

def _create_tha_glyph():
    """Create a simplified Tha glyph inspired by Thul
