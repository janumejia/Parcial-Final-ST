sudo -i
#Inicair streama start
sudo service streama start
#instalar httpd
sudo yum -y install httpd mod_ssl
#Iniciar httpd
systemctl start httpd