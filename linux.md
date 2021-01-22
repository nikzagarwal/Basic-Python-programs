# Linux code

1. **sudo su** - change to root user
2. **hostname**
3. **ifconfig** - gives ip address
4. **hostname** -i -also for ip
5. **cat /etc/os-release**- which os version is used
6. **yum install httpd** **-y**- install apache server
7. **yum remove httpd**
8. **yum update httpd**
9. **service https start**
10. **service httpd status**
11. **chkconfig httpd on/off** - turn on server by default whenever pc starts
12. **which vlc** - checks if software is installed
13. **whoomi** - who am i
14.  **echo** - print on screen for multi users
15. **grep root /etc/psswd** - give output wherever root is there in given path
16. **tree** - shows heirarchy 



17. **useradd** - to create user
18. **groupadd** - to create group
19. **gpasswd** -a/-M - to add user to group or to add multiple user
20. **ln** - hardlink
21. **ln** **-s** - softlink
22. **tar** - zip files togther
23. **gzip** - compress file
24. **wget** - to download from any link



25. **chmod** - used to change access mode of file

    eg: chmod 543 file1

    eg2:chmod u=r,g=rwx,o=wx

    eg3:chmod u-wx,g+w,o=wx

26. **chown** -  change of file or directory

    eg: chown bhupinder file1

25. **chgrp** - change grp of file or directory

    eg: chgrp devop file1

26. **d rwx r_x r--**   -  first letter for file or directory , next 3 is permission of root/owner , next 3 or permissions of group, next 3 for permissions of others

27. **r**- read

    **w**- write

    **x** - execute

