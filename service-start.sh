#!/bin/bash

ssh -tt jenkins@192.168.1.104
cd /
ls -la
cd /shell-script
./mysql.sh

=================================================================
#!/bin/bash

service httpd status | grep 'active (running)' > /dev/null 2>&1

if [ $? != 0 ]
then
        sudo service httpd restart > /dev/null
fi
===============Final Script=======================================
#!/bin/bash

ssh -tt jenkins@192.168.1.104
cd /
ls -la
service httpd status | grep 'active (running)' > /dev/null 2>&1

if [ $? != 0 ]
then
        sudo service httpd restart > /dev/null
fi
