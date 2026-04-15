import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command. Expected format: mv <source> <destination>"
        )

    cmd, source, destination = parts

    if destination.endswith("/"):
        dest_dir = destination
        dest_file = os.path.join(dest_dir, os.path.basename(source))
    else:
        dest_file = destination
        dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as src:
        content: str = src.read()

    with open(dest_file, "w") as dst:
        dst.write(content)

    os.remove(source)
