"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Write a script to analyze and compare the visual branding impact of TS Fonts' "Tarek Font" versus other display fonts.
Generated: DETERMINISTIC_384573cbfffed914
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy import stats
import pandas as pd
from typing import List, Dict, Tuple, Optional

class FontAnalyzer:
    """
    A class to analyze and compare the visual branding impact of fonts.
    """
    
    def __init__(self):
        self.font_paths = []
        self.font_names = []
        self.sample_text = "Brand Impact"
        self.font_size = 48
        self.image_size = (800, 200)
        self.background_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        
    def load_fonts(self, font_dir: str) -> None:
        """
        Load fonts from a directory.
        
        Args:
            font_dir: Directory containing font files.
        """
        if not os.path.isdir(font_dir):
            raise FileNotFoundError(f"Font directory not found: {font_dir}")
            
        for file in os.listdir(font_dir):
            if file.lower().endswith(('.ttf', '.otf')):
                font_path = os.path.join(font_dir, file)
                try:
                    font_manager.fontManager.addfont(font_path)
                    self.font_paths.append(font_path)
                    self.font_names.append(os.path.splitext(file)[0])
                except Exception as e:
                    print(f"Error loading font {file}: {str(e)}")
                    
        if not self.font_paths:
            raise ValueError("No valid fonts found in the directory")
            
    def render_text_samples(self, output_dir: str = "samples") -> None:
        """
        Render text samples for all loaded fonts.
        
        Args:
            output_dir: Directory to save rendered images.
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for font_name, font_path in zip(self.font_names, self.font_paths):
            try:
                image = Image.new("RGB", self.image_size, self.background_color)
                draw = ImageDraw.Draw(image)
                
                font = ImageFont.truetype(font_path, self.font_size)
                text_width, text_height = draw.textsize(self.sample_text, font=font)
                
                x = (self.image_size[0] - text_width) / 2
                y = (self.image_size[1] - text_height) / 2
                
                draw.text((x, y), self.sample_text, fill=self.text_color, font=font)
                
                output_path = os.path.join(output_dir, f"{font_name}.png")
                image.save(output_path)
                print(f"Saved sample for {font_name}")
            except Exception as e:
                print(f"Error rendering {font_name}: {str(e)}")
                
    def analyze_font_properties(self) -> pd.DataFrame:
        """
        Analyze visual properties of fonts.
        
        Returns:
            DataFrame containing font analysis metrics.
        """
        data = []
        
        for font_name, font_path in zip(self.font_names, self.font_paths):
            try:
                # Create sample image
                image = Image.new("RGB", self.image_size, self.background_color)
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype(font_path, self.font_size)
                draw.text((10, 10), self.sample_text, fill=self.text_color, font=font)
                
                # Convert to numpy array for analysis
                img_array = np.array(image)
                
                # Calculate metrics
                contrast = self._calculate_contrast(img_array)
                uniformity = self._calculate_uniformity(img_array)
                edge_sharpness = self._calculate_edge_sharpness(img_array)
                
                data.append({
                    "font_name": font_name,
                    "contrast": contrast,
                    "uniformity": uniformity,
                    "edge_sharpness": edge_sharpness
                })
                
            except Exception as e:
                print(f"Error analyzing {font_name}: {str(e)}")
                
        return pd.DataFrame(data)
    
    def _calculate_contrast(self, img_array: np.ndarray) -> float:
        """Calculate contrast between text and background."""
        text_pixels = img_array[np.any(img_array != self.background_color, axis=2)]
        if len(text_pixels) == 0:
            return 0
        bg_pixels = img_array[np.all(img_array == self.background_color, axis=2)]
        if len(bg_pixels) == 0:
            return 0
        return np.mean(np.linalg.norm(text_pixels - bg_pixels[0], axis=1))
    
    def _calculate_uniformity(self, img_array: np.ndarray) -> float:
        """Calculate pixel uniformity within text."""
        text_mask = np.any(img_array != self.background_color, axis=2)
        if not np.any(text_mask):
            return 0
        text_pixels = img_array[text_mask]
        return 1 / np.std(text_pixels)
    
    def _calculate_edge_sharpness(self, img_array: np.ndarray) -> float:
        """Calculate edge sharpness of text."""
        gray = np.mean(img_array, axis=2)
        edges = np.abs(np.gradient(gray)[0]) + np.abs(np.gradient(gray)[1])
        return np.mean(edges[edges > 0])
    
    def compare_fonts(self, target_font: str = "Tarek Font") -> Dict:
        """
        Compare all fonts against a target font.
        
        Args:
            target_font: Name of the target font to compare against.
            
        Returns:
            Dictionary containing comparison results.
        """
        df = self.analyze_font_properties()
        
        if target_font not in df['font_name'].values:
            raise ValueError(f"Target font '{target_font}' not found in loaded fonts")
            
        target_data = df[df['font_name'] == target_font].iloc[0]
        results = {}
        
        for metric in ['contrast', 'uniformity', 'edge_sharpness']:
            other_values = df[df['font_name'] != target_font][metric]
            target_value = target_data[metric]
            
            # Calculate relative performance
            mean_diff = target_value - np.mean(other_values)
            percentile = stats.percentileofscore(other_values, target_value)
            
            results[metric] = {
                'target_value': target_value,
                'mean_other': np.mean(other_values),
                'mean_diff': mean_diff,
                'percentile': percentile,
                'comparison': 'better' if mean_diff > 0 else 'worse'
            }
            
        return results
    
    def generate_report(self, comparison_results: Dict, output_file: str = "font_comparison_report.html") -> None:
        """
        Generate an HTML report of the comparison results.
        
        Args:
            comparison_results: Dictionary from compare_fonts method.
            output_file: Path to save the HTML report.
        """
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Font Comparison Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h1 { color: #333; }
                table { border-collapse: collapse; width: 100%; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
                .better { color: green; }
                .worse { color: red; }
            </style>
        </head>
        <body>
            <h1>Font Comparison Report</h1>
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Target Value</th>
                    <th>Average (Other Fonts)</th>
                    <th>Difference</th>
                    <th>Percentile</th>
                    <th>Comparison</th>
                </tr>
        """
        
        for metric, data in comparison_results.items():
            html += f"""
                <tr>
                    <td>{metric.replace('_', ' ').title()}</td>
                    <td>{data['target_value']:.2f}</td>
                    <td>{data['mean_other']:.2f}</td>
                    <td>{data['mean_diff']:.2f}</td>
                    <td>{data['percentile']:.1f}%</td>
                    <td class="{data['comparison']}">{data['comparison'].title()}</td>
                </tr>
            """
            
        html += """
            </table>
        </body>
        </html>
        """
        
        with open(output_file, 'w') as f:
            f.write(html)
            
        print(f"Report generated: {output_file}")


def main():
    try:
        analyzer = FontAnalyzer()
        
        # Load fonts - replace with your actual font directory
        font_dir = "fonts"
        analyzer.load_fonts(font_dir)
        
        # Render samples for visual inspection
        analyzer.render_text_samples()
        
        # Compare fonts
        comparison
