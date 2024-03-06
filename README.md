![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fshields.io%2Fbadges%2Fendpoint-badge&label=KeDatech-Exmample&color=Green&link=Passed)

This module purpose is for Exam in KedaTech, include module , unit test and api

Here's an detail for ERD diagram that i used for this module :

![Untitled Diagram drawio](https://github.com/santoso21/kedatech-test/assets/30901764/4be46daf-dd79-45a5-92ce-1de30ab6b560)


### Installation

Just place this module on your addons folder and search Module `kedatech_test` then install.

#### Unit Test

```
odoo-bin -i kedatech_test -c <config_file> -d <db_name> --test-enable
```

#### Controller Test for API

You can test the controller api using the postman with detail below :
* Authentication Bearier Code `KEDATECHTEST`
* URL /api/material/search

<img width="447" alt="image" src="https://github.com/santoso21/kedatech-test/assets/30901764/e0f55d1c-1021-412d-9bf9-ebc229962314">

