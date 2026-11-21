#!/usr/bin/env python3
"""
Main entry point for the news image generator.
Copies entry.png to /output/entry.png, creating /output if needed.
"""

import os
import shutil
import sys


def main():
    # Source image is next to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, 'entry.png')
    
    # Destination
    dst_dir = '/output'
    dst = os.path.join(dst_dir, 'entry.png')
    
    # Create output directory if needed
    os.makedirs(dst_dir, exist_ok=True)
    
    # Copy the file
    if not os.path.exists(src):
        print(f"Error: Source image not found at {src}", file=sys.stderr)
        return 1
    
    shutil.copy2(src, dst)
    print(f"Copied {src} -> {dst}")
    return 0


if __name__ == '__main__':
    sys.exit(main())