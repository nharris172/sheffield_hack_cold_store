CREATE EXTENSION  cstore_fdw;
CREATE EXTENSION  postgis;
-- create server object
CREATE SERVER   cstore_server FOREIGN DATA WRAPPER cstore_fdw;

-- create foreign table
CREATE FOREIGN TABLE   sensor_data
(
    timestamp TIMESTAMP WITHOUT TIME ZONE,
    variable TEXT,
    units TEXT,
    value DOUBLE PRECISION,
    location geometry(POINT, 4326),
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    sensor_id INTEGER,
    sensor_name TEXT,
    observatory TEXT
)
SERVER cstore_server OPTIONS(compression 'pglz');