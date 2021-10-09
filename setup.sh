# Runs as root

# Install IPFS
snap install ipfs
ipfs init
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/readme

# Install Apache
apt-get install -y apache2

# Make sym link to server dir
ln -s /var/www/html ~/data

