***GIT COURSE***
=============
Author : 
   - Simone Bna    (s.bn@cineca.it)
   - Eric Pascolo  (eric.pascolo@cineca.it)



**EX.0 : CONFIGURATION**
====================

 - 0.0.1 Check if git is installed on your machine

        git 
        apt install git (Deb example)
 - 0.0.2 Configure username and email for your account 
         
         git config --global user.name "Name Surname"
         git config --global user.email "name@example.com”

 - 0.0.3 Congfigure your prefered editor
         
         git config --global core.editor vim

 - 0.0.4 Show all setting

        git config --list 


**EX.1: Single Dev**
=========

EX.1.1 : BASIC COMMAND
-----------------------

 - 1.1.1 Create local empty repository 
      
      mkdir ex1_1
      cd ex1_1
      git init remote_url

 - 1.1.2 Create README file in repo

      touch README.md
  
 - 1.1.3 Add new file to commit
      
       git add  README.md

 - 1.1.4 Commit your changes
      
       git commit -m "commit description"

 - 1.1.5 Create directory into repo

       mkdir my_software

 - 1.1.6 Try to add "my_software" to repository, is it allowed?
 - 1.1.7 Use git status to see the repo status

       git status

 - 1.1.8 Create local configuration file in "my_software"

       cd my_software
       touch local_configuration.cfg

 - 1.1.9 Use gitignore file to avoid wrong commit on local_onfiguration.cfg

       touch .gitignore
       echo "local_onfiguration.cfg" >> .gitignore
       git add .gitignore
       git commit -m"create gitignore file"

 - 1.1.10 Modify *local_configuration.cfg* and check if git suggest to commit the file

      echo "username=myname" >> local_configuration.cfg
      git status

 - 1.1.11 Use git log to see the history of repo, how commit do you do?

 - 1.1.12 Use git ls-files to add multiple file to repository
      
      cd my_software
      touch main.py io.py log.py
      git ls-files -o
      git add $(git ls-files -o)
      git commit -m"create message"

 - 1.1.13 Use git tag to identify first code version
      
      git tag v0.1 -m "code version 0.1"

   <!--- - 1.1.14 inserire git diff --->

EX1.2 : REMOTE COMMAND
----------------------

- 1.2.1 Create remote empty repository
- 1.2.2 Show if your local repo have remote repo linked

       git remote -v

- 1.2.3 Copy remote repo URL and add to linked repo

       git remote add your_url origin

- 1.2.4 Sync local and remotes repository with push command

       git push origin master

- 1.2.5 Check if the remote repo is sycronized and if tag is presente remotelly

- 1.2.6 Push the tag

      git push origin --tags

- 1.2.7 Now check if tag is present in remote repo

- 1.2.8 




EX.1.3 : BRANCH COMMAND
-----------------------

      



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

