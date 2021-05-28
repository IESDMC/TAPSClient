# TAPSClient
A python toolbox for request data from TAPS.

### get_stations
```python
>>> from client import Client
>>> client = Client('TAPS')
>>> from obspy import UTCDateTime
>>> starttime = UTCDateTime("2014-01-01")
>>> endtime = UTCDateTime("2016-06-30")
>>> inv = client.get_stations(network="CC", station="*",starttime=starttime,endtime=endtime, level="response")
>>> print(inv)
Inventory created at 2021-05-28T15:10:15.000000Z
        Created by: TECDC WEB SERVICE
                    /fdsnws/station/0/query?starttime=2014-01-01T00:00:00.000000&endtim...
        Sending institution: TECDC (TECDC)
        Contains:
                Networks (1):
                        CC
                Stations (10):
                        CC.IT01 (SNCH)
                        CC.IT02 (HNSN)
                        CC.IT03 (WATN)
                        CC.IT04 (RELI)
                        CC.IT05 (HNME)
                        CC.IT06 (TDAR)
                        CC.IT07 (LNTO)
                        CC.IT08 (HHGN)
                        CC.IT09 (XIDN)
                        CC.IT10 (HNGN)
                Channels (30):
                        CC.IT01..HHZ, CC.IT01..HHN, CC.IT01..HHE, CC.IT02..HHZ, 
                        CC.IT02..HHN, CC.IT02..HHE, CC.IT03..HHZ, CC.IT03..HHN, 
                        CC.IT03..HHE, CC.IT04..HHZ, CC.IT04..HHN, CC.IT04..HHE, 
                        CC.IT05..HHZ, CC.IT05..HHN, CC.IT05..HHE, CC.IT06..HHZ, 
                        CC.IT06..HHN, CC.IT06..HHE, CC.IT07..HHZ, CC.IT07..HHN, 
                        CC.IT07..HHE, CC.IT08..HHZ, CC.IT08..HHN, CC.IT08..HHE, 
                        CC.IT09..HHZ, CC.IT09..HHN, CC.IT09..HHE, CC.IT10..HHZ, 
                        CC.IT10..HHN, CC.IT10..HHE
```

```python
>>> net = inv[0]
>>> print(net)
Network CC (CC)
        Station Count: 10/10 (Selected/Total)
        2014-10-07T00:00:00.000000Z - 2016-07-19T23:59:59.999900Z
        Access: UNKNOWN
        Contains:
                Stations (10):
                        CC.IT01 (SNCH)
                        CC.IT02 (HNSN)
                        CC.IT03 (WATN)
                        CC.IT04 (RELI)
                        CC.IT05 (HNME)
                        CC.IT06 (TDAR)
                        CC.IT07 (LNTO)
                        CC.IT08 (HHGN)
                        CC.IT09 (XIDN)
                        CC.IT10 (HNGN)
                Channels (30):
                        CC.IT01..HHZ, CC.IT01..HHN, CC.IT01..HHE, CC.IT02..HHZ, 
                        CC.IT02..HHN, CC.IT02..HHE, CC.IT03..HHZ, CC.IT03..HHN, 
                        CC.IT03..HHE, CC.IT04..HHZ, CC.IT04..HHN, CC.IT04..HHE, 
                        CC.IT05..HHZ, CC.IT05..HHN, CC.IT05..HHE, CC.IT06..HHZ, 
                        CC.IT06..HHN, CC.IT06..HHE, CC.IT07..HHZ, CC.IT07..HHN, 
                        CC.IT07..HHE, CC.IT08..HHZ, CC.IT08..HHN, CC.IT08..HHE, 
                        CC.IT09..HHZ, CC.IT09..HHN, CC.IT09..HHE, CC.IT10..HHZ, 
                        CC.IT10..HHN, CC.IT10..HHE
```

```python
>>> sta = net[0]
>>> print(sta)
Station IT01 (SNCH)
        Station Code: IT01
        Channel Count: 3/3 (Selected/Total)
        2014-10-07T00:00:00.000000Z - 2016-07-18T23:59:59.999900Z
        Access: None 
        Latitude: 23.34, Longitude: 120.47, Elevation: 120.0 m
        Available Channels:
                IT01..HHZ, IT01..HHN, IT01..HHE
```

```python
>>> cha = sta[0]
>>> print(cha)
Channel 'HHE', Location '' 
        Time range: 2014-10-07T00:00:00.000000Z - 2016-07-18T23:59:59.000000Z
        Latitude: 23.34, Longitude: 120.47, Elevation: 120.0 m, Local Depth: 0.0 m
        Azimuth: 90.00 degrees from north, clockwise
        Dip: 0.00 degrees down from horizontal
        Channel types: GEOPHYSICAL
        Sampling Rate: 100.00 Hz
        Sensor (Description): None (Guralp CMG3ESP_120sec/Quanterra 330 Linear Phase B)
        Response information available
>>> print(cha.response)
Channel Response
        From m/s (velocity in meters per second) to counts (digital counts)
        Overall Sensitivity: 8.48546e+08 defined at 0.300 Hz
        3 stages:
                Stage 1: PolesZerosResponseStage from m/s to V, gain: 2023.09
                Stage 2: CoefficientsTypeResponseStage from V to counts, gain: 419430
                Stage 3: CoefficientsTypeResponseStage from counts to counts, gain: 1
>>>
```