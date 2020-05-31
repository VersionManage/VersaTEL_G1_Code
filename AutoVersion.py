#coding:utf-8

import commands

def get_tag():
    return commands.getoutput('git tag')



print(get_tag())