import json
import os
from datetime import datetime
from pathlib import Path

from setup.packages import update_system, install_packages
from setup.users import create_user
from setup.firewall import configure_firewall
from setup.services import manage_services
from setup.security import harden_ssh


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "setup.log"
CONFIG_FILE = "config.json"


def log_message(message: str) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(entry + "\n")


def load_config(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def check_root() -> bool:
    return os.geteuid() == 0


def main() -> None:
    if not check_root():
        print("Please run this tool with sudo or as root.")
        return

    log_message("Starting automated server setup")

    try:
        config = load_config(CONFIG_FILE)
    except FileNotFoundError:
        log_message("Config file not found.")
        return
    except json.JSONDecodeError:
        log_message("Config file is invalid.")
        return

    packages = config.get("packages", [])
    new_user = config.get("new_user", "")
    ssh_port = config.get("ssh_port", 22)
    allowed_ports = config.get("allowed_ports", [22])
    services = config.get("services", [])

    if update_system():
        log_message("System package list updated successfully")
    else:
        log_message("Failed to update package list")

    if install_packages(packages):
        log_message(f"Packages installed successfully: {packages}")
    else:
        log_message("Failed to install one or more packages")

    if new_user:
        if create_user(new_user):
            log_message(f"User setup completed: {new_user}")
        else:
            log_message(f"Failed to create user: {new_user}")

    if configure_firewall(allowed_ports):
        log_message(f"Firewall configured for ports: {allowed_ports}")
    else:
        log_message("Firewall configuration encountered errors")

    if manage_services(services):
        log_message(f"Services enabled and started: {services}")
    else:
        log_message("Service setup encountered errors")

    if harden_ssh(ssh_port):
        log_message(f"SSH hardened successfully. Port set to {ssh_port}")
        log_message("Restart ssh service manually if needed: systemctl restart ssh")
    else:
        log_message("SSH hardening failed")

    log_message("Server setup completed")


if __name__ == "__main__":
    main()
