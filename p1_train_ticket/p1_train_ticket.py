#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
import requests
import pprint
import sys


def search_tickets():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2016-11-08&leftTicketDTO.from_station=AOH&leftTicketDTO.to_station=HFH&purpose_codes=ADULT'
           
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, headers=headers, verify=False)
    
    pprint.pprint(response.text)
    



def main():
    print(sys.argv)
    print(sys.kwargs)
    # from_station, to_station = sys.argv[1], sys.argv[2]


if __name__ == '__main__':
    main()