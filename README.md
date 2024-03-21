Disclaimer: As I myself do not have a use case for Z-SOAR anymore (and no one else seems to depend on this project), active development for Z-SOAR has been stopped. If you are using this project (or consider using it) please create an issue and I may continue development. 
------- 


# Z-SOAR

Welcome!

**Z-SOAR** is a modular SOAR implementation written in Python. It is designed to be a companion to Znuny/OTRS that uses playbook automation and is able to load integrations to other services.


**To access the full documentation click [here](https://z-soar.readthedocs.io/en/latest/).**

Check out the Usage section for information on how to setup and use the project.
Want to contribute? Nice! Check out the Contributing page for more information.

You may also be interested in swiftbird07/IRIS-SOAR which is another project of mine focussed on providing the fantastic DIFR-IRIS forensic solution with SOAR features.

## Z-SOAR features

- Get detections from various sources (called ‘integrations’) and forward them to Znuny/OTRS
- Provide context for tickets by getting information from various sources (‘integrations’) and adding them to the ticket. All this can be controlled on case-to case basis using ‘playbooks’.
- Using playbooks it is also possible to automate actions on tickets. For example, if a ticket is deemed to be a false positive, it can be closed automatically or if a ticket is deemed to be a real incident, it can be escalated to a higher level of support.
- Z-SOAR is designed and build to be easily extensible. It is possible to add new integrations or playbooks to Z-SOAR with minimal effort.
