#coding:utf-8

import commands

#get list tag  后续没用可以删掉
def get_tag_list():
    return (commands.getoutput('git tag')).split()

#get last tag
def get_last_tag():
    result=(commands.getoutput('git tag')).split()
    return result[-1]

def change_version_commit():
    pass

class AutoVersion(object):
    def __init__(self):
        pass







print(get_last_tag())