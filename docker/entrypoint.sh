#!/usr/bin/bash

echo "Starting SSH server ..."
service ssh start

echo "Startup finished"
tail -F anything