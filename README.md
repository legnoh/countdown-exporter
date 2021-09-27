# countdown-exporter

simple countdown day for specified date for prometheus exporter

## example

e.f) if today is 2021-09-28 ... 

```sh
# HELP countdown_until_seconds 
# TYPE countdown_until_seconds gauge
countdown_until_seconds{date="2021-09-28"} 0.0
countdown_until_seconds{date="2021-09-29"} 86400.0
countdown_until_seconds{date="2021-09-30"} 172800.0
countdown_until_seconds{date="2021-10-01"} 259200.0
countdown_until_seconds{date="2021-10-02"} 345600.0
countdown_until_seconds{date="2021-10-03"} 432000.0
countdown_until_seconds{date="2021-10-04"} 518400.0
countdown_until_seconds{date="2021-10-05"} 604800.0
countdown_until_seconds{date="2021-10-06"} 691200.0
...
```
