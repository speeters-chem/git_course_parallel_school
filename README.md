***GIT COURSE***
=============

**EX.1: Single Dev**
=========


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

