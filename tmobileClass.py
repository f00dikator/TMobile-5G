# -*- coding: utf-8 -*-
# Version: 1.0.0

__author__ = 'John Lampe'
__email__ = 'dmitry.chan@gmail.com'

import requests
import pdb


class tmobile:
    def __init__(self, ip, verify=False):
        self.ip = ip
        self.base_url = "http://{}".format(ip)
        self.session = requests.Session()
        self.session.verify = verify
        self.session.headers = {"Content-Type": "application/x-www-form-urlencoded",
                                "Accept": "application/json",
                                "Sec-GPS": "1",
                                "Referer": "{}/web_whw".format(self.base_url),
                                "Accept-Encoding": "gzip, deflate"}
        self.load_cgis()

    def load_cgis(self):
        self.cgi_files = [
            "login_web_app.cgi",
            "check_expire_web_app.cgi",
            "main_web_app.cgi",
            "system_web_app.cgi",
            "device_status_web_app.cgi",
            "dashboard_device_info_status_web_app.cgi",
            "fastmile_statistics_status_web_app.cgi",
            "fastmile_radio_status_web_app.cgi",
            "lan_ipv4_status_web_app.cgi",
            "statistics_status_web_app.cgi",
            "pon_status_web_app.cgi",
            "voice_info_status_web_app.cgi",
            "lan_ipv6_status_web_app.cgi",
            "wan_config_glb_status_web_app.cgi",
            "wifi_schedule_status_web_app.cgi",
            "dashboard_status_web_app.cgi",
            "wan_internet_status_web_app.cgi",
            "wlan_config_status_web_app.cgi",
            "wan_dhcp_status_web_app.cgi",
            "tr69_status_web_app.cgi",
            "qos_status_web_app.cgi",
            "route_status_web_app.cgi",
            "access_control_status_web_app.cgi",
            "dns_status_web_app.cgi",
            "reboot_web_app.cgi",
            "ddns_status_web_app.cgi",
            "ipfilter_status_web_app.cgi",
            "device_name_status_web_app.cgi",
            "sntp_status_web_app.cgi",
            "macfilter_status_web_app.cgi",
            "urlfilter_status_web_app.cgi",
            "password_status_web_app.cgi",
            "xlink_status_web_app.cgi",
            "xlink_web_app.cgi",
            "upgrade_web_app.cgi",
            "diag_status_web_app.cgi",
            "parental_control_status_web_app.cgi",
            "mesh_status_web_app.cgi",
            "troubleshooting_status_web_app.cgi",
            "slidconfig_status_web_app.cgi",
            "loidconfig_status_web_app.cgi",
            "storage_status_web_app.cgi",
            "whw_beacon_mode_app_web_app.cgi",
            "dongle_status_web_app.cgi",
            "uplink_management_status_web_app.cgi",
            "dashboard_device_status_web_app.cgi",
            "dashboard_ntwtopo_status_web_app.cgi",
            "fastmile_statistics_status_web_app.cgi",
            "apn_config_status_web_app.cgi",
            "radio_config_status_web_app.cgi",
            "multi_apn_status_web_app.cgi",
            "multi_apn_delete_web_app.cgi",
            "multi_apn_config_web_app.cgi"
            ]
        self.cgi_dirs = ["/web_whw/", "/cgi-bin/", "/"]

    def find_cgi_locations(self):
        for dirs in self.cgi_dirs:
            for files in self.cgi_files:
                try:
                    ret = self.session.get("{}{}{}".format(self.base_url,dirs,files))
                    if ret.status_code != 404:
                        print("{} - Found path of {}{}{}".format(ret.status_code, self.base_url,dirs,files))
                except Exception as e:
                    print("Error requesting {}{}{}. Error: {}".format(self.base_url,dirs,files,e))

    def show_all(self):
        self.lan_status()
        self.wan_status()
        self.main_status()
        self.data_fields()
        self.web_stats()

    def lan_status(self):
        print("LAN Stats")
        try:
            ret = self.session.get("{}/lan_status_web_app.cgi?lan".format(self.base_url))
            print(ret.json())
        except Exception as e:
            print("Error retrieving LAN Stats. Error: {}".format(e))

    def wan_status(self):
        print("WAN Stats")
        try:
            ret = self.session.get("{}/fastmile_statistics_status_web_app.cgi".format(self.base_url))
            print(ret.json())
        except Exception as e:
            print("Error retrieving WAN Stats. Error: {}".format(e))

    def main_status(self):
        #main_web_app.cgi
        print("Device Config and attached devices")
        try:
            ret = self.session.get("{}/main_web_app.cgi".format(self.base_url))
            print(ret.json())
        except Exception as e:
            print("Error retrieving device config and attached devices. Error: {}".format(e))

    def data_fields(self):
        #GET /web_whw/assets/i18n/en.json
        print("Information about the configured data fields format")
        try:
            ret = self.session.get("{}/web_whw/assets/i18n/en.json".format(self.base_url))
            print(ret.json())
        except Exception as e:
            print("Error retrieving configured data field formats. Error: {}".format(e))

    def web_stats(self):
        #/statistics_status_web_app.cgi
        print("Web App Statistics")
        try:
            ret = self.session.get("{}/statistics_status_web_app.cgi".format(self.base_url))
            print(ret.json())
        except Exception as e:
            print("Error retrieving Web App statistics. Error: {}".format(e))

