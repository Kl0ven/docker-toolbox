FROM python:3.11-alpine3.18

WORKDIR /app

COPY requirements.txt .

# hadolint ignore=DL3018
RUN pip install --no-cache-dir -r requirements.txt \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache \
    bash \
    bind-tools \
    bird \
    bridge-utils \
    busybox-extras \
    conntrack-tools \
    curl \
    dhcping \
    drill \
    ethtool \
    file \
    fping \
    git \
    htop \
    httpie \
    iftop \
    iotop \
    iperf \
    iperf3 \
    iproute2 \
    ipset \
    iptables \
    iptraf-ng \
    iputils \
    ipvsadm \
    jq \
    libc6-compat \
    liboping \
    ltrace \
    mtr \
    nano \
    net-tools \
    netcat-openbsd \
    nftables \
    ngrep \
    nmap \
    nmap-nping \
    nmap-scripts \
    openssh \
    openssl \
    procps \
    scapy \
    socat \
    speedtest-cli \
    strace \
    tcpdump \
    tcpflow \
    tcptraceroute \
    util-linux \
    websocat

COPY . .

CMD [ "python", "/app/main.py" ]
