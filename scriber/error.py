# The MIT License
#
# Copyright (c) 2015 Scriber (http://scriber.io)
# Copyright (c) 2010-2011 Stripe (http://stripe.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Exceptions
class ScriberError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(ScriberError, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except:
                http_body = ('<Could not decode body as utf-8. '
                             'Please report to support@scriber.io>')

        self.http_body = http_body

        self.http_status = http_status
        self.json_body = json_body


class APIError(ScriberError):
    pass


class APIConnectionError(ScriberError):
    pass


class InvalidRequestError(ScriberError):

    def __init__(self, message, param, http_body=None,
                 http_status=None, json_body=None):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body)
        self.param = param


class AuthenticationError(ScriberError):
    pass
