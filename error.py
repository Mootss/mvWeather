class mvWeatherException(Exception):
# base exception class

    pass


class InvalidArgument(mvWeatherException):
# when an invalid station name is passed in 

    pass

class HTTPError500(mvWeatherException):
# Error 500, internal server error 

    pass
