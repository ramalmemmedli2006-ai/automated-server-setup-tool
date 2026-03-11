import subprocess


def user_exists(username: str) -> bool:
    result = subprocess.run(
        ["id", username],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def create_user(username: str) -> bool:
    if user_exists(username):
        return True

    try:
        subprocess.run(["adduser", "--disabled-password", "--gecos", "", username], check=True)
        subprocess.run(["usermod", "-aG", "sudo", username], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
