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

