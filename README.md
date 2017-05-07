# Unotify

This program needs to be set up manually. Right now I have only tried this for linux, I will soon write the installation manual for windows..

# Ubuntu
first get pip

$ sudo apt-get install python-pip python-dev build-essential 

$ sudo pip install --upgrade pip 

$ sudo pip install --upgrade virtualenv 

Download all the files and place them in a same repository and name it :
Unotify.py

Unotify should be in /home/user_name/

in Unotify create a file: main.sh and write the following commands:

cd path_to_Unotify

python main.py

make another file: switch.sh and type following commands into it:

cd path_to_Unotify

python main.py

make the files executable

$cd path_to_Unotify

$chmod +x main.sh

$chmod +x Switch.sh

click Search your computer button and search for Startup Applications, open it.

click add button, click browse and select main.sh
do the same for switch.sh

great.. it is now up and running.. thax for using 
feel free to contact prajapatiutxav@gmail.com for feedbacks thanks a lot
