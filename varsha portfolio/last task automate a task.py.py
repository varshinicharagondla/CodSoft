import os
import shutil
from datetime import datetime

source = input("Enter full folder path to organize: ").strip()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
organized_root = os.path.join(source, f"Organized_{timestamp}")
os.makedirs(organized_root, exist_ok=True)
log_file = os.path.join(organized_root, "log.txt")

file_groups = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Code": [".py", ".js", ".html", ".cpp"],
    "Audio": [".mp3", ".wav"]
}

with open(log_file, "w") as log:
    for file in os.listdir(source):
        full_path = os.path.join(source, file)
        if os.path.isfile(full_path):
            name, ext = os.path.splitext(file)
            placed = False
            for group, extensions in file_groups.items():
                if ext.lower() in extensions:
                    target = os.path.join(organized_root, group)
                    os.makedirs(target, exist_ok=True)
                    shutil.move(full_path, os.path.join(target, file))
                    log.write(f"{file} -> {group}\n")
                    placed = True
                    break
            if not placed:
                other = os.path.join(organized_root, "Others")
                os.makedirs(other, exist_ok=True)
                shutil.move(full_path, os.path.join(other, file))
                log.write(f"{file} -> Others\n")

print("Organizing done. Files moved to:", organized_root)
