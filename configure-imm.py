#!/usr/bin/python
import os
import getpass
import paramiko

#Take password as input from user
pas = getpass.getpass("Please enter password: \n")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#get hostnames in a list from the file
with open('host-name.txt', 'r') as h:
    hostNames = [line.strip() for line in h]

#variable to be used for rotating the above list
i=0

#function to do execute the command
def cmdExec(cmd):
  stdin,stdout,stderr = ssh.exec_command(cmd)
  outlines=stdout.readlines()
  resp=''.join(outlines)
  print(resp)

#connect to imm ssh one by one and execute commands
with open("host-list.txt","r") as f:
    for host in f:
      hostname= hostNames[i]
      ssh.connect(host,22,'USERID',pas)
      cmdExec("ifconfig eth0 -n %s" %(hostname))
      cmdExec("smtp -s 69.26.45.167")
      cmdExec("smtp -pn 25")
      cmdExec("dns -ddns enabled")
      cmdExec("dns -dnsrc manual")
      cmdExec("dns -ddn testmail.com")
      cmdExec("alertentries -1 -n testGroup")
      cmdExec("alertentries -1 -e test@test.com")
      cmdExec("alertentries -1 -type email")
      cmdExec("alertentries -1 -crt all")
      cmdExec("alertentries -1 -crten enabled")
      cmdExec("alertentries -1 -wrn custom:cp|me")
      cmdExec("alertentries -1 -wrnen enabled")
      cmdExec("alertentries -1 -sys custom:bf|el")
      cmdExec("alertentries -1 -sysen enabled")
      cmdExec("alertentries -1 -status on")
      #optional, if you want to send a test alert
      #cmdExec("alertentries -1 -test")
      i=+1
f.close()
