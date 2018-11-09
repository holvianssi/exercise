Holvi transaction API exercise
==============================

Welcome to Holvi transaction API exercise!

In this exercise, you'll implement an API for recording transactions to
accounts. Simple skeleton Django project is provided, but rest is up to
you.

To get the app running, you should install Python 3.6 and Django 2.1.x
on your development system. On top of that, you should use Django Rest
Framework (DRF) for the implementation of the API. You can use other
libraries if you so wish.

Your submission should be returned as a Git repository. We prefer public
access to Github, but other submission methods are OK, too, as long as we
have access to your code and Git commits. When working with Git we prefer
small commits over larger ones. At least the commit history should
clearly separate the work done by us from your own work.

Minimum requirements
--------------------

Complete the following tasks based on existing database models and
Django Rest Framework:
  1. Implement an API for fetching balance of an account
     (API endpoint GET /account/<uuid>/balance/). The account's
     current balance is returned from the API.
  2. Implement an API for fetching transactions on account.
     The main use case for the API is to build the typical transaction
     listing you can see in most mobile banks. Design the API as you
     see best for this use case.
  3. Implement an API to POST a new transaction on account.
     You should prevent posting withdrawal transactions if doing so
     results in negative account balance. This operation should
     update the account's balance so that it never goes out of sync
     with the balance calculated from transaction listing.
  4. Implement a management command to load some data to the system.
  5. Implement tests for the APIs you have built.

We appreciate if you follow Python's and Django's typical code conventions
for your source code, API design and testing setup. Of course, the solution
should be easy to understand.


Optional tasks
--------------

We have collected a large list of optional additional tasks. The main purpose
of the additional tasks is to allow you to show your skillset a bit more. If
you feel you know a bit more than the usual candidate about some of below
tasks, do let us know by completing the task!

Client & features: 
  1. Implement single page app UI for above APIs
  2. Implement console based client for above APIs
  3. Implement operations access to the system (this should allow operations
     to view details of users, accounts and transactions, and to do
     corrections to transactions data).
  4. Implement a change to the account balance API so that it's possible
     to query the balance of the account at end of given date.

Authentication and audit:
  1. Describe or implement authentication and authorisation solution for above
     APIs.
  2. Describe or implement an audit system for above APIs (basically a solution
     which allows one to see who did what in the system).

Concurrency, scalability, reliability:
  1. Describe possible pain points in scaling the system to tens of thousands
     of users. Some of the users could have very large number of transactions
     on single account. What if the system would need to scale to tens of
     millions of users, each with million transactions on an account?
  2. Describle or implement changes to make the system reliable against
     concurrent POSTing of transactions to an account. 
  3. Assume you already have a million users each with multipe accounts in the
     system. Describe or implement changes to add a new field currency to the
     Account model. The field should default to 'EUR'. In which order database
     migrations, code releases and other possible operations should be applied
     if we want to keep the system running all the time without interruptions.
     For this task you should assume the database is PostgreSQL 10 or
     some other similarly advanced database.

Devops:
  1. Make the application run in a Docker container.
  2. Descrbie how you would implement CI for the application.
  3. Assume you would need to deploy the application in AWS. Which AWS features
     would you use to get the app running? Please provide an example
     configuration or detailed use case for at least one of the AWS features you
     plan to use.

Bookkeeping:
  1. Describe what it would mean to have a double entry bookkeeping system
     instead of the current single entry system. What would it imply on the
     data model side? Why would one want to use such a system for a bank
     in general?
