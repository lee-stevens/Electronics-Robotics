# Raspberry Pi

## Setting up a Raspberry Pi

### Login Details

Check Password Manager for username and password, if password is forgotten somehow, then just type `sudo passwd lee-pi` and set a new one

### Install Git 

```shell
sudo apt-get install git

#Then add username and email
git config --global user.name "Metal-Mantis-Studio"
git config --global user.email "Leepeterstevens@gmail.com"

#Clone the repo
git clone https://github.com/Metal-Mantis-Studio/Electronics-Robotics

#Pull/Push
git pull
git push
```

### Install GitKraken for a GUI

```shell
wget https://release.gitkraken.com/linux/gitkraken-amd64.deb
sudo apt install ./gitkraken-amd64.deb
```

Or via the [website](https://www.gitkraken.com/git-client/try-free)



## Connecting to a Raspberry Pi via Windows

[Official docs](https://www.raspberrypi.com/documentation/computers/remote-access.html)

1. Install RealVNCViewer via the website for both Windows and Ubuntu and login 

1. Find the Local IP via `hostname -I`
Also you could use `nmcli device show` to directly use the Network Manager CLI
We do not care about trailing numbers i.e., /24 at the end of an IP address.

2. Enable SSH and VNC via `sudo raspi-config` --> Interfacing Options --> SSH --> Yes --> VNC --> Yes

3. The server username and password are those found in my Password Manager - Look for the device name and it'll come up