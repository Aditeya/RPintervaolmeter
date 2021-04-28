#!/bin/sh

ip link set up dev eno1
ip addr add 192.168.4.100/24 dev eno1

systemctl start dhcpd4.service

sysctl net.ipv4.ip_forward=1

iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eno1 -o wlan0 -j ACCEPT

ip neigh | grep eno1
