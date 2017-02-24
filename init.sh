#!/bin/bash

#delete nginx default conf
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

#create symlink on our nginx config and restart
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ask.conf
sudo /etc/init.d/nginx restart

#create symlink for our gunicorn config and restart
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

# MYSQL
sudo service mysql restart

sudo mysql -uroot -e "CREATE DATABASE qa CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'django'@'localhost' IDENTIFIED BY '';"


# NEED EMPTY USER PASS
# sudo mysql -uroot -e "CREATE DATABASE qa;"
# sudo mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY '';"
# sudo mysql -uroot -e "GRANT ALL ON qa.* TO 'django@localhost';"
# sudo mysql -uroot -e "FLUSH PRIVILEGES;"
