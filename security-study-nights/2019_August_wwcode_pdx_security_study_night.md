![](highres_2019_August.jpeg)

<!-- Stacy Watts  Senior MSS Platform Engineer at BlueVoyant -->

---

Wifi: VevoGuest
pw: on the whiteboard

---

# [fit] ![inline](vevo_logo.png)
# [fit] Thank you vevo!

---

# About Women Who Code

We are a global nonprofit dedicated to inspiring women to excel in technology careers. Our events offer study groups, technical workshops, hackathons, networking events, panel discussions, lightning talks, and social events featuring influential tech industry experts, innovators, and investors. We help you build the skills you need to raise your professional profile and achieve greater career success. Current and aspiring coders are welcome.

---

# Code of Conduct

WWCode is an inclusive community, dedicated to providing an empowering experience for everyone who participates in or supports our community, regardless of gender, gender identity and expression, sexual orientation, ability, physical appearance, body size, race, ethnicity, age, religion, socioeconomic status, caste or creed. 

---
# ... Code of Conduct 

Our events are intended to inspire women to excel in technology careers, and anyone who is there for this purpose is welcome. We do not tolerate harassment of members in any form.

---

# ... Code of Conduct

Our Code of Conduct applies to all WWCode events and online communities. Read the full version at http://www.womenwhocode.com/codeofconduct. If you would like to report an incident, please reach out to one of our volunteers or submit an incident report form: http://bit.ly/wwcode-incident-report

---

# [fit] A look at 
# [fit] Security Job Posts

---

# Actual job listing bullet point 
- Experience with static and dynamic code analysis, fuzzing and use of vulnerability tools

These skills can be used in security, but they can also be used for development  

---

# Job titles: 
- Engineer, Application Security
- Application Security (AppSec) Defender
- Software Reverse-Engineer
- Security Engineer I
- Project Leader - Software Systems Analysis
- Security Engineer

---

## Note: Please be careful downloading and installing things off the internet.  verify your sources.
## Also anything illegal is illegal.  please use these tools for good.  Or people can prosecute you.

---

# [fit] Static Code
# [fit] Analysis

---

# Static Code Analysis

Static code analysis is a method of debugging by examining source code before a program is run. It's done by analyzing a set of code against a set (or multiple sets) of coding rules. Static code analysis and static analysis are often used interchangeably, along with source code analysis. 

### https://www.perforce.com/blog/sca/what-static-code-analysis

---

# IDEs to the rescue

Anyone who tells you vim is better at everything hasn't had a bug sneak through that an IDE catches on loading your program.  Some of the best static tools out there are built in or plugins to your IDE.  A good example in Pycharm Community Edition from Jetbrains.  They offer the CE version free for open source contributors.

### https://www.jetbrains.com/help/pycharm/code-inspection.html

---

There are a ton of tools out there aside from IDEs:

### https://www.softwaretestinghelp.com/tools/top-40-static-code-analysis-tools/

### We can use deepscan to test against a react open source project.  
### This is only one (paid) example.  There are plenty of open source tools too.  The tradeoff will usually be usablity and features vs free and community maintained.  But not always.  These fields change fast enough definitely keep a security blog in your news feed for up and coming toolsets.

### https://deepscan.io/home/?utm_source=softwaretestinghelp&utm_medium=display&utm_campaign=softwaretestinghelp-2019-1

---

Since we come from a variety of languages try and find the tool with the most coverage for the language or framework you're in.

Static analysis is the same idea you use in software development for testing

---

# [fit] Dynamic Code
# [fit] Analysis

---

# Dynamic Code Analysis

Dynamic program analysis is the analysis of computer software that is performed by executing programs on a real or virtual processor. For dynamic program analysis to be effective, the target program must be executed with sufficient test inputs to produce interesting behavior

### https://en.wikipedia.org/wiki/Dynamic_program_analysis

---

Gcov is a source code coverage analysis and statement-by-statement profiling tool. Gcov generates exact counts of the number of times each statement in a program is executed and annotates source code to add instrumentation. Gcov comes as a standard utility with the GNU Compiler Collection (GCC) suite.

### https://en.wikipedia.org/wiki/Gcov

---

# [fit] Fuzzing

---

# Fuzzing

Fuzz testing (fuzzing) is a quality assurance technique used to discover coding errors and security loopholes in software, operating systems or networks. It involves inputting massive amounts of random data, called fuzz, to the test subject in an attempt to make it crash.

### https://www.owasp.org/index.php/Fuzzing

---

The same tools and techniques used in QA are used by security researchers

---

The great advantage of fuzz testing is that the test design is extremely simple, and free of preconceptions about system behavior
### http://en.wikipedia.org/wiki/Fuzz_testing
### https://www.owasp.org/index.php/Fuzzing#Fuzzing_tools

---

# [fit] live demo
Python example:
https://github.com/Gilks/boofuzz-primer

using the boofuz framework:
https://boofuzz.readthedocs.io
##### What could possibly go wrong?  :-)

---

###### For anyone who missed the demo, here's a recap with my bash history.  I'm on osx.  We started out with looking for a python fuzzing option.  the owasp site had one example, a quick google search showed it high in the rankings.  
###### Next I asked if there was a specific tool folks wanted to test the fuzzing against, we had one live suggestion but rather than waking someone up with a pager we looked for an example demo someone had preset of a localhost web server and followed along.
###### The walkthrough and set up is an example of good documentation.  It was easy to follow to get to a running demo.  Not so much code that it was unwieldy.  Take a look if you're trying to figure out which of the umpteen parameters in the docs are required for a short demo!
###### bash history will include osx setup.  I checked for pip3, python3, and the like before we got going.  definitely ask in the slack channels if you every hit your head on first time python set up, or different python versions

---

```bash
python3 --version                # This is a comment in bash! doesn't impact the code
python3 -m venv ./               # create a virtualenv for a nice clean slate
pip3 install boofuzz
git clone git@github.com:Gilks/boofuzz-primer.git     # this is the example repo
cd boofuzz-primer/

python3 boofuzz_server.py &        # start up a basic webserver
ps aux |grep python
kill 37066

git grep grammar    # Q&A: looking in the git repo for why they made the grammar
git grep HELLO      # Q&A: looking in the git repo for why they used HELLO 

cd boofuzz-primer/
python3 network_protocol_example.py  # we canceled with Ctrl-C after enough of an idea came across

cd boofuzz-results/
less run-2019-08-08T02-32-16.db  # yep, output is a sqlite db, so we could have opened it that way.
```
---

sample of the output on screen:

```bash
$ python3 network_protocol_example.py
[2019-08-07 22:50:15,983]     Info: Web interface can be found at http://localhost:26000
[2019-08-07 22:50:15,984] Test Case: 1: grammar.no-name.1
[2019-08-07 22:50:15,984]     Info: Type: Delim. Default value: b' '. Case 1 of 1488 overall.
[2019-08-07 22:50:15,984]     Info: Opening target connection (127.0.0.1:4444)...
[2019-08-07 22:50:15,985]     Info: Connection opened.
[2019-08-07 22:50:15,985]   Test Step: Fuzzing Node 'grammar'
[2019-08-07 22:50:15,985]     Info: Sending 22 bytes...
127.0.0.1:52317 --- HELLO
PROCESS  AAAA

[2019-08-07 22:50:15,985]     Transmitted 22 bytes: 48 45 4c 4c 4f 0d 0a 50 52 4f 43 45 53 53 20 20 41 41 41 41 0d 0a b'HELLO\r\nPROCESS  AAAA\r\n'
[2019-08-07 22:50:15,985]     Info: Closing target connection...
[2019-08-07 22:50:15,985]     Info: Connection closed.
[2019-08-07 22:50:15,985]   Test Step: Sleep between tests.
[2019-08-07 22:50:15,985]     Info: sleeping for 2.000000 seconds
[2019-08-07 22:50:17,995] Test Case: 2: grammar.no-name.2
[2019-08-07 22:50:17,995]     Info: Type: Delim. Default value: b' '. Case 2 of 1488 overall.
[2019-08-07 22:50:17,995]     Info: Opening target connection (127.0.0.1:4444)...
[2019-08-07 22:50:17,996]     Info: Connection opened.
[2019-08-07 22:50:17,996]   Test Step: Fuzzing Node 'grammar'
[2019-08-07 22:50:17,996]     Info: Sending 25 bytes...
127.0.0.1:52318 --- HELLO
PROCESS     AAAA

[2019-08-07 22:50:17,996]     Transmitted 25 bytes: 48 45 4c 4c 4f 0d 0a 50 52 4f 43 45 53 53 20 20 20 20 20 41 41 41 41 0d 0a b'HELLO\r\nPROCESS     AAAA\r\n'
[2019-08-07 22:50:17,997]     Info: Closing target connection...
[2019-08-07 22:50:17,997]     Info: Connection closed.
[2019-08-07 22:50:17,997]   Test Step: Sleep between tests.
[2019-08-07 22:50:17,997]     Info: sleeping for 2.000000 seconds
[2019-08-07 22:50:20,006] Test Case: 3: grammar.no-name.3
[2019-08-07 22:50:20,006]     Info: Type: Delim. Default value: b' '. Case 3 of 1488 overall.
[2019-08-07 22:50:20,007]     Info: Opening target connection (127.0.0.1:4444)...
[2019-08-07 22:50:20,007]     Info: Connection opened.
[2019-08-07 22:50:20,007]   Test Step: Fuzzing Node 'grammar'
[2019-08-07 22:50:20,007]     Info: Sending 30 bytes...
127.0.0.1:52319 --- HELLO
PROCESS          AAAA

[2019-08-07 22:52:50,743]     Transmitted 26 bytes: 48 45 4c 4c 4f 0d 0a 50 52 4f 43 45 53 53 20 3b 6e 6f 74 65 70 61 64 3b 0d 0a b'HELLO\r\nPROCESS ;notepad;\r\n'
[2019-08-07 22:52:50,744]     Info: Closing target connection...
[2019-08-07 22:52:50,744]     Info: Connection closed.
[2019-08-07 22:52:50,744]   Test Step: Sleep between tests.
[2019-08-07 22:52:50,744]     Info: sleeping for 2.000000 seconds
[2019-08-07 22:52:52,752] Test Case: 79: grammar.no-name.79
[2019-08-07 22:52:52,752]     Info: Type: String. Default value: b'AAAA'. Case 79 of 1488 overall.
[2019-08-07 22:52:52,753]     Info: Opening target connection (127.0.0.1:4444)...
[2019-08-07 22:52:52,753]     Info: Connection opened.
[2019-08-07 22:52:52,753]   Test Step: Fuzzing Node 'grammar'
[2019-08-07 22:52:52,753]     Info: Sending 26 bytes...
127.0.0.1:52411 --- HELLO
PROCESS
NOTEPAD


[2019-08-07 22:52:52,753]     Transmitted 26 bytes: 48 45 4c 4c 4f 0d 0a 50 52 4f 43 45 53 53 20 0a 6e 6f 74 65 70 61 64 0a 0d 0a b'HELLO\r\nPROCESS \nnotepad\n\r\n'
[2019-08-07 22:52:52,754]     Info: Closing target connection...
[2019-08-07 22:52:52,754]     Info: Connection closed.
[2019-08-07 22:52:52,754]   Test Step: Sleep between tests.
[2019-08-07 22:52:52,754]     Info: sleeping for 2.000000 seconds
[2019-08-07 22:52:54,762] Test Case: 80: grammar.no-name.80
[2019-08-07 22:52:54,763]     Info: Type: String. Default value: b'AAAA'. Case 80 of 1488 overall.
[2019-08-07 22:52:54,763]     Info: Opening target connection (127.0.0.1:4444)...
[2019-08-07 22:52:54,763]     Info: Connection opened.
[2019-08-07 22:52:54,763]   Test Step: Fuzzing Node 'grammar'
[2019-08-07 22:52:54,763]     Info: Sending 24 bytes...
[2019-08-07 22:52:54,763]     Transmitted 24 bytes: 48 45 4c 4c 4f 0d 0a 50 52 4f 43 45 53 53 20 7c 72 65 62 6f 6f 74 0d 0a b'HELLO\r\nPROCESS |reboot\r\n'
[2019-08-07 22:52:54,764]     Info: Closing target connection...
[2019-08-07 22:52:54,764]     Info: Connection closed.
127.0.0.1:52412 --- HELLO
PROCESS |REBOOT 
```

---

# [fit] Vulnerability
# [fit] Tools

---


### https://www.eweek.com/security/the-15-most-influential-people-in-security-today

Look at what tools top researchers have developed to get them to the top, they make excellent tools.  This is a short sample!

- Hd Moore metasploit  https://www.metasploit.com/
- Daily Dave mailing list http://lists.immunityinc.com/pipermail/dailydave/
- Stefan Esser hardened PHP project http://www.hardened-php.net/


---

# [fit] Thank you!

---

links suggested from our attendees:

#### http://pdxdata.org
#### coverband (Ruby) https://github.com/danmayer/coverband
#### https://owasp.org
