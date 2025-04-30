#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import subprocess
import requests
import sys

def get_ip_address():
    """
    プライマリなネットワークインターフェースのIPアドレスを取得。
    `hostname -I` コマンドの結果から最初のIPを返す。
    """
    try:
        output = subprocess.check_output(['hostname', '-I'], stderr=subprocess.DEVNULL)
        ip = output.decode('utf-8').strip().split()[0]
        return ip
    except Exception:
        try:
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except Exception as e:
            print(f"IP取得エラー: {e}", file=sys.stderr)
            return None

def post_to_slack(message: str):
    """
    環境変数 SLACK_WEBHOOK_URL に設定された Incoming Webhook にメッセージを送信。
    """
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print("環境変数 SLACK_WEBHOOK_URL が設定されていません", file=sys.stderr)
        sys.exit(1)

    payload = {"text": message}
    resp = requests.post(webhook_url, json=payload)
    if resp.status_code != 200:
        print(f"Slack 通知失敗: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)

def main():
    ip = get_ip_address()
    if not ip:
        sys.exit(1)

    message = f":satellite: Raspberry Pi が起動しました\nIP アドレス: `{ip}`"
    post_to_slack(message)

if __name__ == "__main__":
    main()
