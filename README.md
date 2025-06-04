docker-sql-client/
│
├── docker-compose.yml      
├── app/                      
│   ├── Dockerfile             
│   ├── requirements.txt       
│   └── main.py
│
└── (otomatik oluşturulan Docker elemanları)
    ├── volumes/            
    └── networks/               




docker-sql-client/
The main project folder. Contains all files and subdirectories related to the project.

docker-compose.yml → Defines Services
This file starts both the PostgreSQL database and the Python-based SQL terminal client together.

Contains:
db: Sets up and runs a PostgreSQL container.

client: Builds and runs the Python terminal client from a Dockerfile.

What does it do?
Links the containers together in the same Docker network.

Configures the database using environment variables.

Builds the client container using the Dockerfile.

app/ → Contains the Python Client
The application directory that holds the SQL terminal logic and related files.

app/Dockerfile → Sets Up Python Environment
This Dockerfile defines how to build the client container.

What does it do?
Installs Python 3.10.

Installs necessary Python packages from requirements.txt.

Runs the main Python script (main.py).

app/requirements.txt → Python Dependencies
A simple list of Python libraries required by the project.

txt
Kopyala
Düzenle
psycopg2-binary
What does it do?
Installs the psycopg2 library, which allows Python to communicate with PostgreSQL.

app/main.py → SQL Terminal / Client
The core script of the project, providing a terminal interface for SQL commands.

What does it do?
Connects to the PostgreSQL database using psycopg2.connect(...).

Takes SQL input from the user via input().

Executes the command on the database.

If results exist, it prints them; if not, it commits the transaction.

Exits gracefully when the user types exit.

Volumes (Defined in Compose)
yaml
Kopyala
Düzenle
volumes:
  pgdata:
What does it do?
Creates a persistent volume named pgdata.

Ensures that PostgreSQL data is not lost even if the container is removed.

Networks (Defined in Compose)
yaml
Kopyala
Düzenle
networks:
  appnet:
What does it do?
Ensures both db and client services can communicate.

Since they share the same network, the client can connect using host="db".

