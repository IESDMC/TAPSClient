# TAPSClient
A python toolbox for request data from Taiwan Archive Platform for Seismology ([TAPS](https://taps.earth.sinica.edu.tw)).

## Install
```shell
pip install -r requirement.txt
```

### get_stations
ref: [obspy.clients.fdsn - FDSN web service client for ObsPy](https://docs.obspy.org/packages/obspy.clients.fdsn.html#obspy-clients-fdsn-fdsn-web-service-client-for-obspy)
```python
>>> from client import Client
>>> client = Client('TAPS')
>>> from obspy import UTCDateTime
>>> starttime = UTCDateTime("2008-01-01")
>>> endtime = UTCDateTime("2008-12-31")
>>> inv = client.get_stations(network="TW", station="NSE*",starttime=starttime,endtime=endtime, level="response")
>>> print(inv)
Inventory created at 2021-05-31T04:12:36.000000Z
        Created by: TECDC WEB SERVICE
                    /fdsnws/station/0/query?starttime=2008-01-01T00:00:00.000000&endtim...
        Sending institution: TECDC (TECDC)
        Contains:
                Networks (1):
                        TW
                Stations (27):
                        TW.NSE01 (E.Taiwan Range, NSE01)
                        TW.NSE02 (E.Taiwan Range, NSE02)
                        TW.NSE03 (E.Taiwan Range, NSE03)
                        TW.NSE04 (E.Taiwan Range, NSE04)
                        TW.NSE05 (E.Taiwan Range, NSE05)
                        TW.NSE06 (E.Taiwan Range, NSE06)
                        TW.NSE07 (E.Taiwan Range, NSE07)
                        TW.NSE08 (E.Taiwan Range, NSE08)
                        TW.NSE09 (E.Taiwan Range, NSE09)
                        TW.NSE10 (E.Taiwan Range, NSE10)
                        TW.NSE11 (E.Taiwan Range, NSE11)
                        TW.NSE12 (E.Taiwan Range, NSE12)
                        TW.NSE13 (E.Taiwan Range, NSE13)
                        TW.NSE14 (E.Taiwan Range, NSE14)
                        TW.NSE15 (E.Taiwan Range, NSE15)
                        TW.NSE16 (E.Taiwan Range, NSE16)
                        TW.NSE17 (E.Taiwan Range, NSE17)
                        TW.NSE18 (E.Taiwan Range, NSE18)
                        TW.NSE19 (E.Taiwan Range, NSE19)
                        TW.NSE20 (E.Taiwan Range, NSE20)
                        TW.NSE21 (E.Taiwan Range, NSE21)
                        TW.NSE22 (E.Taiwan Range, NSE22)
                        TW.NSE23 (E.Taiwan Range, NSE23)
                        TW.NSE24 (E.Taiwan Range, NSE24)
                        TW.NSE25 (E.Taiwan Range, NSE25)
                        TW.NSE26 (E.Taiwan Range, NSE26)
                        TW.NSE27 (E.Taiwan Range, NSE27)
                Channels (81):
                        TW.NSE01..EHZ, TW.NSE01..EHN, TW.NSE01..EHE, TW.NSE02..EHZ, 
                        TW.NSE02..EHN, TW.NSE02..EHE, TW.NSE03..EHZ, TW.NSE03..EHN, 
                        TW.NSE03..EHE, TW.NSE04..EHZ, TW.NSE04..EHN, TW.NSE04..EHE, 
                        TW.NSE05..EHZ, TW.NSE05..EHN, TW.NSE05..EHE, TW.NSE06..EHZ, 
                        TW.NSE06..EHN, TW.NSE06..EHE, TW.NSE07..EHZ, TW.NSE07..EHN, 
                        TW.NSE07..EHE, TW.NSE08..EHZ, TW.NSE08..EHN, TW.NSE08..EHE, 
                        TW.NSE09..EHZ, TW.NSE09..EHN, TW.NSE09..EHE, TW.NSE10..EHZ, 
                        TW.NSE10..EHN, TW.NSE10..EHE, TW.NSE11..EHZ, TW.NSE11..EHN, 
                        TW.NSE11..EHE, TW.NSE12..EHZ, TW.NSE12..EHN, TW.NSE12..EHE, 
                        TW.NSE13..EHZ, TW.NSE13..EHN, TW.NSE13..EHE, TW.NSE14..EHZ, 
                        TW.NSE14..EHN, TW.NSE14..EHE, TW.NSE15..EHZ, TW.NSE15..EHN, 
                        TW.NSE15..EHE, TW.NSE16..EHZ, TW.NSE16..EHN, TW.NSE16..EHE, 
                        TW.NSE17..EHZ, TW.NSE17..EHN, TW.NSE17..EHE, TW.NSE18..EHZ, 
                        TW.NSE18..EHN, TW.NSE18..EHE, TW.NSE19..EHZ, TW.NSE19..EHN, 
                        TW.NSE19..EHE, TW.NSE20..EHZ, TW.NSE20..EHN, TW.NSE20..EHE, 
                        TW.NSE21..EHZ, TW.NSE21..EHN, TW.NSE21..EHE, TW.NSE22..EHZ, 
                        TW.NSE22..EHN, TW.NSE22..EHE, TW.NSE23..EHZ, TW.NSE23..EHN, 
                        TW.NSE23..EHE, TW.NSE24..EHZ, TW.NSE24..EHN, TW.NSE24..EHE, 
                        TW.NSE25..EHZ, TW.NSE25..EHN, TW.NSE25..EHE, TW.NSE26..EHZ, 
                        TW.NSE26..EHN, TW.NSE26..EHE, TW.NSE27..EHZ, TW.NSE27..EHN, 
                        TW.NSE27..EHE
```

```python
>>> net = inv[0]
>>> print(net)
Network TW (TAIGER Active Source Experiment March 2008)
        Station Count: 27/27 (Selected/Total)
        2008-02-01T00:00:00.000000Z - 2008-07-31T00:00:00.000000Z
        Access: UNKNOWN
        Contains:
                Stations (27):
                        TW.NSE01 (E.Taiwan Range, NSE01)
                        TW.NSE02 (E.Taiwan Range, NSE02)
                        TW.NSE03 (E.Taiwan Range, NSE03)
                        TW.NSE04 (E.Taiwan Range, NSE04)
                        TW.NSE05 (E.Taiwan Range, NSE05)
                        TW.NSE06 (E.Taiwan Range, NSE06)
                        TW.NSE07 (E.Taiwan Range, NSE07)
                        TW.NSE08 (E.Taiwan Range, NSE08)
                        TW.NSE09 (E.Taiwan Range, NSE09)
                        TW.NSE10 (E.Taiwan Range, NSE10)
                        TW.NSE11 (E.Taiwan Range, NSE11)
                        TW.NSE12 (E.Taiwan Range, NSE12)
                        TW.NSE13 (E.Taiwan Range, NSE13)
                        TW.NSE14 (E.Taiwan Range, NSE14)
                        TW.NSE15 (E.Taiwan Range, NSE15)
                        TW.NSE16 (E.Taiwan Range, NSE16)
                        TW.NSE17 (E.Taiwan Range, NSE17)
                        TW.NSE18 (E.Taiwan Range, NSE18)
                        TW.NSE19 (E.Taiwan Range, NSE19)
                        TW.NSE20 (E.Taiwan Range, NSE20)
                        TW.NSE21 (E.Taiwan Range, NSE21)
                        TW.NSE22 (E.Taiwan Range, NSE22)
                        TW.NSE23 (E.Taiwan Range, NSE23)
                        TW.NSE24 (E.Taiwan Range, NSE24)
                        TW.NSE25 (E.Taiwan Range, NSE25)
                        TW.NSE26 (E.Taiwan Range, NSE26)
                        TW.NSE27 (E.Taiwan Range, NSE27)
                Channels (81):
                        TW.NSE01..EHZ, TW.NSE01..EHN, TW.NSE01..EHE, TW.NSE02..EHZ, 
                        TW.NSE02..EHN, TW.NSE02..EHE, TW.NSE03..EHZ, TW.NSE03..EHN, 
                        TW.NSE03..EHE, TW.NSE04..EHZ, TW.NSE04..EHN, TW.NSE04..EHE, 
                        TW.NSE05..EHZ, TW.NSE05..EHN, TW.NSE05..EHE, TW.NSE06..EHZ, 
                        TW.NSE06..EHN, TW.NSE06..EHE, TW.NSE07..EHZ, TW.NSE07..EHN, 
                        TW.NSE07..EHE, TW.NSE08..EHZ, TW.NSE08..EHN, TW.NSE08..EHE, 
                        TW.NSE09..EHZ, TW.NSE09..EHN, TW.NSE09..EHE, TW.NSE10..EHZ, 
                        TW.NSE10..EHN, TW.NSE10..EHE, TW.NSE11..EHZ, TW.NSE11..EHN, 
                        TW.NSE11..EHE, TW.NSE12..EHZ, TW.NSE12..EHN, TW.NSE12..EHE, 
                        TW.NSE13..EHZ, TW.NSE13..EHN, TW.NSE13..EHE, TW.NSE14..EHZ, 
                        TW.NSE14..EHN, TW.NSE14..EHE, TW.NSE15..EHZ, TW.NSE15..EHN, 
                        TW.NSE15..EHE, TW.NSE16..EHZ, TW.NSE16..EHN, TW.NSE16..EHE, 
                        TW.NSE17..EHZ, TW.NSE17..EHN, TW.NSE17..EHE, TW.NSE18..EHZ, 
                        TW.NSE18..EHN, TW.NSE18..EHE, TW.NSE19..EHZ, TW.NSE19..EHN, 
                        TW.NSE19..EHE, TW.NSE20..EHZ, TW.NSE20..EHN, TW.NSE20..EHE, 
                        TW.NSE21..EHZ, TW.NSE21..EHN, TW.NSE21..EHE, TW.NSE22..EHZ, 
                        TW.NSE22..EHN, TW.NSE22..EHE, TW.NSE23..EHZ, TW.NSE23..EHN, 
                        TW.NSE23..EHE, TW.NSE24..EHZ, TW.NSE24..EHN, TW.NSE24..EHE, 
                        TW.NSE25..EHZ, TW.NSE25..EHN, TW.NSE25..EHE, TW.NSE26..EHZ, 
                        TW.NSE26..EHN, TW.NSE26..EHE, TW.NSE27..EHZ, TW.NSE27..EHN, 
                        TW.NSE27..EHE
```

```python
>>> sta = net[0]
>>> print(sta)
Station NSE01 (E.Taiwan Range, NSE01)
        Station Code: NSE01
        Channel Count: 3/3 (Selected/Total)
        2008-02-01T00:00:00.000000Z - 2008-07-31T00:00:00.000000Z
        Access: None 
        Latitude: 24.08, Longitude: 121.61, Elevation: 30.0 m
        Available Channels:
                NSE01..EHZ, NSE01..EHN, NSE01..EHE
```

```python
>>> cha = sta[0]
>>> print(cha)
Channel 'EHE', Location '' 
        Time range: 2008-02-01T00:00:00.000000Z - 2008-07-30T23:59:59.000000Z
        Latitude: 24.08, Longitude: 121.61, Elevation: 30.0 m, Local Depth: 0.0 m
        Azimuth: 90.00 degrees from north, clockwise
        Dip: 0.00 degrees down from horizontal
        Channel types: GEOPHYSICAL
        Sampling Rate: 100.00 Hz
        Sensor (Description): None (Lennartz Products LE-xD/SAMTAC-801H Datalogger)
        Response information available
>>> print(cha.response)
Channel Response
        From m/s (velocity in meters per second) to counts (digital counts)
        Overall Sensitivity: 2.05008e+08 defined at 5.000 Hz
        2 stages:
                Stage 1: PolesZerosResponseStage from m/s to V, gain: 400.407
                Stage 2: CoefficientsTypeResponseStage from V to counts, gain: 512000
>>>
```

### get_waveforms
```python
>>> from client import Client
>>> client = Client('TAPS')
>>> user = 'user'
>>> password = 'password'
>>> client.set_credentials(user, password)
>>> from obspy import UTCDateTime
>>> t = UTCDateTime("2008-04-16T00:00:00.000")
>>> st = client.get_waveforms("TW", "NSE01", "--", "*", t, t + 60 * 60)
>>> print(st)
1 Trace(s) in Stream:
TW.NSE01..EHZ | 2008-04-16T00:00:00.000000Z - 2008-04-16T00:59:59.990000Z | 100.0 Hz, 360000 samples
>>> st.plot(outfile='singlechannel.png')
```

### Remove response
ref: [obspy.core.trace.Trace.remove_response](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.remove_response.html#obspy-core-trace-trace-remove-response)
```python
>>> tr = st[0]
>>> pre_filt = [0.001, 0.005, 45, 50]
>>> tr.remove_response(inventory=inv, pre_filt=pre_filt, output="DISP",
                   water_level=60, plot='outfile.png')
<...Trace object at 0x...>
```
