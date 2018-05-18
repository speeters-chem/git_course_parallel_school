***GIT*** 
=============

Authors : 
   - Simone Bna    (s.bn@cineca.it)
   - Eric Pascolo  (eric.pascolo@cineca.it)

Version :  Cineca Parallel Summer School 2018

**EX.0 : Configuration**
========================

Follow the steps below to configure git on your machine.

 - 0.0.1 Is git installed on your machine?

         git 
         apt install git (Deb example)
         
 - 0.0.2 Configure username and email for your remote hub account 
         
         git config --global user.name "Name Surname"
         git config --global user.email "name@example.com”

 - 0.0.3 Configure your favorite editor
         
         git config --global core.editor vim

 - 0.0.4 Show all git settings

         git config --list 


**EX.1: Single Dev**
====================

In this exercise we learn the basic git commands, how to set-up multiple remote repos 
and how to manage branches workflow.

EX.1.1 : BASIC COMMAND
-----------------------

 - 1.1.1 Create a local empty repository 
         
         mkdir ex1_1
         cd ex1_1
         git init 

 - 1.1.2 Create a README file in the repo

         touch README.md
  
 - 1.1.3 Add a new file to the staging area
      
         git add README.md

 - 1.1.4 Commit your changes
      
         git commit -m "commit description"

 - 1.1.5 Create a directory into the repo

         mkdir my_software

 - 1.1.6 Try to commit "my_software", is it allowed?

         git add my_software
         git commit -m "commit directoy" 

 - 1.1.7 --**CHECK**-- Use git status to check the repo status

         git status

 - 1.1.8 Create local_configuration file in "my_software"

         cd my_software
         touch local_configuration.cfg

 - 1.1.9 Add a .gitignore file to avoid to commit the "local_configuration.cfg" file
       
         touch .gitignore
         echo "local_configuration.cfg" >> .gitignore
         git statuts -u   # show untracked not ignored file
         git add .gitignore
         git commit -m"create gitignore file"

 - 1.1.10 --**CHECK**-- if directory my_software is now commited

         git ls-tree --full-tree -r master

 - 1.1.11 Use git log to view the history of the repo, how many commits are there?

         git log

 - 1.1.12 Use git ls-files to add multiple files to the repository
      
         cd my_software
         touch main.py io.py log.py
         git ls-files -o             # show list of untrucked files
         git add $(git ls-files -o)  # don't worry, ignored files will be not processed
         git commit -m "create message"

 - 1.1.13 Use git tag to identify the first code version
      
         git tag v0.1 -m "code version 0.1"

 - 1.1.14 Change main.py and commit, check with *git diff* the difference between HEAD and the previous commit (HEAD^)
       
         echo "print(\"Hello World\")" >> main.py
         git add main.py
         git commit -m "create Hello World software"
         git diff HEAD HEAD^

EX1.2 : REMOTE COMMAND
-----------------------

In this exercise we continue to work with the previous local repository.

 - 1.2.1 Create a remote empty repository
 - 1.2.2 Check if your local repo has remote repos linked

         git remote -v

 - 1.2.3 Copy the remote repo URL and link it with the local repo, call it ORIGIN

         git remote add origin your_url 

 - 1.2.4 Sync local and ORIGIN with push command

         git push origin master

 - 1.2.5 --**CHECK**-- if syncronization is completed, can you see tag in ORIGIN?

 - 1.2.6 Push the tag to ORIGIN

         git push origin --tags

 - 1.2.7 --**CHECK**-- if syncronization is really completed

 - 1.2.8 Create a  **new** remote repo for BACKUP and add it to the local repo

         git remote add backup url_backup_repo 

 - 1.2.9 --**CHECK**-- if the local repo is linked with ORIGIN and BACKUP

         git remote -v

 - 1.2.10 Push the local repo to BACKUP

         git push --tags backup master

EX.1.3 : BRANCH COMMAND
------------------------

 - 1.3.1 Create  DEV branch

         git checkout -b dev

 - 1.3.2 --**CHECK**-- how many branches exists in local repository

         git branch

 - 1.3.3 Modify io.py file and commit it
      
         echo "print(\" I'm IO \")" >> io.py
         git add io.py
         git commit -m "change io.py"

 - 1.3.4 Return to Master branch, modify main.py  and commit it
      
         git checkout master
         echo "print(\" I'm main \")" >> main.py
         git add main.py
         git commit -m "change main.py"

 - 1.3.5 Return to dev branch, change log.py  and commit it

         git checkout dev
         echo "print(\" I'm LOG \")" >> log.py
         git add log.py
         git commit -m "change log.py"

 - 1.3.6 Return to master and merge it with DEV branch

         git checkout master 
         git merge dev

 - 1.3.7 Show the branches diagram with git log

         git log --all --graph --decorate --oneline

 - 1.3.8 Reset the last commit in order to try **rebase** of branches instead of merge

         git reset --hard HEAD^

 - 1.3.9 Use git rebase 

         git rebase dev

 - 1.3.10 --**CHECK**-- use git log to see the new diagram of branches, observe the difference between rebase and merge

         git log --all --graph --decorate --oneline


**EX.2 : Team Dev**
=========

This exercise will be done in groups. Create a group of 3 persons (max 4) and define who is the **Team Leader (TL)**. The other members are simply **other developer (OD)**. 
In the first part of the exercise we work with only a single branch (master branch); in the second part we introduce the dev branch to simulate a real developer's workflow. 

EX.2.1 : SINGLE BRANCH
-----------------------

- 2.1.1 TL forks the CINECA git_course repo into the TL's remote repo.
- 2.1.2 ODs fork the TL's remote repo in their public remote repo.
- 2.1.3 TL and OD clone their remote repos locally
- 2.1.4 TL adds as REMOTES the OD's remote repos
- 2.1.5 ODs add as REMOTES the TL's remote repo
- 2.1.6 --**CHECK**--  if history is syncronized on all repos
- 2.1.7 Each member changes a different file
- 2.1.8 Each member pushes and pulls to resync all repos
- 2.1.9 --**CHECK**-- if all repos are syncronized
- 2.1.10 Tl and ODs change the same line of the same file on their local repos
- 2.1.11 TL commits and pushes his change on his remote repo.
- 2.1.12 ODs pull from TL's remote repo and manage the conflict
- 2.1.13 --**CHECK**-- if all repos are syncronized
- 2.1.14 ODs change the same line of the same file, commit and push on their remote repos
- 2.1.15 TL pulls from ODs' remote repos, chooses the correct change and manages the conflict
- 2.1.16 --**CHECK**-- if all repos are syncronized


EX.2.2 : MULTIPLE BRANCH
-------------------------

 - 2.2.1 TL creates the branch DEV on the local repo and pushes it on his remote repo. 
   **ATTENTION** : TL is the only developer that can change the DEV branch
 - 2.2.2 ODs pull TL's remote repo and push the new branch on their remote repos.
 - 2.2.3 --**CHECK**-- if all repos have the DEV brach
 - 2.2.4 ODs create a new branch on their local repos, the branch name has to be unique and has to contain the feature implemented in this branch.
 - 2.2.5 ODs code the feature in the new branch, ODs commit the changes and push on their remote repos.
 - 2.2.6 TL pulls the new branches from ODs remote repos, TL **rebases** the two branches on DEV, TL pushes the changes on his remote repo
 - 2.2.7 ODs pull the rebased DEV branch on their local repo and sync with their remote repos
 - 2.2.8 --**CHECK**-- if all repos have the branch DEV rebased with the OD changes

