This project is meant to help me network. I wrote a script to send automatically generated emails to employees at companies I am interested in. The goal is to set up meetings so that I can learn more about the company and the role that I am interestedn in. The program guesses the employees email based on their first and last name, and the company.



Functionalitie to add:
~~1) Read CSV Data~~
~~2) Generate Email~~
~~3) Send emails with a delay~~
4) Option if email ending is already is known
5) Hide password 
6) Add feedback where my program can detect if an email is invalid or not and then adjust csv?

Down Road
1) Automatically generate CSV's based on just company (basically the code would find names and their positions for me)
2) Store things in a database to learn SQL

Adams suggestion 
Use JSon instead of CSV
Use AWS - set up EC2 Server -> s3 buckets for files
-> storing the information in a sql file
Josh Suggestions  Use SQLLit

Possible improvement: Combine parse and main because right now i am doing extra work of storing everything in array and then looping through array O(2n) vs O(n)
