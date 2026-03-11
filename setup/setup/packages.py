import subprocess


def run_command(command: list[str]) -> bool:
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def update_system() -> bool:
    return run_command(["apt", "update"])


def install_packages(packages: list[str]) -> bool:
    if not packages:
        return True
    return run_command(["apt", "install", "-y", *packages])
