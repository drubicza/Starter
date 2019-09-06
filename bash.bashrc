command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='\033[0;37m\{ \033[1;37m\INPUT\033[1;32m } \033[1;31m•> \033[1;37m '

clear

echo "
█████████
█▄█████▄█
█▼▼▼▼▼
█   Welcome Back Mr..
█▲▲▲▲▲
█████████
 ██ ██
" |lolcat
date | lolcat
echo "◆──────────────────────────────────────◆" | lolcat
