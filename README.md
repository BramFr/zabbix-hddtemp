# Zabbix-hdd-temp

This python script wil read hdd device temperature with smartctl.

Requirements:
```
sudo apt install smartmontools
```

Copy the following file(\`s) `userparameter_hddtemp.conf` and `hddtemp.py` to:
```
/etc/zabbix/zabbix_agentd.d/userparameter_hddtemp.conf
/usr/local/bin/hddtemp.py
```
Don\`t forget to make hddtemp.py executable: `chmod +x /usr/local/bin/hddtemp.py`

Zabbix agent runs with user zabbix that dosn\`t have root/sudo priv. So add the following line to sudoers file:
```
zabbix	ALL=(ALL)NOPASSWD: /usr/sbin/smartctl
```