from pathlib import Path


SSH_CONFIG_PATH = Path("/etc/ssh/sshd_config")


def harden_ssh(ssh_port: int) -> bool:
    try:
        if not SSH_CONFIG_PATH.exists():
            return False

        content = SSH_CONFIG_PATH.read_text(encoding="utf-8")

        updated_lines = []
        port_set = False
        root_login_set = False

        for line in content.splitlines():
            stripped = line.strip()

            if stripped.startswith("Port ") or stripped.startswith("#Port "):
                updated_lines.append(f"Port {ssh_port}")
                port_set = True
            elif stripped.startswith("PermitRootLogin ") or stripped.startswith("#PermitRootLogin "):
                updated_lines.append("PermitRootLogin no")
                root_login_set = True
            else:
                updated_lines.append(line)

        if not port_set:
            updated_lines.append(f"Port {ssh_port}")

        if not root_login_set:
            updated_lines.append("PermitRootLogin no")

        SSH_CONFIG_PATH.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
        return True
    except Exception:
        return False
