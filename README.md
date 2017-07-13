# Log-Analysis
udacity project for fullstack

### How to Run?

#### Setup Project:
  1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the newsdata.zip from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded repository using command and ssh connect to it:
  
  ```
    $ vagrant up
  ```
  ```
    $ vagrant ssh
  ```
  2. Change directory to /vagrant .
  
#### Setting up the database and Creating Views:

  1. Load the data in [PostgreSQL](https://www.postgresql.org/) database:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database.
  
  3. Create view articles_view using:
  ```
   	create view articles_view as select title,author,count(*) 
	as views from articles,log where log.path like concat('%',articles.slug) 
	group by articles.title,articles.author order by views desc;
  ```

  4. Create vier log_error_view using:
  ```
    create view log_error_view as select date(time),
	round(100.0*sum(case log.status when '200 OK' 
	then 0 else 1 end)/count(log.status),2) as "Error" 
	from log group by date(time) order by "Error" desc;
  ```

#### Running the scripts:
  1. From the above directory ,run log_analysis.py :
  ```
    $ python log_analysis.py
  ```
  