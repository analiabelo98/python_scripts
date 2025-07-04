#Purpose: Automate directory backups with timestamped folders
#Usage: python3 [source] [target]

import os
import shutil
from datetime import datetime
import sys

def create_backup(source, target):
    """
    Parameters:
        source (str): Path to the source directory to back up
        target (str): Path where the backup folder will be created
    """
    if not os.path.exists(source):
        print(f"Error: folder '{source}' does not exist.")
        return False
    
    #Generate a timestamp for the backup folder name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #Create the full path for the backup directory
    backup_dir = os.path.join(target, f"backup_{timestamp}")

    try:
        # Copy the entire source directory to the backup folder
        shutil.copytree(source, backup_dir)
        
        print(f"[+] Backup created at: {backup_dir}")
        return True
    except Exception as e:
        print(f"[-] Error creating backup: {e}")
        return False


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("[⚠️] Uso: python3 backup.py [source] [target]")
        sys.exit(1)

    source = sys.argv[1]
    target = sys.argv[2]

    create_backup(source, target)