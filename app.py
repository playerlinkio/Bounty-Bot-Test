from github import Github
from pprint import pprint

import time
g = Github("playerlink-bot", "")
time.sleep(2)

# repo = git_bot.get_repo("SUIBE-Blockchain/IssueStore")
repo = g.get_repo("playerlinkio/Bounty-Bot-Test")
issues_list = []
# issue_dict = {}
for i in repo.get_pull():
    pprint(i)
    issue_dict = {}
    # print(i.labels)
    # print(i.labels)
    # for label in i.labels:
    #     print(label.name)
    # issue_dict['labels'] = [label.name for label in i.labels]
    # # print(i.title)
    # issue_dict['title'] = i.title
    # issue_dict['body'] = i.body
    # issue_dict['number'] = i.number
    # issues_list.append(issue_dict)

pprint(issues_list)