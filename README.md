BPMSummary
==========
Tango device for calculating mean, RMS and maximum deviation values of Beam Position Monitors.

What's inside
-------------
This repository contains installation files required to use BPMSummary Tango 
Device Class. 
 
How to install
--------------

First, clone git repository:
```console
git clone https://github.com/synchrotron-solaris/dev-solaris-bpmsummary.git
```
Then, enter the repository:
```console
cd dev-solaris-bpmsummary
```
Now you can use:
```console
python setup.py install
```
or:
```console
pip install .
```

How to run
----------
After installation, there is only one script: `BPMSummary`.
You can use it via:
```console
BPMSummary instance_name
```
Remember that Device Server instance has to registered in database previously.

Requirements
------------

- `setuptools`
- `numpy`
- `facadedevice` >= 1.0.1
- `pytango` >= 9.2.1

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
