#coding:utf-8

import commands,re,os
import datetime

#get last tag
def get_last_tag():
    result=(commands.getoutput('git tag')).split()
    return result[-1]

def change_file_version():
    replace_version = "Version = '%s'" % get_last_tag()
    old_str = r'Version = (.*)\s'
    with open('Main.py','r') as f1,open('Main2.py','w') as f2:
        for line in f1:
            f2.write(re.sub(old_str,replace_version,line,1))
        os.remove('Main.py')
        os.rename('Main2.py','Main.py')


# def change_version_commit():
#     last_tag=get_last_tag()
#     commands.getoutput('git add Main.py')
#     commands.getoutput('git commit -m "change version info ,add new tag %s" ' % get_last_tag())

def get_test_tag():
    result_tag = (commands.getoutput('git tag')).split()[-1]
    result=result_tag+'_test%s' % datetime.datetime.now().strftime('%Y%m%d_%H:%M:%S')
    return result

if __name__ == '__main__':
    print('get new tag',get_last_tag())
    print('get test tag',get_test_tag())
    change_file_version()