# Project-Idea

Banking Portal

A small web-based banking portal for Kangra Cooperative bank ,developed by a small IT company,to manage customer and account details using HTML, CSS, and JavaScript.

Features

User can securely login to account 

Account Management to view the account deatils funds and profile

Fund Transfer to other banks and within the bank

Transaction Historycan be displayed withdrawls and deposit



I selcted one of my cousins company called FEBA TECHNOLOGIES which is located in HYDERABAD India.

i have my own idea to create a prject which is related to Bank sector along with that i decided what are my requirements to have in my project like i need to have a login page of the user once the user logins he shpuld be able to see his accou9nt number and balance along with this wanted to implement a button to transfer funds and transactions and logout

with my sepecifications taking reference from chatgpt and yoytube i have written each of line of my code i changed complete user page and some part of backend code which i added delete operation based on the remaing part of the code the basic html code i referred youtube vedios and written the code

the complete documentation was written on my own words



1.Introduction
 
The Banking portal is designed for the Bank Kangra Cooperative bank by the small IT company Feba technologies. This is the basic web page for the users to login to their account check for the account balance and transfer funds to the other accounts and it allows users to transaction history; the main concept of the Bank portal web page is to create a user friendly to the users. We use CRUD operations like (Read, update, Create, Delete) using separation of Frontend and Backend.
Creating a web-based banking interface for Kangra Cooperative bank that enables customers to safely log in, check account information, send money, and monitor the history of transactions in real-time is the aim of this project. Utilizing an agile digital system, the system seeks to replicate essential online banking features, offering a streamlined yet useful experience.
We included futures like user can enter his username and password to login, once the user logins to his account he can able to see the details like account number account balance and there are other options like Transfer Funds which could be helpful to transfer funds and as well Transaction History which allows to see the transactions done to other accounts and a click button to logout from the account session.
Transfer Funds could direct user to other page where can be able to enter their account number and amount want to be transferred once transfer is successful the transaction will be loaded into the transactions page so that it can be available to check when it was required to verify the transactions made in the past.
 
 
 
 
 
 
 
2.Requirements:
2.1 Functional Requirements for this web page: 
User login with password: Gives user a unique username and password with hashed which makes user to enhance the data secured and private. This enables the user once login to account he will be redirected to the personal dashboard. if the person enter the invalid username or invalid password it throughs an error and Invalid username or password.
View account balance: Allows user to access the account balance once he was authenticated to the login page with the updated balance details. On each transaction the balance would be updated on the balance tab accurately updated after the transfer to the other accounts
Transfer Funds to account number:  Can transfer funds to other accounts if the entered account number or if enters any negative it shows as Transfer unsuccessful it allows only when the account number is valid and correct amount is specified in their particular fields it immediately displays Transfer successful
View Transaction History: Makes user to visible with the Transactions made on the account shows the each and every transactions with the date and can delete the transactions which are not required to the user.
2.2 Data Requirements for the project: 
Stores user account details (name, account number, balance) 
It stores the users account data like account number name and balance for the validation process and validates transactions properly with a unique identifier to the User Id and username during login along with the password hashed securely as well with the full name and account number and balance
Record transactions (sender, receiver, amount, date) 
Each and every transaction is recorded for the financial purpose and with the transaction id uniquely along with the user Id to whom the transaction done type of the transaction amount and date and timestamsp of transfer


2.3 CRUD Operations Implementation: 
·      Create:
Able to do create a new record of transaction and ensure the system validate the data and balance. Upon the successful transfer it is added to the transaction. Json file and updates the sender’s balance and receiver’s balance accordingly
·      Read:
Fetch user account and transactions data to display. When u user login the data will be  	taken from the users.json accordingly the transactions details are displayed in reverse chronological order.
·      Update:
The main purpose is to update the account balance for each transaction once the transaction is performed it changes the balances of Sender and receiver in the users.josn the changes are saved using file-based storage
·      Delete:  
To remove a transactions from the transaction history, a delete button is displayed beside of each transaction and user can able to delete the transcation which are not required to display in the transaction history.
2.4 Validation requirements for account: 
·                  Need to input valid numbers in positive to do correct transaction 
·                  Valid account number should be entered to transfer amount 
·                  Password is secured with hashing 
2.5 User interface creation: 
·                  Simple html and tables 
·                  Data loading using javascript API calls without having page reloading 





Refernces : chatgpt and youtube for the coding
https://chatgpt.com/share/6876169e-2d74-800a-8a10-2aabd78a6209
https://www.youtube.com/watch?v=FazgJVnrVuI&t=1810s&pp=ygUbaHRtbCBjc3MgamF2YXNjcmlwdCBwcm9qZWN0
https://youtu.be/8ZnB2jYlGl0?si=J6QldVfXurKVNcHS
https://youtu.be/CQZxeoQeo5c?si=ThQzYEBdivzzWDaz
https://chatgpt.com/share/68761f1b-8104-800a-9c54-3c88c67f36bd
https://youtube.com/shorts/T9gZScRvd_0?si=DVJIXoKeKbOPnyN-
            
