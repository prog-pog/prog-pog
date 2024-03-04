import os
bashCommand = ["git pull", "git add -A", "git commit -a", "git push"]
for i in range(len(bashCommand)):
    os.system(bashCommand[i])