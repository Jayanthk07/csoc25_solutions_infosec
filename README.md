# csoc25_solutions_infosec

 0:
 SSH into the Bandit server using the provided credentials.
 ssh bandit0@bandit.labs.overthewire.org -p 2220
 and use the given password

 0->1:
 ssh bandit1@bandit.labs.overthewire.org -p 2220
 check for the files using ls -al
 and read the file "readme"
 the output is ------------- The password you are looking for is: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

 1->2:
 ssh bandit2@bandit.labs.overthewire.org -p 2220
 here the given file is named as "-"
 so if we want to read it we just do ----- cat ./-
 now we get the ouput passwrd as 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

 2->3:
 ssh bandit3@bandit.labs.overthewire.org -p 2220
 cat "spaces in this filename" to get content of these kinda files
 and got the password for the next level which is "MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx"

 3->4:
 ssh bandit4@bandit.labs.overthewire.org -p 2220
 do ls -al
 and now cd inhere and then check ls -al
 we see a hidden file. so we access it like cat ...Hiding-From-You
 and the password we get is 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

 4->5:
 ssh bandit5@bandit.labs.overthewire.org -p 2220
 cd inhere
 and then we see in ls -al and after checking all files in there 
 we get to know that password in -file07
 cat ./-file07 to get the password which is ---- "4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw"

 5->6:
 ssh bandit6@bandit.labs.overthewire.org -p 2220
 find ./inhere/ -type f -readable ! -executable -size 1033c 
 after doin this we get the file path as ---------"/home/bandit5/inhere/maybehere07/.file2"
 cat /home/bandit5/inhere/maybehere07/.file2 gives password as "HWasnPhtq9AVKe0dmk45nxy20cvUa6EG"

6->7:
ssh bandit7@bandit.labs.overthewire.org -p 2220
find / -type f -size 33c -group bandit6 -user bandit7 2>&1 | grep -v "Permission denied"
then we get the output as 
find: ‘/proc/2396479/task/2396479/fdinfo/6’: No such file or directory
find: ‘/proc/2396479/fdinfo/5’: No such file or directory
/var/lib/dpkg/info/bandit7.password
now we do cat /var/lib/dpkg/info/bandit7.password 
to get teh psasword as "morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj"

7->8:
ssh bandit7@bandit.labs.overthewire.org -p 2220
cat "data.txt " and observe the pattern of the file
grep "millionth" data.txt, as both willl be in the same line
which gives me the password as "dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc"

8->9:
ssh bandit9@bandit.labs.overthewire.org -p 2220
sort data.txt | uniq -u
this gives me the password as "4CKMh1JI91bUIZZPXDqGanal4xvAg0JM"

9->10:
ssh bandit10@bandit.labs.overthewire.org -p 2220
strings data.txt | grep "=="
as we knoe only one line is the asnwer , so the last one after checking all gives password as "FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey"

10->11:
ssh bandit11@bandit.labs.overthewire.org -p 2220
do cat dat.txt
it is a base 64 , after decoding that we will get the password as "dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr"

11->12:
ssh bandit12@bandit.labs.overthewire.org -p 2220
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
and thus we get the password as "7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4"

12->13:
ssh bandit13@bandit.labs.overthewire.org -p 2220
bandit12@bandit:~$ mkdir /tmp/jkax
bandit12@bandit:~$ cp data.txt /tmp/jkax
bandit12@bandit:~$ cd /tmp/jkax
bandit12@bandit:/tmp/jkax$ xxd -r data.txt out1
bandit12@bandit:/tmp/jkax$ file out1
out1: gzip compressed data, was "data2.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 585
bandit12@bandit:/tmp/jkax$ mv out1 put2.gz
bandit12@bandit:/tmp/jkax$ gzip -d put2.gz
bandit12@bandit:/tmp/jkax$ file put2
put2: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/jkax$ bzip2 -d put2
bzip2: Can't guess original name for put2 -- using put2.out
bandit12@bandit:/tmp/jkax$ file put2.out
put2.out: gzip compressed data, was "data4.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/jkax$ mv put2.out put3.gz
bandit12@bandit:/tmp/jkax$ gzip -d put3.gz
bandit12@bandit:/tmp/jkax$ file put3
put3: POSIX tar archive (GNU)
bandit12@bandit:/tmp/jkax$ tar -xf put3
bandit12@bandit:/tmp/jkax$ ls
data5.bin  data.txt  put3
bandit12@bandit:/tmp/jkax$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/jkax$ tar -xf data5.bin
bandit12@bandit:/tmp/jkax$ ls
data5.bin  data6.bin  data.txt  put3
bandit12@bandit:/tmp/jkax$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/jkax$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/jkax$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
bandit12@bandit:/tmp/jkax$ tar -xf data6.bin.out
bandit12@bandit:/tmp/jkax$ ls
data5.bin  data6.bin.out  data8.bin  data.txt  put3
bandit12@bandit:/tmp/jkax$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/jkax$ mv data8.bin put4.gz
bandit12@bandit:/tmp/jkax$ gzip -d put4.gz
bandit12@bandit:/tmp/jkax$ file put4
put4: ASCII text
bandit12@bandit:/tmp/jkax$ cat put4
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

13->14:
ssh bandit13@bandit.labs.overthewire.org -p 2220
cat sshkey.private
and now in local machine
nano keys.txt paste that privatekey
chmod 600 keys.txt
ssh -i ~/.ssh/bandit14.key bandit14@bandit.labs.overthewire.org -p 2220 ( as i am using wsl in my pc)

14->15:
logged in using the above techniques
cat /etc/bandit_pass/bandit14 | nc localhost 30000
after diong we get the password as "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo"

15->16:
ssh bandit15@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -quiet
so from this i get th password as "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx"

16->17:
ssh bandit16@bandit.labs.overthewire.org -p 2220
nmap -p31000-32000 localhost(to check which port is open)
now after checking every port this way ---- openssl s_client -connect localhost:<port>
we get the password as a privatekey which i save in a file and do
ssh -i ~/k2.txt bandit17@bandit.labs.overthewire.org -p 2220(as i am in wsl)

17->18:
diff passwords.old passwords.new
as i cant enter and operate, i write command such that it returns output just before kicking out

18->19:
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
which gives me the password as "cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8"

19->20:
ssh bandit19@bandit.labs.overthewire.org -p 2220 
as it thinks i am bandit20 while running the script , i write code as
./bandit20-do cat /etc/bandit_pass/bandit20  to get the passsword "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO"

20->21:
so here we use 2 terminals
in one we open the port and give the input , in other we run the script
t1 : nc -lp 9999 < /etc/bandit_pass/bandit20
t2: ./suconnect 9999
after thsi we will get the password in t1
"EeoULMCra2q0dSkYj561DX7s1CpBuOBt"

21-22:
ssh bandit21@bandit.labs.overthewire.org -p 2220
we do --->  ls -al /etc/cron.d
and see what is written in cronjob_bandit22 file as ---> cat /etc/cron.d/cronjob_bandit22
now we get to know that the script being run is this and we seee it via --->
cat /usr/bin/cronjob_bandit22.sh
and we can see that the script is saving password to some file , now we read it 
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
password is "tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q"

22-23:



