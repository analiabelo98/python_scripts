import shutil
import sys

def check_disk_usage(threshold=80):
    total, used, free = shutil.disk_usage("/")

    # Convert to GB
    total_gb = used // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    percent_used = (used / total) * 100

    print(f"Total: {total_gb} GB")
    print(f"Usado: {used_gb} GB")
    print(f"Libre: {free_gb} GB")
    print(f"Uso del disco: {percent_used:.2f}%")

    if percent_used > threshold:
        print("[ALERTA] ¡El uso del disco está por encima del umbral!")
        return False
    else:
        print("Uso del disco OK.")
        return True

if __name__ == "__main__":
    threshold = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    check_disk_usage(threshold)