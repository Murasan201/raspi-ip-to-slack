# raspi-ip-to-slack

Automatically send your Raspberry Pi’s IP address to Slack on system startup.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running as a Service](#running-as-a-service)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
- Retrieves the Pi’s primary network IP using `hostname -I` (with a socket fallback).
- Posts a formatted notification to Slack via Incoming Webhook.
- Configurable via environment variable `SLACK_WEBHOOK_URL`.
- Launches automatically at boot with systemd after the network is online.

## Prerequisites
- Raspberry Pi running Raspberry Pi OS (or another Debian-based distro).
- Python 3 installed (`python3`).
- `requests` library for Python:
  ```bash
  pip3 install --user requests
  ```
- A Slack Incoming Webhook URL.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/raspi-ip-to-slack.git
   cd raspi-ip-to-slack
   ```
2. Make the script executable:
   ```bash
   chmod +x slack_ip_notify.py
   ```

## Configuration
1. **Set the Slack Webhook URL**
   - For your user session (interactive shell):
     ```bash
     echo 'export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/AAA/BBB/CCC"' >> ~/.bashrc
     source ~/.bashrc
     ```
   - Or globally for all services: edit `/etc/environment`:
     ```bash
     sudo sh -c 'echo "SLACK_WEBHOOK_URL="https://hooks.slack.com/services/AAA/BBB/CCC"" >> /etc/environment'
     ```
   - Or create an environment file for systemd:
     ```bash
     echo 'export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/AAA/BBB/CCC"' | sudo tee /etc/profile.d/slack.sh
     sudo chmod +x /etc/profile.d/slack.sh
     ```

## Usage
- Test the script manually:
  ```bash
  ./slack_ip_notify.py
  ```
- You should see a notification in your configured Slack channel with the Pi’s IP.

## Running as a Service
1. Copy the systemd unit file:
   ```bash
   sudo cp slack_ip_notify.service /etc/systemd/system/
   ```
2. Reload systemd and enable the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable slack_ip_notify.service
   ```
3. Start and check status:
   ```bash
   sudo systemctl start slack_ip_notify.service
   sudo journalctl -u slack_ip_notify.service --no-pager
   ```

## File Structure
```
raspi-ip-to-slack/
├── slack_ip_notify.py     # Main Python script
├── slack_ip_notify.service # systemd unit definition
└── README.md              # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes and push: `git push origin feature-name`.
4. Open a Pull Request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
- **Murasan** – [https://murasan-net.com/](https://murasan-net.com/)
