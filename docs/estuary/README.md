# Install [Estuary](https://github.com/application-research/estuary) for IPFS
### [Install Go](https://go.dev/doc/install)
```
wget https://go.dev/dl/go1.18.linux-amd64.tar.gz
sudo tar -C /usr/local -xvf go1.18.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.profile
source ~/.profile

```

### Install [dependencies](https://github.com/application-research/estuary#building) (Ubuntu 20.04)
```
sudo apt-get install -y jq ocl-icd-opencl-dev libhwloc-dev pkg-config

```

### Build from [source](https://github.com/application-research/estuary)
```
git clone https://github.com/application-research/estuary.git
cd estuary
make clean all

```

### Setup
```
ulimit -n 10000
./estuary setup

```

### [Example Usage](https://github.com/application-research/estuary/tree/master/scripts/samples)
