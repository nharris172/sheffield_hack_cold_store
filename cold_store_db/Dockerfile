FROM mdillon/postgis:9.6




RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    libprotobuf-c-dev \
    make \
    postgresql-server-dev-9.6 \
    protobuf-c-compiler \
    gcc

RUN git config --global http.sslVerify true
RUN apt-get install ca-certificates
RUN cd /tmp && git clone -b v1.6.0 https://github.com/citusdata/cstore_fdw.git

RUN cd /tmp/cstore_fdw && PATH=/usr/local/pgsql/bin/:$PATH make && PATH=/usr/local/pgsql/bin/:$PATH make install
ADD postgresql.conf /conf/postgresql.conf
COPY updateConfig.sh      /docker-entrypoint-initdb.d/_updateConfig.sh
ADD db_schema.sql /docker-entrypoint-initdb.d/10-init.sql

