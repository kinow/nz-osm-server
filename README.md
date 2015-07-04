# nzoss-gis-live-dvd

NZOSS GIS live DVD.

WIP: work project description

## Datasets

WIP: explain the datasets being used

## Infrastructure

The infrastructure is compromised of:

WIP: list exact versions and role

* a Postgres database
* PostGIS extension loaded in Postgres
* mapserver
* imposm
* nginx

This project includes an Ansible playbook, with automated instructions to set up the environment. The playbook
works for both Vagrant and Docker, but it can also be used locally or to set up a server via SSH.

In order to install the infrastructure you will need:

* Vagrant (and VMWare or VirtualBox), or Docker, a Linux computer or SSH access to a server
* Ansible

