#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import ast
import os


def event2txt(s):
    # print s
    dic = ast.literal_eval(s)
    # print len(dic['items'])
    items = dic['items']
    for item in items:
        # print item['id'],
        if 'date' in item['start']:
            print item['start']['date'], item['end']['date']
        else:
            print item['start']['dateTime'], item['end']['dateTime']
        print item['summary']


def listcalendar():
    event_dir = os.getenv('HOME') + '/.cache/calendar.vim/local/event'
    archive_dirs = os.listdir(event_dir)
    for archive_dir in archive_dirs:
        year_dirs = os.path.join(event_dir, archive_dir)
        for year_dir in os.listdir(year_dirs):
            month_dirs = os.path.join(year_dirs, year_dir)
            for month_dir in os.listdir(month_dirs):
                event_dirs = os.path.join(month_dirs, month_dir)
                for event_file in os.listdir(event_dirs):
                    event_file_full_path = os.path.join(event_dirs, event_file)
                    with open(event_file_full_path, 'r') as f:
                        contents = f.readlines()
                        event2txt("".join(contents))


if __name__ == "__main__":
    print "vim calendar to text"
    print "----------------------------------------"
    listcalendar()
