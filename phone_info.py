import platform
import subprocess

def get_basic_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return info

def get_android_specific_info():
    info = {}
    try:
        manufacturer = subprocess.check_output("getprop ro.product.manufacturer", shell=True).decode().strip()
        model = subprocess.check_output("getprop ro.product.model", shell=True).decode().strip()
        android_version = subprocess.check_output("getprop ro.build.version.release", shell=True).decode().strip()
        sdk = subprocess.check_output("getprop ro.build.version.sdk", shell=True).decode().strip()

        info["Manufacturer"] = manufacturer
        info["Model"] = model
        info["Android Version"] = android_version
        info["SDK Level"] = sdk
    except Exception as e:
        info["Error"] = str(e)
    return info

def main():
    print("📱 PHONE INFORMATION")
    print("-" * 40)

    basic_info = get_basic_info()
    for key, value in basic_info.items():
        print(f"{key}: {value}")

    print("\n📲 ANDROID-SPECIFIC INFORMATION")
    print("-" * 40)
    android_info = get_android_specific_info()
    for key, value in android_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
