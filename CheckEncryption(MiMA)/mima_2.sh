# Ansi color code variables
orange="\033[0;33m"
green="\e[0;92m"
reset="\e[0m"
red="\033[0;31m"

# run script
echo -e "${green}[2/2]Collect IoT network traffic!${reset}"
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

echo -e "${orange}Loading Wireshark...${reset}"
echo "[ctrl+c to interrupt]"
echo "Wait 10 secounds..."
sleep 10

tshark -i $netint -w result.pcap -f "host dddrey.info" -a duration:30
