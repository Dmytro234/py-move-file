import os


def move_file(command: str) -> None:
    parts: list[str] = command.split()
    source: str = parts[1]
    destination: str = parts[2]

    if destination.endswith("/"):
        dest_dir: str = destination
        dest_file: str = os.path.join(dest_dir, os.path.basename(source))
    else:
        dest_file = destination
        dest_dir = os.path.dirname(destination)

    if dest_dir:
        dirs: list[str] = dest_dir.rstrip("/").split("/")
        current_path: str = ""
        for directory in dirs:
            if current_path:
                current_path = os.path.join(current_path, directory)
            else:
                current_path = directory
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as src:
        content: str = src.read()

    with open(dest_file, "w") as dst:
        dst.write(content)

    os.remove(source)
