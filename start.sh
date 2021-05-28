#! /bin/bash 

echo "Diagslave is running..."
diagslave/x86_64-linux-gnu/diagslave -m tcp > logfile 2>&1 &

while : ; do echo "${MESSAGE=Idling...}"; sleep ${INTERVAL=600}; done