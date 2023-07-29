# docker-toolbox

Docker + Kubernetes Toolbox for testing and debugging rollout deployment and network issues

This image start a simple http server with a few route. It also contains a suite of network tools.


## Home page `/`
Returns a colored http page. The color and version can be changed using the `COLOR` and `FAKE_VERSION` env variables.

You can change the default port with `HTTP_PORT` env.

```bash
docker run --rm -p 5000:5000 -e COLOR=teal -e FAKE_VERSION=v2.0.0 kloven/docker-toolbox
 * Running on port 0.0.0.0:5000
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on port 0.0.0.0:5000
 * Debugger is active!
[INFO 2023-07-29 16:12:34,905] from 172.26.0.1 on http GET / : 200 OK
[INFO 2023-07-29 16:12:35,448] from 172.26.0.1 on http GET /favicon.ico : 404 NOT FOUND
```


## Health `/health`
Always return 200

## Bad Health `/bad_health`
Always return 500

## Dump `/dump`
Will print The request body / header and environment variable to the console

## Networking Tools

- bash
- bind-tools
- bird
- bridge-utils
- busybox-extras
- conntrack-tools
- curl
- dhcping
- drill
- ethtool
- file
- fping
- git
- htop
- httpie
- iftop
- iotop
- iperf
- iperf3
- iproute2
- ipset
- iptables
- iptraf-ng
- iputils
- ipvsadm
- jq
- libc6-compat
- liboping
- ltrace
- mtr
- nano
- net-tools
- netcat-openbsd
- nftables
- ngrep
- nmap
- nmap-nping
- nmap-scripts
- openssh
- openssl
- procps
- scapy
- socat
- speedtest-cli
- strace
- tcpdump
- tcpflow
- tcptraceroute
- util-linux
- websoc
