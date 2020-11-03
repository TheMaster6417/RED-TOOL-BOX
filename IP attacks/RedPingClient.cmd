@echo off

color 4

title Red Ping Tool

echo d8888b. d88888b d8888b.   d8888b. d888888b d8b   db  d888b     .o88b. db      d888888b d88888b d8b   db d888888b 
echo 88  `8D 88'     88  `8D   88  `8D   `88'   888o  88 88' Y8b   d8P  Y8 88        `88'   88'     888o  88 `~~88~~' 
echo 88oobY' 88ooooo 88   88   88oodD'    88    88V8o 88 88        8P      88         88    88ooooo 88V8o 88    88    
echo 88`8b   88~~~~~ 88   88   88~~~      88    88 V8o88 88  ooo   8b      88         88    88~~~~~ 88 V8o88    88    
echo 88 `88. 88.     88  .8D   88        .88.   88  V888 88. ~8~   Y8b  d8 88booo.   .88.   88.     88  V888    88    
echo 88   YD Y88888P Y8888D'   88      Y888888P VP   V8P  Y888P     `Y88P' Y88888P Y888888P Y88888P VP   V8P    YP    
                                                                                                                

set /p IP=Enter IP::
:top
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=0b & echo ip is down.) 
color 4
ping -t 2 0 10 127.0.0.1 >nul
GoTo top 