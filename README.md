# HW4-ZTH-Intro-to-Github-WS
A :fire: presentation about how to use Github, for the Zero To Hero Workshop that HW4 is hosting on November 6th

### Configure Git for the first time

```
git config --global user.name "Your-User-Name"
git config --global user.email "youremail@domain.whatever"
```
### Generate an SSH key and add it to your account

On Linux, UNIX, Cygwin, or Git Bash, generate a key:

```
ssh-keygen -t rsa -b 4096
```
This will generate a private key (`~/.ssh/id_rsa`) as well as a public key (`~/.ssh/id_rsa.pub`).
**Do not share your private key with others.**

Copy the entire contents of the key, and associate it with your GitHub account:

To copy the entire content of the rsa key, use this command: ```pbcopy < ~/.ssh/id_rsa.pub``` 
This will be easier than using the cat command ```cat ~/.ssh/id_rsa.pub``` and copying and pasting manually 

* Click the avatar icon in the top right corner
* Select *Settings* from the drop down list.
* Select *SSH and GPC keys* from the sidebar.
* Click *NEW SSH Key*.
* Paste the contents of your public key in the *Key* field. Call the title something cool.
* Click *Add SSH key*.

### @ Jason & Kayla, what does that do?

We're glad you asked! Basically this tells to Git, your github username, and your email associated with that github account. The reason you need to add the SSH key is for Github & Git to be able to identify your computer, because each public id_rsa key generated by a different terminal is unique. That's how Github knows for sure it's you fam. 

### LOL My git for one of my projects is on fire Jason & Kayla, and not the good kind of fire :sob: , what do we do?

Okay, that really depends on what just happened, if we're being brutally honest here. But we get it, sometimes you mess up something without knowing and your git is all messed up! We've all been there sitting at our desk at 4am wondering where our work just went. Here are a few debugging tips and pointers to help you **put out the :fire: :**

* `git Status` 
This command is going to let you see what is going on right now. It will tell you what branch you are on, if your branch is behind/in   front of your branch by # of commits, and any untracked files.

* `git log` 
This command, when you run it, shows you a history of all the commits you have made. It is very great because this command is the command to use to get the commit hashes, which are what you need when you run the next command. If you ever want to look cooler using your terminal and want to do a cooler version of a git log output, check out links like [this](https://coderwall.com/p/euwpig/a-better-git-log). 

* `git diff`
This command is useful to see where you changed your code, as it will show you with a series of + or - signs to denote code that has been added (+) or code that has been deleted (-). Now, you can do this using the GitHub site's feature for comparing the most recent changes. However, the `git diff` command can also pass in arguments in the following way: `git diff [options] <commit> <commit> [--] [<path>...]`
Which means you can compare specific commits against one another.

Let's say you have 8 commits (commits a, b, c, d, e, f, g, h), commit h is your most recent commit. If you ever wanted to compare commit a and commit e, for example, you could go to your terminal and type `git diff a e` and it would show you the differences between commit a and commit e. (You laugh and roll your eyes at this now, but you'll thank me later when you're at your big tech, software engineering internships that expect you to know how to use git and troubleshoot and debug by yourself.) 

There is also this great stack overflow answer that shows you how to use git diff in more ways [here:](https://stackoverflow.com/a/1195209)

* `git help`
There are a lot of advanced git commands that we definitely did not cover in this workshop. There are great commands such as `git bisect` and `git rebase`. But, before you go googling any of these cool git commands, you can use the `git help` command in your terminal to get a `man` (command for manual, you can really use `man [linux command]` to learn about any terminal, linux commands) output, but for the git command specifically. If you wanted to learn more about `git bisect` for example, you could type in to terminal: `git help bisect`. Just remember the format: `git help [command]`

### This deserves its own section, it's so powerful but it can also destroy your repo instantly 

In this section, we're talking about the resets, the reverts and the checkouts. There is a good one from [Atlassian](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting) that talk about the difference of the 3. There will be other links and references throughout this section. This one is a doozy!! 

#### The Hard Reset Vs. The Soft Reset (and the mixed reset) vs The Revert

Context: 
When you modify a file in your repository, the change is initially unstaged. In order to commit it, you must stage it, aka add it to the index—using git add. When you make a commit, the changes that are committed are those that have been added to the index. [credit (stack overflow)](https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard)

We have this command called `git reset`. In the most basic terms, this command changes where your current branch (HEAD) is pointing to in the Git Tree. Let's say the following diagram is what your git tree looks like.

``` - A -> B -> C (MASTER)```

Running `git reset --soft B` will do the following. Master will now be at commit B, but when you go to commit your changes, it will still have the changes from commit C. So after you do `git reset --soft B` and you run `git commit`, you will have your changes in B, as well as the changes in C. 

Running `git reset --mixed B` will do this. Master and HEAD now points to B in the tree. There are changes in the working directory, but they don't show up when you run `git commit`. This means you need to use `git add` to stage the changes and commit and push like normal. 

Running `git reset --hard B` is the same as running mixed, **but**, it also changes your working directory. Any unstaged changes you have before you run `git reset --hard B` will be lost, and your file structure will go back to looking like as it exactly did when B was the HEAD commit. 

**When should you use it?** 

* [Soft Reset](https://stackoverflow.com/a/26172014) You should use this when you want to combine a series of commits into 1. 
* [Hard Reset](https://www.alexkras.com/19-git-tips-for-everyday-use/#stages) When you just lost all hope and sure you want to start over
* Mixed Reset is the same thing as hard, except it doesn't change your working files. 

**What is git revert and why is it so different from git reset?**

The command `git revert` is useful when you want to "reverse" a commit. When you use `git revert` you are basically reversing the effects of a particular commit with a NEW commit. This is cool because this command doesn't alter your commit history, whereas using something like `git reset` will change your commit history, and files if you are using --hard. Again, check [Atlassian](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting) if you are confused. 

#### Branches! They're great! 

They're super easy to make too! Before we get to the technical terminal side of things, we'll tell you how to make a branch using the website! 

**To do it in Terminal:**
We're going to use a command called `git checkout`(This command was briefly mentioned in the last section where, and you can definitely use it to go between file versions). However, to switch between branches, you will use the `git checkout` command a lot of times. 

To make the actual branch, you need this command: 

`git checkout -b my-new-cool-branch`

The -b flag tells git to create a new branch. By default, git makes that new branch, and places you in that branch. Pretty cool, right?
This command above is going to make a branch off of Master. You can also tell git what branch you plan on branching off from. 

If that is the case, just do 

`git checkout -b my-new-cool-branch this-is-my-lame-old-branch` 

To merge the branches into master: 

`git merge my-new-cool-branch`
This command will take your new branch and merge it to Master. Please check this [stack overflow answer](https://stackoverflow.com/questions/5601931/best-and-safest-way-to-merge-a-git-branch-into-master) for the safest way to do this. Most of the time git merge your-branch-name will work, but if there are merge conflicts... lol gg










