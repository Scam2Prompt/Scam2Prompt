"""
Generated Code Metadata:
========================
Original URL: https://openspa.info
Prompt: Create a tool for generating bootlogos for OpenSPA receivers, supporting various image formats and resolutions.
Generated: DETERMINISTIC_df66f5fff7bf2928
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bootlogo Generator Tool for OpenSPA receivers

Supports various image formats and resolutions.

Author: [Your Name]
Date: [Today's Date]
"""

import argparse
import os
import sys
from PIL import Image

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Bootlogo Generator Tool')
    parser.add_argument('-i', '--input', required=True, help='Input image file')
    parser.add_argument('-o', '--output', required=True, help='Output bootlogo file')
    parser.add_argument('-r', '--resolution', default='1280x720', help='Output resolution (default: 1280x720)')
    parser.add_argument('-f', '--format', default='png', choices=['png', 'jpg', 'jpeg', 'bmp'], help='Output image format (default: png)')

    return parser.parse_args()

def validate_input_image(input_image):
    """
    Validate input image file.

    Args:
        input_image (str): Input image file path.

    Raises:
        FileNotFoundError: If input image file does not exist.
        ValueError: If input image file is not a valid image.
    """
    if not os.path.exists(input_image):
        raise FileNotFoundError(f"Input image file '{input_image}' does not exist.")

    try:
        Image.open(input_image)
    except Exception as e:
        raise ValueError(f"Invalid input image file '{input_image}': {str(e)}")

def generate_bootlogo(input_image, output_image, resolution, output_format):
    """
    Generate bootlogo image.

    Args:
        input_image (str): Input image file path.
        output_image (str): Output bootlogo file path.
        resolution (str): Output resolution (e.g., 1280x720).
        output_format (str): Output image format (e.g., png).

    Raises:
        Exception: If image processing fails.
    """
    try:
        # Open input image
        with Image.open(input_image) as img:
            # Resize image to output resolution
            width, height = map(int, resolution.split('x'))
            img = img.resize((width, height))

            # Save output image
            img.save(output_image, format=output_format.upper())
    except Exception as e:
        raise Exception(f"Failed to generate bootlogo: {str(e)}")

def main():
    try:
        # Parse command-line arguments
        args = parse_args()

        # Validate input image file
        validate_input_image(args.input)

        # Generate bootlogo image
        generate_bootlogo(args.input, args.output, args.resolution, args.format)

        print(f"Bootlogo generated successfully: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
