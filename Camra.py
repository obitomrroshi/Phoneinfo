#!/usr/bin/env python3
# camra.py
# Simple Termux script to open camera and save a photo

import subprocess
import time
import os

def take_photo():
    # Path to save the photo
    filename = f"/sdcard/DCIM/Camera/photo_{int(time.time())}.jpg"

    try:
        # Open the camera using Termux API
        subprocess.run(["termux-camera-photo", filename], check=True)
        print(f"Photo saved to: {filename}")
    except FileNotFoundError:
        print("Error: termux-camera-photo not found. Install termux-api first.")
    except subprocess.CalledProcessError:
        print("Camera operation failed.")

if __name__ == "__main__":
    take_photo()
