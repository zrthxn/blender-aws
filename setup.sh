sudo yum update -y
sudo nvidia-smi -pm 1
sudo nvidia-smi -acp 0
sudo nvidia-smi --auto-boost-permission=0
sudo nvidia-smi -ac 2505,875

sudo chmod 755 /home/ec2-user
sudo service nginx start