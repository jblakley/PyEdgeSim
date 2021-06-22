#!/usr/bin/env python
import sys
import os

def oscmd(cmdstr): # Prints out to console and returns exit status
    return os.system(cmdstr)
oscmd("sudo apt update")
''' Java '''
oscmd("sudo apt install default-jdk -y")
oscmd("sudo apt install openjdk-8-jre -y")

''' K9s '''

oscmd("sudo apt install -y linuxbrew-wrapper jq influxdb-client webpack npm")
oscmd("brew install k9s")
oscmd("echo alias k9s=\'$HOME/.linuxbrew/bin/k9s\' >> ~/.bashrc")

pipsetup="pip install requests;pip install -r pip_requirements.txt"
setupclient="python lib/setupAutomation.py"

cmdstr = "bash -c ' {} && {}' ".format(pipsetup,setupclient)
oscmd(cmdstr)

cmdstr = "lib/_installgdal.sh"
oscmd(cmdstr)
