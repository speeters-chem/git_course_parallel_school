***GIT COURSE***
=============

**EX.1: Single Dev**
=========


**EX.2 : Team Dev**
=========

This exercise will be done in groups. Create a group of 3 people (max 4) and define who is a developer **Team Leader (TL)** and the other people are a **other developers (OD)**. In the first part of exercise we work with only single branch and after we introduce more branches to simulate a real developer's work. 

EX.2.1 : SINGLE BRANCH
-----------------------

- 2.1.1 TL forks CINECA git_course repo into TL's remote repo.
- 2.1.2 OD fork TL's remote repo in their public remote repo.
- 2.1.3 TL and OD clone their remote repos in local repos
- 2.1.4 TL sets as REMOTES the OD's remote repos
- 2.1.5 OD set as REMOTES the TL's remote repo
- 2.1.6 --**CHECK**--  if history is syncronized on all repos
- 2.1.7 Each member change different file
- 2.1.8 Use push and pull to resync all repos
- 2.1.9 --**CHECK**-- if all repos are syncronized
- 2.1.10 TL and OD change the same line on local repos
- 2.1.11 TL commits and pushes his change on his remote repo.
- 2.1.12 OD pull from TL's remote repo and manage the conflict
- 2.1.13 --**CHECK**-- if all repos are syncronized
- 2.1.14 OD change the same line, commit and push on their remote repos
- 2.1.15 TL pulls from OD's remote repos, choose the correct change and manage the conflict
- 2.1.16 --**CHECK**-- if all repos are syncronized


EX.2.2 : MULTIPLE BRANCH
-------------------------

 - 2.2.1 TL creates the branch DEV on local repo and pushes it on his remote repo. 
   **ATTENTION** : TL is the only developer that can change DEV branch
 - 2.2.2 OD pull TL's remote repo and push the new branch on their remote repos.
 - 2.2.3 --**CHECK**-- if all repos have DEV brach
 - 2.2.4 OD create a new branches on their local repos, the branches must have different names and they  will be call as the features implemented in that branch.
 - 2.2.5 OD code the features in the new branches, OD commit the changes and push on their remote repos.
 - 2.2.6 TL pulls the new branches from OD remote repos, TL **rebases** the two branches on DEV, TL pushes the changes on his remote repo
 - 2.2.7 OD pull the rebased DEV branch on local repo and sync with their remote repos
 - 2.2.8 --**CHECK**-- if all repos have the brach DEV rebased with OD changes

