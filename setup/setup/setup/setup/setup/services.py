import subprocess


def manage_services(services: list[str]) -> bool:
    success = True

    for service in services:
        try:
            subprocess.run(["systemctl", "enable", service], check=True)
            subprocess.run(["systemctl", "start", service], check=True)
        except subprocess.CalledProcessError:
            success = False

    return success
