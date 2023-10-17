Disclamer!
The script is only for your own environment. Running it in other environments is illegal without the owner's consent. We assume no liability for this but provide the script only for review of your own environment.

Description:
This script captures the networktraffic of your IoT Device.
It simulates a Man in the Middle Attack to check the encryption of 
your IoT device. 
This script is only for your your Environment. 
Frist run script mima_1 and during that mima_2.
Be sure that the Sniffer of script 1 is Running.

Prerequisites:
Ensure Bettercap and Whireshart/ tshark is installed on your system.

mima_1.sh:
This script allows you to select a network interface, run Bettercap, and perform ARP spoofing for a specified target.

1.Execute the script: ./mima_1.sh
2.The script will display available network interfaces using ifconfig.
3.Select a network interface by entering its name when prompted.
4.Bettercap is launched on the selected interface using the "control" caplet to collect device information.
5.Enter the target's IP address when prompted.
6.ARP spoofing is enabled, and network sniffing begins.
7.You can interrupt the script at any time by pressing Ctrl+C.

Ensure that Bettercap is properly installed on your system and run the script with appropriate permissions.

mima_2.sh:
1.Execute the script: ./mima_2.sh
2.The script displays available network interfaces using ifconfig.
3.Select a network interface by entering its name when prompted.
4.tshark is launched to capture packets destined for the host with the domain dddrey.info.
5.The capture duration is set to 30 seconds.
6.You can interrupt the packet capture at any time by pressing Ctrl+C.
Ensure that tshark (Wireshark) is installed on your system before running the script.

by IoTech 



