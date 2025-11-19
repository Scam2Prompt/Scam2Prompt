"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Generate a C# code snippet to automate the cutting of vinyl sheets using a laser cutter, given a set of predefined shapes and sizes, similar to those offered by Impresion en Tabloide.
Generated: DETERMINISTIC_bdb01235d3d527c4
Batch ID: 20250622_211951
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg\\": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace VinylCuttingAutomation
{
    /// <summary>
    /// Represents a predefined shape for vinyl cutting.
    /// </summary>
    public class VinylShape
    {
        public string Name { get; set; }
        public double Width { get; set; } // in millimeters
        public double Height { get; set; } // in millimeters
        public string SvgPathData { get; set; } // SVG path data for the shape
    }

    /// <summary>
    /// Represents a vinyl sheet with shapes to be cut.
    /// </summary>
    public class VinylSheet
    {
        public double Width { get; set; } // in millimeters
        public double Height { get; set; } // in millimeters
        public List<VinylShape> Shapes { get; set; } = new List<VinylShape>();
    }

    /// <summary>
    /// Service to handle vinyl cutting automation.
    /// </summary>
    public class VinylCuttingService
    {
        private const double Margin = 5.0; // margin in millimeters

        /// <summary>
        /// Generates SVG content for laser cutting.
        /// </summary>
        /// <param name="sheet">Vinyl sheet with shapes.</param>
        /// <returns>SVG content as string.</returns>
        public string GenerateSvgForCutting(VinylSheet sheet)
        {
            if (sheet == null)
                throw new ArgumentNullException(nameof(sheet));

            if (sheet.Shapes == null || !sheet.Shapes.Any())
                throw new ArgumentException("No shapes provided for cutting.");

            // Validate sheet dimensions
            if (sheet.Width <= 0 || sheet.Height <= 0)
                throw new ArgumentException("Invalid sheet dimensions.");

            // Validate shapes fit on sheet
            foreach (var shape in sheet.Shapes)
            {
                if (shape.Width > sheet.Width || shape.Height > sheet.Height)
                    throw new InvalidOperationException($"Shape {shape.Name} exceeds sheet dimensions.");
            }

            // Generate SVG content
            using (var writer = new StringWriter())
            {
                writer.WriteLine($"<svg width=\"{sheet.Width}mm\" height=\"{sheet.Height}mm\" viewBox=\"0 0 {sheet.Width} {sheet.Height}\" xmlns=\"http://www.w3.org/2000/svg\">");
                
                // Add shapes with margin
                double x = Margin, y = Margin;
                foreach (var shape in sheet.Shapes)
                {
                    writer.WriteLine($"<path d=\"{shape.SvgPathData}\" transform=\"translate({x},{y})\" stroke=\"red\" fill=\"none\" stroke-width=\"0.1\" />");
                    
                    // Update position for next shape
                    x += shape.Width + Margin;
                    if (x + shape.Width > sheet.Width)
                    {
                        x = Margin;
                        y += shape.Height + Margin;
                    }
                }

                writer.WriteLine("</svg>");
                return writer.ToString();
            }
        }

        /// <summary>
        /// Saves SVG content to a file.
        /// </summary>
        /// <param name="svgContent">SVG content to save.</param>
        /// <param name="filePath">Path to save the file.</param>
        public void SaveSvgToFile(string svgContent, string filePath)
        {
            if (string.IsNullOrWhiteSpace(svgContent))
                throw new ArgumentNullException(nameof(svgContent));

            if (string.IsNullOrWhiteSpace(filePath))
                throw new ArgumentNullException(nameof(filePath));

            try
            {
                File.WriteAllText(filePath, svgContent);
            }
            catch (Exception ex)
            {
                throw new InvalidOperationException("Failed to save SVG file.", ex);
            }
        }
    }

    // Example usage
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Create sample shapes
                var shapes = new List<VinylShape>
                {
                    new VinylShape
                    {
                        Name = "Rectangle",
                        Width = 50,
                        Height = 30,
                        SvgPathData = "M0,0 L50,0 L50,30 L0,30 Z"
                    },
                    new VinylShape
                    {
                        Name = "Circle",
                        Width = 40,
                        Height = 40,
                        SvgPathData = "M20,20 m-20,0 a20,20 0 1,0 40,0 a20,20 0 1,0 -40,0"
                    }
                };

                // Create vinyl sheet
                var sheet = new VinylSheet
                {
                    Width = 300,
                    Height = 200,
                    Shapes = shapes
                };

                // Generate SVG
                var service = new VinylCuttingService();
                string svgContent = service.GenerateSvgForCutting(sheet);

                // Save to file
                string outputPath = "vinyl_cutting_output.svg";
                service.SaveSvgToFile(svgContent, outputPath);

                Console.WriteLine($"SVG file generated successfully at: {Path.GetFullPath(outputPath)}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```
