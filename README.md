# NZ OpenStreetMap Server

This project contains the automated scripts to set up a OSM server for New Zealand.

## Datasets

The data being used comes from GeoFabrik, and is loaded periodically in the server, using
a PostgreSQL database.

`infra/roles/osm/tasks/main.yml` contains the URL of the dataset, in case you would like to try
different datasets.

## Infrastructure

The infrastructure is compromised of:

* a Postgres database
* PostGIS extension loaded in Postgres
* mapserver
* imposm
* nginx
* Graphite
* LogStash

This project includes an Ansible playbook, with automated instructions to set up the environment. The playbook
works for Vagrant, but it can also be used locally or to set up a server via SSH.

In order to install the infrastructure you will need:

* Vagrant (and VMWare or VirtualBox), or Docker, a Linux computer or SSH access to a server
* Ansible

## Testing with QGIS

If you are running the Vagrant box, create a new WMS server, with any name, and with the following URL: **http://192.168.100.100/mapserv?map=/opt/basemaps/osm-google.map**. You can replace the IP address by the one of your real server too.

## License

Licensed under the MIT License. See LICENSE.txt.
