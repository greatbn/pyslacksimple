#!/bin/env python
import json
from  prettytable import PrettyTable
from  slackclient import SlackClient
import os
import sys
from operator import itemgetter
class PySlackSimpleException(Exception):
    pass
class PySlackSimple(object):
    def __init__(self,token):
        self.token = token
        try:
            os.environ['SLACK_TOKEN']
            self.token = os.getenv("SLACK_TOKEN")
        except KeyError:
            print "Please input token or SLACK_TOKEN environment"
            sys.exit(1)
    def get_channel_list(self,sc):
        token = self.token
        channels_list = sc.api_call("channels.list")
        return channels_list
    def get_user_list(self,sc):
        token = self.token
        users_list = sc.api_call("users.list")
        return users_list
    def print_table(self,data,data_type,sc):
        if data_type == "channels":
            table = PrettyTable(["ID", "Channel Name", "Number of Members", "Creator","Topic"])
            table.align["ID"] = "1"
            table.padding_width = 1
            users_list = self.get_user_list(sc)
            for i in range(0,len(data[data_type])):
                user = users_list['members'][map(itemgetter('id'),users_list['members']).index(
                    data[data_type][1]['creator'])]['name']
                table.add_row([ data[data_type][i]['id'], data[data_type][i]['name'],
                    data[data_type][i]['num_members'], user,
                    data[data_type][i]['topic']['value'] ])
        elif data_type == "members":
            table = PrettyTable(["ID", "Username", "Real Name", "Email", "Is Admin" ])
            table.align["ID"] = "1"
            table.padding_width = 1
            for i in range(0,len(data[data_type])):
                if data[data_type][i]['deleted'] == False:
                    try:
                        table.add_row([data[data_type][i]['id'], data[data_type][i]['name'],
                            data[data_type][i]['profile']['real_name'],data[data_type][i]['profile']['email'],
                            data[data_type][i]['is_admin'] ])
                    except:
                        pass
        return table
    def run(self):
        sc = SlackClient(self.token)
        return sc
if __name__ == "__main__":
    token =""
    slacksimple = PySlackSimple(token)
    sc = slacksimple.run()
    data = slacksimple.get_channel_list(sc)
    #print data
    print slacksimple.print_table(data,"channels",sc)
    data = slacksimple.get_user_list(sc)
    print slacksimple.print_table(data,"members",sc)
