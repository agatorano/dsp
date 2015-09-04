# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Interest commands I have found useful
> > 
> > diff - performs a line by line comparison of two files
> > 
> > comm - allows you to see the commonalities between two files. Like diff but instead has three lines: one contains the entirety of the first file, the sencond contains the entirety of the second, and the third shows the lines in common. You can toggle which lines to remove using th command -1,-2,-3 or any combination to remove the first second or third line respectively.
> > 
> > df - shows the disk space available generally df -h is most useful
> > 
> > grep - one of the most useful commands on the command line. Finds any files containing text you choose. It can also replace these lines if you would like. 
> > 
> > tar - can gzip and bzip files for easy compression. tar -czvf is to zip and tar -cxvf is to unzip. Hard to remember :disappointed:
> > 
> > wget - downloads files from web links. I use this all of the time! 
> > 
> > sudo !! - if you forget sudo on the last command, sudo !! uses the same command with sudo privleges. 
> > 
> > scp - sends files from a local machine to a remote machine
> > 
> > mkdir -p - I always forget I can make nested directories with one command
> > 
> > alias - allows you to rename some commands. For example if you wante to always require affirmation before deletion you could set rm to equal rm -i.
> > 

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists files and directory in your current directory or one designated by a path. 
> > 
> > ls -a: lists even hidden files and directories
> > 
> > ls -l: lists the longform information of each of the files and directories (e.g. size permissions date-modified, etc.)
> > 
> > ls -lh: lists the same as ls -l but uses human readable file sizes instead of raw bytes. 
> > 
> >ls -alh: this would list all of the hidden and unhidden files and directories. It would give all of the information of the file and also make sure the units were displayed in human readable format

---


---

What does `xargs` do? Give an example of how to use it.

> > `xargs` lets us send the output of one command into another command. xargs itself just controls the list of arguments that are genereated by the argument you piped to it. 
> >
> > for example `echo 1 2 3 4| xargs` would just print the same information as echo 1 2 3 4. xargs just holds the arguments and is ready to send them to another tool. You can control the arguments themselves using xargs commands. `echo a b c d|xargs -n 1` would display only one item at a time instead of all at once. If the first argument listed files 1 at a time, the default xargs will still display the contents on one line (e.g. ls | xargs).
> > 
> > If you use xargs to execute another utility you can simply run the next command afterwards. For example use find to find a file in the current directory and then display the contents.
> > 
> > find . -name "*.R" -type f -print |xargs cat

---

