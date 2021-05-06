#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:37:57 2021

@author: Allison
"""
# save this to the local repository

#######################
# Things that worked
# Create remote repository on github
# Copy link and use !git clone repo-url to clone remote repository to local system
# Now work in that local folder, say make a new Python script
# To upload changes, make sure to navigate to appropriate folder in console using cd
# eg cd /Users/Allison/Documents/Python_practice/a_test_of_git/another_test
# use !git status to make sure you're in the correct place
# !git add filename
# !git commit -m "your commit message here"
# !git add 
# NOTE: thought I'd have to do !git add -u origin master but that didn't work;
# just plain !git add seemed to do the trick and the file showed up in the remote repo

########################
# If you just do !git init in a project to initiate a local git repository and then, 
# !git add remote origin remote_repo_url --> pulls the remote repo to merge with files you have locally that you want to push
# !git add filename
# !git commit -m "new commit message"
# !git push -u origin master --> this will end up pushing everything back as a new branch
