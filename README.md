# TMobile-5G
WHere I'm gonna store all my TMobile 5G gateway scripts and such. 

Recon:

python3 test_tmobile.py -i 192.168.12.1 -h

usage: test_tmobile.py [-h] [-v] [-i IP_ADDRESS] [-l] [-w] [-c] [-d] [-a] [-f]

Performs Recon on the T-Mobile Internet Gateway 4G/5G device

optional arguments:
  -h, --help            show this help message and exit
  
  -v, --verbose         Verbose logging enabled
  
  -i IP_ADDRESS, --ip IP_ADDRESS
                        The IP address to scan
  
  -l, --lan_stats       Show LAN stats
  
  -w, --wan_stats       Show WAN stats
  
  -c, --config          Shows device configuration as well as all attached devices
  
  -d, --data_fields     Show the different form fields and their expected format
  
  -a, --all             Grabs *all* of the config/stats (can be a lot of data)
  
  -f, --find_links      find valid CGI/JS endpoints






