DROP TABLE if EXISTS entity_freebase;
DROP TABLE if EXISTS relation;
DROP TABLE if EXISTS train;
DROP TABLE if EXISTS valid;
DROP TABLE if EXISTS test;

CREATE TABLE entity_freebase(
   synset_id text PRIMARY KEY NOT NULL,
   name text,
   UNIQUE (synset_id, name)
);

CREATE TABLE relation(
   id SERIAL PRIMARY KEY,
   name text UNIQUE
);

CREATE TABLE train(
   id SERIAL PRIMARY KEY,
   subject text,
   predicate text,
   object text,
   UNIQUE (subject, predicate, object)
);

CREATE TABLE valid(
   id SERIAL PRIMARY KEY,
   subject text,
   predicate text,
   object text,
   UNIQUE (subject, predicate, object)
);

CREATE TABLE test(
   id SERIAL PRIMARY KEY,
   subject text,
   predicate text,
   object text,
   UNIQUE (subject, predicate, object)
);
