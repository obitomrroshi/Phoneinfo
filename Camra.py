#!/usr/bin/env python3
# camra.py
# Full Termux camera script
# Opens the camera, takes a photo, and saves it to your storage

import subprocess
import time
import os

def ensure_storage():
    """
    Ensure Termux has storage access.
    """
    try:
        subprocess.run(["termux-setup-storage"], check=True)
    except subprocess.CalledProcessError:
        print("Warning: Could not request storage access.")

def take_photo():
    """
    Opens Termux camera UI and saves a photo to DCIM/Camera
    """
    # Create filename with timestamp
    filename = f"/sdcard/DCIM/Camera/photo_{int(time.time())}.jpg"

    try:
        # Open camera via Termux API
        subprocess.run(["termux-camera-photo", filename], check=True)
        print(f"✅ Photo saved to: {filename}")
    except FileNotFoundError:
        print("❌ Error: termux-camera-photo not found. Install termux-api first.")
    except subprocess.CalledProcessError:
        print("❌ Camera operation failed. Make sure permissions are granted.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    print("📸 Opening camera...")
    ensure_storage()
    take_photo()
    print("Done.")

if __name__ == "__main__":
    main()
