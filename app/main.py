import os
import shutil


def move_file(command: str) -> None:
    parts: list[str] = command.split()
    # parts[0] = "mv", parts[1] = source, parts[2] = destination
    source: str = parts[1]
    destination: str = parts[2]

    # If destination ends with '/', treat it as a directory path
    if destination.endswith("/"):
        dest_dir: str = destination
        dest_file: str = os.path.join(dest_dir, os.path.basename(source))
    else:
        dest_file = destination
        dest_dir = os.path.dirname(destination)

    # Create all intermediate directories if needed
    if dest_dir:
        dirs: list[str] = dest_dir.rstrip("/").split("/")
        current_path: str = ""
        for directory in dirs:
            current_path = os.path.join(current_path, directory) if current_path else directory
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    # Copy file content to destination
    with open(source, "r") as src:
        content: str = src.read()

    with open(dest_file, "w") as dst:
        dst.write(content)

    # Remove the source file
    os.remove(source)
