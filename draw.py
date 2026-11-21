#!/usr/bin/env python3
"""
Draw the world news summary image for 20 November 2026.
Output: entry.png (max 1024x1024, < 1 MiB, valid PNG)
"""

import sys
import os
import math

# Try to import PIL, install if needed
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    # Install pillow to a temp location
    import subprocess
    tmpdir = os.environ.get('TMPDIR', '/tmp')
    pip_target = os.path.join(tmpdir, 'py')
    os.makedirs(pip_target, exist_ok=True)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--target', pip_target, 'pillow'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sys.path.insert(0, pip_target)
    from PIL import Image, ImageDraw, ImageFont


def find_font():
    """Find a suitable TTF font on macOS."""
    font_paths = [
        '/System/Library/Fonts/HelveticaNeue.ttc',
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/ArialHB.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
        '/System/Library/Fonts/Geneva.ttf',
    ]
    for path in font_paths:
        if os.path.exists(path):
            return path
    raise RuntimeError("No suitable font found")


def draw_icon(draw, x, y, size, icon_type, color):
    """Draw a simple icon/symbol for each story category."""
    half = size // 2
    cx, cy = x + half, y + half
    w = 2  # line width
    
    if icon_type == 'oil':  # Oil tanker / fire
        # Tanker ship silhouette
        draw.rectangle([cx - 16, cy - 6, cx + 16, cy + 6], outline=color, width=w)
        draw.rectangle([cx - 6, cy - 14, cx + 6, cy - 6], outline=color, width=w)
        # Fire above stack
        draw.polygon([(cx, cy - 14), (cx - 5, cy - 22), (cx + 5, cy - 22)], fill=color)
        draw.polygon([(cx, cy - 18), (cx - 3, cy - 26), (cx + 3, cy - 26)], fill=(255, 140, 0))
    elif icon_type == 'airstrike':  # Fighter jet
        # Jet body
        draw.polygon([(cx, cy - 12), (cx - 10, cy + 6), (cx - 5, cy + 6), (cx - 5, cy + 10), (cx + 5, cy + 10), (cx + 5, cy + 6), (cx + 10, cy + 6)], outline=color, width=w)
        # Missile dropping
        draw.line([(cx, cy + 10), (cx, cy + 18)], fill=color, width=w)
        draw.ellipse([cx - 2, cy + 16, cx + 2, cy + 20], fill=color)
    elif icon_type == 'missile':  # Missile impact / explosion
        # Explosion burst
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = cx + int(6 * math.cos(rad))
            y1 = cy + int(6 * math.sin(rad))
            x2 = cx + int(16 * math.cos(rad))
            y2 = cy + int(16 * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=color, width=w)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], outline=color, width=w)
        # Impact marker
        draw.line([(cx - 8, cy + 14), (cx + 8, cy + 14)], fill=color, width=w)
        draw.line([(cx, cy + 6), (cx, cy + 14)], fill=color, width=w)
    elif icon_type == 'boat':  # Boat disaster
        # Boat hull
        draw.polygon([(cx - 14, cy + 4), (cx + 14, cy + 4), (cx + 10, cy - 6), (cx - 10, cy - 6)], outline=color, width=w)
        # Mast
        draw.line([(cx, cy - 6), (cx, cy - 16)], fill=color, width=w)
        # Waves
        draw.arc([cx - 18, cy + 2, cx + 18, cy + 16], 0, 180, fill=color, width=w)
        draw.arc([cx - 14, cy + 6, cx + 14, cy + 20], 0, 180, fill=color, width=w)
    elif icon_type == 'strike':  # General strike / protest
        # Raised fist
        draw.polygon([(cx - 5, cy + 12), (cx - 5, cy - 6), (cx - 9, cy - 6), (cx - 9, cy - 10), (cx + 9, cy - 10), (cx + 9, cy - 6), (cx + 5, cy - 6), (cx + 5, cy + 12)], outline=color, width=w)
        # Knuckles
        for dx in [-6, -2, 2, 6]:
            draw.line([(cx + dx, cy - 10), (cx + dx, cy - 6)], fill=color, width=w)
    elif icon_type == 'math':  # Math/AI proof
        # Integral symbol
        draw.line([(cx, cy - 14), (cx, cy + 14)], fill=color, width=3)
        draw.arc([cx - 8, cy - 16, cx + 2, cy - 4], 180, 360, fill=color, width=3)
        draw.arc([cx - 8, cy + 4, cx + 2, cy + 16], 0, 180, fill=color, width=3)
        # Neural network nodes (small)
        for dx, dy in [(-12, -8), (-12, 8), (12, -8), (12, 8)]:
            draw.ellipse([cx + dx - 3, cy + dy - 3, cx + dx + 3, cy + dy + 3], fill=color)
        # Connections to center
        draw.line([(cx - 12, cy - 8), (cx - 2, cy - 1)], fill=color, width=1)
        draw.line([(cx - 12, cy + 8), (cx - 2, cy + 1)], fill=color, width=1)
        draw.line([(cx + 12, cy - 8), (cx + 2, cy - 1)], fill=color, width=1)
        draw.line([(cx + 12, cy + 8), (cx + 2, cy + 1)], fill=color, width=1)
    elif icon_type == 'handshake':  # Diplomatic deal
        # Two hands shaking
        draw.ellipse([cx - 12, cy - 4, cx - 1, cy + 10], outline=color, width=w)
        draw.ellipse([cx + 1, cy - 4, cx + 12, cy + 10], outline=color, width=w)
        # Thumbs
        draw.ellipse([cx - 14, cy - 2, cx - 7, cy + 5], outline=color, width=w)
        draw.ellipse([cx + 7, cy - 2, cx + 14, cy + 5], outline=color, width=w)
        # Handshake lines
        draw.line([(cx - 1, cy + 2), (cx + 1, cy + 2)], fill=color, width=w)
        draw.line([(cx - 1, cy + 5), (cx + 1, cy + 5)], fill=color, width=w)
    elif icon_type == 'balance':  # Iraq militia deal / balance of power
        # Scales
        draw.line([(cx, cy - 16), (cx, cy - 4)], fill=color, width=w)
        draw.line([(cx - 14, cy - 4), (cx + 14, cy - 4)], fill=color, width=w)
        # Left pan
        draw.line([(cx - 14, cy - 4), (cx - 14, cy + 6)], fill=color, width=w)
        draw.arc([cx - 20, cy + 6, cx - 8, cy + 18], 0, 180, fill=color, width=w)
        # Right pan
        draw.line([(cx + 14, cy - 4), (cx + 14, cy + 6)], fill=color, width=w)
        draw.arc([cx + 8, cy + 6, cx + 20, cy + 18], 0, 180, fill=color, width=w)
        # Balance indicator (level)
        draw.line([(cx - 3, cy - 2), (cx + 3, cy - 2)], fill=color, width=w)
    else:
        # Generic circle
        draw.ellipse([cx - half + 2, cy - half + 2, cx + half - 2, cy + half - 2], outline=color, width=w)


def wrap_text(draw, text, font, max_width):
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines


def main():
    # Image dimensions
    WIDTH, HEIGHT = 1024, 1024
    MARGIN = 30
    PANEL_PADDING = 15
    
    # Colors
    BG_COLOR = (245, 246, 248)
    HEADLINE_COLOR = (20, 25, 35)
    PANEL_BG = (255, 255, 255)
    PANEL_BORDER = (190, 195, 205)
    TEXT_COLOR = (30, 35, 45)
    REGION_BG = (0, 90, 180)
    REGION_TEXT = (255, 255, 255)
    ICON_COLOR = (50, 55, 65)
    
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    font_path = find_font()
    # HelveticaNeue.ttc indices: 0=Regular, 1=Bold, 2=Italic, 3=Bold Italic, 9=Condensed Black
    headline_font = ImageFont.truetype(font_path, 40, index=9)  # Condensed Black for headline
    title_font = ImageFont.truetype(font_path, 22, index=1)      # Bold for titles
    region_font = ImageFont.truetype(font_path, 13, index=1)     # Bold for region tags
    body_font = ImageFont.truetype(font_path, 15, index=0)       # Regular
    
    # Draw main headline
    headline = "World News — Friday 20 November 2026"
    h_bbox = draw.textbbox((0, 0), headline, font=headline_font)
    h_width = h_bbox[2] - h_bbox[0]
    draw.text(((WIDTH - h_width) // 2, 22), headline, fill=HEADLINE_COLOR, font=headline_font)
    
    # Draw a separator line
    draw.line([(MARGIN, 78), (WIDTH - MARGIN, 78)], fill=PANEL_BORDER, width=2)
    
    # Stories data
    stories = [
        {
            'icon': 'oil',
            'title': 'Oil Tanker Damaged in Strait of Hormuz',
            'region': 'MIDDLE EAST',
        },
        {
            'icon': 'airstrike',
            'title': 'Saudi Airstrikes on Houthi Targets in Yemen',
            'region': 'MIDDLE EAST',
        },
        {
            'icon': 'missile',
            'title': 'Russian Missile Hits Poland Near NATO Exercise',
            'region': 'EUROPE',
        },
        {
            'icon': 'boat',
            'title': 'Nigeria Boat Capsizes: 30 Dead, ~300 Missing',
            'region': 'AFRICA',
        },
        {
            'icon': 'strike',
            'title': 'Italy General Strike Paralyzes Transport',
            'region': 'EUROPE',
        },
        {
            'icon': 'math',
            'title': 'Anthropic Claims Riemann Proof via AI',
            'region': 'GLOBAL',
        },
        {
            'icon': 'handshake',
            'title': 'UK–EU Deal on Food, Emissions, Youth Mobility',
            'region': 'EUROPE',
        },
        {
            'icon': 'balance',
            'title': 'Iraq PM Reaches Deal with Kata\'ib Hezbollah',
            'region': 'MIDDLE EAST',
        },
    ]
    
    # Layout: 4 rows x 2 columns
    rows, cols = 4, 2
    panel_w = (WIDTH - 2 * MARGIN - (cols - 1) * PANEL_PADDING) // cols
    panel_h = (HEIGHT - 90 - 2 * MARGIN - (rows - 1) * PANEL_PADDING) // rows
    
    icon_size = 52
    
    for idx, story in enumerate(stories):
        row = idx // cols
        col = idx % cols
        
        x = MARGIN + col * (panel_w + PANEL_PADDING)
        y = 90 + row * (panel_h + PANEL_PADDING)
        
        # Panel background with rounded corners
        draw.rounded_rectangle(
            [x, y, x + panel_w, y + panel_h],
            radius=10,
            fill=PANEL_BG,
            outline=PANEL_BORDER,
            width=2
        )
        
        # Icon area (left side)
        icon_x = x + PANEL_PADDING
        icon_y = y + PANEL_PADDING
        draw_icon(draw, icon_x, icon_y, icon_size, story['icon'], ICON_COLOR)
        
        # Region tag (top-right) - solid background
        region_text = story['region']
        r_bbox = draw.textbbox((0, 0), region_text, font=region_font)
        r_width = r_bbox[2] - r_bbox[0]
        r_height = r_bbox[3] - r_bbox[1]
        tag_pad_x, tag_pad_y = 10, 5
        tag_x1 = x + panel_w - PANEL_PADDING - r_width - 2 * tag_pad_x
        tag_y1 = y + PANEL_PADDING
        tag_x2 = x + panel_w - PANEL_PADDING
        tag_y2 = y + PANEL_PADDING + r_height + 2 * tag_pad_y
        
        draw.rounded_rectangle(
            [tag_x1, tag_y1, tag_x2, tag_y2],
            radius=5,
            fill=REGION_BG,
            outline=REGION_BG,
            width=0
        )
        draw.text(
            (tag_x1 + tag_pad_x, tag_y1 + tag_pad_y),
            region_text,
            fill=REGION_TEXT,
            font=region_font
        )
        
        # Title text (next to icon, wrapped)
        text_x = icon_x + icon_size + 12
        text_max_w = panel_w - (icon_size + 12) - PANEL_PADDING - (r_width + 2 * tag_pad_x + 10) - 10
        if text_max_w < 150:
            text_max_w = panel_w - (icon_size + 12) - PANEL_PADDING - 10
        
        lines = wrap_text(draw, story['title'], title_font, text_max_w)
        
        line_height = 28
        total_text_h = len(lines) * line_height
        start_y = icon_y + (icon_size - total_text_h) // 2
        
        for i, line in enumerate(lines):
            draw.text((text_x, start_y + i * line_height), line, fill=TEXT_COLOR, font=title_font)
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), 'entry.png')
    img.save(output_path, 'PNG', optimize=True)
    
    # Verify
    size = os.path.getsize(output_path)
    print(f"Saved: {output_path}")
    print(f"Dimensions: {WIDTH}x{HEIGHT}")
    print(f"File size: {size} bytes ({size/1024:.1f} KiB)")
    print(f"Under 1 MiB: {size < 1024*1024}")
    
    # Verify PNG signature
    png_sig = b'\x89PNG\r\n\x1a\n'
    with open(output_path, 'rb') as f:
        sig = f.read(8)
        print(f"PNG signature valid: {sig == png_sig}")


if __name__ == '__main__':
    main()