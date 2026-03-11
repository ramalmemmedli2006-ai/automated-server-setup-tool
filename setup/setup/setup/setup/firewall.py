import subprocess


def run_command(command: list[str]) -> bool:
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def configure_firewall(allowed_ports: list[int]) -> bool:
    success = True

    success &= run_command(["ufw", "--force", "enable"])

    for port in allowed_ports:
        if not run_command(["ufw", "allow", str(port)]):
            success = False

    return success
