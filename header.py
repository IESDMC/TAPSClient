# -*- coding: utf-8 -*-
"""
FDSN Web service client for TAPS.
:copyright:
    The TAPS Development Team (dmc@earth.sinica.edu.tw)
"""
import platform
import sys

from obspy import UTCDateTime
version = '0.0.1'

class FDSNException(Exception):
    status_code = None

    def __init__(self, value, server_info=None):
        if server_info is not None:
            if self.status_code is None:
                value = "\n".join([value, "Detailed response of server:", "",
                                   server_info])
            else:
                value = "\n".join([value,
                                   "HTTP Status code: {}"
                                   .format(self.status_code),
                                   "Detailed response of server:",
                                   "",
                                   server_info])
        super(FDSNException, self).__init__(value)


class FDSNNoDataException(FDSNException):
    status_code = 204


class FDSNBadRequestException(FDSNException):
    status_code = 400


class FDSNUnauthorizedException(FDSNException):
    status_code = 401


class FDSNForbiddenException(FDSNException):
    status_code = 403


class FDSNRequestTooLargeException(FDSNException):
    status_code = 413


class FDSNTooManyRequestsException(FDSNException):
    status_code = 429


class FDSNInternalServerException(FDSNException):
    status_code = 500


class FDSNServiceUnavailableException(FDSNException):
    status_code = 503


class FDSNTimeoutException(FDSNException):
    pass


class FDSNRedirectException(FDSNException):
    pass


class FDSNNoAuthenticationServiceException(FDSNException):
    pass


class FDSNDoubleAuthenticationException(FDSNException):
    pass


class FDSNInvalidRequestException(FDSNException):
    pass


class FDSNNoServiceException(FDSNException):
    pass

# https://www.fdsn.org/webservices/datacenters/
URL_MAPPINGS = {
    "TAPS": "https://taps.earth.sinica.edu.tw",
    }

URL_DEFAULT_SUBPATH = '/fdsnws'

FDSNWS = ("dataselect", "station")

encoding = sys.getdefaultencoding() or "UTF-8"
platform_ = platform.platform().encode(encoding).decode("ascii", "ignore")
# The default User Agent that will be sent with every request.
DEFAULT_USER_AGENT = "TAPSCliennnt/%s (%s, Python %s)" % (
    version, platform_, platform.python_version())


PARAMETER_ALIASES = {
    "net": "network",
    "sta": "station",
    "loc": "location",
    "cha": "channel",
    "start": "starttime",
    "end": "endtime",
    "minlat": "minlatitude",
    "maxlat": "maxlatitude",
    "minlon": "minlongitude",
    "maxlon": "maxlongitude",
    "lat": "latitude",
    "lon": "longitude",
    "minmag": "minmagnitude",
    "maxmag": "maxmagnitude",
    "magtype": "magnitudetype",
}

DEFAULT_DATASELECT_PARAMETERS = [
    "starttime", "endtime", "network", "station", "location", "channel"]

OPTIONAL_DATASELECT_PARAMETERS = [
    "quality", "minimumlength", "longestonly"]

DEFAULT_STATION_PARAMETERS = [
    "starttime", "endtime", "network", "station", "location", "channel",
    "minlatitude", "maxlatitude", "minlongitude", "maxlongitude", "level"]

OPTIONAL_STATION_PARAMETERS = [
    "startbefore", "startafter", "endbefore", "endafter", "latitude",
    "longitude", "minradius", "maxradius", "includerestricted",
    "includeavailability", "updatedafter", "matchtimeseries", "format"]

DEFAULT_PARAMETERS = {
    "dataselect": DEFAULT_DATASELECT_PARAMETERS,
    "station": DEFAULT_STATION_PARAMETERS}

OPTIONAL_PARAMETERS = {
    "dataselect": OPTIONAL_DATASELECT_PARAMETERS,
    "station": OPTIONAL_STATION_PARAMETERS}

# The default types if none are given. If the parameter can not be found in
# here and has no specified type, the type will be assumed to be a string.
DEFAULT_TYPES = {
    "starttime": UTCDateTime,
    "endtime": UTCDateTime,
    "network": str,
    "station": str,
    "location": str,
    "channel": str,
    "quality": str,
    "minimumlength": float,
    "longestonly": bool,
    "startbefore": UTCDateTime,
    "startafter": UTCDateTime,
    "endbefore": UTCDateTime,
    "endafter": UTCDateTime,
    "maxlongitude": float,
    "minlongitude": float,
    "longitude": float,
    "maxlatitude": float,
    "minlatitude": float,
    "latitude": float,
    "maxdepth": float,
    "mindepth": float,
    "maxmagnitude": float,
    "minmagnitude": float,
    "magnitudetype": str,
    "maxradius": float,
    "minradius": float,
    "level": str,
    "includerestricted": bool,
    "includeavailability": bool,
    "includeallorigins": bool,
    "includeallmagnitudes": bool,
    "includearrivals": bool,
    "matchtimeseries": bool,
    "eventid": str,
    "eventtype": str,
    "limit": int,
    "offset": int,
    "orderby": str,
    "catalog": str,
    "contributor": str,
    "updatedafter": UTCDateTime,
    "format": str}

DEFAULT_VALUES = {
    "starttime": None,
    "endtime": None,
    "network": None,
    "station": None,
    "location": None,
    "channel": None,
    "quality": "B",
    "minimumlength": 0.0,
    "longestonly": False,
    "startbefore": None,
    "startafter": None,
    "endbefore": None,
    "endafter": None,
    "maxlongitude": 180.0,
    "minlongitude": -180.0,
    "longitude": 0.0,
    "maxlatitude": 90.0,
    "minlatitude": -90.0,
    "latitude": 0.0,
    "maxdepth": None,
    "mindepth": None,
    "maxmagnitude": None,
    "minmagnitude": None,
    "magnitudetype": None,
    "maxradius": 180.0,
    "minradius": 0.0,
    "level": "station",
    "includerestricted": True,
    "includeavailability": False,
    "includeallorigins": False,
    "includeallmagnitudes": False,
    "includearrivals": False,
    "matchtimeseries": False,
    "eventid": None,
    "eventtype": None,
    "limit": None,
    "offset": 1,
    "orderby": "time",
    "catalog": None,
    "contributor": None,
    "updatedafter": None,
}

DEFAULT_SERVICES = {}
for service in ["dataselect", "station"]:
    DEFAULT_SERVICES[service] = {}

    for default_param in DEFAULT_PARAMETERS[service]:
        DEFAULT_SERVICES[service][default_param] = {
            "default_value": DEFAULT_VALUES[default_param],
            "type": DEFAULT_TYPES[default_param],
            "required": False,
        }

    for optional_param in OPTIONAL_PARAMETERS[service]:
        if optional_param == "format":
            if service == "dataselect":
                default_val = "miniseed"
            else:
                default_val = "xml"
        else:
            default_val = DEFAULT_VALUES[optional_param]

        DEFAULT_SERVICES[service][optional_param] = {
            "default_value": default_val,
            "type": DEFAULT_TYPES[optional_param],
            "required": False,
        }

WADL_PARAMETERS_NOT_TO_BE_PARSED = ["nodata"]