#coding:utf-8

import commands,re,os,datetime
#import Sundry as sy

##############public function
#get last tag
def get_last_tag():
    result=(commands.getoutput('git tag')).split()
    if result:
        return result[-1]

def change_file_version(last_tag):
    replace_version = "Version = '%s'" % last_tag
    old_str = r'Version = (.*)\s'
    with open('Main.py','r') as f1,open('Main2.py','w') as f2:
        for line in f1:
            f2.write(re.sub(old_str,replace_version,line,1))
        os.remove('Main.py')
        os.rename('Main2.py','Main.py')

def change_version_commit(last_tag):
    commands.getoutput('git add *.py')
    commands.getoutput('git commit -m "change version info ,add new tag %s" ' % last_tag)

def time_now_tag():
    return datetime.datetime.now().strftime('%Y%m%d_%H:%M:%S')


######auto version
def change_file_formal_version():
    if get_last_tag():
        change_file_version(get_last_tag())

def commit_main():
    if get_last_tag():
        change_version_commit(get_last_tag())

#####cut test version
def get_cut_tag(cut_type):
    if get_last_tag():
        result=get_last_tag()+'_%s%s' % (cut_type,time_now_tag())
        return result

def change_file_cut_version(cut_type):
    if get_last_tag():
        change_file_version(get_cut_tag(cut_type))

def create_cut_tag(cut_type):
    if get_last_tag():
        commands.getoutput('git tag %s' % get_cut_tag(cut_type))

def commit_main_cut_version(cut_type):
    if get_last_tag():
        change_version_commit(get_cut_tag(cut_type))

#####call function
def auto_version():
    change_file_formal_version()
    commit_main()

def auto_cut_version(cut_type):
    change_file_cut_version(cut_type)
    commit_main_cut_version(cut_type)
    create_cut_tag(cut_type)


if __name__ == '__main__':
    auto_cut_version('aplt')