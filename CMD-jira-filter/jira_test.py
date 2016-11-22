#!/usr/bin/python
from jira import JIRA, JIRAError
import sys

options = {
        'server': 'http://your.jira.server.com'

}

USERNAME = "your username"
PASSWORD = "your password"

jira = None
try:
    jira = JIRA(options, basic_auth=(USERNAME, PASSWORD))

except JIRAError as e:
    print "CODE: " + str(e.status_code) + "TEXT: " + e.text
    print "full: " + str(e)
    sys.exit()

def check_history():
    issue = jira.issue('ISSUE-ID', expand='changelog')
    changelog = issue.changelog

    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status':
                print 'Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString

def check_filter():
    for i in jira.search_issues('filter=111111'):
        print i.key

check_filter()
