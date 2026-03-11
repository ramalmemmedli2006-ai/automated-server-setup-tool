# Automated Server Setup Tool

A Python-based tool that automates the initial configuration of a Linux server for system administration and IT infrastructure tasks.

## Author
Ramal Memmedli  
IT Student | Network | Cybersecurity | Helpdesk | System Administration

---

## Project Overview

Automated Server Setup Tool helps system administrators and IT students quickly prepare a Linux server with common packages, firewall rules, user creation, service setup, and basic security hardening.

This project is useful for:
- Linux server setup automation
- System administration practice
- DevOps and infrastructure learning
- Building a strong GitHub portfolio project

---

## Features

- Install common server packages
- Create a new admin user
- Configure UFW firewall
- Enable and start important services
- Apply basic SSH security settings
- Log actions to a file
- Use a JSON configuration file

---

## Tech Stack

- Python
- Subprocess
- JSON
- Linux system commands

---

## Project Structure

```text
automated-server-setup-tool/
├── README.md
├── requirements.txt
├── main.py
├── config.json
├── setup/
│   ├── packages.py
│   ├── firewall.py
│   ├── users.py
│   ├── services.py
│   └── security.py
└── logs/
