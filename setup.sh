# Runs as root

# Install IPFS
snap install ipfs
ipfs init
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/readme

# Install Apache
apt-get install -y apache2

# Install dependencies
apt-get install -y wget python3 vim git

# Make sym link to server dir
ln -s /var/www/html ~/data

