#!/bin/sh
set -e
/usr/sbin/sshd -e -f /etc/ssh/ssh_config
exec python /app/main.py
