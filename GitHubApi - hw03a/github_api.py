# github link: https://github.com/cmorcos/SSW567/tree/main/GitHubApi%20-%20hw03a

import requests  # send requests to github api, installed using python3 -m pip install requests
import json # unsure if this is needed when paired with response.json

def get_repos(username):    # get user repositories
    url = f"https://api.github.com/users/{username}/repos"  # github API url using username
    response = requests.get(url)    # get request to github
    if response.status_code != 200: # if no successful response from github
        return []  # empty list
    return response.json()  # json response to python data

def get_commit_count(username, repo_name):  # counts commits in repo
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"    # github API url for repo commits
    response = requests.get(url)    # get request
    if response.status_code != 200: # unsuccessful
        return 0  # 0 commits
    commits = response.json()   # json response --> python data
    return len(commits) # len of list = num of commits

def get_repo_info(username):    # combine repo names + commit count
    repos = get_repos(username) # get all user repos
    results = []    # list to store final results
    for repo in repos:  # loop through each repo
        repo_name = repo["name"]    # repo name from json data
        commit_count = get_commit_count(username, repo_name)    # num of commits in said repo
        results.append((repo_name, commit_count))   # store repo name + commit count
    return results  # list of repo info


if __name__ == "__main__":
    username = input("Enter GitHub username: ") # enter user
    repo_info = get_repo_info(username) # repo info
    for repo_name, commit_count in repo_info:   # goes through repos + commit count
        print(f"Repo: {repo_name} Number of commits: {commit_count}")   # result