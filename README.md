# MovieInfoService

Simple example for demonstrate how to create a web service according to REST API and export storing data about movies from MySQL database.

### What is it

This service provide a REST API endpoint (_GET /movies_) for a getting movies information:
```
{
    result: [
        { 'name' : 'Name 1', /* ... */ },
        { 'name' : 'Name 2', /* ... */ },
        /* ... */
    ]
}
```
Movies info include:
1. Name (title)
2. Description
3. List of actors

Information about movies store in MySQL database.

## Getting Started

### Prerequisites

For using this example you should install python (verison>=3.5) and next python libraries
1. asyncio
2. aiohttp
3. sqlalchemy
4. configparser

```
pip install asyncio aiohttp sqlalchemy configparser
```

Also you should write a correct information about your connection to MySQL into [config.ini](config.ini) file.

The database should has table _'movie'_ which created by:
```
CREATE TABLE movie (
  id            INT   NOT NULL AUTO_INCREMENT PRIMARY KEY,
  level         INT,
  title         TEXT,
  description   TEXT,
  actors        TEXT,
  genre         TEXT,
  year	        INT,
  country       TEXT,
  director      TEXT
) DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
```

### Running

For run this service use next comnand

```
python web_app.py
```

And web-service will be available on **<host_ip>**:8080

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
