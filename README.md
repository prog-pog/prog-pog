# Commit Changes With `git ...`
> [!NOTE]
> You can repeat step 2 for all the files, or if you want to commit all files you can skip to step 3 and use `git commit -a` instead!
1. Use `git pull` to get all files to make shure you are up to date.
2. Use `git add <filename>` where \<filename\> is the name of the file. *duh*
3. Use `git commit` a file will come up and ask for a commit message
4. You have to put a commit message then close the file.
5. Use `git push` to push the changes to Githubs servers.
6. You should be done!

# Commit Deleted Files With `git ...`
1. Use `git pull` to get all files to make shure you are up to date.
2. Delete a file
3. Use `git commit` an area in the file opened should say:
```
# Changes to be committed:
#	deleted:    <filename>
```
4. \<filename\> is the file. *duh*
5. You have to put a commit message then close the file.
6. Use `git push` to push the changes to Githubs servers.
7. You should be done!