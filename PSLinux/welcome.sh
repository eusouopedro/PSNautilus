#!/bin/bash

echo "Bem Vindo $USER ao terminal do $HOSTNAME!"

curl wttr.in/?0

uptime >> /home/$USER/.welcome.data
